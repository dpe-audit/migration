from typing import Self
from .enveloppe import Enveloppe
from .ventilation import Ventilation
from .refroidissement import Climatisation
from .chauffage import InstallationChauffage
from .ecs import InstallationEcs
from .production import ProductionElecEnr
from .utils import intval, floatval, boolval


class CaracteristiqueGenerale:
    hsp: float
    annee_construction: int | None
    surface_habitable_logement: float | None
    surface_habitable_immeuble: float | None
    nombre_niveau_immeuble: int | None
    nombre_niveau_logement: int | None
    nombre_appartement: int | None

    enum_periode_construction_id: int
    enum_methode_application_dpe_log_id: int
    enum_calcul_echantillonnage_id: int | None
    enum_scenario_id: int | None
    enum_etape_id: int | None

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.hsp = floatval(data, "hsp")
        entity.annee_construction = intval(data, "annee_construction")
        entity.surface_habitable_logement = floatval(data, "surface_habitable_logement")
        entity.surface_habitable_immeuble = floatval(data, "surface_habitable_immeuble")
        entity.nombre_niveau_immeuble = intval(data, "nombre_niveau_immeuble")
        entity.nombre_niveau_logement = intval(data, "nombre_niveau_logement")
        entity.nombre_appartement = intval(data, "nombre_appartement")
        entity.enum_periode_construction_id = intval(
            data, "enum_periode_construction_id"
        )
        entity.enum_methode_application_dpe_log_id = intval(
            data, "enum_methode_application_dpe_log_id"
        )
        entity.enum_calcul_echantillonnage_id = intval(
            data, "enum_calcul_echantillonnage_id"
        )
        entity.enum_scenario_id = intval(data, "enum_scenario_id")
        entity.enum_etape_id = intval(data, "enum_etape_id")
        return entity

    def etat_initial(self) -> bool:
        return self.enum_scenario_id == None or self.enum_scenario_id == 0


class Meteo:
    batiment_materiaux_anciens: bool
    altitude: int | None

    enum_zone_climatique_id: int
    enum_classe_altitude_id: int

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.batiment_materiaux_anciens = boolval(data, "batiment_materiaux_anciens")
        entity.altitude = intval(data, "altitude")
        entity.enum_zone_climatique_id = intval(data, "enum_zone_climatique_id")
        entity.enum_classe_altitude_id = intval(data, "enum_classe_altitude_id")
        return entity


class Deperdition:
    hvent: float
    hperm: float
    deperdition_renouvellement_air: float
    deperdition_mur: float
    deperdition_plancher_bas: float
    deperdition_plancher_haut: float
    deperdition_baie_vitree: float
    deperdition_porte: float
    deperdition_pont_thermique: float
    deperdition_enveloppe: float

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.hvent = floatval(data, "hvent")
        entity.hperm = floatval(data, "hperm")
        entity.deperdition_renouvellement_air = floatval(
            data, "deperdition_renouvellement_air"
        )
        entity.deperdition_mur = floatval(data, "deperdition_mur")
        entity.deperdition_plancher_bas = floatval(data, "deperdition_plancher_bas")
        entity.deperdition_plancher_haut = floatval(data, "deperdition_plancher_haut")
        entity.deperdition_baie_vitree = floatval(data, "deperdition_baie_vitree")
        entity.deperdition_porte = floatval(data, "deperdition_porte")
        entity.deperdition_pont_thermique = floatval(data, "deperdition_pont_thermique")
        entity.deperdition_enveloppe = floatval(data, "deperdition_enveloppe")
        return entity


class ApportBesoin:
    surface_sud_equivalente: float
    apport_solaire_fr: float
    apport_interne_fr: float
    apport_solaire_ch: float
    apport_interne_ch: float
    fraction_apport_gratuit_ch: float
    fraction_apport_gratuit_depensier_ch: float
    pertes_distribution_ecs_recup: float
    pertes_distribution_ecs_recup_depensier: float
    pertes_stockage_ecs_recup: float
    pertes_generateur_ch_recup: float
    pertes_generateur_ch_recup_depensier: float
    nadeq: float
    v40_ecs_journalier: float
    v40_ecs_journalier_depensier: float
    besoin_ch: float
    besoin_ch_depensier: float
    besoin_ecs: float
    besoin_ecs_depensier: float
    besoin_fr: float
    besoin_fr_depensier: float

    @classmethod
    def from_data(cls, data: dict) -> Self:
        value = cls()
        value.surface_sud_equivalente = floatval(data, "surface_sud_equivalente")
        value.apport_solaire_fr = floatval(data, "apport_solaire_fr")
        value.apport_interne_fr = floatval(data, "apport_interne_fr")
        value.apport_solaire_ch = floatval(data, "apport_solaire_ch")
        value.apport_interne_ch = floatval(data, "apport_interne_ch")
        value.fraction_apport_gratuit_ch = floatval(data, "fraction_apport_gratuit_ch")
        value.fraction_apport_gratuit_depensier_ch = floatval(
            data, "fraction_apport_gratuit_depensier_ch"
        )
        value.pertes_distribution_ecs_recup = floatval(
            data, "pertes_distribution_ecs_recup"
        )
        value.pertes_distribution_ecs_recup_depensier = floatval(
            data, "pertes_distribution_ecs_recup_depensier"
        )
        value.pertes_stockage_ecs_recup = floatval(data, "pertes_stockage_ecs_recup")
        value.pertes_generateur_ch_recup = floatval(data, "pertes_generateur_ch_recup")
        value.pertes_generateur_ch_recup_depensier = floatval(
            data, "pertes_generateur_ch_recup_depensier"
        )
        value.nadeq = floatval(data, "nadeq")
        value.v40_ecs_journalier = floatval(data, "v40_ecs_journalier")
        value.v40_ecs_journalier_depensier = floatval(
            data, "v40_ecs_journalier_depensier"
        )
        value.besoin_ch = floatval(data, "besoin_ch")
        value.besoin_ch_depensier = floatval(data, "besoin_ch_depensier")
        value.besoin_ecs = floatval(data, "besoin_ecs")
        value.besoin_ecs_depensier = floatval(data, "besoin_ecs_depensier")
        value.besoin_fr = floatval(data, "besoin_fr")
        value.besoin_fr_depensier = floatval(data, "besoin_fr_depensier")
        return value


class ConfortEte:
    inertie_lourde: bool
    protection_solaire_exterieure: bool
    isolation_toiture: bool | None
    aspect_traversant: bool | None
    brasseur_air: bool | None

    enum_indicateur_confort_ete_id: int

    @classmethod
    def from_data(cls, data: dict) -> Self:
        value = cls()
        value.inertie_lourde = boolval(data, "inertie_lourde")
        value.protection_solaire_exterieure = boolval(
            data, "protection_solaire_exterieure"
        )
        value.isolation_toiture = boolval(data, "isolation_toiture")
        value.aspect_traversant = boolval(data, "aspect_traversant")
        value.brasseur_air = boolval(data, "brasseur_air")
        value.enum_indicateur_confort_ete_id = intval(
            data, "enum_indicateur_confort_ete_id"
        )
        return value


class Sortie:
    deperdition: Deperdition
    apport_et_besoin: ApportBesoin
    confort_ete: ConfortEte

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.deperdition = Deperdition.from_data(data.get("deperdition", {}))
        entity.apport_et_besoin = ApportBesoin.from_data(
            data.get("apport_et_besoin", {})
        )
        entity.confort_ete = ConfortEte.from_data(data.get("confort_ete", {}))
        return entity


class Logement:
    caracteristique_generale: CaracteristiqueGenerale
    meteo: Meteo
    enveloppe: Enveloppe
    ventilation_collection: list[Ventilation]
    climatisation_collection: list[Climatisation]
    installation_ecs_collection: list[InstallationEcs]
    installation_chauffage_collection: list[InstallationChauffage]
    production_elec_enr: ProductionElecEnr | None
    sortie: Sortie

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.caracteristique_generale = CaracteristiqueGenerale.from_data(
            data.get("caracteristique_generale", {})
        )
        entity.meteo = Meteo.from_data(data.get("meteo", {}))
        entity.enveloppe = Enveloppe.from_data(data.get("enveloppe", {}))
        entity.ventilation_collection = [
            Ventilation.from_data(item)
            for item in data.get("ventilation_collection", [])
        ]
        entity.climatisation_collection = [
            Climatisation.from_data(item)
            for item in data.get("climatisation_collection", [])
        ]
        entity.installation_ecs_collection = [
            InstallationEcs.from_data(item)
            for item in data.get("installation_ecs_collection", [])
        ]
        entity.installation_chauffage_collection = [
            InstallationChauffage.from_data(item)
            for item in data.get("installation_chauffage_collection", [])
        ]
        entity.production_elec_enr = (
            ProductionElecEnr.from_data(item)
            if (item := data.get("production_elec_enr"))
            else None
        )
        entity.sortie = Sortie.from_data(data.get("sortie", {}))

        return entity
