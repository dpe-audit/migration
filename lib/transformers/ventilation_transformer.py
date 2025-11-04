from ..models.ressource import Ressource
from ..models.logement import Logement
from ..models.ventilation import Ventilation


def to_type_ventilation(data: Ventilation) -> str:
    match data.enum_type_ventilation_id:
        case 1:
            return "ventilation_naturelle_ouverture_fenetres"
        case 2:
            return "ventilation_naturelle_entrees_air_hautes_basses"
        case 25:
            return "ventilation_naturelle_conduit"
        case 34:
            return "ventilation_naturelle_conduit_entrees_air_hygroreglables"
        case _:
            return "ventilation_mecanique"


def to_type_generateur(data: Ventilation) -> str | None:
    match data.enum_type_ventilation_id:
        case 3 | 4 | 5 | 6 | 7 | 8 | 9 | 13 | 14 | 15:
            return "vmc_simple_flux"
        case 10 | 11 | 12:
            return "vmc_simple_flux_gaz"
        case 16 | 17 | 18:
            return "vmc_basse_pression"
        case 19 | 20 | 21 | 22 | 23 | 24:
            return "vmc_double_flux"
        case 26 | 27 | 28 | 29 | 30 | 31:
            return "ventilation_hybride"
        case 32 | 33:
            return "ventilation_mecanique"
        case 35 | 36 | 37 | 38:
            return "puit_climatique"
        case _:
            return None


def to_type_vmc(data: Ventilation) -> str | None:
    match data.enum_type_ventilation_id:
        case 1 | 2 | 25 | 34:
            return None
        case 3 | 4 | 5 | 6 | 16 | 26 | 27 | 28:
            return "autoreglable"
        case 7 | 8 | 9 | 17:
            return "hygroreglable_type_a"
        case 13 | 14 | 15 | 18 | 29 | 30 | 31:
            return "hygroreglable_type_b"
        case _:
            match (data.pvent_moy):
                case 35 | 65:
                    return "autoreglable"
                case 15 | 50:
                    return "hygroreglable_type_a"
                case 80 | 35:
                    return "hygroreglable_type_b"
                case _:
                    return "autoreglable"


def to_annee_installation_generateur(
    data: Ventilation, context: Ressource
) -> int | None:
    match data.enum_type_ventilation_id:
        case 3:
            return 1981
        case 4 | 7 | 10 | 13 | 26 | 29:
            return 2000
        case 5 | 8 | 11 | 14 | 19 | 21 | 23 | 27 | 30 | 32 | 35 | 37:
            return 2012
        case 6 | 9 | 12 | 15 | 20 | 22 | 24 | 28 | 31 | 33 | 36 | 38:
            return context.get_administratif().annee_etablissement()
        case _:
            return None


def to_presence_echangeur_thermique(data: Ventilation) -> bool:
    match data.enum_type_ventilation_id:
        case 19 | 20 | 21 | 22 | 37 | 38:
            return True
        case _:
            return False


def to_generateur_collectif(data: Ventilation) -> bool:
    match data.enum_type_ventilation_id:
        case 21 | 22:
            return True
        case _:
            return False


def to_installation(data: Ventilation) -> dict:
    entity = {}
    entity["id"] = data.id
    entity["description"] = data.description or "-"
    entity["surface"] = data.surface_ventile
    entity["type"] = to_type_ventilation(data)
    entity["generateur_id"] = None

    if to_type_generateur(data) is not None:
        entity["generateur_id"] = data.id

    return entity


def to_generateur(data: Ventilation, context: Ressource) -> dict | None:
    if to_type_generateur(data) is None:
        return None

    entity = {}
    entity["id"] = data.id
    entity["description"] = data.description or "-"
    entity["type"] = to_type_generateur(data)
    entity["type_vmc"] = to_type_vmc(data)
    entity["generateur_collectif"] = to_generateur_collectif(data)
    entity["presence_echangeur_thermique"] = to_presence_echangeur_thermique(data)
    entity["annee_installation"] = to_annee_installation_generateur(data, context)
    return entity


def to_ventilation(data: Logement, context: Ressource) -> dict:
    registry = []
    aggregate = {}
    aggregate["installations"] = []
    aggregate["generateurs"] = []

    for ventilation in data.ventilation_collection:
        if ventilation.id in registry:
            continue

        registry.append(ventilation.id)
        aggregate["installations"].append(to_installation(ventilation))

        if (generateur := to_generateur(ventilation, context)) is not None:
            aggregate["generateurs"].append(generateur)

    return aggregate
