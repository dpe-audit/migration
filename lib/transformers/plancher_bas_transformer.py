from ..models.ressource import Ressource
from ..models.logement import Logement
from ..models.plancher_bas import PlancherBas
from .paroi_transformer import (
    to_mitoyennete,
    to_inertie,
    to_etat_isolation,
    to_type_isolation,
    to_annee_isolation,
)


def to_type_structure(data: PlancherBas) -> str | None:
    match data.enum_type_plancher_bas_id:
        case 2:
            return "plancher_avec_ou_sans_remplissage"
        case 3:
            return "plancher_entre_solives_metalliques"
        case 4:
            return "plancher_entre_solives_bois"
        case 5:
            return "plancher_bois_sur_solives_metalliques"
        case 6:
            return "bardaux_et_remplissage"
        case 7:
            return "voutains_sur_solives_metalliques"
        case 8:
            return "voutains_briques_ou_moellons"
        case 9:
            return "dalle_beton"
        case 10:
            return "plancher_bois_sur_solives_bois"
        case 11:
            return "plancher_lourd_type_entrevous_terre_cuite_ou_poutrelles_beton"
        case 12:
            return "plancher_entrevous_isolant"
        case _:
            return None


# Les références internes issues des données XML sont à transformer en UUID
def to_local_non_chauffe_id(data: PlancherBas) -> str | None:
    match to_mitoyennete(data.enum_type_adjacence_id):
        case "local_non_chauffe":
            return data.reference_lnc or data.id
        case _:
            return None


def to_position(data: PlancherBas) -> dict:
    value = {}
    value["local_non_chauffe_id"] = to_local_non_chauffe_id(data)
    value["surface"] = data.surface_paroi_opaque
    value["mitoyennete"] = to_mitoyennete(data.enum_type_adjacence_id)
    value["surface_ue"] = data.surface_ue
    value["perimetre_ue"] = data.perimetre_ue
    return value


def to_isolation(data: PlancherBas, context: Ressource) -> dict:
    value = {}
    value["etat"] = to_etat_isolation(data.enum_type_isolation_id)
    value["type"] = to_type_isolation(data.enum_type_isolation_id)
    value["epaisseur"] = (
        data.epaisseur_isolation * 10 if data.epaisseur_isolation is not None else None
    )
    value["resistance_thermique"] = data.resistance_isolation
    value["annee_installation"] = to_annee_isolation(
        data.enum_periode_isolation_id, context
    )

    return value


def to_plancher_bas(data: PlancherBas, context: Ressource) -> dict:
    value = {}
    value["description"] = data.description or "-"
    value["type_structure"] = to_type_structure(data)
    value["inertie"] = to_inertie(context.get_logement())
    value["annee_construction"] = None
    value["annee_renovation"] = None
    value["u0"] = data.upb0_saisi
    value["u"] = data.upb_saisi
    value["position"] = to_position(data)
    value["isolation"] = to_isolation(data, context)
    return value


def to_planchers_bas(data: Logement, context: Ressource) -> list:
    return [
        to_plancher_bas(item, context)
        for item in data.enveloppe.plancher_bas_collection
    ]
