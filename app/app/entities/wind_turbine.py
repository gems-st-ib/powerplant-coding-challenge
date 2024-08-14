from app.app.controller.dto.productionplan.request.fuels_dto import FuelsDTO
from app.app.entities.abstract_power_plant import AbstractPowerPlant
from app.app.utils.constants import Constants


class WindTurbine(AbstractPowerPlant):
    def __init__(self, name: str, efficiency: float, pmin: int, pmax: int, fuels: FuelsDTO):
        super().__init__(name, Constants.WIND_TURBINE, efficiency, pmin, pmax, fuels)
        self.wind_percentage = fuels.wind

    def compute_cost_per_unit(self, fuels: FuelsDTO) -> float:
        return 0

    def compute_produced_power(self, power: float) -> float:
        return power * (self.wind_percentage/100)
