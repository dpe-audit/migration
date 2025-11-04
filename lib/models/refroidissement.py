import uuid
from typing import Self
from .utils import strval, intval, floatval, boolval


class Climatisation:
    id: str
    reference: str
    description: str | None

    surface_clim: float
    eer: float

    enum_methode_calcul_conso_id: int
    enum_periode_installation_fr_id: int
    enum_methode_saisie_carac_sys_id: int
    enum_type_generateur_fr_id: int
    enum_type_energie_id: int | None

    tv_seer_id: int | None

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.id = str(uuid.uuid4())
        entity.reference = strval(data, "reference")
        entity.description = strval(data, "description")
        entity.surface_clim = floatval(data, "surface_clim")
        entity.eer = floatval(data, "eer")

        entity.enum_methode_calcul_conso_id = intval(
            data, "enum_methode_calcul_conso_id"
        )
        entity.enum_periode_installation_fr_id = intval(
            data, "enum_periode_installation_fr_id"
        )
        entity.enum_type_generateur_fr_id = intval(data, "enum_type_generateur_fr_id")
        entity.enum_type_energie_id = intval(data, "enum_type_energie_id")
        entity.enum_methode_saisie_carac_sys_id = intval(
            data, "enum_methode_saisie_carac_sys_id"
        )
        entity.tv_seer_id = intval(data, "tv_seer_id")

        return entity
