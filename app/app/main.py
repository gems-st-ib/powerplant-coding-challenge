from urllib.request import Request

from app.app.exception.invalid_power_plant_type_exception import InvalidPowerPlantTypeException
from app.app.exception.power_plant_challenge_exception import PowerPlantChallengeException
from fastapi import FastAPI
from app.app.controller.main_controller import router
from fastapi.responses import JSONResponse
from app.app.logging_config import setup_logging
import logging
logger = logging.getLogger(__name__)

setup_logging()

app = FastAPI()
app.include_router(router, prefix="/api")

logger.info("Code challenge starting!!")

@app.exception_handler(InvalidPowerPlantTypeException)
def dependency_exception_handler(request: Request, exc: InvalidPowerPlantTypeException):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )


@app.exception_handler(PowerPlantChallengeException)
def dependency_exception_handler(request: Request, exc: PowerPlantChallengeException):
    return JSONResponse(
        status_code=500,
        content={"message": str(exc)},
    )
