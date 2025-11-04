import uuid
from typing import Self
from .utils import strval, intval, floatval


class EtsBaie:
    id: str
    reference: str
    description: str | None
    surface_totale_baie: float
    nb_baie: int
    enum_orientation_id: int
    enum_inclinaison_vitrage_id: int

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.id = str(uuid.uuid4())
        entity.reference = strval(data, "reference")
        entity.description = strval(data, "description")
        entity.surface_totale_baie = floatval(data, "surface_totale_baie")
        entity.nb_baie = intval(data, "nb_baie")
        entity.enum_orientation_id = intval(data, "enum_orientation_id")
        entity.enum_inclinaison_vitrage_id = intval(data, "enum_inclinaison_vitrage_id")
        return entity


class Ets:
    id: str
    reference: str
    description: str | None
    coef_transparence_ets: float

    enum_cfg_isolation_lnc_id: int
    tv_coef_transparence_ets_id: int
    tv_coef_reduction_deperdition_id: int | None

    baie_ets_collection: list[EtsBaie]

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.id = str(uuid.uuid4())
        entity.reference = strval(data, "reference")
        entity.description = strval(data, "description")
        entity.coef_transparence_ets = floatval(data, "coef_transparence_ets")
        entity.enum_cfg_isolation_lnc_id = intval(data, "enum_cfg_isolation_lnc_id")
        entity.tv_coef_transparence_ets_id = intval(data, "tv_coef_transparence_ets_id")
        entity.tv_coef_reduction_deperdition_id = intval(
            data, "tv_coef_reduction_deperdition_id"
        )

        entity.baie_ets_collection = [
            EtsBaie.from_data(item) for item in data.get("baie_ets_collection", [])
        ]

        return entity
