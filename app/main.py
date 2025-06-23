from fastapi import FastAPI
from app.controllers.hello_controller import router as api_router
from app.metrics import metrics_middleware, metrics_router

app = FastAPI(title="FastAPI Skeleton")

app.include_router(api_router, prefix="/v1")
app.include_router(metrics_router)

app.middleware("http")(metrics_middleware)
