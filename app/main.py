from fastapi import FastAPI
from app.api.hello_controller import router as api_router

app = FastAPI(title="FastAPI Skeleton")

app.include_router(api_router, prefix="/v1")
