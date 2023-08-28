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

# Database
from sqlalchemy import BigInteger, Boolean, Column, Integer, Float, String, CHAR, DateTime, ForeignKey, Date, TIMESTAMP, JSON, insert, select, update
from sqlalchemy.ext.declarative import declarative_base
app = FastAPI(title="Backend Ganador")

# DB
DRIVER: str = "postgresql+asyncpg"
USER: str = os.environ.get("DB_USER", "postgres")
PASSWORD: str = os.environ.get("DB_PASS", "123")
HOST: str = os.environ.get("DB_HOST", "localhost")
NAME: str = os.environ.get("DB_NAME", "challenge")

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

# Queries & DDL

class ReporteRepo:
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
        estado="pendiente",
        sucursal_id=input.sucursal)

        report = await database.execute(stmt_insert)

        return marcas_json, stmt_insert

    @classmethod
    async def update(cls, report_id:int, marcas) -> Reporte:
        await asyncio.sleep(10)
        stmt_update = (
        update(Reporte).
        where(and_(Reporte.id == report_id)).
        values(
            archivo=marcas,
            estado="finalizado"
        )
    )
        report = await database.execute(stmt_update)
        return report

    @classmethod
    async def get(cls, db, task_id:int) -> Reporte:
        stmt = select(Reporte).where(Reporte.task == task_id)
        return (await db.execute(stmt)).scalar()

# Endpoints
@app.get("/reportes")
async def version():
    """ Get all reportes """
    return {"version": "666", "environment": "Master"}

@app.get("/version")
async def version():
    """ Get versión """
    return {"version": "666", "environment": "Master"}

@app.post("/upload")
async def upload(input:ExecutionSchema):
    """ Generar reporte """
    print(f"Generación reporte en curso")

    marcas,id_reporte = await ReporteRepo.create(input)
    loop = asyncio.get_event_loop()
    task = loop.create_task(ReporteRepo.update(id_reporte,marcas))

    print(f"Reporte: {id_reporte} en proceso")
    return JSONResponse(jsonable_encoder("Reporte en proceso!"),status_code=201)

# Functions
class Uploader:
    """ Clase para ejecutar el proceso de carga de datos para las tablas
        output,output_contratos,monthly,monthly_contratos """
    async def upload(self,input : ExecutionSchema):
        """ Generación reporte en cola """
        # generar async await de 10 segundos
        await asyncio.sleep(10)
        #
        op_insert,opc_insert = await OutputPlanningRepo.create(database,
                input.task["id"],input.periods,input.periods_contratos)

        # inserción monthly_planning
        df_monthly = pd.DataFrame(input.months)
        df_contrato = pd.DataFrame(input.months_contratos)

        opm_insert = await OutputPlanningMonthlyRepo.create(
                                                    database,input.task["id"],
                                                    df_monthly,df_contrato)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if opm_insert:
            update_task = await TaskRepo.update(database,
                                input.task["id"],timestamp,input.task["estado"])
            print("Ejecución Finalizada: ",input.task["id"])
