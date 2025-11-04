import uuid
from typing import Self
from .utils import strval, intval, floatval, boolval


class PlancherBas:
    id: str
    reference: str
    reference_lnc: str | None
    description: str | None

    surface_aiu: float | None
    surface_aue: float | None
    surface_paroi_opaque: float
    paroi_lourde: bool | None
    upb0_saisi: float | None
    upb_saisi: float | None
    resistance_isolation: float | None
    epaisseur_isolation: float | None
    calcul_ue: bool
    perimetre_ue: float | None
    surface_ue: float | None

    enum_type_adjacence_id: int
    enum_type_plancher_bas_id: int
    enum_methode_saisie_u0_id: int
    enum_methode_saisie_u_id: int
    enum_type_isolation_id: int
    enum_cfg_isolation_lnc_id: int | None
    enum_periode_isolation_id: int | None

    tv_coef_reduction_deperdition_id: int | None
    tv_upb0_id: int | None
    tv_upb_id: int | None

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.id = str(uuid.uuid4())
        entity.reference = strval(data, "reference")
        entity.reference_lnc = strval(data, "reference_lnc")
        entity.description = strval(data, "description")

        entity.surface_aiu = floatval(data, "surface_aiu")
        entity.surface_aue = floatval(data, "surface_aue")
        entity.surface_paroi_opaque = floatval(data, "surface_paroi_opaque")
        entity.paroi_lourde = boolval(data, "paroi_lourde")
        entity.upb0_saisi = floatval(data, "upb0_saisi")
        entity.upb_saisi = floatval(data, "upb_saisi")
        entity.resistance_isolation = floatval(data, "resistance_isolation")
        entity.epaisseur_isolation = floatval(data, "epaisseur_isolation")
        entity.calcul_ue = boolval(data, "calcul_ue")
        entity.perimetre_ue = floatval(data, "perimetre_ue")
        entity.surface_ue = floatval(data, "surface_ue")

        entity.enum_type_adjacence_id = intval(data, "enum_type_adjacence_id")
        entity.enum_methode_saisie_u_id = intval(data, "enum_methode_saisie_u_id")
        entity.enum_type_plancher_bas_id = intval(data, "enum_type_plancher_bas_id")
        entity.enum_methode_saisie_u0_id = intval(data, "enum_methode_saisie_u0_id")
        entity.enum_type_isolation_id = intval(data, "enum_type_isolation_id")
        entity.enum_cfg_isolation_lnc_id = intval(data, "enum_cfg_isolation_lnc_id")
        entity.enum_periode_isolation_id = intval(data, "enum_periode_isolation_id")

        entity.tv_upb0_id = intval(data, "tv_upb0_id")
        entity.tv_upb_id = intval(data, "tv_upb_id")
        entity.tv_coef_reduction_deperdition_id = intval(
            data, "tv_coef_reduction_deperdition_id"
        )

        return entity
