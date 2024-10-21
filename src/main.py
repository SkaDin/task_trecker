import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.tasks import task_router
from src.auth import auth_router

app = FastAPI()


app.include_router(auth_router)
app.include_router(task_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("src.main:app", port=8000, log_level="info", reload=True)
