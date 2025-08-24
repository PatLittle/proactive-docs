
# Open Data Inventory / Inventaire des données ouvertes

**Dataset Type:** `inventory`  
**Last Generated:** 2025-08-24T01:40:03 (UTC)  
**Source:** dictionaries/inventory.json  
**Commit:** `ece18ac`

This dataset houses your departmental open data inventory. This is where you can access and upload your open data inventory template. / Ce jeu de données contient l’inventaire des données ouvertes de votre ministère. C’est l’occasion pour accéder à et pour télécharger votre modèle d'inventaire des données ouvertes.

---

## Resources


- [Open Data Inventory / Inventaire des données ouvertes](#inventory)


---


## Open Data Inventory / Inventaire des données ouvertes 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `ref_number` | Reference Number / Numéro de référence | `text` | Yes |  |  | The unique reference number given to each line item in the spreadsheet. Having … |
| `title_en` | Title (English) / Titre (anglais) | `text` | Yes |  |  | The English name by which the dataset is known. |
| `title_fr` | Title (French) / Titre (français) | `text` | Yes |  |  | The French name by which the dataset is known. |
| `description_en` | Description (English) / Description (anglais) | `text` | Yes |  |  | An account of the dataset, in English. A description may include but is not lim… |
| `description_fr` | Description (French) / Description (français) | `text` | Yes |  |  | An account of the dataset, in French. A description may include but is not limi… |
| `publisher_en` | Publisher - Name at Publication (English) / Publisher - Name at Publication (English) | `text` | No |  |  | Name, in English, of the organization primarily responsible for publishing the … |
| `publisher_fr` | Publisher - Name at Publication (French) / Publisher - Name at Publication (French) | `text` | No |  |  | Name, in French, of the organization primarily responsible for publishing the d… |
| `date_published` | Date Published / Date Published | `date` | Yes |  |  | The date of issuance (e.g., publication) of the dataset |
| `language` | Language / Langue | `text` | Yes |  | language | The language of the resource. |
| `size` | Size / Size | `bigint` | Yes |  |  | The [estimated] size of the resource(in Bytes) |
| `eligible_for_release` | Eligible for Release / Eligible for Release | `text` | Yes |  | eligible_for_release | Is all of the content within the dataset eligible to be publicly released based… |
| `program_alignment_architecture_en` | Program Alignment Architecture (English) / Program Alignment Architecture (English) | `text` | Yes |  |  | The Program Alignment Architecture (PAA) in English. The Program Alignment Arch… |
| `program_alignment_architecture_fr` | Program Alignment Architecture (French) / Program Alignment Architecture (French) | `text` | Yes |  |  | The Program Alignment Architecture (PAA) in French. The Program Alignment Archi… |
| `date_released` | Date Released / Date Released | `date` | Yes |  |  | The date on which the metadata record was released, made available, on the Open… |
| `portal_url_en` | Open Government Portal Record (English) / Open Government Portal Record (English) | `text` | Yes |  |  | The location for online access to the distribution of the resource, in French. … |
| `portal_url_fr` | Open Government Portal Record (French) / Open Government Portal Record (French) | `text` | Yes |  |  | The location for online access to the distribution of the resource, in French. … |
| `user_votes` | User Votes / User Votes | `int` | No |  |  | Count of users that voted for this dataset on open.canada.ca |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `ref_number` – Reference Number / Numéro de référence

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: The unique reference number given to each line item in the spreadsheet. Having a unique identifier for each item will allow departments to locate a specific item in the system if revisions or deletions are required. This element will not be displayed to the public.  
FR: Un identificateur unique est attribué à chaque poste dans la feuille de calcul. Un identificateur unique pour chaque poste permettra aux ministères de trouver un élément précis dans le système, si des modifications ou des suppressions sont nécessaires. Cet élément ne sera pas présenté au public.


---

#### `title_en` – Title (English) / Titre (anglais)

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: The English name by which the dataset is known.  
FR: Le nom en anglais sous lequel le jeu de données est connu.


---

#### `title_fr` – Title (French) / Titre (français)

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: The French name by which the dataset is known.  
FR: Le nom en français sous lequel le jeu de données est connu.


---

#### `description_en` – Description (English) / Description (anglais)

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: An account of the dataset, in English. A description may include but is not limited to, an abstract, a table of contents, or a free-text account of the dataset.  
FR: Un compte rendu du jeu de données en anglais. Une description peut inclure, entre autres, un résumé, une table des matières ou du texte libre sur le jeu de données.


---

#### `description_fr` – Description (French) / Description (français)

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: An account of the dataset, in French. A description may include but is not limited to, an abstract, a table of contents, or a free-text account of the dataset.  
FR: Un compte rendu du jeu de données en français. Une description peut inclure, entre autres, un résumé, une table des matières ou du texte libre sur le jeu de données.


---

#### `publisher_en` – Publisher - Name at Publication (English) / Publisher - Name at Publication (English)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: Name, in English, of the organization primarily responsible for publishing the dataset at the time of the publication (if applicable, i.e. if different than current name).  
FR: Nom, en anglais, de l’organisation principalement responsable de l’édition du jeu de données au moment de la publication (s’il y a lieu, c.-à-d. s’il est différent du nom actuel)


---

#### `publisher_fr` – Publisher - Name at Publication (French) / Publisher - Name at Publication (French)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: Name, in French, of the organization primarily responsible for publishing the dataset at the time of the publication (if applicable, i.e. if different than current name).  
FR: Nom, en français, de l’organisation principalement responsable de l’édition du jeu de données au moment de la publication (s’il y a lieu, c.-à-d. s’il est différent du nom actuel)


---

#### `date_published` – Date Published / Date Published

**Type:** `date`  
**Required:** Yes  


**Description:**  
EN: The date of issuance (e.g., publication) of the dataset  
FR: Date de diffusion (p. ex., publication) du jeu de données.


---

#### `language` – Language / Langue

**Type:** `text`  
**Required:** Yes  
**Choice Set:** language (6 values)  


**Description:**  
EN: The language of the resource.  
FR: Langue de la ressource


##### Allowed Values (language)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `en` | English | Anglais |
| `en+fr` | Bilingual (English and French) | Bilingue (Anglais et Français) |
| `fr` | French | Français |
| `iu` | Inuktitut | Inuktitut |
| `other` | Other | Autre |
| `zxx` | No linguistic content ; Not applicable | Pas de contenu linguistique; non applicable |




---

#### `size` – Size / Size

**Type:** `bigint`  
**Required:** Yes  


**Description:**  
EN: The [estimated] size of the resource(in Bytes)  
FR: La taille [estimée] de la ressource (en octets).


---

#### `eligible_for_release` – Eligible for Release / Eligible for Release

**Type:** `text`  
**Required:** Yes  
**Choice Set:** eligible_for_release (2 values)  


**Description:**  
EN: Is all of the content within the dataset eligible to be publicly released based on the application of the Eligibility Criteria in the Guide to Implementing the Directive on Open Government?  
FR: Tout le contenu du jeu de données peut être diffusé publiquement selon les critères d’admissibilité mentionnés dans le guide de la mise en œuvre de la Directive sur le gouvernement ouvert?


##### Allowed Values (eligible_for_release)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `N` | No | Non |
| `Y` | Yes | Oui |




---

#### `program_alignment_architecture_en` – Program Alignment Architecture (English) / Program Alignment Architecture (English)

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: The Program Alignment Architecture (PAA) in English. The Program Alignment Architecture (PAA) is an inventory of each organization’s programs. It provides an overview of the organization’s responsibilities.  
FR: L’Architecture d’alignement des programmes (AAP) en anglais. L’Architecture d’alignement des programmes (AAP) est un inventaire des programmes de chaque organisation. Il offre un aperçu des responsabilités de l’organisation.


---

#### `program_alignment_architecture_fr` – Program Alignment Architecture (French) / Program Alignment Architecture (French)

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: The Program Alignment Architecture (PAA) in French. The Program Alignment Architecture (PAA) is an inventory of each organization’s programs. It provides an overview of the organization’s responsibilities.  
FR: L’Architecture d’alignement des programmes (AAP) en français. L’Architecture d’alignement des programmes (AAP) est un inventaire des programmes de chaque organisation. Il offre un aperçu des responsabilités de l’organisation.


---

#### `date_released` – Date Released / Date Released

**Type:** `date`  
**Required:** Yes  


**Description:**  
EN: The date on which the metadata record was released, made available, on the Open Government portal; only if applicable  
FR: La date à laquelle l’enregistrement de métadonnées a été diffusé et rendu accessible à partir du Portail du gouvernement ouvert, s’il y a lieu seulement.


---

#### `portal_url_en` – Open Government Portal Record (English) / Open Government Portal Record (English)

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: The location for online access to the distribution of the resource, in French. This element is only mandatory if applicable The entry should point to the metadata record page on Open.Canada.ca.  
FR: L’emplacement en ligne où il est possible d’accéder à la ressource, en anglais. Cet élément n’est obligatoire que le cas échéant. La valeur saisie doit mener à la page de l’enregistrement sur ouvert.canada.ca.


---

#### `portal_url_fr` – Open Government Portal Record (French) / Open Government Portal Record (French)

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: The location for online access to the distribution of the resource, in French. This element is only mandatory if applicable The entry should point to the metadata record page on Open.Canada.ca.  
FR: L’emplacement en ligne où il est possible d’accéder à la ressource, en français. Cet élément n’est obligatoire que le cas échéant. La valeur saisie doit mener à la page de l’enregistrement sur ouvert.canada.ca.


---

#### `user_votes` – User Votes / User Votes

**Type:** `int`  
**Required:** No  


**Description:**  
EN: Count of users that voted for this dataset on open.canada.ca  
FR: Nombre d’utilisateurs qui ont voté pour ce jeu de données sur le site Web ouvert.canada.ca


---




## Appendix

### Choice Sets Summary (All Resources)
| Choice Set | Field(s) | Values | Standalone Doc |
|------------|----------|--------|----------------|


### Generation Metadata

- Generated: 2025-08-24T01:40:03 (UTC)
- Source: dictionaries/inventory.json
- Commit: `ece18ac`
- Tool Version: simple-1

### Validation

- JSON Schema Validation: **PASSED**


### Notes

This documentation is auto-generated. Do not hand-edit; instead update the source recombinant JSON and re-run generation.