
from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
from sqlalchemy import create_engine, text
import os, time

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://app:app@localhost:5432/appdb")
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

app = FastAPI(title="Enterprise API")
requests_total = Counter("api_requests_total", "Total API requests")
latency = Histogram("api_request_latency_seconds", "Request latency")

class Item(BaseModel):
    name: str

@app.on_event("startup")
def init_db():
    with engine.begin() as conn:
        conn.execute(text("CREATE TABLE IF NOT EXISTS items (id SERIAL PRIMARY KEY, name TEXT NOT NULL)"))

@app.get("/healthz")
def healthz():
    return {"ok": True}

@app.get("/")
def root():
    requests_total.inc()
    start = time.time()
    with engine.begin() as conn:
        result = conn.execute(text("SELECT count(*) FROM items")).scalar()
    latency.observe(time.time() - start)
    return {"status": "ok", "items": result}

@app.post("/items")
def create_item(item: Item):
    with engine.begin() as conn:
        conn.execute(text("INSERT INTO items(name) VALUES(:n)"), {"n": item.name})
    return {"created": item.name}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
