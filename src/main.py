import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.auth import auth_router
from src.utils.middleware import TokenMiddleware

app = FastAPI()
app.include_router(auth_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(TokenMiddleware)

if __name__ == "__main__":
    uvicorn.run("src.main:app", port=8000, log_level="info", reload=True)
