# python-hello-service
Repository that holds the python backend for the `hello-service`

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

# Build Docker Image
```shell
docker build -t python-hello-service .
```

# Run Flake8 Linter
```shell
flake8 .
```

# Deploy to Kubernetes

## Kind Create The Cluster
```shell
kind create cluster --name python-dev
```

## Kind Load Docker Image
```shell
kind load docker-image python-hello-service:latest --name python-dev
```

## Run the `deployment.yml`
This creates and maintains the pods
```shell
kubectl apply -f /mnt/p/GitRepos/SampleAWSProject/python-microservice/deploy/deployment.yml
```

## Run the `service.yml`
This allows for connectivity to the service
```shell
kubectl apply -f /mnt/p/GitRepos/SampleAWSProject/python-microservice/deploy/service.yml
```

## Port-forward Into The Pod
```shell
kubectl port-forward python-hello-service-68b547bfdf-bdn5t 8000:8000
```



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