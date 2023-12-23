import streamlit as st
import pandas as pd
import plotly.express as px
import requests

def mostrar_dashboard():
    @st.cache_data
    def load_data(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            print("Error al obtener datos:", r.status_code)
            return None
        
        mijson = r.json()
        listado = mijson['casos']
        df = pd.DataFrame.from_records(listado)
        print("Datos cargados correctamente:", df.shape)  
        return df

    # URL del FastAPI
    api_url = 'http://127.0.0.1:8000/retrieve_data'

    # Haciendo la solicitud al FastAPI para obtener los datos de casos COVID-19
    df_covid = load_data(api_url)
    
    # Diseño del dashboard
    st.title('Dashboard de Casos de COVID-19 en Comunidades Autónomas de España')

    st.header('Información General')
    info_general_col1, info_general_col2, info_general_col3 = st.columns(3)
    with info_general_col1:
        st.metric("Total de Registros", df_covid.shape[0])
    with info_general_col2:
        st.metric("Total de CCAA", df_covid['ccaa_iso'].nunique())
    with info_general_col3:
        st.metric("Total de Fechas Registradas", df_covid['fecha'].nunique())

    st.header('Análisis Interactivo')

    # Distribución de casos por Comunidad Autónoma
    st.subheader('Casos de COVID-19 por Comunidad Autónoma')
    fig_cases = px.bar(df_covid, x='ccaa_iso', y='num_casos', title='Casos de COVID-19 por Comunidad Autónoma')
    st.plotly_chart(fig_cases)
    st.markdown("Este gráfico muestra el número total de casos de COVID-19 por Comunidad Autónoma.")

    # Tendencia temporal de casos a lo largo del tiempo
    st.subheader('Tendencia Temporal de Casos')
    fig_time_series = px.line(df_covid, x='fecha', y='num_casos', title='Tendencia Temporal de Casos')
    st.plotly_chart(fig_time_series)
    st.markdown("Este gráfico ofrece una perspectiva de la evolución temporal del número de casos de COVID-19. Permite identificar patrones, picos, y tendencias a lo largo del tiempo, lo que ayuda a entender mejor la propagación de la enfermedad y evaluar la efectividad de las medidas tomadas para controlarla. Como podemos observar existen picos justo antes del confinamiento (Marzo) y despues del confinamiento (siendo Enero 2021 donde alcanza los máximos), esto puede decir que erán cuando mas tendencia de contagia había o tambien podemos suponer que es cuando mas pruebas se realizaban.")
    
    # Gráfico de dispersión (scatter plot)
    st.subheader('Relación entre Casos y Pruebas PCR')
    fig_scatter = px.scatter(df_covid, x='num_casos_prueba_pcr', y='num_casos', color='ccaa_iso',
                              title='Relación entre Casos de COVID-19 y Pruebas PCR')
    st.plotly_chart(fig_scatter)
    st.markdown("Este gráfico muestra la relación entre el número de casos de COVID-19 y las pruebas PCR realizadas por Comunidad Autónoma. Como podemos observar, parece seguir una regresión lineal, pero esto se puede deber a la calidad o depuracion de los datos elegidos (haciendo doble click sobre cada comunidad en la leyenda de las Comunidades Autonomas podrás visualizar cada Comunidad individualmente en el grafico). Aun así, podemos hacer una hipotesis suponiendo que las pcr eran las pruebas mas potentes y significativas entre esos años (las que más casos registraban)")
    
    # Relación entre Casos y Pruebas de Antígeno
    st.subheader('Relación entre Casos y Pruebas de Antígeno')
    fig_scatter_antigen = px.scatter(df_covid, x='num_casos_prueba_ag', y='num_casos', color='ccaa_iso',
                              title='Relación entre Casos de COVID-19 y Pruebas de Antígeno')
    st.plotly_chart(fig_scatter_antigen)
    st.markdown("Este gráfico muestra la relación entre el número de casos de COVID-19 y las pruebas de antígeno realizadas, identificando cada Comunidad Autónoma. En este caso, parece seguir una regresión lineal pero mucho mas dispersa en comparación con las de pcr, esto se debe a que a pesar de que eran temas de gran peso, no suponian tanta importancia como podian ser las pcr (haciendo doble click sobre cada comunidad en la leyenda de las Comunidades Autonomas podrás visualizar cada Comunidad individualmente en el grafico)")

    # Relación entre Casos y Pruebas ELISA
    st.subheader('Relación entre Casos y Pruebas ELISA')
    fig_scatter_elisa = px.scatter(df_covid, x='num_casos_prueba_elisa', y='num_casos', color='ccaa_iso',
                              title='Relación entre Casos de COVID-19 y Pruebas ELISA')
    st.plotly_chart(fig_scatter_elisa)
    st.markdown("Este gráfico muestra la relación entre el número de casos de COVID-19 y las pruebas ELISA realizadas, estas pruebas no se deben tener en cuenta debido a la poca fiabilidad que muestran los gráficos, deducimos entonces que estas pruebas no eran de peso a la hora de realizar registro de casos.")

    # Relación entre Casos y Pruebas Desconocidas
    st.subheader('Relación entre Casos y Pruebas Desconocidas')
    fig_scatter_unknown = px.scatter(df_covid, x='num_casos_prueba_desconocida', y='num_casos', color='ccaa_iso',
                              title='Relación entre Casos de COVID-19 y Pruebas Desconocidas')
    st.plotly_chart(fig_scatter_unknown)
    st.markdown("Este gráfico muestra la relación entre el número de casos de COVID-19 y las pruebas desconocidas realizadas, al igual que con las pruebas ELISA, estas pruebas no se deben tener en cuenta debido a la poca fiabilidad que muestran los gráficos, deducimos entonces que estas pruebas no eran de peso a la hora de realizar registro de casos.")

if __name__ == '__main__':
    mostrar_dashboard()



