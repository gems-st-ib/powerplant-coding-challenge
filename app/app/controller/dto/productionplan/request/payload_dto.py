from pydantic import BaseModel
from typing import List

from app.app.controller.dto.productionplan.request.fuels_dto import FuelsDTO
from app.app.controller.dto.productionplan.request.power_plant_dto import PowerPlantDTO


class PayloadDTO(BaseModel):
    load: int
    fuels: FuelsDTO
    powerplants: List[PowerPlantDTO]

