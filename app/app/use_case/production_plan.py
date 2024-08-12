from typing import List

from app.app.controller.dto.productionplan.request.payload_dto import PayloadDTO
from app.app.controller.dto.productionplan.response.plant_power_dto import PlantPower
from app.app.entities.fuels import Fuels
from app.app.entities.abstract_power_plant import AbstractPowerPlant
from app.app.utils.constants import Constants


def calculate_production_plan(payload: PayloadDTO):
    return list(map(power_plant_to_plant_power, payload.powerplants))


def calculate_production_plan2(load: int, fuels: Fuels, powerplants: List[AbstractPowerPlant]):
    powerplants.sort(key=lambda pp: pp.cost_per_unit, reverse=False)

    print(powerplants)

    remaining_load = load

    for index, powerplant in enumerate(powerplants):

        powerplant.power_produced = powerplant.pmax if remaining_load > powerplant.pmax else remaining_load
        remaining_load -= powerplant.power_produced

        print(f"Index: {index}, Powerplant: {powerplant}")
        print(f"Remaining Load: {remaining_load}")

        if remaining_load <= 0:
            break

    return list(map(power_plant_to_plant_power, powerplants))


def get_price_per_unit(power_plant_type, prices):
    match power_plant_type:
        case Constants.TURBO_JET:
            return prices.kerosine
        case Constants.GAS_FIRED:
            return prices.gas
        case Constants.WIND_TURBINE:
            return prices.wind


def compute_cost(self, price_per_unit, load):
    if self.efficiency <= 0:
        return -1
    # In a more advence develop this power plant must be excluded

    real_load = load if load < self.pmax else self.pmax
    return (real_load / self.efficiency) * price_per_unit


def power_plant_to_plant_power(power_plant: AbstractPowerPlant):
    return PlantPower(power_plant.name, power_plant.power_produced)
