import uuid
from typing import Self
from .utils import strval, intval, floatval, boolval


class Porte:
    id: str
    reference: str
    reference_paroi: str | None
    reference_lnc: str | None
    description: str | None

    surface_porte: float
    presence_joint: bool
    presence_retour_isolation: bool | None
    surface_aiu: float | None
    surface_aue: float | None
    uporte_saisi: float | None
    nb_portes: int | None
    largeur_dormant: float | None

    enum_methode_saisie_uporte_id: int
    enum_type_adjacence_id: int
    enum_type_porte_id: int
    enum_type_pose_id: int
    enum_cfg_isolation_lnc_id: int | None

    tv_uporte_id: int | None

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.id = str(uuid.uuid4())
        entity.reference = strval(data, "reference")
        entity.reference_paroi = strval(data, "reference_paroi")
        entity.reference_lnc = strval(data, "reference_lnc")
        entity.description = strval(data, "description")
        entity.surface_aiu = floatval(data, "surface_aiu")
        entity.surface_aue = floatval(data, "surface_aue")
        entity.surface_porte = floatval(data, "surface_porte")
        entity.uporte_saisi = floatval(data, "uporte_saisi")
        entity.nb_portes = intval(data, "nb_portes")
        entity.largeur_dormant = floatval(data, "largeur_dormant")
        entity.presence_joint = boolval(data, "presence_joint")
        entity.presence_retour_isolation = boolval(data, "presence_retour_isolation")

        entity.enum_type_pose_id = intval(data, "enum_type_pose_id")
        entity.enum_methode_saisie_uporte_id = intval(
            data, "enum_methode_saisie_uporte_id"
        )
        entity.enum_type_porte_id = intval(data, "enum_type_porte_id")
        entity.enum_type_adjacence_id = intval(data, "enum_type_adjacence_id")
        entity.enum_cfg_isolation_lnc_id = intval(data, "enum_cfg_isolation_lnc_id")
        entity.tv_uporte_id = intval(data, "tv_uporte_id")
    
        return entity
