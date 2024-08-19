from abc import ABC, abstractmethod
from math import nan

from app.app.controller.dto.productionplan.request.fuels_dto import FuelsDTO


class AbstractPowerPlant(ABC):
    def __init__(self, name: str, type_: str, efficiency: float, pmin: int, pmax: int, fuels: FuelsDTO):
        self.name = name
        self.type = type_
        self.efficiency = efficiency
        self.pmin = pmin
        self.pmax = pmax
        self.cost_per_unit = self.compute_cost_per_unit(fuels)
        self.power_produced = 0

    def __repr__(self):
        return (f"PowerPlant(name={self.name}, type={self.type}, class={self.__class__}, efficiency={self.efficiency}, "
                f"pmin={self.pmin}, pmax={self.pmax}, power_produced={self.power_produced}"
                f", cost_per_unit={self.cost_per_unit}, total_cost={self.get_total_cost()})")

    def get_total_cost(self):
        return self.power_produced * self.cost_per_unit

    @abstractmethod
    def compute_cost_per_unit(self, fuels: FuelsDTO) -> float:
        pass

    @abstractmethod
    def compute_produced_power(self, power: float) -> float:
        pass
