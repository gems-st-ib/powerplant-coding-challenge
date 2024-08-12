from app.app.entities.power_plant import PowerPlant
from app.app.utils.constants import Constants


class Turbojet(PowerPlant):
    def __init__(self, name: str, efficiency: float, pmin: int, pmax: int):
        super().__init__(name, Constants.TURBO_JET, efficiency, pmin, pmax)

    def calculate_output(self, fuel_price: float) -> float:
        # Redefine el cálculo para Turbojet, por ejemplo
        return self.efficiency * (self.pmax - self.pmin) * 0.8 - fuel_price
