from ..models.ressource import Ressource
from ..models.logement import Logement
from ..models.baie_vitree import BaieVitree, MasqueLointainNonHomogene


def to_configuration_masque_proche(data: BaieVitree) -> str | None:
    match data.tv_coef_masque_proche_id:
        case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12:
            return "fond_balcon"
        case 13 | 14 | 15 | 16:
            return "balcon_ou_auvent"
        case 17:
            return "paroi_laterale_sans_obstacle_au_sud"
        case 18:
            return "paroi_laterale_avec_obstacle_au_sud"
        case _:
            return None


def to_configuration_masque_lointain_homogene(data: BaieVitree) -> str | None:
    return "homogene" if data.tv_coef_masque_lointain_homogene_id is not None else None


def to_orientation_masque_proche(data: BaieVitree) -> float | None:
    match data.tv_coef_masque_proche_id:
        case 1 | 2 | 3 | 4:
            return 0.0
        case 5 | 6 | 7 | 8:
            return 180.0
        case 9 | 10 | 11 | 12:
            return 90.0
        case _:
            return None


def to_orientation_masque_lointain_homogene(data: BaieVitree) -> float | None:
    match data.tv_coef_masque_lointain_homogene_id:
        case 1 | 2 | 3 | 4:
            return 0.0
        case 5 | 6 | 7 | 8:
            return 180.0
        case 9 | 10 | 11 | 12:
            return 90.0
        case _:
            return None


def to_orientation_masque_lointain_non_homogene(
    data: MasqueLointainNonHomogene,
) -> float | None:
    match data.tv_coef_masque_lointain_non_homogene_id:
        case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8:
            return 0.0
        case 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20:
            return 90.0


def to_hauteur_masque_lointain_homogene(data: BaieVitree) -> float | None:
    match data.tv_coef_masque_lointain_homogene_id:
        case 1 | 5 | 9:
            return 7.5
        case 2 | 6 | 10:
            return 22.5
        case 3 | 7 | 11:
            return 45.0
        case 4 | 8 | 12:
            return 75.0
        case _:
            return None


def to_hauteur_masque_lointain_non_homogene(
    data: MasqueLointainNonHomogene,
) -> float | None:
    match data.tv_coef_masque_lointain_non_homogene_id:
        case 1 | 5 | 9 | 13 | 17:
            return 7.5
        case 2 | 6 | 10 | 14 | 18:
            return 22.5
        case 3 | 7 | 11 | 15 | 19:
            return 45.0
        case 4 | 8 | 12 | 16 | 20:
            return 75.0


def to_profondeur_masque_proche(data: BaieVitree) -> float | None:
    match data.tv_coef_masque_proche_id:
        case 1 | 5 | 9 | 13:
            return 0.5
        case 2 | 6 | 10 | 14:
            return 1.5
        case 3 | 7 | 11 | 15:
            return 2.5
        case 4 | 8 | 12 | 16:
            return 3.5
        case _:
            return None


def to_secteur(data: MasqueLointainNonHomogene) -> str:
    match data.tv_coef_masque_lointain_non_homogene_id:
        case 1 | 2 | 3 | 4:
            return "lateral"
        case 5 | 6 | 7 | 8:
            return "central"
        case 9 | 10 | 11 | 12:
            return "lateral_sud"
        case 13 | 14 | 15 | 16:
            return "central_sud"
        case 17 | 18 | 19 | 20:
            return "lateral"


def to_masque_proche(data: BaieVitree) -> dict | None:
    if to_configuration_masque_proche(data) is None:
        return None

    entity = {}
    entity["id"] = data.id
    entity["description"] = "Masque proche"
    entity["type"] = "proche"
    entity["configuration"] = to_configuration_masque_proche(data)
    entity["orientation"] = to_orientation_masque_proche(data)
    entity["profondeur"] = to_profondeur_masque_proche(data)
    entity["hauteur"] = None
    entity["secteur"] = None
    return entity


def to_masque_lointain_homogene(data: BaieVitree) -> dict | None:
    if to_configuration_masque_lointain_homogene(data) is None:
        return None

    entity = {}
    entity["id"] = data.id
    entity["description"] = "Masque lointain homogène"
    entity["type"] = "lointain"
    entity["configuration"] = to_configuration_masque_lointain_homogene(data)
    entity["orientation"] = to_orientation_masque_lointain_homogene(data)
    entity["profondeur"] = None
    entity["hauteur"] = to_hauteur_masque_lointain_homogene(data)
    entity["secteur"] = None
    return entity


def to_masque_lointain_non_homogene(data: MasqueLointainNonHomogene) -> dict:
    entity = {}
    entity["id"] = data.id
    entity["description"] = "Masque lointain non homogène"
    entity["type"] = "lointain"
    entity["configuration"] = "non_homogene"
    entity["orientation"] = to_orientation_masque_lointain_non_homogene(data)
    entity["profondeur"] = None
    entity["hauteur"] = to_hauteur_masque_lointain_non_homogene(data)
    entity["secteur"] = to_secteur(data)
    return entity


def to_masques(data: Logement, context: Ressource) -> list[dict]:
    collection = []

    for baie_vitree in data.enveloppe.baie_vitree_collection:
        # Masque proche
        entity = to_masque_proche(baie_vitree)
        if entity is not None:
            collection.append(entity)

        # Masque lointain homogène
        entity = to_masque_lointain_homogene(baie_vitree)
        if entity is not None:
            collection.append(entity)

        # Masques lointains non homogènes
        for (
            masque_lointain_non_homogene
        ) in baie_vitree.masque_lointain_non_homogene_collection:
            entity = to_masque_lointain_non_homogene(masque_lointain_non_homogene)
            collection.append(entity)

    return collection
