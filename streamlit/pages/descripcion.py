import streamlit as st
import pandas as pd
import plotly.express as px
import requests



def mostrar_descripcion():

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


    # URL del FastAPI
    api_url = 'http://127.0.0.1:8000/retrieve_data'

    # Haciendo la solicitud al FastAPI para obtener los datos de casos COVID-19
    df_covid = load_data(api_url)

    ## Estructura de los Datos
    st.header('Estructura de los Datos')
    st.markdown(f"""
    Es crucial comprender la estructura de los datos antes de iniciar el análisis de un archivo CSV de casos de COVID-19. Conocer la disposición de las columnas, como la fecha, el número de casos, ubicaciones geográficas, y otros atributos relevantes, es esencial para aplicar correctamente técnicas de limpieza y preparación de datos. Esto implica identificar y manejar datos faltantes o inconsistentes, así como también, asegurar la coherencia de los tipos de datos para llevar a cabo análisis significativos. Además, comprender la estructura del archivo CSV facilita la selección adecuada de herramientas y métodos de visualización y modelado, permitiendo así una interpretación precisa de tendencias, patrones y correlaciones que puedan existir en los datos de los casos de COVID-19. En última instancia, esta comprensión previa proporciona un fundamento sólido para tomar decisiones informadas y estratégicas basadas en la información extraída del archivo CSV.
    - **Número de Filas y Columnas:** El conjunto de datos contiene un total de {df_covid.shape[0]} registros y {df_covid.shape[1]} columnas.
    - **Descripción de las Columnas:** 
    - `ccaa_iso`: Código ISO de la Comunidad Autónoma.
    - `fecha`: Fecha del reporte de los casos.
    - `num_casos`: Número total de casos reportados.
    - `num_casos_prueba_pcr`: Número de casos detectados mediante prueba PCR.
    - `num_casos_prueba_test_ac`: Número de casos detectados mediante prueba de test de anticuerpos.
    - `num_casos_prueba_ag`: Número de casos detectados mediante prueba de antígenos.
    - `num_casos_prueba_elisa`: Número de casos detectados mediante prueba ELISA.
    - `num_casos_prueba_desconocida`: Número de casos detectados mediante prueba de método desconocido.
    - **Tipos de Datos:** Las columnas contienen principalmente datos de tipo entero (números enteros), fecha y cadenas de texto.
    - **Valores Faltantes o Nulos:** No se encontraron valores faltantes en el conjunto de datos.
    """)

    ## Contexto y Detalles Relevantes
    st.header('Contexto y Detalles Relevantes')
    st.markdown("""
    Entender el contexto epidemiológico de los datos de casos de COVID-19 y los detalles como el periodo de tiempo y los métodos de recolección es esencial. El periodo de tiempo revela la evolución temporal de la enfermedad, mientras que conocer los métodos de recolección asegura la interpretación correcta de los datos. Esta comprensión previa es crucial para analizar los datos con precisión y obtener conclusiones relevantes sobre la propagación y el impacto de la enfermedad.
    - **Periodo de Tiempo:** Los datos abarcan un período desde finales de 2019 hasta 2021.
    - **Contexto Epidemiológico:** Los datos reflejan los reportes de casos de COVID-19 en diferentes Comunidades Autónomas de España.
    - **Métodos de Recolección de Datos:** Los datos son recopilados y reportados por los servicios de salud de las Comunidades Autónomas de España.
    """)
    ## Referencias y Agradecimientos
    st.header('Referencias y Agradecimientos')
    st.markdown("""
    No hay que olvidar mencionar de donde hemos sacado los datos y agradecer a todo lo que nos haya podido permitir realizar esta investigación.
    - **Referencias:** Los datos fueron obtenidos de [datos.gob.es](https://datos.gob.es/es/catalogo/e05070101-evolucion-de-enfermedad-por-el-coronavirus-covid-19).
    - **Agradecimientos:** Agradecimiento a los servicios de salud de las Comunidades Autónomas de España por recopilar y compartir estos datos.
    """)

if __name__ == '__main__':
    mostrar_descripcion()
