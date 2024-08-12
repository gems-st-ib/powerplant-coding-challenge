

class PowerPlant:
    name: str
    type: str
    efficiency: float
    pmin: int
    pmax: int

    def compute_cost(self, price_per_unit: float, load) -> float:
        if self.efficiency <= 0:
            return -1
        # In a more advence develop this power plant must be excluded

        real_load = load if load < self.pmax else self.pmax
        return (real_load / self.efficiency) * price_per_unit
