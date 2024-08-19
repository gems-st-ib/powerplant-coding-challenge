from typing import List
from app.app.entities.abstract_power_plant import AbstractPowerPlant
from app.app.utils.utils import floor_decimal, ceil_decimal, round_decimal

import logging
logger = logging.getLogger(__name__)


def calculate_production_plan(load: int, powerplants: List[AbstractPowerPlant]):

    total_power = compute_powerplants_produced_power(load, powerplants)

    logger.debug(f"total_power 1st round: {total_power}")

    if total_power > load:
        subtract_production_exceeds(total_power - load, powerplants)

    logs_results(load, powerplants)

    return powerplants


def compute_powerplants_produced_power(load: float, powerplants: List[AbstractPowerPlant]):
    powerplants.sort(key=lambda pp: (pp.cost_per_unit, pp.pmin), reverse=False)
    remaining_load = load
    for index, powerplant in enumerate(powerplants):
        powerplant.power_produced = compute_powerplant_produced_power(powerplant, remaining_load)
        remaining_load -= powerplant.power_produced
    return load-remaining_load


def compute_powerplant_produced_power(powerplant: AbstractPowerPlant, remaining_load: float) -> float:
    decimals = 1

    if remaining_load > powerplant.compute_produced_power(powerplant.pmax):
        return floor_decimal(powerplant.compute_produced_power(powerplant.pmax), decimals)

    elif remaining_load > powerplant.compute_produced_power(powerplant.pmin):
        return round_decimal(remaining_load, decimals)

    elif remaining_load > 0:
        return ceil_decimal(powerplant.compute_produced_power(powerplant.pmin), decimals)

    else:
        return 0


def subtract_production_exceeds(exceeded_load: float, powerplants: List[AbstractPowerPlant]):
    powerplants.reverse()
    for index, powerplant in enumerate(powerplants):
        reducible_load = max(0, powerplant.power_produced - powerplant.pmin)
        if reducible_load > 0:
            reduced_load = reducible_load if exceeded_load > reducible_load else exceeded_load
            powerplant.power_produced -= reduced_load
            exceeded_load -= reduced_load

        if exceeded_load <= 0:
            break
    powerplants.reverse()


def logs_results(load: float, powerplants: List[AbstractPowerPlant]):
    total_power_final = 0
    total_cost = 0
    for index, powerplant in enumerate(powerplants):
        logger.debug(powerplant.__repr__())
        total_power_final += powerplant.power_produced
        total_cost += powerplant.get_total_cost()
    logger.info(F"load: {load} MWh")
    logger.info(F"total_power: {total_power_final} MWh")
    logger.info(F"total_cost: {ceil_decimal(total_cost, 2)} €")
