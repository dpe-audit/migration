import uuid
from typing import Self
from .utils import strval, intval, floatval, boolval


class PlancherHaut:
    id: str
    reference: str
    reference_lnc: str | None
    description: str | None

    surface_paroi_opaque: float
    surface_aiu: float | None
    surface_aue: float | None
    paroi_lourde: bool | None
    uph0_saisi: float | None
    uph_saisi: float | None
    resistance_isolation: float | None
    epaisseur_isolation: float | None

    enum_type_plancher_haut_id: int
    enum_methode_saisie_u0_id: int
    enum_methode_saisie_u_id: int
    enum_type_adjacence_id: int
    enum_type_isolation_id: int
    enum_periode_isolation_id: int | None
    enum_cfg_isolation_lnc_id: int | None

    tv_uph0_id: int | None
    tv_coef_reduction_deperdition_id: int | None
    tv_uph_id: int | None

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.id = str(uuid.uuid4())
        entity.reference = strval(data, "reference")
        entity.reference_lnc = strval(data, "reference_lnc")
        entity.description = strval(data, "description")

        entity.surface_paroi_opaque = floatval(data, "surface_paroi_opaque")
        entity.surface_aiu = floatval(data, "surface_aiu")
        entity.surface_aue = floatval(data, "surface_aue")
        entity.paroi_lourde = boolval(data, "paroi_lourde")
        entity.uph0_saisi = floatval(data, "uph0_saisi")
        entity.uph_saisi = floatval(data, "uph_saisi")
        entity.resistance_isolation = floatval(data, "resistance_isolation")
        entity.epaisseur_isolation = floatval(data, "epaisseur_isolation")

        entity.enum_methode_saisie_u_id = intval(data, "enum_methode_saisie_u_id")
        entity.enum_type_adjacence_id = intval(data, "enum_type_adjacence_id")
        entity.enum_type_plancher_haut_id = intval(data, "enum_type_plancher_haut_id")
        entity.enum_methode_saisie_u0_id = intval(data, "enum_methode_saisie_u0_id")
        entity.enum_type_isolation_id = intval(data, "enum_type_isolation_id")
        entity.enum_periode_isolation_id = intval(data, "enum_periode_isolation_id")
        entity.enum_cfg_isolation_lnc_id = intval(data, "enum_cfg_isolation_lnc_id")

        entity.tv_uph_id = intval(data, "tv_uph_id")
        entity.tv_uph0_id = intval(data, "tv_uph0_id")
        entity.tv_coef_reduction_deperdition_id = intval(
            data, "tv_coef_reduction_deperdition_id"
        )

        return entity
