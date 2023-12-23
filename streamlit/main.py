import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from inicio import mostrar_inicio
from descripcion import mostrar_descripcion
from analisis import mostrar_analisis
from dashboard import mostrar_dashboard
from observaciones import mostrar_observaciones


@st.cache_data
def load_data(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        print("Error al obtener datos:", r.status_code)
        return None
    
    mijson = r.json()
    listado = mijson['casos']
    df = pd.DataFrame.from_records(listado)
    print("Datos cargados correctamente:", df.shape)  # Agrega esta línea para imprimir la forma del DataFrame cargado
    return df

# Logo página microbio
st.set_page_config(page_title='Práctica COVID19', page_icon=':microbe:', layout="wide")

# Crear un menú lateral de selección de páginas
page = st.sidebar.selectbox("Seleccionar Página", ["Inicio", "Descripción", "Análisis", "Dashboard", "Observaciones"])

# URL del FastAPI
api_url = 'http://fastapi:8000/retrieve_data'

# Haciendo la solicitud al FastAPI para obtener los datos de casos COVID-19
df_covid = load_data(api_url)

# Mostrar el contenido correspondiente a la página seleccionada
if page == "Inicio":
    mostrar_inicio()
elif page == "Descripción":
    mostrar_descripcion()
elif page == "Análisis":
    mostrar_analisis()
elif page == "Dashboard":
    mostrar_dashboard()
elif page == "Observaciones":
    mostrar_observaciones()
