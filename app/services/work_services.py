import asyncio
import logging

logger = logging.getLogger("app")


class WorkService:
    def __init__(self):
        self._lock = asyncio.Lock()

    async def work(self) -> None:
        logger.info("Executing 'work' in WorkService (waiting 3 seconds)")
        try:
            await asyncio.sleep(3)
            logger.info("Work completed successfully in WorkService")
        except Exception as e:
            logger.error(f"Error during work execution in WorkService: {str(e)}")
            raise

    async def execute(self) -> None:
        logger.info("Trying to acquire lock in WorkService")
        async with self._lock:
            logger.info("Lock acquired in WorkService")
            await self.work()
        logger.info("Work completed and lock released in WorkService")
