
import os, time, random, redis
from prometheus_client import Counter, start_http_server

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
jobs = Counter("worker_jobs_total", "Total jobs processed")

if __name__ == "__main__":
    start_http_server(9100)
    r = redis.from_url(REDIS_URL)
    while True:
        # simulate consuming a job
        time.sleep(random.uniform(0.5, 2.0))
        jobs.inc()
