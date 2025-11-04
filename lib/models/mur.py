import uuid
from typing import Self
from .utils import strval, intval, floatval, boolval


class Mur:
    id: str
    reference: str
    reference_lnc: str | None
    description: str | None

    surface_aiu: float | None
    surface_aue: float | None
    surface_paroi_totale: float | None
    surface_paroi_opaque: float
    paroi_lourde: bool | None
    umur0_saisi: float | None
    epaisseur_structure: float | None
    enduit_isolant_paroi_ancienne: bool
    umur_saisi: float | None
    resistance_isolation: float | None
    epaisseur_isolation: float | None

    enum_type_adjacence_id: int
    enum_methode_saisie_u_id: int
    enum_type_doublage_id: int
    enum_type_isolation_id: int
    enum_materiaux_structure_mur_id: int
    enum_methode_saisie_u0_id: int
    enum_orientation_id: int
    enum_cfg_isolation_lnc_id: int | None
    enum_periode_isolation_id: int | None

    tv_umur_id: int | None
    tv_umur0_id: int | None
    tv_coef_reduction_deperdition_id: int | None

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.id = str(uuid.uuid4())
        entity.reference = strval(data, "reference")
        entity.reference_lnc = strval(data, "reference_lnc")
        entity.description = strval(data, "description")

        entity.surface_aiu = floatval(data, "surface_aiu")
        entity.surface_aue = floatval(data, "surface_aue")
        entity.surface_paroi_totale = floatval(data, "surface_paroi_totale")
        entity.surface_paroi_opaque = floatval(data, "surface_paroi_opaque")
        entity.paroi_lourde = boolval(data, "paroi_lourde")
        entity.umur0_saisi = floatval(data, "umur0_saisi")
        entity.epaisseur_structure = floatval(data, "epaisseur_structure")
        entity.enum_materiaux_structure_mur_id = intval(
            data, "enum_materiaux_structure_mur_id"
        )
        entity.enduit_isolant_paroi_ancienne = boolval(
            data, "enduit_isolant_paroi_ancienne"
        )
        entity.umur_saisi = floatval(data, "umur_saisi")
        entity.resistance_isolation = floatval(data, "resistance_isolation")
        entity.epaisseur_isolation = floatval(data, "epaisseur_isolation")

        entity.enum_methode_saisie_u0_id = intval(data, "enum_methode_saisie_u0_id")
        entity.enum_methode_saisie_u_id = intval(data, "enum_methode_saisie_u_id")
        entity.enum_type_doublage_id = intval(data, "enum_type_doublage_id")
        entity.enum_type_isolation_id = intval(data, "enum_type_isolation_id")
        entity.enum_type_adjacence_id = intval(data, "enum_type_adjacence_id")
        entity.enum_orientation_id = intval(data, "enum_orientation_id")
        entity.enum_cfg_isolation_lnc_id = intval(data, "enum_cfg_isolation_lnc_id")
        entity.enum_periode_isolation_id = intval(data, "enum_periode_isolation_id")

        entity.tv_umur0_id = intval(data, "tv_umur0_id")
        entity.tv_umur_id = intval(data, "tv_umur_id")
        entity.tv_coef_reduction_deperdition_id = intval(
            data, "tv_coef_reduction_deperdition_id"
        )

        return entity
