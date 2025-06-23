from fastapi import FastAPI
from app.controllers.hello_controller import hello_router
from app.controllers.metrics_controller import metrics_router
from app.service.metrics_service import metrics_middleware

app = FastAPI(title="FastAPI Skeleton")

app.include_router(hello_router, prefix="/v1")
app.include_router(metrics_router)

app.middleware("http")(metrics_middleware)
