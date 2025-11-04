import uuid
from typing import Self
from .utils import strval, intval, floatval, boolval


class PanneauPv:
    id: str

    surface_totale_capteurs: float | None
    ratio_virtualisation: float | None
    nombre_modules: int | None

    enum_orientation_pv_id: int | None
    enum_inclinaison_pv_id: int | None
    tv_coef_orientation_pv_id: int | None

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.id = str(uuid.uuid4())
        entity.surface_totale_capteurs = floatval(data, "surface_totale_capteurs")
        entity.ratio_virtualisation = floatval(data, "ratio_virtualisation")
        entity.nombre_modules = intval(data, "nombre_modules")
        entity.enum_orientation_pv_id = intval(data, "enum_orientation_pv_id")
        entity.enum_inclinaison_pv_id = intval(data, "enum_inclinaison_pv_id")
        entity.tv_coef_orientation_pv_id = intval(data, "tv_coef_orientation_pv_id")
        return entity


class ProductionElecEnr:
    reference: str
    description: str | None
    presence_production_pv: bool
    taux_autoproduction: float | None
    production_pv: float
    conso_elec_ac: float

    enum_type_enr_id: int

    panneaux_pv_collection: list[PanneauPv]

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.reference = strval(data, "reference")
        entity.description = strval(data, "description")
        entity.presence_production_pv = boolval(data, "presence_production_pv")
        entity.enum_type_enr_id = intval(data, "enum_type_enr_id")
        entity.taux_autoproduction = floatval(data, "taux_autoproduction")
        entity.production_pv = floatval(data, "production_pv")
        entity.conso_elec_ac = floatval(data, "conso_elec_ac")
        entity.panneaux_pv_collection = [
            PanneauPv.from_data(item) for item in data.get("panneaux_pv_collection", [])
        ]
        return entity
