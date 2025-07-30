from fastapi import APIRouter, HTTPException, Request
from models.instrumentos import Instrumento, InstrumentoIn
from controllers.instrumentos import (
    crear_instrumento,
    obtener_instrumentos,
    obtener_instrumento_por_id,
    actualizar_instrumento,
    eliminar_instrumento
)
from utils.security import validateadmin

router = APIRouter(prefix="/instrumentos")

@router.post("/", response_model=Instrumento, tags=["🎸 Instrumentos"])
@validateadmin
async def crear_instrumento_endpoint(request: Request, instrumento: InstrumentoIn) -> Instrumento:
    """Registrar un nuevo instrumento musical (solo admin)"""
    return await crear_instrumento(instrumento)

@router.get("/", tags=["🎸 Instrumentos"])
async def obtener_instrumentos_endpoint() -> dict:
    """Obtener todos los instrumentos disponibles"""
    return await obtener_instrumentos()

@router.get("/{instrumento_id}", response_model=Instrumento, tags=["🎸 Instrumentos"])
async def obtener_instrumento_por_id_endpoint(instrumento_id: str) -> Instrumento:
    """Obtener los detalles de un instrumento por su ID"""
    return await obtener_instrumento_por_id(instrumento_id)

@router.put("/{instrumento_id}", response_model=Instrumento, tags=["🎸 Instrumentos"])
@validateadmin
async def actualizar_instrumento_endpoint(request: Request, instrumento_id: str, instrumento: InstrumentoIn) -> Instrumento:
    """Actualizar información de un instrumento (solo admin)"""
    return await actualizar_instrumento(instrumento_id, instrumento)

@router.delete("/{instrumento_id}", tags=["🎸 Instrumentos"])
@validateadmin
async def eliminar_instrumento_endpoint(request: Request, instrumento_id: str) -> dict:
    """Eliminar instrumento del catálogo (solo admin)"""
    return await eliminar_instrumento(instrumento_id)
