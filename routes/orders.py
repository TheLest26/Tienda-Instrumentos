from fastapi import APIRouter, HTTPException, Request
from models.orders import Order, OrderIn
from controllers.orders import (
    crear_pedido,
    obtener_pedidos,
    obtener_pedido_por_id,
    actualizar_pedido,
    eliminar_pedido
)
from utils.security import validateuser

router = APIRouter(prefix="/pedidos")

@router.post("/", response_model=Order, tags=[" Pedidos"])
@validateuser
async def crear_pedido_endpoint(request: Request, pedido: OrderIn) -> Order:
    
    return await crear_pedido(pedido)

@router.get("/", tags=[" Pedidos"])
async def obtener_pedidos_endpoint() -> dict:
    
    return await obtener_pedidos()

@router.get("/{pedido_id}", response_model=Order, tags=[" Pedidos"])
async def obtener_pedido_por_id_endpoint(pedido_id: str) -> Order:
    
    return await obtener_pedido_por_id(pedido_id)

@router.put("/{pedido_id}", response_model=Order, tags=[" Pedidos"])
@validateuser
async def actualizar_pedido_endpoint(request: Request, pedido_id: str, pedido: OrderIn) -> Order:
    
    return await actualizar_pedido(pedido_id, pedido)

@router.delete("/{pedido_id}", tags=[" Pedidos"])
@validateuser
async def eliminar_pedido_endpoint(request: Request, pedido_id: str) -> dict:
    
    return await eliminar_pedido(pedido_id)
