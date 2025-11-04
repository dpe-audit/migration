import uuid
from datetime import date
from typing import Self
from .utils import strval, intval, floatval, boolval, dateval


class GenerateurEcs:
    id: str
    reference: str
    reference_generateur_mixte: str | None
    identifiant_reseau_chaleur: str | None
    date_arrete_reseau_chaleur: date | None
    description: str | None

    position_volume_chauffe: bool
    volume_stockage: float
    position_volume_chauffe_stockage: bool | None
    presence_ventouse: bool | None
    pn: float | None
    qp0: float | None
    pveilleuse: float | None
    rpn: float | None
    cop: float | None

    enum_type_generateur_ecs_id: int
    enum_usage_generateur_id: int
    enum_type_energie_id: int
    enum_methode_saisie_carac_sys_id: int
    enum_periode_installation_ecs_thermo_id: int | None
    enum_type_stockage_ecs_id: int | None

    tv_generateur_combustion_id: int | None
    tv_pertes_stockage_id: int | None
    tv_scop_id: int | None
    tv_reseau_chaleur_id: int | None

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.id = str(uuid.uuid4())
        entity.reference = strval(data, "reference")
        entity.reference_generateur_mixte = strval(data, "reference_generateur_mixte")
        entity.identifiant_reseau_chaleur = strval(data, "identifiant_reseau_chaleur")
        entity.date_arrete_reseau_chaleur = dateval(data, "date_arrete_reseau_chaleur")
        entity.description = strval(data, "description")

        entity.position_volume_chauffe = boolval(data, "position_volume_chauffe")
        entity.position_volume_chauffe_stockage = boolval(
            data, "position_volume_chauffe_stockage"
        )
        entity.presence_ventouse = boolval(data, "presence_ventouse")

        entity.volume_stockage = floatval(data, "volume_stockage")
        entity.pn = floatval(data, "pn")
        entity.qp0 = floatval(data, "qp0")
        entity.pveilleuse = floatval(data, "pveilleuse")
        entity.rpn = floatval(data, "rpn")
        entity.cop = floatval(data, "cop")

        entity.enum_type_generateur_ecs_id = intval(data, "enum_type_generateur_ecs_id")
        entity.enum_usage_generateur_id = intval(data, "enum_usage_generateur_id")
        entity.enum_type_energie_id = intval(data, "enum_type_energie_id")
        entity.enum_methode_saisie_carac_sys_id = intval(
            data, "enum_methode_saisie_carac_sys_id"
        )
        entity.enum_periode_installation_ecs_thermo_id = intval(
            data, "enum_periode_installation_ecs_thermo_id"
        )
        entity.enum_type_stockage_ecs_id = intval(data, "enum_type_stockage_ecs_id")

        entity.tv_generateur_combustion_id = intval(data, "tv_generateur_combustion_id")
        entity.tv_pertes_stockage_id = intval(data, "tv_pertes_stockage_id")
        entity.tv_scop_id = intval(data, "tv_scop_id")
        entity.tv_reseau_chaleur_id = intval(data, "tv_reseau_chaleur_id")

        return entity


class InstallationEcs:
    id: str
    reference: str
    description: str | None

    surface_habitable: float
    nombre_logement: int
    rdim: float
    nombre_niveau_installation_ecs: int
    reseau_distribution_isole: bool
    fecs_saisi: float | None
    ratio_virtualisation: float | None
    cle_repartition_ecs: float | None

    enum_cfg_installation_ecs_id: int
    enum_type_installation_id: int
    enum_bouclage_reseau_ecs_id: int
    enum_methode_calcul_conso_id: int
    enum_methode_saisie_fact_couv_sol_id: int | None
    enum_type_installation_solaire_id: int | None

    tv_rendement_distribution_ecs_id: int
    tv_facteur_couverture_solaire_id: int | None

    generateur_ecs_collection: list[GenerateurEcs]

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.id = str(uuid.uuid4())
        entity.reference = strval(data, "reference")
        entity.description = strval(data, "description")

        entity.surface_habitable = floatval(data, "surface_habitable")
        entity.nombre_logement = floatval(data, "nombre_logement")
        entity.rdim = floatval(data, "rdim")
        entity.nombre_niveau_installation_ecs = intval(
            data, "nombre_niveau_installation_ecs"
        )
        entity.reseau_distribution_isole = boolval(data, "reseau_distribution_isole")
        entity.fecs_saisi = floatval(data, "fecs_saisi")
        entity.ratio_virtualisation = floatval(data, "ratio_virtualisation")
        entity.cle_repartition_ecs = floatval(data, "cle_repartition_ecs")

        entity.enum_cfg_installation_ecs_id = intval(
            data, "enum_cfg_installation_ecs_id"
        )
        entity.enum_type_installation_id = intval(data, "enum_type_installation_id")
        entity.enum_bouclage_reseau_ecs_id = intval(data, "enum_bouclage_reseau_ecs_id")
        entity.enum_methode_calcul_conso_id = intval(
            data, "enum_methode_calcul_conso_id"
        )
        entity.enum_methode_saisie_fact_couv_sol_id = intval(
            data, "enum_methode_saisie_fact_couv_sol_id"
        )
        entity.enum_type_installation_solaire_id = intval(
            data, "enum_type_installation_solaire_id"
        )
        entity.tv_rendement_distribution_ecs_id = intval(
            data, "tv_rendement_distribution_ecs_id"
        )
        entity.tv_facteur_couverture_solaire_id = intval(
            data, "tv_facteur_couverture_solaire_id"
        )
        entity.generateur_ecs_collection = [
            GenerateurEcs.from_data(item)
            for item in data.get("generateur_ecs_collection", [])
        ]
