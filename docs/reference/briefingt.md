
# Proactive Publication - Briefing Note Titles and Numbers / Publication proactive - Titres et numéros des notes d’information

**Dataset Type:** `briefingt`  
**Last Generated:** 2025-08-10T01:49:23 (UTC)  
**Source:** dictionaries/briefingt.json  
**Commit:** `0b1c865`

Access, upload and modify the Briefing Note Titles and Numbers reports for your organization / Accès, téléversement et modifications des rapports sur les titres at numéros des notes d’information pour votre organisation

---

## Resources


- [Proactive Publication - Briefing Note Titles and Numbers / Publication proactive - Titres et numéros des notes d’information](#briefingt)

- [Proactive Publication - Briefing Note Titles and Numbers Nothing to Report / Publication proactive - Titres et numéros des notes d’information rien à signaler](#briefingt-nil)


---


## Proactive Publication - Briefing Note Titles and Numbers / Publication proactive - Titres et numéros des notes d’information 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `tracking_number` | Briefing Note Number / Numéro de suivi | `text` | Yes |  |  | This field will display the internal tracking number of the Briefing Note. |
| `title_en` | Title (English) / Titre (en anglais) | `text` | Yes |  |  | This field is populated by the user with the official title of the Briefing Not… |
| `title_fr` | Title (French) / Titre (en français) | `text` | Yes |  |  | This field is populated by the user with the official title of the Briefing Not… |
| `originating_sector_en` | Originating Sector (English) / Secteur d’origine (en anglais) | `text` | Yes |  |  | The Sector, Branch, or Division where the Briefing Note originated in English. … |
| `originating_sector_fr` | Originating Sector (French) / Secteur d’origine (en français) | `text` | Yes |  |  | The Sector, Branch, or Division where the Briefing Note originated in French. I… |
| `addressee` | Addressee / Destinataire | `text` | Yes |  | addressee | This field will display the person to whom the briefing note is addressed. |
| `date_received` | Date Received / Date de réception | `date` | Yes |  |  | This field will display the date on which the Briefing Note was received in the… |
| `action_required` | Action Required / Mesure requise | `text` | Yes |  | action_required | The Action Required is the purpose of the briefing note; For Information: If th… |
| `additional_information_en` | Additional Information (English) / Renseignements supplémentaires (en anglais) | `text` | No |  |  | This field will display any additional information/comments for the Briefing No… |
| `additional_information_fr` | Additional Information (French) / Renseignements supplémentaires (en français) | `text` | No |  |  | This field will display any additional information/comments for the Briefing No… |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `tracking_number` – Briefing Note Number / Numéro de suivi

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field will display the internal tracking number of the Briefing Note.  
FR: Ce champ affichera le numéro de suivi interne de la note de breffage.


---

#### `title_en` – Title (English) / Titre (en anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field is populated by the user with the official title of the Briefing Note, in English.  
FR: Ce champ est rempli par l'utilisateur avec le titre officiel de la note de breffage, en anglais.


---

#### `title_fr` – Title (French) / Titre (en français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field is populated by the user with the official title of the Briefing Note, in French.  
FR: Ce champ est rempli par l'utilisateur avec le titre officiel de la note de breffage, en français.


---

#### `originating_sector_en` – Originating Sector (English) / Secteur d’origine (en anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: The Sector, Branch, or Division where the Briefing Note originated in English. If there are multiple sectors/branches/divisions, they may be separated by a semicolon (;)  
FR: Le secteur, la direction ou la division d'où provient la note de breffage en anglais. S'il y a plusieurs secteurs/directions/divisions, on peut les séparer par un point-virgule (;).


---

#### `originating_sector_fr` – Originating Sector (French) / Secteur d’origine (en français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: The Sector, Branch, or Division where the Briefing Note originated in French. If there are multiple sectors/branches/divisions, they may be separated by a semicolon (;)  
FR: Le secteur, la direction ou la division d'où provient la note de breffage en français S'il y a plusieurs secteurs/directions/divisions, on peut les séparer par un point-virgule (;).


---

#### `addressee` – Addressee / Destinataire

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  
**Choice Set:** addressee (2 values)  


**Description:**  
EN: This field will display the person to whom the briefing note is addressed.  
FR: Ce champ affichera le nom de la personne à qui la note de breffage est adressée.


##### Allowed Values (addressee)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `D` | Deputy head (including a person appointed to a position of an equivalent rank) | Administrateurs généraux (y compris une personne nommée à un poste de rang équivalent) |
| `M` | Minister | Ministre |




---

#### `date_received` – Date Received / Date de réception

**Type:** `date`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field will display the date on which the Briefing Note was received in the addressee's office.  
FR: Ce champ affichera la date à laquelle la note de breffage a été reçue par le bureau du destinataire.


---

#### `action_required` – Action Required / Mesure requise

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  
**Choice Set:** action_required (3 values)  


**Description:**  
EN: The Action Required is the purpose of the briefing note; For Information: If the item is being routed solely for the information of the addressee; For Approval/Signature: If the item is for approval or signature only of the addressee; For Decision: If the item requests the addressee make a decisive decision  
FR: La mesure requise représente le but de la note de breffage; À titre d'information : Si l'élément n'est envoyé que pour informer le destinataire; Pour approbation/signature; Si l'élément est envoyé à des fins d'approbation ou de signature seulement par le destinataire; Pour décision : Si l'élément demande au destinataire de prendre une décision décisive.


##### Allowed Values (action_required)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `D` | For Decision | Décision attendue |
| `I` | For Information | Pour Information |
| `S` | For Signature | Pour Signature |




---

#### `additional_information_en` – Additional Information (English) / Renseignements supplémentaires (en anglais)

**Type:** `text`  
**Required:** No  
**Validation:** None / None  


**Description:**  
EN: This field will display any additional information/comments for the Briefing Note, in English.  
FR: Ce champ affichera de plus amples renseignements/commentaires concernant la note de breffage, en anglais.


---

#### `additional_information_fr` – Additional Information (French) / Renseignements supplémentaires (en français)

**Type:** `text`  
**Required:** No  
**Validation:** None / None  


**Description:**  
EN: This field will display any additional information/comments for the Briefing Note, in French.  
FR: Ce champ affichera de plus amples renseignements/commentaires concernant la note de breffage, en français.


---



## Proactive Publication - Briefing Note Titles and Numbers Nothing to Report / Publication proactive - Titres et numéros des notes d’information rien à signaler 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `year` | Year / Année | `year` | Yes |  |  | This tab / field in the template is only populated if there are no briefing not… |
| `month` | Month (1-12) / Mois (1-12) | `month` | Yes |  |  | This tab / field in the template is only populated if there are no briefing not… |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `year` – Year / Année

**Type:** `year`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This tab / field in the template is only populated if there are no briefing notes for the reporting period. This field should be populated with the year of the reporting period.  
FR: Cet onglet/champ du modèle n’est rempli que s'il n'y a pas de notes de breffage pour la période d’établissement de rapports. Ce champ doit être rempli avec l’année de la période d’établissement de rapports.


---

#### `month` – Month (1-12) / Mois (1-12)

**Type:** `month`  
**Required:** Yes  
**Validation:** Must be in the range of 1-12 (representing January-December). / Doit être dans la gamme de 1-12 (représente janvier-décembre)  


**Description:**  
EN: This tab / field in the template is only populated if there are no briefing notes for the reporting period. This field should be populated with the month of the reporting period.  
FR: Cet onglet/champ du modèle n’est rempli que s'il n'y a pas de notes de breffage pour la période d’établissement de rapports. Ce champ doit être rempli avec le mois de la période d’établissement de rapports.


---




## Appendix

### Choice Sets Summary (All Resources)
| Choice Set | Field(s) | Values | Standalone Doc |
|------------|----------|--------|----------------|


### Generation Metadata

- Generated: 2025-08-10T01:49:23 (UTC)
- Source: dictionaries/briefingt.json
- Commit: `0b1c865`
- Tool Version: simple-1

### Validation

- JSON Schema Validation: **PASSED**


### Notes

This documentation is auto-generated. Do not hand-edit; instead update the source recombinant JSON and re-run generation.