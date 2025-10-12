
# Proactive Publication - Departmental Audit Committee / Publication proactive - Comités ministériels d’audit

**Dataset Type:** `dac`  
**Last Generated:** 2025-10-12T01:23:31 (UTC)  
**Source:** dictionaries/dac.json  
**Commit:** `d437fb3`

Access, upload and modify your Departmental Audit Committee members’ remuneration and expenses. / Accès, téléversement et modification de la rémunération et des dépenses des membres de votre Comité ministériel d’audit.

---

## Resources


- [Proactive Publication - Departmental Audit Committee / Publication proactive - Comités ministériels d’audit](#dac)


---


## Proactive Publication - Departmental Audit Committee / Publication proactive - Comités ministériels d’audit 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `reporting_period` | Reporting Period / Période de déclaration | `text` | Yes |  | reporting_period | The current reporting period and fiscal year |
| `line_number` | Line Number / Numéro de ligne | `int` | Yes |  |  | The line number of the disclosure. |
| `member_name` | Member’s Name / Nom du membre | `text` | Yes |  |  | The member’s full name. |
| `province` | Province or Territory of Primary Residence / Province ou territoire de résidence primaire | `text` | Yes |  | province | The province or territory of the member’s main residence at the time the remune… |
| `role` | Role / Rôle | `text` | Yes |  | role | The member’s role at the time the remuneration and/or expenses were incurred (i… |
| `meeting_hours` | Number of Hours Spent at Meeting(s) / Nombre d&#39;heures consacrées à la rencontre (ou aux rencontres) | `numeric` | Yes |  |  | The number of hours when the member met with the committee in person or via tel… |
| `other_hours` | Number of hours spent on preparation, travel and/or training or orientation / Nombre d&#39;heures consacrées à la préparation, le déplacement et/ou à la formation ou à l&#39;orientation | `numeric` | Yes |  |  | The number of hours the member spent on preparation, travel and/or training or … |
| `remuneration` | Total Remuneration / Rémunération totale | `money` | Yes |  |  | The total amount paid to the member for time spent at meetings, preparation, tr… |
| `travel_expenses` | Total Travel Expenses / Frais de voyage totaux | `money` | Yes |  |  | The total travel expenses incurred by the member during the reporting period, i… |
| `notes_en` | Notes (English) / Notes (Anglais) | `text` | No |  |  | Any other relevant information (e.g. description of the activities included in … |
| `notes_fr` | Notes (French) / Notes (Français) | `text` | No |  |  | Any other relevant information (e.g. description of the activities included in … |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `reporting_period` – Reporting Period / Période de déclaration

**Type:** `text`  
**Required:** Yes  
**Choice Set:** reporting_period (32 values)  


**Description:**  
EN: The current reporting period and fiscal year  
FR: La période de déclaration et l’exercice financier en cours.


##### Allowed Values (reporting_period)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `2018-2019-Q1` | 2018-2019-Q1 | 2018-2019-Q1 |
| `2018-2019-Q2` | 2018-2019-Q2 | 2018-2019-Q2 |
| `2018-2019-Q3` | 2018-2019-Q3 | 2018-2019-Q3 |
| `2018-2019-Q4` | 2018-2019-Q4 | 2018-2019-Q4 |
| `2019-2020-Q1` | 2019-2020-Q1 | 2019-2020-Q1 |
| `2019-2020-Q2` | 2019-2020-Q2 | 2019-2020-Q2 |
| `2019-2020-Q3` | 2019-2020-Q3 | 2019-2020-Q3 |
| `2019-2020-Q4` | 2019-2020-Q4 | 2019-2020-Q4 |
| `2020-2021-Q1` | 2020-2021-Q1 | 2020-2021-Q1 |
| `2020-2021-Q2` | 2020-2021-Q2 | 2020-2021-Q2 |
| `2020-2021-Q3` | 2020-2021-Q3 | 2020-2021-Q3 |
| `2020-2021-Q4` | 2020-2021-Q4 | 2020-2021-Q4 |
| `2021-2022-Q1` | 2021-2022-Q1 | 2021-2022-Q1 |
| `2021-2022-Q2` | 2021-2022-Q2 | 2021-2022-Q2 |
| `2021-2022-Q3` | 2021-2022-Q3 | 2021-2022-Q3 |
| `2021-2022-Q4` | 2021-2022-Q4 | 2021-2022-Q4 |
| `2022-2023-Q1` | 2022-2023-Q1 | 2022-2023-Q1 |
| `2022-2023-Q2` | 2022-2023-Q2 | 2022-2023-Q2 |
| `2022-2023-Q3` | 2022-2023-Q3 | 2022-2023-Q3 |
| `2022-2023-Q4` | 2022-2023-Q4 | 2022-2023-Q4 |
| `2023-2024-Q1` | 2023-2024-Q1 | 2023-2024-Q1 |
| `2023-2024-Q2` | 2023-2024-Q2 | 2023-2024-Q2 |
| `2023-2024-Q3` | 2023-2024-Q3 | 2023-2024-Q3 |
| `2023-2024-Q4` | 2023-2024-Q4 | 2023-2024-Q4 |
| `2024-2025-Q1` | 2024-2025-Q1 | 2024-2025-Q1 |
| `2024-2025-Q2` | 2024-2025-Q2 | 2024-2025-Q2 |
| `2024-2025-Q3` | 2024-2025-Q3 | 2024-2025-Q3 |
| `2024-2025-Q4` | 2024-2025-Q4 | 2024-2025-Q4 |
| `2025-2026-Q1` | 2025-2026-Q1 | 2025-2026-Q1 |
| `2025-2026-Q2` | 2025-2026-Q2 | 2025-2026-Q2 |
| `2025-2026-Q3` | 2025-2026-Q3 | 2025-2026-Q3 |
| `2025-2026-Q4` | 2025-2026-Q4 | 2025-2026-Q4 |




---

#### `line_number` – Line Number / Numéro de ligne

**Type:** `int`  
**Required:** Yes  


**Description:**  
EN: The line number of the disclosure.  
FR: Le numéro de ligne de la divulgation.


---

#### `member_name` – Member’s Name / Nom du membre

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: The member’s full name.  
FR: Le nom complet du membre.


---

#### `province` – Province or Territory of Primary Residence / Province ou territoire de résidence primaire

**Type:** `text`  
**Required:** Yes  
**Choice Set:** province (14 values)  


**Description:**  
EN: The province or territory of the member’s main residence at the time the remuneration and/or expenses were incurred.  
FR: La province ou le territoire de la résidence principale du membre au moment où la rémunération et/ou les frais ont été engagés.


##### Allowed Values (province)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `AB` | Alberta | Alberta |
| `BC` | British Columbia | Colombie-Britannique |
| `MB` | Manitoba | Manitoba |
| `NB` | New Brunswick | Nouveau-Brunswick |
| `NL` | Newfoundland &amp; Labrador | Terre-Neuve-et-Labrador |
| `NS` | Nova Scotia | Nouvelle-Écosse |
| `NT` | Northwest Territories | Territoires du Nord-Ouest |
| `NU` | Nunavut | Nunavut |
| `ON` | Ontario | Ontario |
| `OTHER` | OTHER | AUTRES |
| `PE` | Prince Edward Island | Île-du-Prince-Édouard |
| `QC` | Quebec | Québec |
| `SK` | Saskatchewan | Saskatchewan |
| `YT` | Yukon | Yukon |




---

#### `role` – Role / Rôle

**Type:** `text`  
**Required:** Yes  
**Choice Set:** role (2 values)  


**Description:**  
EN: The member’s role at the time the remuneration and/or expenses were incurred (i.e. “C-P” is for chair and “M-M” is for member)  
FR: Le rôle du membre au moment où la rémunération et/ou les frais ont été engagés (c’est-à-dire, « C-P » est pour président(e) et « M-M » est pour membre).


##### Allowed Values (role)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `C-P` | Chair | Président(e) |
| `M-M` | Member | Membre |




---

#### `meeting_hours` – Number of Hours Spent at Meeting(s) / Nombre d'heures consacrées à la rencontre (ou aux rencontres)

**Type:** `numeric`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: The number of hours when the member met with the committee in person or via teleconference during the reporting period.  
FR: Le nombre d’heures où le membre a rencontré le comité en personne ou par téléconférence au cours de la période de déclaration.


---

#### `other_hours` – Number of hours spent on preparation, travel and/or training or orientation / Nombre d'heures consacrées à la préparation, le déplacement et/ou à la formation ou à l'orientation

**Type:** `numeric`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: The number of hours the member spent on preparation, travel and/or training or orientation during the reporting period.  
FR: Le nombre d’heures que le membre a consacré à la préparation, le déplacement et/ou à la formation ou à l’orientation au cours de la période de déclaration.


---

#### `remuneration` – Total Remuneration / Rémunération totale

**Type:** `money`  
**Required:** Yes  


**Description:**  
EN: The total amount paid to the member for time spent at meetings, preparation, travel and/or training or orientation during the reporting period (i.e. per diem rate ÷ 7.5 hours x number of hours worked).  
FR: Le montant total payé au membre pour le temps consacré aux réunions, à la préparation, le déplacement et/ou à la formation ou à l’orientation au cours de la période de déclaration (c’est-à-dire, taux journalier ÷ 7,5 heures x nombre d’heures travaillées).


---

#### `travel_expenses` – Total Travel Expenses / Frais de voyage totaux

**Type:** `money`  
**Required:** Yes  


**Description:**  
EN: The total travel expenses incurred by the member during the reporting period, including transportation, meals, incidentals, etc.  
FR: Les frais de voyage totaux engagés par le membre au cours de la période de déclaration, y compris le transport, les repas, faux frais, etc.


---

#### `notes_en` – Notes (English) / Notes (Anglais)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: Any other relevant information (e.g. description of the activities included in the total remuneration, point of origin of a member’s travel, etc.)  
FR: Toute autre information pertinente (par exemple, une description des activités incluses dans la rémunération totale, le point de départ du déplacement d’un membre, etc.)


---

#### `notes_fr` – Notes (French) / Notes (Français)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: Any other relevant information (e.g. description of the activities included in the total remuneration, point of origin of a member’s travel, etc.)  
FR: Toute autre information pertinente (par exemple, une description des activités incluses dans la rémunération totale, le point de départ du déplacement d’un membre, etc.)


---




## Appendix

### Choice Sets Summary (All Resources)
| Choice Set | Field(s) | Values | Standalone Doc |
|------------|----------|--------|----------------|


### Generation Metadata

- Generated: 2025-10-12T01:23:31 (UTC)
- Source: dictionaries/dac.json
- Commit: `d437fb3`
- Tool Version: simple-1

### Validation

- JSON Schema Validation: **PASSED**


### Notes

This documentation is auto-generated. Do not hand-edit; instead update the source recombinant JSON and re-run generation.