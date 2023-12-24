import streamlit as st
import pandas as pd
import plotly.express as px
import requests

def mostrar_analisis():

    st.header('Análisis y Posibles Usos')
    st.markdown("""
    **Potenciales Análisis:** 
    - Identificación de tendencias temporales en la propagación de casos.
    - Comparaciones entre Comunidades Autónomas en cuanto a la detección de casos por diferentes métodos de prueba.
    - Correlaciones entre los métodos de prueba y la cantidad de casos reportados.""")
    st.image("pages/foto1.png")
    st.markdown("[Referencia de la imagen](https://www.rtve.es/noticias/coronavirus-covid-19/)")
    st.markdown("""
    El análisis de estos datos puede proporcionar una comprensión profunda de la evolución y distribución de la enfermedad en las diferentes regiones de España. Algunos de los enfoques de análisis y posibles usos incluyen: Identificación de Tendencias Temporales, Comparación entre Comunidades Autónomas, Análisis de Métodos de Detección, Correlaciones y Factores de Influencia, Predicciones y Modelado, y Seguimiento de Estrategias de Salud Pública. Estos análisis proporcionarán información valiosa para los epidemiólogos, autoridades sanitarias y el público en general, facilitando la toma de decisiones informadas y el desarrollo de estrategias efectivas para combatir la propagación de la enfermedad.
    """)

if __name__ == '__main__':
    mostrar_analisis()
