import sentry_sdk
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.tasks import tasks_router
from src.auth import auth_router
from src.core.config import config

sentry_sdk.init(
    dsn=config.SENTRY_DSN,
)
app = FastAPI()


app.include_router(auth_router)
app.include_router(tasks_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("src.main:app", port=8000, log_level="info", reload=True)
