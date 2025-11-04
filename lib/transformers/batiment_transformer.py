from ..models.ressource import Ressource


def to_type_batiment(data: Ressource) -> str:
    match data.get_logement().caracteristique_generale.enum_methode_application_dpe_log_id:
        case 1 | 14 | 18:
            return "maison"
        case _:
            return "immeuble"


def to_annee_construction(data: Ressource) -> int:
    if data.get_logement().caracteristique_generale.annee_construction is not None:
        return data.get_logement().caracteristique_generale.annee_construction
    else:
        match data.get_logement().caracteristique_generale.enum_periode_construction_id:
            case 1:
                return 1947
            case 2:
                return 1966
            case 3:
                return 1976
            case 4:
                return 1980
            case 5:
                return 1985
            case 6:
                return 1995
            case 7:
                return 2003
            case 8:
                return 2009
            case 9:
                return 2017
            case 10:
                return 2021


def to_altitude(data: Ressource) -> int:
    if data.get_logement().meteo.altitude is not None:
        return data.get_logement().meteo.altitude
    else:
        match data.get_logement().meteo.enum_classe_altitude_id:
            case 1:
                return 0
            case 2:
                return 600
            case 3:
                return 1000


def to_adresse(data: Ressource) -> dict:
    adresse = data.get_administratif().geolocalisation.adresses.adresse_bien
    value = {}
    value["ban_id"] = adresse.ban_id
    value["nom"] = adresse.ban_label or adresse.label_brut_avec_complement
    value["code_postal"] = adresse.ban_postcode or adresse.code_postal_brut
    value["code_insee"] = adresse.ban_citycode or adresse.code_postal_brut
    value["commune"] = adresse.ban_city or adresse.nom_commune_brut
    return value


def to_batiment(data: Ressource) -> dict:
    caracteristique_generale = data.get_logement().caracteristique_generale
    meteo = data.get_logement().meteo

    entity = {}
    entity["rnb_id"] = data.get_administratif().geolocalisation.id_batiment_rnb
    entity["type"] = to_type_batiment(data)
    entity["annee_construction"] = to_annee_construction(data)
    entity["altitude"] = to_altitude(data)
    entity["logements"] = caracteristique_generale.nombre_appartement or 1
    entity["surface_habitable"] = (
        caracteristique_generale.surface_habitable_immeuble
        or caracteristique_generale.surface_habitable_logement
    )
    entity["hauteur_sous_plafond"] = caracteristique_generale.hsp
    entity["materiaux_anciens"] = bool(meteo.batiment_materiaux_anciens)
    entity["adresse"] = to_adresse(data)
    return entity
