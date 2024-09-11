import asyncio
import logging
from time import monotonic

from app.schemas.response import ResponseModel

logger = logging.getLogger("app")

lock = asyncio.Lock()
last_request_time = None
cumulative_time = 0


class TestService:
    async def handle(self) -> ResponseModel:
        global last_request_time, cumulative_time
        logger.info("Received a request. Waiting for lock...")

        async with lock:
            logger.info("Lock acquired. Starting work...")

            current_time = monotonic()

            if last_request_time:
                time_since_last_request = current_time - last_request_time
                if time_since_last_request < 3:
                    sleep_time = 3 - time_since_last_request
                    logger.info(f"Sleeping for {sleep_time:.4f} seconds to ensure 3-second difference.")
                    await asyncio.sleep(sleep_time)
                cumulative_time += 3
            else:
                cumulative_time = 3

            last_request_time = monotonic()

            await asyncio.sleep(3)
            elapsed_time = cumulative_time

            logger.info(f"Work completed. Elapsed time: {elapsed_time:.4f} seconds")
            return ResponseModel(elapsed=elapsed_time)


def get_test_service() -> TestService:
    return TestService()
