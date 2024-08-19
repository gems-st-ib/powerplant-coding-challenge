
from app.app.controller.mapper.plant_power_mapper import power_plant_to_plant_power
from fastapi import APIRouter
from app.app.controller.dto.productionplan.request.payload_dto import PayloadDTO
from app.app.controller.mapper.power_plant_mapper import map_powerplant_dto_to_powerplant
from app.app.use_case.production_plan import calculate_production_plan

import logging
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@router.post("/productionplan/")
async def production_plan(payload: PayloadDTO):
    logger.info(f"Production plan request: payload: {payload}")
    power_plants = calculate_production_plan(
        payload.load, list(map(lambda pp: map_powerplant_dto_to_powerplant(pp, payload.fuels), payload.powerplants)))
    logger.info(f"Production plan response data: power_plants: {power_plants}")
    response = list(map(power_plant_to_plant_power, power_plants))
    logger.info(f"Response: {response.__repr__()}")
    return response



