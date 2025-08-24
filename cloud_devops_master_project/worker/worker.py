
import os, time, random
from prometheus_client import Counter, start_http_server

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
jobs_processed = Counter("worker_jobs_processed_total", "Jobs processed")

if __name__ == "__main__":
    # Expose metrics on 9100
    start_http_server(9100)
    while True:
        # simulate work
        time.sleep(random.uniform(0.5, 2.0))
        jobs_processed.inc()
