import uuid
from typing import Self
from .utils import strval, intval, floatval


class PontThermique:
    id: str
    reference: str
    reference_1: str | None
    reference_2: str | None
    description: str | None

    pourcentage_valeur_pont_thermique: float
    l: float
    k_saisi: float | None

    enum_methode_saisie_pont_thermique_id: int
    enum_type_liaison_id: int
    tv_pont_thermique_id: int | None

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.id = str(uuid.uuid4())
        entity.reference = strval(data, "reference")
        entity.reference_1 = strval(data, "reference_1")
        entity.reference_2 = strval(data, "reference_2")
        entity.description = strval(data, "description")
        entity.pourcentage_valeur_pont_thermique = floatval(
            data, "pourcentage_valeur_pont_thermique"
        )
        entity.l = floatval(data, "l")
        entity.k_saisi = floatval(data, "k_saisi")

        entity.enum_methode_saisie_pont_thermique_id = intval(
            data, "enum_methode_saisie_pont_thermique_id"
        )
        entity.enum_type_liaison_id = intval(data, "enum_type_liaison_id")
        entity.tv_pont_thermique_id = intval(data, "tv_pont_thermique_id")

        return entity
