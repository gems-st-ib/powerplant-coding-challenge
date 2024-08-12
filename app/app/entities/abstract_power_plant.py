from abc import ABC, abstractmethod
from math import nan

from app.app.entities.fuels import Fuels


class AbstractPowerPlant(ABC):
    def __init__(self, name: str, type_: str, efficiency: float, pmin: int, pmax: int, fuels: Fuels):
        self.name = name
        self.type = type_
        self.efficiency = efficiency
        self.pmin = pmin
        self.pmax = pmax
        self.cost_per_unit = self.compute_cost_per_unit(fuels)
        self.power_produced = 0

    def __repr__(self):
        return (f"PowerPlant(name={self.name}, type={self.type}, efficiency={self.efficiency}, "
                f"pmin={self.pmin}, pmax={self.pmax}, cost_per_unit={self.cost_per_unit}"
                f", power_produced={self.power_produced})")

    def get_min_cost(self, fuels: Fuels) -> float:
        return self.pmin * self.cost_per_unit

    @abstractmethod
    def compute_cost_per_unit(self, fuels: Fuels) -> float:
        pass