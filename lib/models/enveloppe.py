from typing import Self
from .baie_vitree import BaieVitree
from .ets import Ets
from .mur import Mur
from .plancher_haut import PlancherHaut
from .plancher_bas import PlancherBas
from .porte import Porte
from .pont_thermique import PontThermique
from .utils import intval, boolval


class Inertie:
    inertie_plancher_bas_lourd: bool
    inertie_plancher_haut_lourd: bool
    inertie_paroi_verticale_lourd: bool
    enum_classe_inertie_id: int

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.inertie_plancher_bas_lourd = boolval(data, "inertie_plancher_bas_lourd")
        entity.inertie_plancher_haut_lourd = boolval(
            data, "inertie_plancher_haut_lourd"
        )
        entity.inertie_paroi_verticale_lourd = boolval(
            data, "inertie_paroi_verticale_lourd"
        )
        entity.enum_classe_inertie_id = intval(data, "enum_classe_inertie_id")
        return entity


class Enveloppe:
    inertie: Inertie
    mur_collection: list[Mur]
    plancher_bas_collection: list[PlancherBas]
    plancher_haut_collection: list[PlancherHaut]
    porte_collection: list[Porte]
    baie_vitree_collection: list[BaieVitree]
    ets_collection: list[Ets]
    pont_thermique_collection: list[PontThermique]

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.inertie = Inertie.from_data(data.get("inertie", {}))
        entity.mur_collection = [
            Mur.from_data(item) for item in data.get("mur_collection", [])
        ]
        entity.plancher_bas_collection = [
            PlancherBas.from_data(item)
            for item in data.get("plancher_bas_collection", [])
        ]
        entity.plancher_haut_collection = [
            PlancherHaut.from_data(item)
            for item in data.get("plancher_haut_collection", [])
        ]
        entity.porte_collection = [
            Porte.from_data(item) for item in data.get("porte_collection", [])
        ]
        entity.baie_vitree_collection = [
            BaieVitree.from_data(item)
            for item in data.get("baie_vitree_collection", [])
        ]
        entity.ets_collection = [
            Ets.from_data(item) for item in data.get("ets_collection", [])
        ]
        entity.pont_thermique_collection = [
            PontThermique.from_data(item)
            for item in data.get("pont_thermique_collection", [])
        ]
        return entity
