from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Tienda de Instrumentos API")

@app.get("/")
def root():
    return {"message": "API REST OOP de la Tienda de Instrumentos en ejecución"}
