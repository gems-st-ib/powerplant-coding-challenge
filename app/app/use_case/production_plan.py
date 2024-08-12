from typing import List

from app.app.controller.dto.productionplan.request.payload_dto import PayloadDTO
from app.app.controller.dto.productionplan.response.plant_power_dto import PlantPower
from app.app.entities.fuels import Fuels
from app.app.entities.power_plant import PowerPlant
from app.app.utils.constants import Constants


def calculate_production_plan(payload: PayloadDTO):
    return list(map(power_plant_to_plant_power, payload.powerplants))


def calculate_production_plan2(load: int, fuels: Fuels, powerplants: List[PowerPlant]):
    powerplants: List[PowerPlant] = list(
        map(lambda pp: cost_computed_powerplant(pp, fuels, load), powerplants))

    # Ordenar por cost_euro_per_mwh_pmax
    powerplants.sort(key=lambda pp: pp.cost_euro_per_mwh_pmax, reverse=False)

    print(powerplants)

    return  


def get_price_per_unit(power_plant_type, prices):
    match power_plant_type:
        case Constants.TURBO_JET:
            return prices.kerosine
        case Constants.GAS_FIRED:
            return prices.gas
        case Constants.WIND_TURBINE:
            return prices.wind


def cost_computed_powerplant(power_plant, prices, load):
    power_plant.cost_euro_per_mwh_pmax = compute_cost(power_plant, get_price_per_unit(power_plant.type, prices), load)
    return power_plant


def compute_cost(self, price_per_unit, load):
    if self.efficiency <= 0:
        return -1
    # In a more advence develop this power plant must be excluded

    real_load = load if load < self.pmax else self.pmax
    return (real_load / self.efficiency) * price_per_unit


def power_plant_to_plant_power(power_plant):
    return PlantPower(power_plant.name, power_plant.pmax)
