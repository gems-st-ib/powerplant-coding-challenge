from fastapi import APIRouter
from app.app.controller.dto.productionplan.request.payload_dto import PayloadDTO
from app.app.controller.mapper.fuels_mapper import map_fuels_dto_to_fuels
from app.app.controller.mapper.power_plant_mapper import map_powerplant_dto_to_powerplant
from app.app.use_case.production_plan import calculate_production_plan, calculate_production_plan2

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@router.post("/productionplan/")
async def production_plan(payload: PayloadDTO):
    return calculate_production_plan(payload)


@router.post("/productionplan2/")
async def production_plan(payload: PayloadDTO):
    return calculate_production_plan(payload)


    # return calculate_production_plan2(
    #     payload.load,
    #     map_fuels_dto_to_fuels(payload.fuels),
    #     list(map(map_powerplant_dto_to_powerplant, payload.powerplants)))

