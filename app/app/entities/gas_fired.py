from abc import ABC

from app.app.entities.fuels import Fuels
from app.app.entities.abstract_power_plant import AbstractPowerPlant
from app.app.utils.constants import Constants


class GasFired(AbstractPowerPlant, ABC):
    def __init__(self, name: str, efficiency: float, pmin: int, pmax: int, fuels: Fuels):
        super().__init__(name, Constants.GAS_FIRED, efficiency, pmin, pmax, fuels)

    def compute_cost_per_unit(self, fuels: Fuels) -> float:
        return fuels.gas / self.efficiency
