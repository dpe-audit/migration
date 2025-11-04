from typing import Self
from datetime import date
from .utils import strval, intval, floatval, dateval


class Adresse:
    adresse_brut: str
    code_postal_brut: str
    nom_commune_brut: str
    label_brut: str
    label_brut_avec_complement: str
    compl_nom_residence: str | None
    compl_ref_batiment: str | None
    compl_etage_appartement: int | None
    compl_ref_cage_escalier: str | None
    compl_ref_logement: str | None

    ban_date_appel: date
    ban_id: str | None
    ban_id_ban_adresse: str | None
    ban_label: str | None
    ban_housenumber: str | None
    ban_street: str | None
    ban_citycode: str | None
    ban_postcode: str | None
    ban_city: str | None
    ban_type: str | None
    ban_score: float | None
    ban_x: float | None
    ban_y: float | None

    enum_statut_geocodage_ban_id: int

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.adresse_brut = strval(data, "adresse_brut")
        entity.code_postal_brut = strval(data, "code_postal_brut")
        entity.nom_commune_brut = strval(data, "nom_commune_brut")
        entity.label_brut = strval(data, "label_brut")
        entity.label_brut_avec_complement = strval(data, "label_brut_avec_complement")
        entity.compl_nom_residence = strval(data, "compl_nom_residence")
        entity.compl_ref_batiment = strval(data, "compl_ref_batiment")
        entity.compl_etage_appartement = intval(data, "compl_etage_appartement")
        entity.compl_ref_cage_escalier = strval(data, "compl_ref_cage_escalier")
        entity.compl_ref_logement = strval(data, "compl_ref_logement")
        entity.ban_date_appel = dateval(data, "ban_date_appel")
        entity.ban_id = strval(data, "ban_id")
        entity.ban_id_ban_adresse = strval(data, "ban_id_ban_adresse")
        entity.ban_label = strval(data, "ban_label")
        entity.ban_housenumber = strval(data, "ban_housenumber")
        entity.ban_street = strval(data, "ban_street")
        entity.ban_citycode = strval(data, "ban_citycode")
        entity.ban_postcode = strval(data, "ban_postcode")
        entity.ban_city = strval(data, "ban_city")
        entity.ban_type = strval(data, "ban_type")
        entity.ban_score = floatval(data, "ban_score")
        entity.ban_x = floatval(data, "ban_x")
        entity.ban_y = floatval(data, "ban_y")
        entity.enum_statut_geocodage_ban_id = intval(
            data, "enum_statut_geocodage_ban_id"
        )
        return entity


class Adresses:
    adresse_bien: Adresse

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.adresse_bien = Adresse.from_data(data.get("adresse_bien", {}))
        return entity


class Geolocalisation:
    invar_logement: str | None
    numero_fiscal_local: str | None
    id_batiment_rnb: str | None
    rpls_log_id: str | None
    rpls_org_id: str | None
    idpar: str | None
    immatriculation_copropriete: str | None

    adresses: Adresses

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.invar_logement = strval(data, "invar_logement")
        entity.numero_fiscal_local = strval(data, "numero_fiscal_local")
        entity.id_batiment_rnb = strval(data, "id_batiment_rnb")
        entity.rpls_log_id = strval(data, "rpls_log_id")
        entity.rpls_org_id = strval(data, "rpls_org_id")
        entity.idpar = strval(data, "idpar")
        entity.immatriculation_copropriete = strval(data, "immatriculation_copropriete")
        entity.adresses = Adresses.from_data(data.get("adresses", {}))
        return entity


class Administratif:
    numero_dpe: str | None
    dpe_a_remplacer: str | None
    audit_a_remplacer: str | None
    dpe_immeuble_associe: str | None
    reference_interne_projet: str | None
    motif_remplacement: str | None

    date_visite_diagnostiqueur: date | None
    date_visite_auditeur: date | None
    date_etablissement_dpe: date | None
    date_etablissement_audit: date | None
    date_expiration_audit: date | None

    enum_version_id: str
    enum_version_dpe_id: str | None
    enum_version_audit_id: str | None
    enum_modele_dpe_id: str | None
    enum_modele_audit_id: str | None

    geolocalisation: Geolocalisation

    @classmethod
    def from_data(cls, data: dict) -> Self:
        entity = cls()
        entity.numero_dpe = strval(data, "numero_dpe")
        entity.dpe_a_remplacer = strval(data, "dpe_a_remplacer")
        entity.audit_a_remplacer = strval(data, "audit_a_remplacer")
        entity.dpe_immeuble_associe = strval(data, "dpe_immeuble_associe")
        entity.reference_interne_projet = strval(data, "reference_interne_projet")
        entity.motif_remplacement = strval(data, "motif_remplacement")
        entity.date_visite_diagnostiqueur = dateval(data, "date_visite_diagnostiqueur")
        entity.date_visite_auditeur = dateval(data, "date_visite_auditeur")
        entity.date_etablissement_dpe = dateval(data, "date_etablissement_dpe")
        entity.date_etablissement_audit = dateval(data, "date_etablissement_audit")
        entity.date_expiration_audit = dateval(data, "date_expiration_audit")
        entity.enum_version_id = strval(data, "enum_version_id")
        entity.enum_version_dpe_id = strval(data, "enum_version_dpe_id")
        entity.enum_version_audit_id = strval(data, "enum_version_audit_id")
        entity.enum_modele_dpe_id = strval(data, "enum_modele_dpe_id")
        entity.enum_modele_audit_id = strval(data, "enum_modele_audit_id")
        entity.geolocalisation = Geolocalisation.from_data(
            data.get("geolocalisation", {})
        )
        return entity

    def date_visite(self) -> date:
        return self.date_visite_diagnostiqueur() or self.date_visite_auditeur()

    def date_etablissement(self) -> date:
        return self.date_etablissement_dpe() or self.date_etablissement_audit()

    def annee_etablissement(self) -> int:
        return self.date_etablissement().year
