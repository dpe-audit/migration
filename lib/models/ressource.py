import uuid
from typing import Self
from abc import ABC
from .administratif import Administratif
from .logement import Logement
from .utils import strval, intval, floatval, boolval


class LogementVisite:
    id: str
    description: str | None
    surface_habitable_logement: float
    enum_position_etage_logement_id: int
    enum_typologie_logement_id: int

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.id = str(uuid.uuid4())
        entity.description = strval(data, "description")
        entity.surface_habitable_logement = floatval(data, "surface_habitable_logement")
        entity.enum_position_etage_logement_id = intval(
            data, "enum_position_etage_logement_id"
        )
        entity.enum_typologie_logement_id = intval(data, "enum_typologie_logement_id")
        return entity


class DPEImmeuble:
    logement_visite_collection: list[LogementVisite]

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.logement_visite_collection = [
            LogementVisite.from_data(item)
            for item in data.get("logement_visite_collection", [])
        ]
        return entity


class Ressource(ABC):
    def get_administratif(self) -> Administratif:
        raise NotImplementedError

    def get_logement(self) -> Logement:
        raise NotImplementedError

    def get_dpe_immeuble(self) -> DPEImmeuble | None:
        raise NotImplementedError


class Audit(Ressource):
    id: str
    hashkey: str
    version: str

    administratif: Administratif
    dpe_immeuble: DPEImmeuble | None
    logement_collection: list[Logement]

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.id = strval(data, "id")
        entity.hashkey = strval(data, "hashkey")
        entity.version = strval(data, "version")
        entity.administratif = Administratif.from_data(data.get("administratif", {}))
        entity.dpe_immeuble = (
            DPEImmeuble.from_data(item)
            if (item := data.get("dpe_immeuble", None))
            else None
        )
        entity.logement_collection = [
            Logement.from_data(item) for item in data.get("logement_collection", [])
        ]
        return entity

    def get_logement(self) -> Logement:
        for item in self.logement_collection:
            if item.caracteristique_generale.etat_initial:
                return item

    def get_administratif(self) -> Administratif:
        return self.administratif

    def get_dpe_immeuble(self) -> DPEImmeuble | None:
        return self.dpe_immeuble


class DPE:
    id: str
    hashkey: str
    version: str

    administratif: Administratif
    logement: Logement
    dpe_immeuble: DPEImmeuble | None

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.id = strval(data, "id")
        entity.hashkey = strval(data, "hashkey")
        entity.version = strval(data, "version")
        entity.administratif = Administratif.from_data(data.get("administratif", {}))
        entity.logement = Logement.from_data(data.get("logement", {}))
        entity.dpe_immeuble = (
            DPEImmeuble.from_data(item)
            if (item := data.get("dpe_immeuble", None))
            else None
        )
        return entity

    def get_administratif(self) -> Administratif:
        return self.administratif

    def get_logement(self) -> Logement:
        return self.logement

    def get_dpe_immeuble(self) -> DPEImmeuble | None:
        return self.dpe_immeuble
