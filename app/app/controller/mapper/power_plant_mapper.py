from app.app.controller.dto.productionplan.request.power_plant_dto import PowerPlantDTO
from app.app.entities.fuels import Fuels
from app.app.entities.gas_fired import GasFired
from app.app.entities.abstract_power_plant import AbstractPowerPlant
from app.app.entities.turbo_jet import Turbojet
from app.app.entities.wind_turbine import WindTurbine
from app.app.utils.constants import Constants


def map_powerplant_dto_to_powerplant(dto: PowerPlantDTO, fuels: Fuels) -> AbstractPowerPlant:
    if dto.type == Constants.GAS_FIRED:
        return GasFired(name=dto.name, efficiency=dto.efficiency, pmin=dto.pmin, pmax=dto.pmax, fuels=fuels)
    elif dto.type == Constants.TURBO_JET:
        return Turbojet(name=dto.name, efficiency=dto.efficiency, pmin=dto.pmin, pmax=dto.pmax, fuels=fuels)
    elif dto.type == Constants.WIND_TURBINE:
        return WindTurbine(name=dto.name, efficiency=dto.efficiency, pmin=dto.pmin, pmax=dto.pmax, fuels=fuels)
    else:
        print("control PowerPlant NOT SUPPOSED TO HAPPEN!!!")
        return AbstractPowerPlant(name=dto.name, type_=dto.type, efficiency=dto.efficiency, pmin=dto.pmin,
                                  pmax=dto.pmax, fuels=fuels)
