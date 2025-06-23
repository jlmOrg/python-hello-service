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

# Build Docker Image
```shell
docker build -t python-hello-service .
```


# Metrics
## Prometheus
### Download Prometheus
https://prometheus.io/download/

### Update `prometheus.yml`
Add another job to the `scrape_configs`. This allows Prometheus to scrape this service running locally on port `8000`
```yaml
  - job_name: 'python-hello-service'
    static_configs:
      - targets: ['localhost:8000']
```

### Start Prometheus
From the directory where `prometheus.exe` and `prometheus.yml` lie, run this in a command prompt
```shell
./prometheus --config.file=prometheus.yml
```

Now Prometheus can be viewable on port `9090`

## Grafana
### Download Grafana
https://grafana.com/grafana/download

### Run Grafana
Run `grafana-server` to start Grafana. Will run on port `3000`

## Add Prometheus Datasource
Add Prometheus as a datasource via `http://localhost:9000`



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