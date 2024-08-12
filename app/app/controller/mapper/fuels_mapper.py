from app.app.controller.dto.productionplan.request.fuels_dto import FuelsDTO
from app.app.entities.fuels import Fuels


def map_fuels_dto_to_fuels(fuels_dto: FuelsDTO) -> Fuels:
    """
    Convierte una instancia de FuelsDTO en una instancia de Fuels.

    :param fuels_dto: Una instancia de FuelsDTO.
    :return: Una nueva instancia de Fuels con los mismos valores de atributos.
    """
    return Fuels(
        gas=fuels_dto.gas,
        kerosine=fuels_dto.kerosine,
        co2=fuels_dto.co2,
        wind=fuels_dto.wind
    )

