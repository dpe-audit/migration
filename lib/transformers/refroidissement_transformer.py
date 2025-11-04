from ..models.ressource import Ressource
from ..models.logement import Logement
from ..models.refroidissement import Climatisation


def to_type_generateur(data: Climatisation) -> str:
    match data.enum_type_generateur_fr_id:
        case 1 | 2 | 3:
            return "pac_air_air"
        case 4 | 5 | 6 | 7:
            return "pac_air_eau"
        case 8 | 9 | 10 | 11:
            return "pac_eau_eau"
        case 12 | 13 | 14 | 15:
            return "pac_eau_glycolee_eau"
        case 16 | 17 | 18 | 19:
            return "pac_geothermique"
        case 20 | 21:
            return "autre_systeme_thermodynamique"
        case 22:
            return "autre"
        case 23:
            return "reseau_froid"


def to_energie_tenerateur(data: Climatisation) -> str:
    match data.enum_type_energie_id:
        case 1 | 12:
            return "electricite"
        case 2:
            return "gaz_naturel"
        case 9 | 10 | 13:
            return "gpl"
        case 15:
            return "reseau_froid"
        case _:
            match data.enum_type_generateur_fr_id:
                case 21:
                    return "gaz_naturel"
                case 23:
                    return "reseau_froid"
                case _:
                    return "electricite"


def to_annee_installation(data: Climatisation, context: Ressource) -> int:
    match data.enum_type_generateur_fr_id:
        case 1 | 4 | 8 | 12 | 16:
            return 2007
        case 2 | 5 | 9 | 13 | 17:
            return 2014
        case 6 | 10 | 14 | 18:
            return 2016
        case 3 | 7 | 11 | 15 | 19:
            return context.get_administratif().annee_etablissement()
        case 20 | 21 | 22 | 23:
            match data.enum_periode_installation_fr_id:
                case 1:
                    return 2007
                case 2:
                    return 2014
                case 3:
                    return context.get_administratif().annee_etablissement()


def to_seer(data: Climatisation) -> float | None:
    if data.eer is None:
        return None
    match data.enum_methode_saisie_carac_sys_id:
        case 6 | 7 | 8:
            return data.eer / 0.95
        case _:
            return None


def to_installation(data: Climatisation) -> dict:
    entity = {}
    entity["id"] = data.id
    entity["description"] = data.description or "-"
    entity["surface"] = data.surface_clim
    return entity


def to_generateur(data: Climatisation, context: Ressource) -> dict:
    entity = {}
    entity["id"] = data.id
    entity["description"] = data.description or "-"
    entity["type"] = to_type_generateur(data)
    entity["energie"] = to_energie_tenerateur(data)
    entity["annee_installation"] = to_annee_installation(data, context)
    entity["seer"] = to_seer(data)
    entity["reseau_froid_id"] = None
    return entity


def to_systeme(data: Climatisation) -> dict:
    entity = {}
    entity["id"] = data.id
    entity["description"] = data.description or "-"
    entity["installation_id"] = data.id
    entity["generateur_id"] = data.id
    return entity


def to_refroidissement(data: Logement, context: Ressource) -> dict:
    registry = []
    aggregate = {}
    aggregate["installations"] = []
    aggregate["generateurs"] = []
    aggregate["systemes"] = []

    for climatisation in data.climatisation_collection:
        if climatisation.id in registry:
            continue

        registry.append(climatisation.id)
        aggregate["installations"].append(to_installation(climatisation))
        aggregate["generateurs"].append(to_generateur(climatisation, context))
        aggregate["systemes"].append(to_systeme(climatisation))

    return aggregate
