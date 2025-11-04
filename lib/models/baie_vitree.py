import uuid
from typing import Self
from .utils import strval, intval, floatval, boolval


class DoubleFenetre:
    id: str
    epaisseur_lame: float | None
    vitrage_vir: bool | None
    ug_saisi: float | None
    uw_saisi: float | None
    sw_saisi: float | None

    enum_type_materiaux_menuiserie_id: int
    enum_type_baie_id: int
    enum_type_pose_id: int
    enum_type_vitrage_id: int
    enum_inclinaison_vitrage_id: int
    enum_methode_saisie_perf_vitrage_id: int
    enum_type_gaz_lame_id: int | None

    tv_ug_id: int | None
    tv_uw_id: int | None
    tv_sw_id: int | None

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.id = str(uuid.uuid4())
        entity.epaisseur_lame = floatval(data, "epaisseur_lame")
        entity.ug_saisi = floatval(data, "ug_saisi")
        entity.uw_saisi = floatval(data, "uw_saisi")
        entity.sw_saisi = floatval(data, "sw_saisi")
        entity.vitrage_vir = boolval(data, "vitrage_vir")

        entity.enum_type_baie_id = intval(data, "enum_type_baie_id")
        entity.enum_type_pose_id = intval(data, "enum_type_pose_id")
        entity.enum_type_vitrage_id = intval(data, "enum_type_vitrage_id")
        entity.enum_inclinaison_vitrage_id = intval(data, "enum_inclinaison_vitrage_id")
        entity.enum_methode_saisie_perf_vitrage_id = intval(
            data, "enum_methode_saisie_perf_vitrage_id"
        )
        entity.enum_type_materiaux_menuiserie_id = intval(
            data, "enum_type_materiaux_menuiserie_id"
        )
        entity.enum_type_gaz_lame_id = intval(data, "enum_type_gaz_lame_id")

        entity.tv_ug_id = intval(data, "tv_ug_id")
        entity.tv_sw_id = intval(data, "tv_sw_id")
        entity.tv_uw_id = intval(data, "tv_uw_id")

        return entity


class MasqueLointainNonHomogene:
    id: str
    tv_coef_masque_lointain_non_homogene_id: int

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.id = str(uuid.uuid4())
        entity.tv_coef_masque_lointain_non_homogene_id = intval(
            data, "tv_coef_masque_lointain_non_homogene_id"
        )
        return entity


class BaieVitree:
    id: str
    reference: str
    reference_paroi: str | None
    reference_lnc: str | None
    description: str | None

    surface_totale_baie: float
    largeur_dormant: float
    nb_baie: int
    double_fenetre: bool
    presence_joint: bool
    presence_protection_solaire_hors_fermeture: bool
    presence_retour_isolation: bool
    vitrage_vir: bool | None
    surface_aiu: float | None
    surface_aue: float | None
    epaisseur_lame: float | None
    ujn_saisi: float | None
    sw_saisi: float | None
    ug_saisi: float | None
    uw_saisi: float | None
    uw_1: float | None
    uw_2: float | None
    sw_1: float | None
    sw_2: float | None

    enum_type_adjacence_id: int
    enum_type_materiaux_menuiserie_id: int
    enum_type_baie_id: int
    enum_methode_saisie_perf_vitrage_id: int
    enum_type_fermeture_id: int
    enum_type_pose_id: int
    enum_orientation_id: int
    enum_type_vitrage_id: int
    enum_inclinaison_vitrage_id: int
    enum_type_gaz_lame_id: int | None
    enum_cfg_isolation_lnc_id: int | None

    tv_coef_masque_proche_id: int
    tv_ug_id: int | None
    tv_deltar_id: int | None
    tv_uw_id: int | None
    tv_ujn_id: int | None
    tv_sw_id: int | None
    tv_coef_masque_lointain_homogene_id: int | None
    tv_coef_reduction_deperdition_id: int | None

    baie_vitree_double_fenetre: DoubleFenetre | None
    masque_lointain_non_homogene_collection: list[MasqueLointainNonHomogene]

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.id = str(uuid.uuid4())
        entity.reference = strval(data, "reference")
        entity.reference_paroi = strval(data, "reference_paroi")
        entity.reference_lnc = strval(data, "reference_lnc")
        entity.description = strval(data, "description")

        entity.surface_totale_baie = floatval(data, "surface_totale_baie")
        entity.nb_baie = intval(data, "nb_baie")
        entity.largeur_dormant = floatval(data, "largeur_dormant")
        entity.presence_retour_isolation = boolval(data, "presence_retour_isolation")
        entity.double_fenetre = boolval(data, "double_fenetre")
        entity.presence_joint = boolval(data, "presence_joint")
        entity.presence_protection_solaire_hors_fermeture = boolval(
            data, "presence_protection_solaire_hors_fermeture"
        )
        entity.vitrage_vir = boolval(data, "vitrage_vir")

        entity.surface_aiu = floatval(data, "surface_aiu")
        entity.surface_aue = floatval(data, "surface_aue")
        entity.epaisseur_lame = floatval(data, "epaisseur_lame")
        entity.ug_saisi = floatval(data, "ug_saisi")
        entity.uw_saisi = floatval(data, "uw_saisi")
        entity.uw_1 = floatval(data, "uw_1")
        entity.uw_2 = floatval(data, "uw_2")
        entity.sw_1 = floatval(data, "sw_1")
        entity.sw_2 = floatval(data, "sw_2")
        entity.ujn_saisi = floatval(data, "ujn_saisi")
        entity.sw_saisi = floatval(data, "sw_saisi")

        entity.enum_type_adjacence_id = intval(data, "enum_type_adjacence_id")
        entity.enum_type_fermeture_id = intval(data, "enum_type_fermeture_id")
        entity.enum_type_pose_id = intval(data, "enum_type_pose_id")
        entity.enum_orientation_id = intval(data, "enum_orientation_id")
        entity.enum_type_baie_id = intval(data, "enum_type_baie_id")
        entity.enum_type_vitrage_id = intval(data, "enum_type_vitrage_id")
        entity.enum_inclinaison_vitrage_id = intval(data, "enum_inclinaison_vitrage_id")
        entity.enum_methode_saisie_perf_vitrage_id = intval(
            data, "enum_methode_saisie_perf_vitrage_id"
        )
        entity.enum_type_materiaux_menuiserie_id = intval(
            data, "enum_type_materiaux_menuiserie_id"
        )
        entity.enum_cfg_isolation_lnc_id = intval(data, "enum_cfg_isolation_lnc_id")
        entity.enum_type_gaz_lame_id = intval(data, "enum_type_gaz_lame_id")

        entity.tv_coef_masque_proche_id = intval(data, "tv_coef_masque_proche_id")
        entity.tv_ug_id = intval(data, "tv_ug_id")
        entity.tv_deltar_id = intval(data, "tv_deltar_id")
        entity.tv_ujn_id = intval(data, "tv_ujn_id")
        entity.tv_sw_id = intval(data, "tv_sw_id")
        entity.tv_uw_id = intval(data, "tv_uw_id")
        entity.tv_coef_masque_lointain_homogene_id = intval(
            data, "tv_coef_masque_lointain_homogene_id"
        )
        entity.tv_coef_reduction_deperdition_id = intval(
            data, "tv_coef_reduction_deperdition_id"
        )

        entity.baie_vitree_double_fenetre = (
            DoubleFenetre.from_data(item)
            if (item := data.get("baie_vitree_double_fenetre")) is not None
            else None
        )
        entity.masque_lointain_non_homogene_collection = [
            MasqueLointainNonHomogene.from_data(item)
            for item in data.get("masque_lointain_non_homogene_collection", [])
        ]

        return entity
