import streamlit as st
import pandas as pd
import plotly.express as px
import requests

def mostrar_observaciones():
    st.header('Observaciones Finales')
    st.image("foto2.png")
    st.markdown("[Referencia de la imagen](https://www.agenciasinc.es/Opinion/COVID-19-hay-que-esperar-lo-mejor-y-estar-preparados-para-lo-peor)")
    st.markdown("""
    Estos datos sobre casos de COVID-19 en Comunidades Autónomas de España son valiosos para entender la evolución y distribución de la enfermedad en diferentes regiones, y su relacion con el peso de cada prueba que se realizaba por aquellas fechas. Recordemos que por aquellas fechas los datos que se registraban era muy variados y poco consistentes, con este analisis que hemos realizado hemos logrado visualizar las pruebas que tenian suficiente peso como para su consideración y la relación también con cada comunidad autonoma y como ha ejecutado dichas pruebas dependiendo de sus diferentes politicas regulatorias. Se debe tener en cuenta que los datos están sujetos a cambios y actualizaciones, ya que se está trabajando continuamente para mejorar la calidad y precisión de la información ofrecida. Utilizar estos datos con cautela y considerar el contexto epidemiológico al realizar este análisis o interpretación ha sido algo vital para llegar a dichas conclusiones.
    """)

if __name__ == '__main__':
    mostrar_observaciones()
