import grpc
import redis.asyncio as aioredis
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import APIKeyHeader

from protos.gen.python import sso_pb2
from src.auth.auth import get_grpc_client

# Создаем объект Redis (асинхронный)
red = aioredis.from_url("redis://localhost:6379")

api_key_header = APIKeyHeader(name="Authorization", auto_error=True)
router = APIRouter()


@router.post("/register")
async def register(email: str, password: str, grpc_client=Depends(get_grpc_client)):
    try:
        request = sso_pb2.RegisterRequest(email=email, password=password)
        response = grpc_client.Register(request)
        return {"user_id": response.user_id}
    except grpc.RpcError as e:
        raise HTTPException(status_code=500, detail=f"gRPC error: {e.details()}")


@router.post("/login")
async def login(email: str, password: str, app_id: int, grpc_client=Depends(get_grpc_client)):
    try:
        request = sso_pb2.LoginRequest(email=email, password=password, app_id=app_id)
        response = grpc_client.Login(request)
        await red.set(request.email, response.token)
        return {"token": response.token}
    except grpc.RpcError as e:
        raise HTTPException(status_code=500, detail=f"gRPC error: {e.details()}")


@router.get("/is_admin")
async def is_admin(user_id: int, grpc_client=Depends(get_grpc_client)):
    try:
        request = sso_pb2.IsAdminRequest(user_id=user_id)
        response = grpc_client.IsAdmin(request)
        return {"is_admin": response.isAdmin}
    except grpc.RpcError as e:
        raise HTTPException(status_code=500, detail=f"gRPC error: {e.details()}")


@router.get("/protected")
async def protected_route(token: str = Depends(api_key_header)):
    # result = await red.get("")
    # print(f"\n\n\n\n{token}")
    # if result is None:
    #     raise HTTPException(status_code=403, detail="Invalid token")
    return {"message": "This is a protected route", "token": token}
