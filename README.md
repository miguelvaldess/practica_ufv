# Práctica final programación II (Miguel Valdés)
# Casos COVID correelación con pruebas medicas y casos registrados por Comunidad Autonoma

He creado una página donde analizo y creo unos cuantos dashboard interactivos que permita explorar y comprender la evolución de la enfermedad en diferentes regiones, identificar tendencias temporales, comparar el número de casos entre Comunidades Autónomas y analizar la distribución de métodos de diagnóstico. Nuestro objetivo se basa en analizar los casos registrados y compararlos con las pruebas que se realizaban para verificar la vericidad de estos y el peso de cada tipo de prueba. Como explico abajo, para ejecutar estos codigos lo he realizado por Visual Studio donde abría el servidor fastappi bajo los puertos mostrados abajo (ya que otros no me dejaba), y en otra terminal aparte ejecutaba el streamlit bajo mi directorio particular (streamlit run C:\Users\Portatil\Desktop\practicafinal\main.py). Donde main es el programa por el que empezar.

# Ejecución de FastAPI y Streamlit

# Requisitos

-  Python instalado
-  Librerias correspondientes y requirements completados
-  

## Ejecución del FastAPI

1. **FastAPI**:
 
    - Dirígete al directorio que contiene `server.py`.
    - Inicia el servidor FastAPI ejecutando:
    - 
        uvicorn server:app --reload

    - El servidor FastAPI estará disponible en `http://127.0.0.1:8000`.

## Ejecución del Streamlit

2. **Streamlit**:

    - Dirígete al directorio que contiene `main.py`.
    - Ejecuta la interfaz de Streamlit con el siguiente comando:

        streamlit run [Directorio correspondiente]main.py

    - La interfaz de Streamlit estará disponible en tu navegador en `http://localhost:8501`.

Todo el resto de la información se encuentra dentro de la propia página con los ánalisis y comentarios correspondientes.
