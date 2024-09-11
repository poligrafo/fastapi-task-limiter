import asyncio
import logging
from time import monotonic

from app.schemas.response import ResponseModel

logger = logging.getLogger("app")
lock = asyncio.Lock()


class TestService:
    async def handle(self) -> ResponseModel:
        logger.info("Received a request. Waiting for lock...")

        async with lock:
            logger.info("Lock acquired. Starting work...")
            ts1 = monotonic()
            await asyncio.sleep(3)  # Simulate work by sleeping for 3 seconds
            ts2 = monotonic()
            elapsed_time = ts2 - ts1

            logger.info(f"Work completed. Elapsed time: {elapsed_time:.4f} seconds")
            return ResponseModel(elapsed=elapsed_time)


def get_test_service() -> TestService:
    return TestService()
