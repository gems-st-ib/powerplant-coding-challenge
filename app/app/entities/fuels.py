from pydantic import BaseModel


class Fuels(BaseModel):
    gas: float
    kerosine: float
    co2: float
    wind: float
