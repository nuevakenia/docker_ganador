# Base
import asyncio
from datetime import date, datetime
from databases import Database
import os
import json
import pandas as pd
from pydantic import BaseModel

# API
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi import HTTPException

# Database
from sqlalchemy import BigInteger, Boolean, Column, Integer, Float, String, CHAR, DateTime, ForeignKey, Date, TIMESTAMP, JSON, insert, select, update, and_, desc
from sqlalchemy.ext.declarative import declarative_base
from pandas import DataFrame
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

app = FastAPI(title="Backend Ganador")

# DB

DRIVER: str = "postgresql+asyncpg"
USER: str = os.environ.get("DB_USER", "postgres")
PASSWORD: str = os.environ.get("DB_PASS", "123")
HOST: str = os.environ.get("DB_HOST", "db")
NAME: str = os.environ.get("DB_NAME", "challenge")
print(F"variables:'{DRIVER}://{USER}:{PASSWORD}@{HOST}/{NAME}'")
database = Database(F'{DRIVER}://{USER}:{PASSWORD}@{HOST}/{NAME}')

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

###############################################################

# Schema
class ExecutionSchema(BaseModel):
    sucursal : int
    start_date : date
    end_date : date

# Models
Base = declarative_base()

class Sucursal(Base):
    __tablename__ = "sucursal"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)

class Colaborador(Base):
    __tablename__ = "colaborador"
    id = Column(Integer, primary_key=True)
    personnum = Column(String(255), nullable=False)
    nombre = Column(String(255), nullable=False)
    sucursal_id = Column(Integer, ForeignKey("sucursal.id"))

class Marca(Base):
    __tablename__ = "marca"
    id = Column(Integer, primary_key=True)
    timestamp = Column(TIMESTAMP)
    colaborador_id = Column(Integer, ForeignKey("colaborador.id"))

class Reporte(Base):
    __tablename__ = "reporte"
    id = Column(Integer, primary_key=True)
    archivo = Column(JSON)
    estado = Column(String(50))
    sucursal_id = Column(Integer, ForeignKey("sucursal.id"))
    start_date = Column(Date)
    end_date = Column(Date)

# Queries & DDL

class ReporteRepo:
    @classmethod
    async def get_all(cls, db) -> Reporte:
        stmt = select(Reporte).order_by(desc(Reporte.id)).limit(10)
        result = await db.fetch_all(stmt)
        return result

    @classmethod
    async def get(cls, db, reporte_id:int) -> Reporte:
        stmt = select(Reporte).where(Reporte.id == reporte_id)
        result = await db.fetch_one(stmt)
        if result:
            return result
        else:
            return None

    @classmethod
    async def create(cls,input : ExecutionSchema) -> Reporte:
        stmt_colabs = select(Colaborador.id).where(Colaborador.sucursal_id == input.sucursal)
        stmt_marcas = select(Marca).where(
                    (Marca.timestamp >= input.start_date) &
                    (Marca.timestamp <= input.end_date) &
                    (Marca.colaborador_id.in_(stmt_colabs))
                )

        stmt_colab_names = select([Colaborador.id, Colaborador.nombre])
        colab_names_data = await database.fetch_all(stmt_colab_names)
        colaborador_names = {colab.id: colab.nombre for colab in colab_names_data}

        grouped_marcas = await database.fetch_all(stmt_marcas)
        marcas_by_colaborador = {}
        for marca in grouped_marcas:
            if marca.colaborador_id not in marcas_by_colaborador:
                marcas_by_colaborador[marca.colaborador_id] = []
            marcas_by_colaborador[marca.colaborador_id].append(marca)

        marcas_json = {}
        for colaborador_id, marcas in marcas_by_colaborador.items():

            colaborador_name = colaborador_names.get(colaborador_id, "Desconocido")
            marcas_json[colaborador_name] = [marca.timestamp.isoformat() for marca in marcas]

        stmt_insert = insert(Reporte).values(
        archivo={},
        estado="Generado",
        sucursal_id=input.sucursal,
        start_date=input.start_date,
        end_date=input.end_date)

        report = await database.execute(stmt_insert)

        return marcas_json, report

    @classmethod
    async def update(cls, report_id:int, marcas) -> Reporte:
        await asyncio.sleep(10)
        stmt_update = (
        update(Reporte).
        where(and_(Reporte.id == report_id)).
        values(
            estado="En proceso"
        )
    )
        report = await database.execute(stmt_update)

        await asyncio.sleep(10)
        stmt_update2 = (
        update(Reporte).
        where(and_(Reporte.id == report_id)).
        values(
            archivo=marcas,
            estado="Finalizado"
        )
    )
        report = await database.execute(stmt_update2)
        return report



def json_to_txt(json_data: dict, file_path: str):
    directory = os.path.dirname(file_path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(file_path, "w") as f:
        f.write(json.dumps(json_data, indent=4))

# Endpoints
@app.get("/reportes")
async def reportes():
    """ Get all reportes """
    reportes = await ReporteRepo.get_all(database)
    return JSONResponse(jsonable_encoder(reportes),status_code=200)


@app.get("/descargar/{reporte_id}")
async def descargar_reporte(reporte_id: int):
    """ Descargar un reporte """
    reporte = await ReporteRepo.get(database, reporte_id)
    if not reporte:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")

    if reporte.estado != 'Finalizado':
        raise HTTPException(status_code=400, detail="Reporte no finalizado")
    reportee = reporte.archivo
    data_dict = json.loads(reporte.archivo)
    if not data_dict:
        raise HTTPException(status_code=400, detail="Reporte sin datos")

    df = DataFrame(data_dict)

    # Comprobar si el directorio 'temp' existe, si no, crearlo
    if not os.path.exists('temp'):
        os.makedirs('temp')

    # Convertir el DataFrame a una lista de listas, una lista por cada fila
    data = [df.columns.tolist()] + df.values.tolist()
    now = datetime.now()
    formatted_date = now.strftime("%H%M%S_%d%m%Y")
    # Definir el archivo PDF de salida
    nombre_pdf = f"{reporte.id}_{formatted_date}.pdf"
    file_path = f"temp/{nombre_pdf}"

    pdf = SimpleDocTemplate(file_path, pagesize=letter)

    # Configuración de estilos
    styles = getSampleStyleSheet()
    styleN = styles["BodyText"]
    styleH = styles["Heading1"]

    # Título y Subtítulo
    titulo = Paragraph(f"Reporte de Sucursal: {reporte.sucursal_id}", styleH)
    subtitulo = Paragraph(f"Fecha de inicio: {reporte.start_date}, Fecha de fin: {reporte.end_date}", styleN)

    # Convierte el DataFrame en una lista de listas
    data = [df.columns.tolist()] + df.values.tolist()

    # Crea la tabla
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    # Agrega el título, subtítulo y tabla al PDF
    elements = [titulo, subtitulo, table]
    pdf.build(elements)

    return FileResponse(file_path)

@app.post("/upload")
async def upload(input:ExecutionSchema):
    """ Generar reporte """
    print(f"Generación reporte en curso")

    marcas,id_reporte = await ReporteRepo.create(input)
    loop = asyncio.get_event_loop()
    task = loop.create_task(ReporteRepo.update(id_reporte,marcas))

    print(f"Reporte: {id_reporte} en proceso")
    return JSONResponse(jsonable_encoder("Reporte en proceso!"),status_code=201)

@app.get("/version")
async def version():
    """ Get versión """
    return {"version": "Ganadora 666", "environment": "Master"}

