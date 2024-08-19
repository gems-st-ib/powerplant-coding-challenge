from pydantic import BaseModel


class PowerPlantDTO(BaseModel):
    name: str
    type: str
    efficiency: float
    pmin: int
    pmax: int
