from app.app.controller.dto.productionplan.request.power_plant_dto import PowerPlantDTO
from app.app.entities.gas_fired import GasFired
from app.app.entities.power_plant import PowerPlant
from app.app.entities.turbo_jet import Turbojet
from app.app.entities.wind_turbine import WindTurbine
from app.app.utils.constants import Constants


def map_powerplant_dto_to_powerplant(dto: PowerPlantDTO) -> PowerPlant:

    print(dto)

    if dto.type == Constants.TURBO_JET:
        return Turbojet(name=dto.name, efficiency=dto.efficiency, pmin=dto.pmin, pmax=dto.pmax)
    elif dto.type == Constants.GAS_FIRED:
        return GasFired(name=dto.name, efficiency=dto.efficiency, pmin=dto.pmin, pmax=dto.pmax)
    elif dto.type == Constants.WIND_TURBINE:
        return WindTurbine(name=dto.name, efficiency=dto.efficiency, pmin=dto.pmin, pmax=dto.pmax)
    else:
        return WindTurbine(name=dto.name, efficiency=dto.efficiency, pmin=dto.pmin, pmax=dto.pmax)

        # return PowerPlant(name=dto.name, efficiency=dto.efficiency, pmin=dto.pmin, pmax=dto.pmax)
