from abc import ABC

from app.app.controller.dto.productionplan.request.fuels_dto import FuelsDTO
from app.app.entities.abstract_power_plant import AbstractPowerPlant
from app.app.utils.constants import Constants


class GasFired(AbstractPowerPlant, ABC):
    # Tons of CO2 produced per MWh produced
    CO2_TONS_PER_MWH = 0.3

    def __init__(self, name: str, efficiency: float, pmin: int, pmax: int, fuels: FuelsDTO):
        super().__init__(name, Constants.GAS_FIRED, efficiency, pmin, pmax, fuels)

    def compute_cost_per_unit(self, fuels: FuelsDTO, co2tons_per_mwh=CO2_TONS_PER_MWH) -> float:
        return (fuels.gas / self.efficiency) + (fuels.co2 * co2tons_per_mwh)

    def compute_produced_power(self, power: float) -> float:
        return power
