import uuid
from ..models.logement import Logement


def to_surface(data: Logement) -> float:
    return (
        data.caracteristique_generale.surface_habitable_immeuble
        or data.caracteristique_generale.surface_habitable_logement
    )


def to_inertie_paroi_verticale(data: Logement) -> str:
    inertie = data.enveloppe.inertie
    return "lourde" if inertie.inertie_paroi_verticale_lourd else "legere"


def to_inertie_plancher_haut(data: Logement) -> str:
    inertie = data.enveloppe.inertie
    return "lourde" if inertie.inertie_plancher_haut_lourd else "legere"


def to_inertie_plancher_bas(data: Logement) -> str:
    inertie = data.enveloppe.inertie
    return "lourde" if inertie.inertie_plancher_bas_lourd else "legere"


def to_niveau(data: Logement) -> dict:
    entity = {}
    entity["id"] = str(uuid.uuid4())
    entity["description"] = "Niveau reconstitué"
    entity["surface"] = to_surface(data)
    entity["inertie_paroi_verticale"] = to_inertie_paroi_verticale(data)
    entity["inertie_plancher_haut"] = to_inertie_plancher_haut(data)
    entity["inertie_plancher_bas"] = to_inertie_plancher_bas(data)
    return entity


def to_niveaux(data: Logement) -> list[dict]:
    return [to_niveau(data)]
