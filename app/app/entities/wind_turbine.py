from app.app.entities.power_plant import PowerPlant
from app.app.utils.constants import Constants


class WindTurbine(PowerPlant):
    def __init__(self, name: str, efficiency: float, pmin: int, pmax: int):
        super().__init__(name, Constants.WIND_TURBINE, efficiency, pmin, pmax)

    def calculate_output(self, wind_percentage: float) -> float:
        # Redefine el cálculo para WindTurbine
        return self.pmax * (wind_percentage / 100) * self.efficiency
