import uuid
from typing import Self
from .utils import strval, intval, floatval, boolval


class Ventilation:
    id: str
    reference: str
    description: str | None

    plusieurs_facade_exposee: bool
    surface_ventile: float
    q4pa_conv: float
    q4pa_conv_saisi: float | None
    pvent_moy: float | None

    enum_methode_saisie_q4pa_conv_id: int
    enum_type_ventilation_id: int

    tv_debits_ventilation_id: int
    tv_q4pa_conv_id: int | None

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.id = str(uuid.uuid4())
        entity.reference = strval(data, "reference")
        entity.description = strval(data, "description")

        entity.plusieurs_facade_exposee = boolval(data, "plusieurs_facade_exposee")
        entity.surface_ventile = floatval(data, "surface_ventile")
        entity.q4pa_conv = floatval(data, "q4pa_conv")
        entity.q4pa_conv_saisi = floatval(data, "q4pa_conv_saisi")
        entity.pvent_moy = floatval(data, "pvent_moy")

        entity.enum_methode_saisie_q4pa_conv_id = intval(
            data, "enum_methode_saisie_q4pa_conv_id"
        )
        entity.enum_type_ventilation_id = intval(data, "enum_type_ventilation_id")
        entity.tv_debits_ventilation_id = intval(data, "tv_debits_ventilation_id")
        entity.tv_q4pa_conv_id = intval(data, "tv_q4pa_conv_id")

        return entity
