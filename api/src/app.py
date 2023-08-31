# app.py

# Importamos las bibliotecas necesarias
import base64
from datetime import date, datetime
import os
import streamlit as st
from streamlit import components
from streamlit_option_menu import option_menu
import pandas as pd
import requests
import json
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(layout="wide")
# Se esconden los elementos no usados.
st.markdown("""
<style>
    button[title="View fullscreen"]{
    visibility: hidden;}
    footer {visibility: hidden; }
    .css-1rs6os {visibility: hidden;}
    .css-17ziqus {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

style = """
<style>
table {
    margin-left: auto;
    margin-right: auto;
}
</style>
"""
style_title = """
<style>
.stApp h1 {
    text-align: center;
}
</style>
"""
endpoint_url = os.environ.get("ENDPOINT_URL")
st.image('https://scmlatam.com/wp-content/uploads/2022/04/logo-colores-scm.svg', width=200)

# menu variables
# permite que cambie el menu según la variable de entorno, test(arcos dorados o pruebas de claudio), spsa(spsa) y all(desarrollo)

selected = option_menu(
    menu_title="Challenge Ganador 🐳",
    options= ["Generar reporte", "Visualizar reportes"],
    icons=["clipboard2-plus", "window-sidebar"],
    menu_icon="none",
    default_index=0,
    orientation="horizontal",
    styles={
            "container": {"background-color": "#ffffff"},
        },
)

# def get_pdf_download_link(bytes_pdf, file_name):
#     b64 = base64.b64encode(bytes_pdf).decode()
#     href = f'<a href="data:file/pdf;base64,{b64}" download="{file_name}">Descargar archivo PDF</a>'
#     return href

def get_pdf_download_link(file_path):
    with open(file_path, "rb") as f:
        bytes_pdf = f.read()
    b64 = base64.b64encode(bytes_pdf).decode()
    href = f'<a href="data:file/pdf;base64,{b64}" download="{file_path.split("/")[-1]}">Descargar</a>'
    return href



def generar_pdf(reporte):
    archivo = reporte["archivo"]
    df = pd.DataFrame(archivo)
    if not os.path.exists('temp'):
        os.makedirs('temp')
    data = [df.columns.tolist()] + df.values.tolist()
    now = datetime.now()
    formatted_date = now.strftime("%H%M%S_%d%m%Y")
    nombre_pdf = f"{reporte['id']}_{formatted_date}.pdf"
    file_path = f"temp/{nombre_pdf}"
    pdf = SimpleDocTemplate(file_path, pagesize=letter)
    styles = getSampleStyleSheet()
    styleN = styles["BodyText"]
    styleH = styles["Heading1"]
    titulo = Paragraph(f"Reporte de Sucursal: {reporte['sucursal_id']}", styleH)
    subtitulo = Paragraph(f"Fecha de inicio: {reporte['start_date']}, Fecha de fin: {reporte['end_date']}", styleN)
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
    elements = [titulo, subtitulo, table]
    pdf.build(elements)
    return file_path


if selected == "Generar reporte":

    sucursales = ["Talagante", "Maipo", "Buin"]
    sucursal_to_code = {"Talagante": 1, "Maipo": 2, "Buin": 3}  # Mapeo de nombres a códigos

    st.markdown(style_title, unsafe_allow_html=True)
    st.title(f"{selected}")

    with st.form(key='form_reporte'):
        st.write("Generar Reporte")

        # Recolectar entradas del usuario
        sucursal = st.selectbox('Sucursales', options=sucursales)
        start = st.date_input('Fecha de inicio', value=date(2023, 3, 27))
        end = st.date_input('Fecha de fin', value=date(2023, 4, 6))

        # Botón de envío del formulario
        submit_button = st.form_submit_button(label='Enviar')

    if submit_button:
        endpoint_url_upload = F'{endpoint_url}upload'
        sucursal_code = sucursal_to_code[sucursal]  # Obtener el código numérico para la sucursal seleccionada

        start_str = start.strftime("%Y-%m-%d")
        end_str = end.strftime("%Y-%m-%d")

        data = {
            "sucursal": sucursal_code,
            "start_date": start_str,
            "end_date": end_str
        }

        response = requests.post(endpoint_url_upload, json=data)

        # Imprimir la respuesta
        if response.status_code == 201:
            st.success('Generación de reporte iniciada con exito! para visualizar el reporte ir a la sección "visualizar reportes"')
        else:
            st.error(f"Hubo un error en la generación de reporte. Código de estado: {response.status_code}")


elif selected == "Visualizar reportes":
    st.markdown(style_title, unsafe_allow_html=True)

    sucursal_to_name = {1: "Talagante", 2: "Maipo", 3: "Buin"}
    endpoint_url_reportes = f'{endpoint_url}reportes'
    response = requests.get(endpoint_url_reportes)

    if response.status_code == 200:
        reportes = response.json()
        if reportes:
            for reporte in reportes:
                reporte['Descargar'] = ''
                reporte['sucursal_id'] = sucursal_to_name.get(reporte['sucursal_id'], 'Desconocido')
                if reporte["archivo"]:
                    file_path = generar_pdf(reporte)
                    reporte['Descargar'] = get_pdf_download_link(file_path)

            sorted_reportes = sorted(reportes, key=lambda x: x['id'], reverse=True)
            df = pd.DataFrame(sorted_reportes)
            df = df.rename(columns={'sucursal_id': 'Sucursal', 'start_date': 'Fecha Inicio', 'end_date': 'Fecha Fin', 'estado': 'Estado'})
            df = df.fillna('no disponible')
            html_table = df[['Sucursal', 'Fecha Inicio', 'Fecha Fin', 'Estado', 'Descargar']].to_html(escape=False, index=False)
            st.markdown(f'{style}{html_table}', unsafe_allow_html=True)
    else:
        st.error(f"No hay reportes generados. Código de estado: {response.status_code}")
