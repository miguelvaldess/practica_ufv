import streamlit as st
import pandas as pd
import plotly.express as px
import requests

def mostrar_inicio():
    # Documentación del conjunto de datos
    st.title('Datos de casos de COVID-19 en Comunidades Autónomas de España')

    ## Descripción General
    st.header('Descripción General')
    st.markdown("""
    El proyecto se centra en analizar y visualizar datos de casos de COVID-19 reportados en diferentes Comunidades Autónomas de España. Utilizaremos un conjunto de datos proporcionado por los servicios de salud, que incluye información detallada sobre la cantidad de casos, métodos de diagnóstico utilizados y fechas de reporte. El objetivo es crear un dashboard interactivo que permita explorar y comprender la evolución de la enfermedad en diferentes regiones, identificar tendencias temporales, comparar el número de casos entre Comunidades Autónomas y analizar la distribución de métodos de diagnóstico. Nuestro objetivo se basa en analizar los casos registrados y compararlos con las pruebas que se realizaban para verificar la vericidad de estos y el peso de cada tipo de prueba.
    """)
    st.image("foto.png", use_column_width=True, width=200)
    st.markdown("[Referencia de la imagen](https://www.aa.com.tr/es/mundo/españa-registra-más-de-1000-nuevos-contagios-por-covid-19-en-un-solo-día/1768238)")


if __name__ == '__main__':
    mostrar_inicio()
