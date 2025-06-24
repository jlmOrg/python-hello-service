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


# Metrics

## Local Instance
### Prometheus
#### Download Prometheus
https://prometheus.io/download/

#### Update `prometheus.yml`
Add another job to the `scrape_configs`. This allows Prometheus to scrape this service running locally on port `8000`
```yaml
  - job_name: 'python-hello-service'
    static_configs:
      - targets: ['localhost:8000']
```

#### Start Prometheus
From the directory where `prometheus.exe` and `prometheus.yml` lie, run this in a command prompt
```shell
./prometheus --config.file=prometheus.yml
```

Now Prometheus can be viewable on port `9090`

### Grafana
#### Download Grafana
https://grafana.com/grafana/download

#### Run Grafana
Run `grafana-server` to start Grafana. Will run on port `3000`

### Add Prometheus Datasource
Add Prometheus as a datasource via `http://localhost:9000`

## Deployed Instance
### Set Correct Context
```shell
kubectl config use-context arn:aws:eks:us-east-1:550487074477:cluster/dev-hello-service
```

### Deploy Prometheus (if not already)
```shell
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack
```

### Apply `servicemonitor` (if not already)
```shell
kubectl apply -f servicemonitor.yml
```
### Port-Forward Grafana
```shell
kubectl port-forward svc/prometheus-grafana 6789:80
```
This makes it so that `localhost:6789` will bring you to the Grafana login page 

### Get Grafana Password
```shell
 kubectl --namespace default get secrets prometheus-grafana -o jsonpath="{.data.admin-password}" | base64 -d ; echo
 ```
Use this password to log in and view the metrics

# Connect to EKS
## Add EKS Cluster
```shell
aws eks update-kubeconfig --region us-east-1 --name dev-hello-service
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