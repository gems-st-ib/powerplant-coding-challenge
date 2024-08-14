from app.app.controller.dto.productionplan.request.fuels_dto import FuelsDTO
from app.app.controller.dto.productionplan.request.power_plant_dto import PowerPlantDTO
from app.app.entities.gas_fired import GasFired
from app.app.entities.abstract_power_plant import AbstractPowerPlant
from app.app.entities.turbo_jet import Turbojet
from app.app.entities.wind_turbine import WindTurbine
from app.app.exception.invalid_power_plant_type_exception import InvalidPowerPlantTypeException
from app.app.utils.constants import Constants


def map_powerplant_dto_to_powerplant(pp: PowerPlantDTO, fuels: FuelsDTO) -> AbstractPowerPlant:
    powerplant_map = {
        Constants.GAS_FIRED: GasFired,
        Constants.TURBO_JET: Turbojet,
        Constants.WIND_TURBINE: WindTurbine
    }

    powerplant_class = powerplant_map.get(pp.type)

    if powerplant_class is None:
        raise InvalidPowerPlantTypeException(f"Unknown power plant type: {pp.type}")

    return powerplant_class(
        name=pp.name,
        efficiency=pp.efficiency,
        pmin=pp.pmin,
        pmax=pp.pmax,
        fuels=fuels
    )
