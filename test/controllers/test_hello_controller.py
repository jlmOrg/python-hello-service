from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.controllers.hello_controller import hello_router

app = FastAPI()
app.include_router(hello_router)

client = TestClient(app)


# get_hello returns 200 and "Hello, world!"
def test_get_hello_should_return_200():
    response = client.get("/hello")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}


# get_hello returns 200 and "Hello, Bob!" when "Bob" is supplied as the name
def test_post_hello_should_return_200_when_name_is_supplied():
    response = client.post("/hello", json={"name": "Bob"})

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Bob!"}


# get_hello returns 422 when key "name" is spelled incorrectly
def test_post_hello_should_return_422_when_name_is_spelt_incorrectly():
    response = client.post("/hello", json={"nme": "Bob"})

    assert response.status_code == 422


# get_hello returns 422 when json payload is missing
def test_post_hello_should_return_422_when_name_is_missing():
    response = client.post("/hello", json={})

    assert response.status_code == 422
