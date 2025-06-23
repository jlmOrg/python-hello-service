from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
from fastapi import APIRouter, Request
import time

# Metrics definitions
REQUEST_COUNT = Counter(
    "request_count_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "http_status"]
)
REQUEST_LATENCY = Histogram(
    "request_latency_seconds",
    "Latency of HTTP requests in seconds",
    ["method", "endpoint"]
)
ERROR_COUNT = Counter(
    "error_count_total",
    "Total number of HTTP error responses",
    ["method", "endpoint"]
)

# Metrics endpoint router
metrics_router = APIRouter()

@metrics_router.get("/metrics")
async def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)

# Middleware function to collect metrics on all requests
async def metrics_middleware(request: Request, call_next):
    method = request.method
    # Use route path if available; fallback to raw URL path (e.g., for 404)
    endpoint = request.scope.get("route").path if request.scope.get("route") else request.url.path

    start_time = time.time()
    response = await call_next(request)
    status_code = response.status_code

    latency = time.time() - start_time
    REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(latency)
    REQUEST_COUNT.labels(method=method, endpoint=endpoint, http_status=str(status_code)).inc()

    # Count all 4xx and 5xx responses as errors
    if status_code >= 400:
        ERROR_COUNT.labels(method=method, endpoint=endpoint).inc()

    return response
