
from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI(title="API Service")
requests_total = Counter("api_requests_total", "Total API requests")

@app.get("/")
def root():
    requests_total.inc()
    return {"status": "ok", "service": "api"}

@app.get("/healthz")
def health():
    return {"ok": True}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
