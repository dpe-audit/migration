from ..models.ressource import Ressource
from ..models.logement import Logement
from .niveau_transformer import to_niveaux
from .masque_transformer import to_masques
from .plancher_bas_transformer import to_planchers_bas
from .porte_transformer import to_portes


def to_exposition(data: Logement) -> str:
    for ventilation in data.ventilation_collection:
        match ventilation.plusieurs_facade_exposee:
            case True:
                return "exposition_multiple"
            case False:
                return "exposition_simple"

    return "exposition_multiple"


def to_q4pa_conv(data: Logement) -> float | None:
    for ventilation in data.ventilation_collection:
        if ventilation.q4pa_conv is not None:
            return ventilation.q4pa_conv

    return None


def to_presence_brasseurs_air(data: Logement) -> bool:
    return (
        data.sortie.confort_ete.brasseur_air
        if data.sortie.confort_ete.brasseur_air is not None
        else False
    )


def to_enveloppe(data: Logement, context: Ressource) -> dict:
    aggregate = {}
    aggregate["exposition"] = to_exposition(data)
    aggregate["q4pa_conv"] = to_q4pa_conv(data)
    aggregate["presence_brasseurs_air"] = to_presence_brasseurs_air(data)
    aggregate["niveaux"] = to_niveaux(data)
    aggregate["locaux_non_chauffes"] = []
    aggregate["murs"] = []
    aggregate["planchers_bas"] = to_planchers_bas(data, context)
    aggregate["planchers_hauts"] = []
    aggregate["baies"] = []
    aggregate["portes"] = to_portes(data)
    aggregate["ponts_thermiques"] = []
    aggregate["doubles_fenetres"] = []
    aggregate["masques"] = to_masques(data, context)

    return aggregate
