import asyncio
import logging
from time import monotonic

from app.schemas.response import ResponseModel

logger = logging.getLogger("app")



class TestService:
    async def handle(self) -> ResponseModel:
        ts1 = monotonic()
        await asyncio.sleep(3)
        ts2 = monotonic()
        return ResponseModel(elapsed=ts2 - ts1)


def get_test_service() -> TestService:
    return TestService()
