import asyncio
import json
import logging
import random
import time
import uuid

from prometheus_client import Counter, Gauge, Histogram, Summary, start_http_server

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()

# Application metrics
REQUESTS = Counter("app_requests_total", "Total number of requests")
IN_PROGRESS = Gauge("app_in_progress_requests", "Number of requests in progress")
REQUEST_DURATION = Summary(
    "app_request_duration_seconds", "Request duration in seconds"
)
REQUEST_SIZE = Histogram(
    "app_request_size_bytes",
    "Request size in bytes",
    buckets=(100, 500, 1000, 5000, 10000),
)


async def process_request(request_id):
    """A dummy function that processes a request."""
    REQUESTS.inc()
    IN_PROGRESS.inc()

    request_size = random.randint(100, 10000)
    REQUEST_SIZE.observe(request_size)

    # Simulate request processing time
    start_time = time.time()
    await asyncio.sleep(random.uniform(0.1, 7.5))
    duration = time.time() - start_time
    REQUEST_DURATION.observe(duration)

    # Log request details
    log_entry = {
        "request_id": str(request_id),
        "status": "processed",
        "latency": duration,
        "size": request_size,
        "timestamp": time.time(),
    }
    logger.info(json.dumps(log_entry))

    IN_PROGRESS.dec()


async def generate_requests():
    """Continuously generates random number of requests asynchronously to produce metrics."""
    while True:
        num_requests = random.randint(1, 10)
        tasks = [process_request(uuid.uuid4()) for _ in range(num_requests)]
        await asyncio.gather(*tasks)
        await asyncio.sleep(random.uniform(1.0, 5.0))


def run():
    # Start the HTTP server to expose the metrics.
    start_http_server(8000)
    print("Prometheus metrics exposed on http://localhost:8000/metrics")

    # Initialize the asyncio event loop.
    loop = asyncio.get_event_loop()

    # Schedule the continuous request generation.
    loop.create_task(generate_requests())

    # Run the event loop forever.
    loop.run_forever()


if __name__ == "__main__":
    run()
