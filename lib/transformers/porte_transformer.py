from ..models.logement import Logement
from ..models.porte import Porte
from .paroi_transformer import to_mitoyennete


# Les références internes issues des données XML sont à transformer en UUID
def to_local_non_chauffe_id(data: Porte) -> str | None:
    match to_mitoyennete(data.enum_type_adjacence_id):
        case "local_non_chauffe":
            return data.reference_lnc or data.id
        case _:
            return None


def to_isolation(data: Porte) -> str | None:
    match data.enum_type_porte_id:
        case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12:
            return "non_isole"
        case 13 | 15:
            return "isole"
        case _:
            return None


def to_materiau(data: Porte) -> str | None:
    match data.enum_type_porte_id:
        case 1 | 2 | 3 | 4:
            return "bois"
        case 5 | 6 | 7 | 8:
            return "pvc"
        case 9 | 10 | 11 | 12:
            return "metal"
        case _:
            return None


def to_type_vitrage(data: Porte) -> str | None:
    match data.enum_type_porte_id:
        case 2 | 3 | 6 | 7 | 10 | 11:
            return "simple_vitrage"
        case 4 | 8 | 12 | 15:
            return "double_vitrage"
        case _:
            return None


def to_surface_vitrage(data: Porte) -> float:
    match data.enum_type_porte_id:
        case 2 | 6 | 11:
            return data.surface_porte * 0.15
        case 3 | 7 | 12:
            return data.surface_porte * 0.45
        case 4 | 8 | 10:
            return data.surface_porte * 0.30
        case _:
            return 0.0


def to_presence_sas(data: Porte) -> bool:
    return data.enum_type_porte_id == 14


def to_type_pose(data: Porte) -> str | None:
    match data.enum_type_pose_id:
        case 1:
            return "nu_exterieur"
        case 2:
            return "nu_interieur"
        case 3:
            return "tunnel"
        case _:
            return None


def to_largeur_dormant(data: Porte) -> float | None:
    return data.largeur_dormant * 10 if data.largeur_dormant is not None else None


def to_position(data: Porte) -> dict:
    value = {}
    value["paroi_id"] = None
    value["local_non_chauffe_id"] = to_local_non_chauffe_id(data)
    value["surface"] = data.surface_porte
    value["mitoyennete"] = to_mitoyennete(data.enum_type_adjacence_id)
    value["orientation"] = None
    value["presence_sas"] = to_presence_sas(data)
    value["type_pose"] = to_type_pose(data)
    return value


def to_menuiserie(data: Porte) -> dict:
    value = {}
    value["largeur_dormant"] = to_largeur_dormant(data)
    value["presence_joint"] = data.presence_joint
    value["presence_retour_isolation"] = data.presence_retour_isolation
    return value


def to_vitrage(data: Porte) -> dict:
    value = {}
    value["surface"] = to_surface_vitrage(data)
    value["type"] = to_type_vitrage(data)
    return value


def to_porte(data: Porte) -> dict:
    entity = {}
    entity["id"] = data.id
    entity["description"] = data.description or "-"
    entity["isolation"] = to_isolation(data)
    entity["materiau"] = to_materiau(data)
    entity["annee_installation"] = None
    entity["u"] = data.uporte_saisi

    entity["position"] = to_position(data)
    entity["menuiserie"] = to_menuiserie(data)
    entity["vitrage"] = to_vitrage(data)

    return entity


def to_portes(data: Logement) -> list[dict]:
    return [to_porte(item) for item in data.enveloppe.porte_collection]
