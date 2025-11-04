import xmltodict
from .models.ressource import DPE
from .models.ressource import Audit


def normalize_element(data: dict):
    data.update(data.get("donnee_entree", {}))
    data.update(data.get("donnee_intermediaire", {}))
    data.pop("donnee_entree", None)
    data.pop("donnee_intermediaire", None)


def normalize_collection(data: dict, name: str):
    collection_key = f"{name}_collection"

    if data.get(collection_key, None) is None:
        data[collection_key] = []
        return

    collection = {}
    collection[collection_key] = data.get(collection_key).get(name, [])

    data.update(collection)
    for item in data.get(collection_key):
        normalize_element(item)


def normalize_baie_vitree(data: dict):
    normalize_collection(data, "masque_lointain_non_homogene")


def normalize_enveloppe(data: dict):
    normalize_collection(data, "mur")
    normalize_collection(data, "plancher_bas")
    normalize_collection(data, "plancher_haut")
    normalize_collection(data, "baie_vitree")
    normalize_collection(data, "porte")
    normalize_collection(data, "ets")
    normalize_collection(data, "pont_thermique")

    for item in data.get("baie_vitree_collection", []):
        normalize_baie_vitree(item)


def normalize_installation_chauffage(data: dict):
    normalize_collection(data, "generateur_chauffage")
    normalize_collection(data, "emetteur_chauffage")


def normalize_installation_ecs(data: dict):
    normalize_collection(data, "generateur_ecs")


def normalize_production_elec_enr(data: dict):
    normalize_element(data)
    normalize_collection(data, "panneaux_pv")


def normalize_logement(data: dict):
    normalize_enveloppe(data.get("enveloppe", {}))
    normalize_production_elec_enr(data.get("production_elec_enr", {}))
    normalize_collection(data, "climatisation")
    normalize_collection(data, "ventilation")
    normalize_collection(data, "installation_chauffage")
    normalize_collection(data, "installation_ecs")

    for item in data.get("installation_chauffage_collection", []):
        normalize_installation_chauffage(item)
    for item in data.get("installation_ecs_collection", []):
        normalize_installation_ecs(item)


def normalize_dpe_immeuble(data: dict):
    normalize_collection(data, "logement")


def deserialize_xml(xml: str) -> dict:
    force_list = []
    force_list.append("climatisation")
    force_list.append("ventilation")
    force_list.append("baie_vitree")
    force_list.append("mur")
    force_list.append("plancher_bas")
    force_list.append("plancher_haut")
    force_list.append("porte")
    force_list.append("pont_thermique")
    force_list.append("masque_lointain_non_homogene")
    force_list.append("ets")
    force_list.append("baie_ets")
    force_list.append("panneaux_pv")
    force_list.append("installation_ecs")
    force_list.append("generateur_ecs")
    force_list.append("installation_chauffage")
    force_list.append("generateur_chauffage")
    force_list.append("emetteur_chauffage")

    data = xmltodict.parse(
        xml_input=xml,
        force_list=force_list,
    )

    return data


def deserialize_dpe(xml: str) -> DPE:
    data = deserialize_xml(xml)
    data = data.get("dpe", {})

    normalize_logement(data.get("logement", {}))
    normalize_dpe_immeuble(data.get("dpe_immeuble", {}))

    return DPE.from_data(data)


def deserialize_audit(xml: str) -> Audit:
    data = deserialize_xml(xml)
    data = data.get("audit", {})

    normalize_collection(data, "logement_collection")
    normalize_dpe_immeuble(data.get("dpe_immeuble", {}))

    return Audit.from_data(data)
