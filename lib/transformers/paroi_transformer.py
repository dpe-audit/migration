from ..models.ressource import Ressource
from ..models.logement import Logement


def to_mitoyennete(enum_type_adjacence_id: int) -> str:
    match enum_type_adjacence_id:
        case 1:
            return "exterieur"
        case 2:
            return "enterre"
        case 3:
            return "vide_sanitaire"
        case 4:
            return "local_non_residentiel"
        case 5:
            return "terre_plein"
        case 6:
            return "sous_sol_non_chauffe"
        case 7:
            return "local_non_accessible"
        case 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 21:
            return "local_non_chauffe"
        case 20:
            return "local_non_residentiel"
        case 22:
            return "local_residentiel"


def to_inertie(data: Logement) -> str | None:
    match data.enveloppe.inertie.inertie_plancher_bas_lourd:
        case True:
            return "lourde"
        case False:
            return "legere"
        case _:
            return None


def to_etat_isolation(enum_type_isolation_id: int) -> str | None:
    match enum_type_isolation_id:
        case 2:
            return "non_isole"
        case 3 | 4 | 5 | 6 | 7 | 8:
            return "isole"
        case _:
            return None


def to_type_isolation(enum_type_isolation_id: int | None) -> str | None:
    match enum_type_isolation_id:
        case 3:
            return "iti"
        case 4:
            return "ite"
        case 5:
            return "itr"
        case 6:
            return "iti_ite"
        case 7:
            return "iti_itr"
        case 8:
            return "ite_itr"
        case _:
            return None


def to_annee_isolation(
    enum_periode_isolation_id: int | None, ressource: Ressource
) -> int | None:
    match enum_periode_isolation_id:
        case 1:
            return 1947
        case 2:
            return 1974
        case 3:
            return 1977
        case 4:
            return 1982
        case 5:
            return 1988
        case 6:
            return 2000
        case 7:
            return 2005
        case 8:
            return 2012
        case 9:
            return 2021
        case _:
            return ressource.get_administratif().annee_etablissement()
