# app.py

# Importamos las bibliotecas necesarias
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

    sucursales = ["Talagante", "San Bernardo", "Maipo"]

    with st.form(key='form_reporte'):
        st.write("Generar Reporte")

        # Recolectar entradas del usuario
        sucursal = st.selectbox('Sucursales', options=sucursales)
        start = st.date_input('Fecha de inicio')
        end = st.date_input('Fecha de fin')

        # Botón de envío del formulario
        submit_button = st.form_submit_button(label='Enviar')

    if submit_button:
        endpoint_url = os.environ.get("ENDPOINT_URL")

        start_str = start.strftime("%Y-%m-%d")
        end_str = end.strftime("%Y-%m-%d")

        data = {
            "sucursal": sucursal,
            "start": start_str,
            "end": end_str
        }

        response = requests.post(endpoint_url, json=data)

        # Imprimir la respuesta
        if response.status_code == 200:
            st.success('Generación de reporte iniciada con exito!, para visualizar el reporte, ir a la sección "visualizar reportes"')
        else:
            st.error(f"Hubo un error en la generación de reporte. Código de estado: {response.status_code}")

if selected == "Visualizar reportes":
    st.title(f"{selected} seleccionado")

