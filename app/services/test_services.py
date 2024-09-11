import logging
from time import monotonic

from app.schemas.response import TestResponse
from app.services.work_services import WorkService

logger = logging.getLogger("app")


class TestService:
    def __init__(self, work_service: WorkService):
        self.work_service = work_service

    async def handle(self) -> TestResponse:
        logger.info("Starting 'work' in TestService")
        try:
            ts1 = monotonic()
            await self.work_service.execute()
            ts2 = monotonic()
            elapsed_time = ts2 - ts1
            logger.info(f"Finished 'work' in TestService, elapsed time: {elapsed_time:.2f} seconds")
            return TestResponse(elapsed=elapsed_time)
        except Exception as e:
            logger.error(f"Error during handling in TestService: {str(e)}")
            raise

def get_test_service(work_service: WorkService = WorkService()) -> TestService:
    return TestService(work_service)