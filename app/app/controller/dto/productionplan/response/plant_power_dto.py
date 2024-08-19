class PlantPower:
    def __init__(self, name, p):
        self.name = name
        self.p = p

    def __repr__(self):
        return f"PowerPlant(name={self.name}, p={self.p})"
