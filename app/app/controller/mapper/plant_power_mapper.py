from app.app.controller.dto.productionplan.response.plant_power_dto import PlantPower
from app.app.entities.abstract_power_plant import AbstractPowerPlant


def power_plant_to_plant_power(powerplant: AbstractPowerPlant):
    return PlantPower(powerplant.name, powerplant.power_produced)
