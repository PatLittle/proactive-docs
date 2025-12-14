
# Experimentation Inventory / Répertoire d'expérimentation

**Dataset Type:** `experiment`  
**Last Generated:** 2025-12-14T01:45:17 (UTC)  
**Source:** dictionaries/experiment.json  
**Commit:** `ddfad99`

Access, upload and modify the Experimentation Inventory for your organization / Accès, téléversement et modifier le répertoire d'expérimentation pour votre organisation

---

## Resources


- [Experimentation Inventory / Répertoire d'expérimentation](#experiment)


---


## Experimentation Inventory / Répertoire d'expérimentation 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `reference_number` | Reference Number / Numéro de référence | `text` | Yes |  |  | This field is populated by the user with the reference number of the Experiment… |
| `titre_du_projet_en` | Project Title (English) / Titre du projet (en anglais) | `text` | Yes |  |  | This field describes the project title, in English |
| `titre_du_projet_fr` | Project Title (French) / Titre du projet (en français) | `text` | Yes |  |  | This field describes the project title, in French |
| `question_de_recherche_en` | Research Question (English) / Question de recherche (en anglais) | `text` | Yes |  |  | This field describes the research question informing the project, in English |
| `question_de_recherche_fr` | Research Question (French) / Question de recherche (en français) | `text` | Yes |  |  | This field describes the research question informing the project, in French |
| `project_summary_en` | Project Summary (English) / Résumé du projet (en anglais) | `text` | Yes |  |  | This field summarizes the key information about the project, including any find… |
| `project_summary_fr` | Project Summary (French) / Résumé du projet (en français) | `text` | Yes |  |  | This field summarizes the key information about the project, including any find… |
| `last_updated` | Last Updated / Dernière mise à jour | `date` | Yes |  |  | This field will display the latest update provided for the project. |
| `experimental_area` | Experimental area / Secteur d&#39;expérimentation | `text` | Yes |  | experimental_area | This field will display the area in which the experiment is taking place. |
| `research_design` | Design / Devis | `text` | Yes |  | research_design | This field will describe the research design used for the project. |
| `design_details_en` | Design Details (English) / Devis details (anglais) | `text` | Yes |  |  | This field will describe the details of the research design used for the project. |
| `design_details_fr` | Design Details (French) / Devis details (français) | `text` | Yes |  |  | This field will describe the details of the research design used for the project. |
| `intervention_en` | Intervention (English) / Intervention (anglais) | `text` | Yes |  |  | This field will describe the intervention tested in the project. |
| `intervention_fr` | Intervention (French) / Intervention (français) | `text` | Yes |  |  | This field will describe the intervention tested in the project. |
| `mesure_des_resultats_en` | Outcomes (English) / Mesure des résultats (anglais) | `text` | Yes |  |  | This field will describe the intervention tested in the project. |
| `mesure_des_resultats_fr` | Outcomes (French) / Mesure des résultats (françcais) | `text` | Yes |  |  | This field will describe the outcomes measured in the project. |
| `resultats_en` | Findings (English) / Résultats (anglais) | `text` | No |  |  | This field will describe the outcomes measured in the project. |
| `resultats_fr` | Findings (French) / Résultats (françcais) | `text` | No |  |  | This field will describe the findings of the project. |
| `status` | Status / Statut | `text` | Yes |  | status | This field will describe the status of the project. |
| `lead_branch_en` | Lead Branch and/or Unit (English) / Direction et/ou unité responsable (en anglais) | `text` | No |  |  | This field describes the organizational structure tied to the project owner (if… |
| `lead_branch_fr` | Lead Branch and/or Unit (French) / Direction et/ou unité responsable (en français)) | `text` | No |  |  | This field describes the organizational structure tied to the project owner (if… |
| `info_supplementaire_en` | Further Information / Links (English) / Informations supplémentaires / liens (anglais) | `text` | No |  |  | This field includes a URL link to additional information on the project (e.g. r… |
| `info_supplementaire_fr` | Further Information / Links (French) / Informations supplémentaires / liens (en français) | `text` | No |  |  | This field includes a URL link to additional information on the project (e.g. r… |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `reference_number` – Reference Number / Numéro de référence

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field is populated by the user with the reference number of the Experiment. This number is a mandatory system requirement when publishing a template.  
FR: Ce champ est rempli par l’utilisateur avec le numéro de référence de l'experiment. Le numéro est une exigence de système obligatoire pour la publication d’un modèle.


---

#### `titre_du_projet_en` – Project Title (English) / Titre du projet (en anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field describes the project title, in English  
FR: Ce champ décrira le titre du projet, en anglais


---

#### `titre_du_projet_fr` – Project Title (French) / Titre du projet (en français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field describes the project title, in French  
FR: Ce champ décrira le titre du projet, en français


---

#### `question_de_recherche_en` – Research Question (English) / Question de recherche (en anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field describes the research question informing the project, in English  
FR: Ce champ décrira la question de recherche guidant le projet, en anglais


---

#### `question_de_recherche_fr` – Research Question (French) / Question de recherche (en français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field describes the research question informing the project, in French  
FR: Ce champ décrira la question de recherche guidant le projet, en français


---

#### `project_summary_en` – Project Summary (English) / Résumé du projet (en anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field summarizes the key information about the project, including any findings once the initiative is completed, in English  
FR: Ce champ résumera les information-clés à propos du projet, y compris les résultats lorque le projet est complété, en anglais


---

#### `project_summary_fr` – Project Summary (French) / Résumé du projet (en français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field summarizes the key information about the project, including any findings once the initiatve is completed, in French  
FR: Ce champ résumera les information-clés à propos du projet, y compris les résultats lorque le projet est complété, en français


---

#### `last_updated` – Last Updated / Dernière mise à jour

**Type:** `date`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field will display the latest update provided for the project.  
FR: Ce champ décrira à quand remonte la dernière mise à jour.


---

#### `experimental_area` – Experimental area / Secteur d'expérimentation

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  
**Choice Set:** experimental_area (7 values)  


**Description:**  
EN: This field will display the area in which the experiment is taking place.  
FR: Ce champ décrira dans quel secteur l'expérience prend place.


##### Allowed Values (experimental_area)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `GC` | Grants and Contributions | Subventions et contributions |
| `OA` | Other | autres |
| `PO` | Policy | Politique |
| `PR` | Program | Programme |
| `RE` | Regulatory | Règlementation |
| `SE` | Service Delivery | Prestation de services |
| `SI` | Internal Services | Services internes |




---

#### `research_design` – Design / Devis

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  
**Choice Set:** research_design (4 values)  


**Description:**  
EN: This field will describe the research design used for the project.  
FR: Ce champ décrira le devis de recherche employé dans le projet.


##### Allowed Values (research_design)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `OTH` | Other | Autre |
| `QEX` | Quasi-experimental | Quasi-expérimental |
| `RDM` | Randomized | Randomisé |
| `STR` | Structured pre-post | Avant-après structuré |




---

#### `design_details_en` – Design Details (English) / Devis details (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field will describe the details of the research design used for the project.  
FR: Ce champ décrira les détails du devis de recherche employé dans le projet.


---

#### `design_details_fr` – Design Details (French) / Devis details (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field will describe the details of the research design used for the project.  
FR: Ce champ décrira les détails du devis de recherche employé dans le projet.


---

#### `intervention_en` – Intervention (English) / Intervention (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field will describe the intervention tested in the project.  
FR: Ce champ décrira l’intervention testée dans le projet.


---

#### `intervention_fr` – Intervention (French) / Intervention (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field will describe the intervention tested in the project.  
FR: Ce champ décrira l’intervention testée dans le projet.


---

#### `mesure_des_resultats_en` – Outcomes (English) / Mesure des résultats (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field will describe the intervention tested in the project.  
FR: Ce champ décrira l’intervention testée dans le projet.


---

#### `mesure_des_resultats_fr` – Outcomes (French) / Mesure des résultats (françcais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field will describe the outcomes measured in the project.  
FR: Ce champ décrira la/les mesure(s) de résultat(s) employée(s) dans le projet.


---

#### `resultats_en` – Findings (English) / Résultats (anglais)

**Type:** `text`  
**Required:** No  
**Validation:** None / None  


**Description:**  
EN: This field will describe the outcomes measured in the project.  
FR: Ce champ décrira la/les mesure(s) de résultat(s) employée(s) dans le projet.


---

#### `resultats_fr` – Findings (French) / Résultats (françcais)

**Type:** `text`  
**Required:** No  
**Validation:** None / None  


**Description:**  
EN: This field will describe the findings of the project.  
FR: Ce champ décrira les résultats observés dans le projet.


---

#### `status` – Status / Statut

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  
**Choice Set:** status (3 values)  


**Description:**  
EN: This field will describe the status of the project.  
FR: Ce champ décrira le statut du projet.


##### Allowed Values (status)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `ACT` | Active | Actif |
| `COM` | Completed | Complété |
| `INA` | Inactive | Inactif |




---

#### `lead_branch_en` – Lead Branch and/or Unit (English) / Direction et/ou unité responsable (en anglais)

**Type:** `text`  
**Required:** No  
**Validation:** None / None  


**Description:**  
EN: This field describes the organizational structure tied to the project owner (if applicable), in English  
FR: Ce champ décrira la structure organisationnelle liée à ce projet (si applicable), en anglais


---

#### `lead_branch_fr` – Lead Branch and/or Unit (French) / Direction et/ou unité responsable (en français))

**Type:** `text`  
**Required:** No  
**Validation:** None / None  


**Description:**  
EN: This field describes the organizational structure tied to the project owner (if applicable), in French.  
FR: Ce champ décrira la structure organisationnelle liée à ce projet (si applicable), en français


---

#### `info_supplementaire_en` – Further Information / Links (English) / Informations supplémentaires / liens (anglais)

**Type:** `text`  
**Required:** No  
**Validation:** None / None  


**Description:**  
EN: This field includes a URL link to additional information on the project (e.g. report, blog post, etc.), in English.  
FR: Ce champ incluera un lien URL fournissant des information additionnelles (p.ex. rapport, blogue), en anglais.


---

#### `info_supplementaire_fr` – Further Information / Links (French) / Informations supplémentaires / liens (en français)

**Type:** `text`  
**Required:** No  
**Validation:** None / None  


**Description:**  
EN: This field includes a URL link to additional information on the project (e.g. report, blog post, etc.), in Frencjh.  
FR: Ce champ incluera un lien URL fournissant des information additionnelles (p.ex. rapport, blogue), en français.


---




## Appendix

### Choice Sets Summary (All Resources)
| Choice Set | Field(s) | Values | Standalone Doc |
|------------|----------|--------|----------------|


### Generation Metadata

- Generated: 2025-12-14T01:45:17 (UTC)
- Source: dictionaries/experiment.json
- Commit: `ddfad99`
- Tool Version: simple-1

### Validation

- JSON Schema Validation: **PASSED**


### Notes

This documentation is auto-generated. Do not hand-edit; instead update the source recombinant JSON and re-run generation.