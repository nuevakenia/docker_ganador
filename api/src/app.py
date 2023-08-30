# app.py

# Importamos las bibliotecas necesarias
from datetime import date
import os
import streamlit as st
from streamlit import components
from streamlit_option_menu import option_menu
import pandas as pd
import requests
import json

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
            st.success('Generación de reporte iniciada con exito!, el proceso puede tardar unos segundos, para visualizar el reporte ir a la sección "visualizar reportes"')
        else:
            st.error(f"Hubo un error en la generación de reporte. Código de estado: {response.status_code}")


elif selected == "Visualizar reportes":

    st.markdown(style_title, unsafe_allow_html=True)

# Añadir el título
    st.title(f"{selected}")
    sucursal_to_name = {1: "Talagante", 2: "Maipo", 3: "Buin"}

    endpoint_url_reportes = f'{endpoint_url}reportes'  # Asegúrate de cambiar esta dirección por la de tu API
    response = requests.get(endpoint_url_reportes)
    if response.status_code == 200:
        reportes = response.json()

        # Reemplaza el código de la sucursal con el nombre
        for reporte in reportes:
            reporte['sucursal_id'] = sucursal_to_name.get(reporte['sucursal_id'], 'Desconocido')
            reporte['descargar'] = f"<a href='{endpoint_url}descargar/{reporte['id']}'>Descargar</a>"  # Enlace de descarga

        # Ordena los reportes por ID de mayor a menor
        sorted_reportes = sorted(reportes, key=lambda x: x['id'], reverse=True)

        # Convertir a DataFrame de Pandas para mostrar como tabla
        df = pd.DataFrame(sorted_reportes)
        df = df.rename(columns={'sucursal_id': 'Sucursal', 'start_date': 'Fecha Inicio', 'end_date': 'Fecha Fin', 'estado': 'Estado', 'descargar': 'Descargar'})

        # Usar to_html para convertir el DataFrame en una tabla HTML
        html_table = df[['Sucursal', 'Fecha Inicio', 'Fecha Fin', 'Estado', 'Descargar']].to_html(render_links=True, escape=False, index=False)

        # Renderizar la tabla HTML en Streamlit
        st.markdown(f'{style}{html_table}', unsafe_allow_html=True)

    else:
        st.error(f"Hubo un error en la obtención de reportes. Código de estado: {response.status_code}")

