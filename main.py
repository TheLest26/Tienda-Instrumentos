from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Conexión a Firebase y MongoDB
from utils.mongodb import connect_to_mongo
from utils.security import initialize_firebase

# Rutas disponibles (las que vos tenés en tu carpeta routes)
from routes.instruments import router as instruments_router
from routes.instruments_type import router as instruments_type_router
from routes.instruments_details import router as instruments_details_router
from routes.order_statuses import router as order_statuses_router
from routes.orders import router as orders_router

# Crear la aplicación FastAPI
app = FastAPI(
    title="API Tienda de Instrumentos Musicales",
    description="Plataforma RESTful para administrar una tienda de instrumentos: catálogos, tipos, detalles, pedidos y estados.",
    version="1.0.0"
)

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar en producción por dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializar Firebase y MongoDB al iniciar la app
@app.on_event("startup")
async def startup_event():
    initialize_firebase()
    await connect_to_mongo()

# Registrar las rutas reales
app.include_router(instruments_router, prefix="/instruments", tags=["Instrumentos"])
app.include_router(instruments_type_router, prefix="/instrument-types", tags=["Tipos de Instrumentos"])
app.include_router(instruments_details_router, prefix="/instrument-details", tags=["Detalles de Instrumentos"])
app.include_router(order_statuses_router, prefix="/order-statuses", tags=["Estados de Pedidos"])
app.include_router(orders_router, prefix="/orders", tags=["Pedidos"])

# Ruta raíz
@app.get("/", tags=["Inicio"])
async def read_root():
    return {"message": "Bienvenido a la API de la Tienda de Instrumentos Musicales 🎸🥁🎷"}
