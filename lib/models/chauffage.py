import uuid
from datetime import date
from typing import Self
from .utils import strval, intval, floatval, boolval, dateval


class EmetteurChauffage:
    id: str
    reference: str
    description: str | None

    surface_chauffee: float
    reseau_distribution_isole: bool | None

    enum_type_emission_distribution_id: int
    enum_equipement_intermittence_id: int
    enum_type_regulation_id: int
    enum_type_chauffage_id: int
    enum_temp_distribution_ch_id: int
    enum_lien_generateur_emetteur_id: int
    enum_periode_installation_emetteur_id: int | None

    tv_rendement_emission_id: int
    tv_rendement_distribution_ch_id: int
    tv_rendement_regulation_id: int
    tv_intermittence_id: int

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.id = str(uuid.uuid4())
        entity.reference = strval(data, "reference")
        entity.description = strval(data, "description")
        entity.surface_chauffee = floatval(data, "surface_chauffee")
        entity.reseau_distribution_isole = boolval(data, "reseau_distribution_isole")

        entity.enum_type_emission_distribution_id = intval(
            data, "enum_type_emission_distribution_id"
        )
        entity.enum_equipement_intermittence_id = intval(
            data, "enum_equipement_intermittence_id"
        )
        entity.enum_type_regulation_id = intval(data, "enum_type_regulation_id")
        entity.enum_type_chauffage_id = intval(data, "enum_type_chauffage_id")
        entity.enum_temp_distribution_ch_id = intval(
            data, "enum_temp_distribution_ch_id"
        )
        entity.enum_lien_generateur_emetteur_id = intval(
            data, "enum_lien_generateur_emetteur_id"
        )
        entity.enum_periode_installation_emetteur_id = intval(
            data, "enum_periode_installation_emetteur_id"
        )

        entity.tv_rendement_emission_id = intval(data, "tv_rendement_emission_id")
        entity.tv_rendement_distribution_ch_id = intval(
            data, "tv_rendement_distribution_ch_id"
        )
        entity.tv_rendement_regulation_id = intval(data, "tv_rendement_regulation_id")
        entity.tv_intermittence_id = intval(data, "tv_intermittence_id")

        return entity


class GenerateurChauffage:
    id: str
    reference: str
    reference_generateur_mixte: str | None
    identifiant_reseau_chaleur: str | None
    date_arrete_reseau_chaleur: date | None
    description: str | None

    position_volume_chauffe: bool
    presence_ventouse: bool | None
    presence_regulation_combustion: bool | None
    n_radiateurs_gaz: int | None
    priorite_generateur_cascade: int | None
    scop: float | None
    pn: float | None
    pveilleuse: float | None
    qp0: float | None
    rpn: float | None
    rpint: float | None
    temp_fonc_30: float | None
    temp_fonc_100: float | None

    enum_type_generateur_ch_id: int
    enum_usage_generateur_id: int
    enum_type_energie_id: int
    enum_methode_saisie_carac_sys_id: int
    enum_lien_generateur_emetteur_id: int

    tv_rendement_generation_id: int | None
    tv_scop_id: int | None
    tv_temp_fonc_100_id: int | None
    tv_temp_fonc_30_id: int | None
    tv_generateur_combustion_id: int | None
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
        entity.presence_ventouse = boolval(data, "presence_ventouse")
        entity.presence_regulation_combustion = boolval(
            data, "presence_regulation_combustion"
        )
        entity.n_radiateurs_gaz = intval(data, "n_radiateurs_gaz")
        entity.priorite_generateur_cascade = intval(data, "priorite_generateur_cascade")
        entity.scop = floatval(data, "scop")
        entity.pn = floatval(data, "pn")
        entity.pveilleuse = floatval(data, "pveilleuse")
        entity.qp0 = floatval(data, "qp0")
        entity.rpn = floatval(data, "rpn")
        entity.rpint = floatval(data, "rpint")
        entity.temp_fonc_30 = floatval(data, "temp_fonc_30")
        entity.temp_fonc_100 = floatval(data, "temp_fonc_100")

        entity.enum_type_generateur_ch_id = intval(data, "enum_type_generateur_ch_id")
        entity.enum_usage_generateur_id = intval(data, "enum_usage_generateur_id")
        entity.enum_type_energie_id = intval(data, "enum_type_energie_id")
        entity.enum_methode_saisie_carac_sys_id = intval(
            data, "enum_methode_saisie_carac_sys_id"
        )
        entity.enum_lien_generateur_emetteur_id = intval(
            data, "enum_lien_generateur_emetteur_id"
        )

        entity.tv_rendement_generation_id = intval(data, "tv_rendement_generation_id")
        entity.tv_scop_id = intval(data, "tv_scop_id")
        entity.tv_temp_fonc_100_id = intval(data, "tv_temp_fonc_100_id")
        entity.tv_temp_fonc_30_id = intval(data, "tv_temp_fonc_30_id")
        entity.tv_generateur_combustion_id = intval(data, "tv_generateur_combustion_id")
        entity.tv_reseau_chaleur_id = intval(data, "tv_reseau_chaleur_id")

        return entity


class InstallationChauffage:
    id: str
    reference: str
    description: str | None

    surface_chauffee: float
    nombre_niveau_installation_ch: int
    rdim: float
    nombre_logement_echantillon: int | None
    ratio_virtualisation: float | None
    coef_ifc: float | None
    cle_repartition_ch: float | None
    fch_saisi: float | None

    enum_cfg_installation_ch_id: int
    enum_type_installation_id: int
    enum_methode_calcul_conso_id: int
    enum_methode_saisie_fact_couv_sol_id: int | None

    tv_facteur_couverture_solaire_id: int | None

    emetteur_chauffage_collection: list[EmetteurChauffage]
    generateur_chauffage_collection: list[GenerateurChauffage]

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.id = str(uuid.uuid4())
        entity.reference = strval(data, "reference")
        entity.description = strval(data, "description")
        entity.surface_chauffee = floatval(data, "surface_chauffee")
        entity.nombre_niveau_installation_ch = intval(
            data, "nombre_niveau_installation_ch"
        )
        entity.rdim = floatval(data, "rdim")
        entity.nombre_logement_echantillon = intval(data, "nombre_logement_echantillon")
        entity.ratio_virtualisation = floatval(data, "ratio_virtualisation")
        entity.coef_ifc = floatval(data, "coef_ifc")
        entity.cle_repartition_ch = floatval(data, "cle_repartition_ch")
        entity.fch_saisi = floatval(data, "fch_saisi")

        entity.enum_cfg_installation_ch_id = intval(data, "enum_cfg_installation_ch_id")
        entity.enum_type_installation_id = intval(data, "enum_type_installation_id")
        entity.enum_methode_calcul_conso_id = intval(
            data, "enum_methode_calcul_conso_id"
        )
        entity.enum_methode_saisie_fact_couv_sol_id = intval(
            data, "enum_methode_saisie_fact_couv_sol_id"
        )
        entity.tv_facteur_couverture_solaire_id = intval(
            data, "tv_facteur_couverture_solaire_id"
        )

        entity.emetteur_chauffage_collection = [
            EmetteurChauffage.from_data(item)
            for item in data.get("emetteur_chauffage_collection", [])
        ]
        entity.generateur_chauffage_collection = [
            GenerateurChauffage.from_data(item)
            for item in data.get("generateur_chauffage_collection", [])
        ]

        return entity
