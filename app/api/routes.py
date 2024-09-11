import logging
from fastapi import APIRouter, Depends, HTTPException

from app.schemas.response import TestResponse
from app.services.test_services import TestService, get_test_service

logger = logging.getLogger("app")
router = APIRouter()

@router.get("/test", response_model=TestResponse)
async def handler(test_service: TestService = Depends(get_test_service)) -> TestResponse:
    logger.info("Received request on /test")
    try:
        response = await test_service.handle()
        logger.info(f"Returning response from /test: {response.elapsed:.2f} seconds")
        return response
    except Exception as e:
        logger.error(f"Error processing request on /test: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
