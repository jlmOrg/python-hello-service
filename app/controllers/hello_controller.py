from fastapi import APIRouter

from app.models.hello_dto import HelloRequest

router = APIRouter()

@router.get("/hello")
def hello():
    return {"message": "Hello, world!"}

@router.post("/hello")
def hello_post(request: HelloRequest):
    return {"message": f"Hello, {request.name}!"}
