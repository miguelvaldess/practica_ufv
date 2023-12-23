
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pandas as pd

app = FastAPI(
    title="Datos de Casos COVID-19 por Región",
    description="Servicio para obtener datos de casos de COVID-19 en diferentes regiones de España.",
    version="0.1.0",
)

class CasosCOVID(BaseModel):
    ccaa_iso: str
    fecha: str
    num_casos: int
    num_casos_prueba_pcr: int
    num_casos_prueba_test_ac: int
    num_casos_prueba_ag: int
    num_casos_prueba_elisa: int
    num_casos_prueba_desconocida: int

class ListadoCasosCOVID(BaseModel):
    casos: List[CasosCOVID]

@app.get("/retrieve_data/")
async def retrieve_data():
    file_path = "casos_diagnostico_ccaa.csv"
    df_covid = pd.read_csv(file_path)
    datos_covid = df_covid.to_dict(orient='records')
    listado_covid = ListadoCasosCOVID(casos=datos_covid)
    return listado_covid
