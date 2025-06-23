from fastapi import APIRouter

from app.models.hello_dto import HelloRequest

hello_router = APIRouter()


@hello_router.get("/hello")
def hello():
    return {"message": "Hello, world!"}


@hello_router.post("/hello")
def hello_post(request: HelloRequest):
    return {"message": f"Hello, {request.name}!"}
