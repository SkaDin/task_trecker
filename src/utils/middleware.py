from fastapi import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from src.infrastructure.redis.redis_connect import redis
from src.utils.decode_token import decode_token


class TokenMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        if request.url.path in ["/docs", "/openapi.json", "/login", "/register"]:
            return await call_next(request)

        token = request.headers.get("Authorization")
        if token is None:
            raise HTTPException(status_code=403, detail="Missing token")

        payload = decode_token(token)

        email = payload.get("email")
        stored_token = await redis.get(email)
        stored_token = stored_token.decode("utf-8")
        if stored_token is None or stored_token != token:
            raise HTTPException(status_code=403, detail="Invalid token")

        return await call_next(request)
