# python-microservice
Repository that holds the python backend

# Run Service
```shell
poetry run uvicorn app.main:app --reload
```

<!---
# Update Dependencies (as needed)
```shell
poetry export --without-hashes --format=requirements.txt > requirements.txt
```
--->

# Endpoints
Current prefix is `v1`

## GET
- `/hello` - 
  - **Returns →** "Hello, world!"

## POST
- `/hello`  
  - **Requests →** string (name)
  - **Returns →** "Hello, (name)!"

# Setup
## Install Poetry
```shell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

## Create Poetry project
```shell
poetry init --name fastapi_skeleton --description "FastAPI Skeleton" --author "Joseph McDonough" --python "^3.13" --dependency fastapi --dependency uvicorn[standard] --no-interaction
```

## Install `export` plugin for `requirements.txt`
```shell
pip install poetry-plugin-export
```