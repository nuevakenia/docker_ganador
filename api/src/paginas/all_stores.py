import streamlit as st
from streamlit import components

st.set_page_config(layout="wide")
st.title('Staffing Planning - Todas las tiendas📊')

grupo = '4'
url_all_stores_v4 = f'https://analytics.mypaltime.com/d/a-kFhFl4k/staffing-planning-todas-las-tiendas-v4-refactor?orgId=1&var-group={grupo}&var-store=All&var-section=1&var-driver=1&var-task=167&from=1680318000000&to=1719979199000&theme=light&kiosk=full&var-month=1'

iframe_all_stores = f'<iframe src="{url_all_stores_v4}" width="100%" height="1080" frameborder="0"></iframe>'

components.v1.html(iframe_all_stores, height=1080)
