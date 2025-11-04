from ..models.ressource import Ressource
from ..models.logement import Logement
from ..models.production import PanneauPv


def to_orientation(data: PanneauPv) -> int | None:
    match data.enum_orientation_pv_id:
        case 1:
            return 180
        case 2:
            return 0
        case 3:
            return 90
        case 4:
            return 270
        case _:
            match data.tv_coef_orientation_pv_id:
                case 1 | 6 | 11 | 16:
                    return 90
                case 2 | 7 | 12 | 17:
                    return 135
                case 3 | 8 | 13 | 18:
                    return 180
                case 4 | 9 | 14 | 19:
                    return 225
                case 5 | 10 | 15 | 20:
                    return 270
                case _:
                    return None


def to_inclinaison(data: PanneauPv) -> int | None:
    match data.enum_inclinaison_pv_id:
        case 1:
            return 10
        case 2:
            return 30
        case 3:
            return 60
        case 4:
            return 80
        case _:
            match data.tv_coef_orientation_pv_id:
                case 1 | 2 | 3 | 4 | 5:
                    return 10
                case 6 | 7 | 8 | 9 | 10:
                    return 30
                case 11 | 12 | 13 | 14 | 15:
                    return 60
                case 16 | 17 | 18 | 19 | 20:
                    return 80
                case _:
                    return None


def to_modules(data: PanneauPv) -> int | None:
    if data.nombre_modules is not None:
        return data.nombre_modules

    return 1 if data.surface_totale_capteurs > 0 else None


def to_installation_collective(data: PanneauPv) -> bool:
    return (
        data.ratio_virtualisation > 0
        if data.ratio_virtualisation is not None
        else False
    )


def to_panneau_photovoltaique(data: PanneauPv) -> dict | None:
    entity = {}
    entity["id"] = data.id
    entity["description"] = "-"
    entity["surface"] = data.surface_totale_capteurs
    entity["orientation"] = to_orientation(data)
    entity["inclinaison"] = to_inclinaison(data)
    entity["modules"] = to_modules(data)
    entity["installation_collective"] = to_installation_collective(data)

    if entity["surface"] is None:
        return None
    elif entity["orientation"] is None:
        return None
    elif entity["inclinaison"] is None:
        return None
    elif entity["modules"] is None:
        return None
    else:
        return entity


def to_production(data: Logement, context: Ressource) -> dict:
    aggregate = {}
    aggregate["panneaux_photovoltaiques"] = []

    if data.production_elec_enr is None:
        return aggregate

    for panneaux_pv in data.production_elec_enr.panneaux_pv_collection:
        entity = to_panneau_photovoltaique(panneaux_pv)
        if entity is not None:
            aggregate["panneaux_photovoltaiques"].append(entity)

    return aggregate
