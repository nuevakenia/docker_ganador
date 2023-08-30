import streamlit as st
from streamlit import components

st.set_page_config(layout="wide")
st.title('Staffing Planning - Vista tienda 📊')


grupo = '4' # Sustituye esto con el valor de tu grupo.

# Define la URL del iframe.
url_single_store_v4 = f'https://analytics.mypaltime.com/d/7RNKr4SVk/staffing-planning-v4-refactor?orgId=1&from=1680318000000&to=1690948799000&var-group={grupo}&var-store=All&var-section=1&var-driver=1&var-month=4&var-task=167&theme=light&kiosk=full'
iframe_single_store = f'<iframe src="{url_single_store_v4}" width="100%" height="1080" frameborder="0"></iframe>'

components.v1.html(iframe_single_store, height=1080)

