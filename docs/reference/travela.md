
# Proactive Publication - Annual Travel, Hospitality and Conferences / Publication proactive - Dépenses annuelles de voyages, d’accueil, de conférences et d’événements

**Dataset Type:** `travela`  
**Last Generated:** 2025-08-24T01:39:58 (UTC)  
**Source:** dictionaries/travela.json  
**Commit:** `ece18ac`

This dataset includes all of the annual reports on travel expenses incurred within your organization. / Ce jeu de données comprend tous les rapports annuels sur les dépenses de voyage ayant été encourues au sein de votre organisation.

---

## Resources


- [Proactive Publication - Annual Travel, Hospitality and Conferences / Publication proactive - Dépenses annuelles de voyages, d’accueil, de conférences et d’événements](#travela)


---


## Proactive Publication - Annual Travel, Hospitality and Conferences / Publication proactive - Dépenses annuelles de voyages, d’accueil, de conférences et d’événements 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `year` | Fiscal Year Ending / Dépenses pour l’exercice financier se terminant | `year` | Yes |  |  | This fields shows the current fiscal reporting period’s ending (March 31, YYYY). |
| `mandate_description_en` | Description of departmental mandate (English) / Description du mandat du ministère (anglais) | `text` | Yes |  |  | Provide a brief explanation, in English, of the department’s mandate, major pro… |
| `mandate_description_fr` | Description of departmental mandate (French) / Description du mandat du ministère (français) | `text` | Yes |  |  | Provide a brief explanation, in French, of the department’s mandate, major prog… |
| `operational_activities_kdollars` | Travel ≥2018 – Operational activities ($ thousands) / Voyage ≥2018 – activités opérationnelles (Milliers de dollars) | `numeric` | No |  |  | This field shows annual expenditures for travel of public servants and non-publ… |
| `key_stakeholders_kdollars` | Travel ≥2018 – Key stakeholders ($ thousands) / Voyage ≥2018 – Principaux intervenants (Milliers de dollars) | `numeric` | No |  |  | This field shows annual expenditures for travel of public servants and non-publ… |
| `training_kdollars` | Travel ≥2018 – Training ($ thousands) / Voyage ≥2018 – Formation (Milliers de dollars) | `numeric` | No |  |  | This field shows annual expenditures for travel of public servants and non-publ… |
| `other_kdollars` | Travel ≥2018 – Other ($ thousands) / Voyage ≥2018 – Autre (Milliers de dollars) | `numeric` | No |  |  | This field shows annual expenditures for travel of public servants and non-publ… |
| `internal_governance_kdollars` | Travel ≥2018 – Internal governance ($ thousands) / Voyage ≥2018 – Gouvernance interne (Milliers de dollars) | `numeric` | No |  |  | This field shows annual expenditures for travel of public servants and non-publ… |
| `non_public_servants_kdollars` | Travel &lt;2018 – Non-Public Servants ($ thousands) / Voyage &lt;2018 – non-fonctionnaires (Milliers de dollars) | `numeric` | No |  |  | This field shows annual expenditures for travel of non-public servants for the … |
| `public_servants_kdollars` | Travel &lt;2018 – Public Servants ($ thousands) / Voyage &lt;2018 – fonctionnaires (Milliers de dollars) | `numeric` | No |  |  | This field shows annual expenditures for travel of public servants for the curr… |
| `hospitality_kdollars` | Hospitality ($ thousands) / Accueil (Milliers de dollars) | `numeric` | Yes |  |  | This field shows annual expenditures for hospitality for the previous reporting… |
| `conference_fees_kdollars` | Conference Fees ($ thousands) / Frais de participation aux conférences (Milliers de dollars) | `numeric` | Yes |  |  | This field shows annual expenditures for conference fees for the current report… |
| `minister_kdollars` | International Travel by Minister and Minister&#39;s Staff ($ thousands) / Voyages internationaux du ministre et du personnel du ministre (Milliers de dollars) | `numeric` | Yes |  |  | This field shows annual expenditures for international travel by Minister and M… |
| `travel_compared_fiscal_year_en` | Explanation of Significant Variance of the total travel expenditure (English) / Explication d’un écart important du total des dépenses de voyages (anglais) | `text` | No |  |  | Provide a brief explanation, in English, of the significant reason(s) for the i… |
| `travel_compared_fiscal_year_fr` | Explanation of Significant Variance of the total travel expenditure (French) / Explication d’un écart important du total des dépenses de voyages (français) | `text` | No |  |  | Provide a brief explanation, in French, of the significant reason(s) for the in… |
| `hospitality_compared_fiscal_year_en` | Hospitality - Explanation of Significant Variance (English) / Accueil - Explication d’un écart important (anglais) | `text` | No |  |  | Provide a brief explanation, in English, of the significant reason(s) for the i… |
| `hospitality_compared_fiscal_year_fr` | Hospitality - Explanation of Significant Variance (French) / Accueil - Explication d’un écart important (français) | `text` | No |  |  | Provide a brief explanation, in French, of the significant reason(s) for the in… |
| `conference_fees_compared_fiscal_year_en` | Conference Fees - Explanation of Significant Variance (English) / Frais de participation aux conférences - Explication d’un écart important (anglais) | `text` | No |  |  | Provide a brief explanation, in English, of the significant reason(s) for the i… |
| `conference_fees_compared_fiscal_year_fr` | Conference Fees - Explanation of Significant Variance (French) / Frais de participation aux conférences - Explication d’un écart important (français) | `text` | No |  |  | Provide a brief explanation, in French, of the significant reason(s) for the in… |
| `minister_compared_fiscal_year_en` | International Travel by Minister and Minister’s Staff - Explanation of Significant Variance (English) / Voyages internationaux du ministre et du personnel du ministre - Explication d’un écart important (anglais) | `text` | No |  |  | Provide a brief explanation, in English, of the significant reason(s) for the i… |
| `minister_compared_fiscal_year_fr` | International Travel by Minister and Minister’s Staff - Explanation of Significant Variance (French) / Voyages internationaux du ministre et du personnel du ministre - Explication d’un écart important (français) | `text` | No |  |  | Provide a brief explanation, in French, of the significant reason(s) for the in… |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `year` – Fiscal Year Ending / Dépenses pour l’exercice financier se terminant

**Type:** `year`  
**Required:** Yes  


**Description:**  
EN: This fields shows the current fiscal reporting period’s ending (March 31, YYYY).  
FR: Ce champ montre l’année de clôture de l’exercice financier en cours (31 mars AAAA).


---

#### `mandate_description_en` – Description of departmental mandate (English) / Description du mandat du ministère (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: Provide a brief explanation, in English, of the department’s mandate, major programs and linkages with core laws or regulations to help readers understand the travel, hospitality and conference expenditures incurred by the department and how they support the department’s mandate, including significant structural or program changes.  
FR: Décrivez brièvement, en anglais, le mandat du ministère, ses principaux programmes et les liens avec les lois ou les règlements fondamentaux afin d’aider les lecteurs à comprendre les dépenses de voyages, d’accueil et de conférences engagées par le ministère, et en quoi ces dépenses soutiennent le mandat du ministère


---

#### `mandate_description_fr` – Description of departmental mandate (French) / Description du mandat du ministère (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: Provide a brief explanation, in French, of the department’s mandate, major programs and linkages with core laws or regulations to help readers understand the travel, hospitality and conference expenditures incurred by the department and how they support the department’s mandate, including significant structural or program changes.  
FR: Décrivez brièvement, en français, le mandat du ministère, ses principaux programmes et les liens avec les lois ou les règlements fondamentaux afin d’aider les lecteurs à comprendre les dépenses de voyages, d’accueil et de conférences engagées par le ministère, et en quoi ces dépenses soutiennent le mandat du ministère


---

#### `operational_activities_kdollars` – Travel ≥2018 – Operational activities ($ thousands) / Voyage ≥2018 – activités opérationnelles (Milliers de dollars)

**Type:** `numeric`  
**Required:** No  


**Description:**  
EN: This field shows annual expenditures for travel of public servants and non-public servants for the expenditure category – Operational activities for the current reporting fiscal year (Year Ending March 31, YYYY) in thousands of dollars  
FR: Ce champ montre les dépenses annuelles de voyage de fonctionnaires et non-fonctionnaires pour la catégorie de dépenses activités opérationnelles pour l’exercice financier en cours (année se terminant le 31 mars AAAA), en milliers de dollars


---

#### `key_stakeholders_kdollars` – Travel ≥2018 – Key stakeholders ($ thousands) / Voyage ≥2018 – Principaux intervenants (Milliers de dollars)

**Type:** `numeric`  
**Required:** No  


**Description:**  
EN: This field shows annual expenditures for travel of public servants and non-public servants for the expenditure category – key stakeholders for the current reporting fiscal year (Year Ending March 31, YYYY) in thousands of dollars  
FR: Ce champ montre les dépenses annuelles de voyage de -fonctionnaires et non-fonctionnaires pour la catégorie de dépenses principaux intervenants,  pour l’exercice financier en cours (année se terminant le 31 mars AAAA), en milliers de dollars


---

#### `training_kdollars` – Travel ≥2018 – Training ($ thousands) / Voyage ≥2018 – Formation (Milliers de dollars)

**Type:** `numeric`  
**Required:** No  


**Description:**  
EN: This field shows annual expenditures for travel of public servants and non-public servants for the expenditure category – Training for the current reporting fiscal year (Year Ending March 31, YYYY) in thousands of dollars  
FR: Ce champ montre les dépenses annuelles de voyage de fonctionnaires et non-fonctionnaires pour la catégorie de dépenses formation, pour l’exercice financier en cours (année se terminant le 31 mars AAAA), en milliers de dollars


---

#### `other_kdollars` – Travel ≥2018 – Other ($ thousands) / Voyage ≥2018 – Autre (Milliers de dollars)

**Type:** `numeric`  
**Required:** No  


**Description:**  
EN: This field shows annual expenditures for travel of public servants and non-public servants for the expenditure category – Other for the current reporting fiscal year (Year Ending March 31, YYYY) in thousands of dollars  
FR: Ce champ montre les dépenses annuelles de voyage de fonctionnaires et non-fonctionnaires pour la catégorie de dépenses autre, pour l’exercice financier en cours (année se terminant le 31 mars AAAA), en milliers de dollars


---

#### `internal_governance_kdollars` – Travel ≥2018 – Internal governance ($ thousands) / Voyage ≥2018 – Gouvernance interne (Milliers de dollars)

**Type:** `numeric`  
**Required:** No  


**Description:**  
EN: This field shows annual expenditures for travel of public servants and non-public servants for the expenditure category – Internal governance for the current reporting fiscal year (Year Ending March 31, YYYY) in thousands of dollars  
FR: Ce champ montre les dépenses annuelles de voyage de fonctionnaires et non-fonctionnaires pour la catégorie de dépenses gouvernance interne, pour l’exercice financier en cours (année se terminant le 31 mars AAAA), en milliers de dollars


---

#### `non_public_servants_kdollars` – Travel <2018 – Non-Public Servants ($ thousands) / Voyage <2018 – non-fonctionnaires (Milliers de dollars)

**Type:** `numeric`  
**Required:** No  


**Description:**  
EN: This field shows annual expenditures for travel of non-public servants for the current reporting fiscal year (Year Ending March 31, YYYY) in thousands of dollars  
FR: Ce champ montre les dépenses annuelles de voyage de non-fonctionnaires pour l’exercice financier en cours (année se terminant le 31 mars AAAA), en milliers de dollars


---

#### `public_servants_kdollars` – Travel <2018 – Public Servants ($ thousands) / Voyage <2018 – fonctionnaires (Milliers de dollars)

**Type:** `numeric`  
**Required:** No  


**Description:**  
EN: This field shows annual expenditures for travel of public servants for the current reporting fiscal year (Year Ending March 31, YYYY) in thousands of dollars  
FR: Ce champ montre les dépenses annuelles de voyage de fonctionnaires pour l’exercice financier en cours (année se terminant le 31 mars AAAA), en milliers de dollars


---

#### `hospitality_kdollars` – Hospitality ($ thousands) / Accueil (Milliers de dollars)

**Type:** `numeric`  
**Required:** Yes  


**Description:**  
EN: This field shows annual expenditures for hospitality for the previous reporting fiscal year (Year Ending March 31, YYYY-1) in thousands of dollars  
FR: Ce champ montre les dépenses annuelles d’accueil pour l’exercice financier précédent (année se terminant le 31 mars AAAA-1), en milliers de dollars


---

#### `conference_fees_kdollars` – Conference Fees ($ thousands) / Frais de participation aux conférences (Milliers de dollars)

**Type:** `numeric`  
**Required:** Yes  


**Description:**  
EN: This field shows annual expenditures for conference fees for the current reporting fiscal year (Year Ending March 31, YYYY) in thousands of dollars  
FR: Ce champ montre les dépenses annuelles de conférences pour l’exercice financier en cours (année se terminant le 31 mars AAAA), en milliers de dollars


---

#### `minister_kdollars` – International Travel by Minister and Minister's Staff ($ thousands) / Voyages internationaux du ministre et du personnel du ministre (Milliers de dollars)

**Type:** `numeric`  
**Required:** Yes  


**Description:**  
EN: This field shows annual expenditures for international travel by Minister and Minister’s staff for the current reporting year (Year Ending March 31, YYYY) in thousands of dollars  
FR: Ce champ montre les dépenses annuelles de voyage à l’étranger du ministre et de son personnel pour l’exercice financier en cours (année se terminant le 31 mars AAAA), en milliers de dollars


---

#### `travel_compared_fiscal_year_en` – Explanation of Significant Variance of the total travel expenditure (English) / Explication d’un écart important du total des dépenses de voyages (anglais)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: Provide a brief explanation, in English, of the significant reason(s) for the increase/decrease in annual expenditures for travel of public servants and non-public servants.  
FR: Expliquez brièvement, en anglais, la ou les raisons significatives de l’augmentation ou de la diminution des dépenses annuelles de voyage pour les fonctionnaires et non-fonctionnaires.


---

#### `travel_compared_fiscal_year_fr` – Explanation of Significant Variance of the total travel expenditure (French) / Explication d’un écart important du total des dépenses de voyages (français)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: Provide a brief explanation, in French, of the significant reason(s) for the increase/decrease in annual expenditures for travel of public servants and non-public servants.  
FR: Expliquez brièvement, en français, la ou les raisons significatives de l’augmentation ou de la diminution des dépenses annuelles de voyage pour les fonctionnaires et non-fonctionnaires.


---

#### `hospitality_compared_fiscal_year_en` – Hospitality - Explanation of Significant Variance (English) / Accueil - Explication d’un écart important (anglais)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: Provide a brief explanation, in English, of the significant reason(s) for the increase/decrease in annual expenditures for hospitality.  
FR: Expliquez brièvement, en anglais, la ou les raisons significatives de l’augmentation ou de la diminution des dépenses annuelles d’accueil.


---

#### `hospitality_compared_fiscal_year_fr` – Hospitality - Explanation of Significant Variance (French) / Accueil - Explication d’un écart important (français)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: Provide a brief explanation, in French, of the significant reason(s) for the increase/decrease in annual expenditures for hospitality.  
FR: Expliquez brièvement, en français, la ou les raisons significatives de l’augmentation ou de la diminution des dépenses annuelles d’accueil.


---

#### `conference_fees_compared_fiscal_year_en` – Conference Fees - Explanation of Significant Variance (English) / Frais de participation aux conférences - Explication d’un écart important (anglais)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: Provide a brief explanation, in English, of the significant reason(s) for the increase/decrease in annual expenditures for conference fees.  
FR: Expliquez brièvement, en anglais, la ou les raisons significatives de l’augmentation ou de la diminution des dépenses annuelles de conférences.


---

#### `conference_fees_compared_fiscal_year_fr` – Conference Fees - Explanation of Significant Variance (French) / Frais de participation aux conférences - Explication d’un écart important (français)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: Provide a brief explanation, in French, of the significant reason(s) for the increase/decrease in annual expenditures for conference fees.  
FR: Expliquez brièvement, en français, la ou les raisons significatives de l’augmentation ou de la diminution des dépenses annuelles de conférences


---

#### `minister_compared_fiscal_year_en` – International Travel by Minister and Minister’s Staff - Explanation of Significant Variance (English) / Voyages internationaux du ministre et du personnel du ministre - Explication d’un écart important (anglais)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: Provide a brief explanation, in English, of the significant reason(s) for the increase/decrease in annual expenditures for international travel by the minister and minister's staff.  
FR: Expliquez brièvement, en anglais, la ou les raisons significatives de l’augmentation ou de la diminution des dépenses annuelles de voyage à l’étranger pour le ministre et son personnel.


---

#### `minister_compared_fiscal_year_fr` – International Travel by Minister and Minister’s Staff - Explanation of Significant Variance (French) / Voyages internationaux du ministre et du personnel du ministre - Explication d’un écart important (français)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: Provide a brief explanation, in French, of the significant reason(s) for the increase/decrease in annual expenditures for international travel by the minister and minister's staff.  
FR: Expliquez brièvement, en français, la ou les raisons significatives de l’augmentation ou de la diminution des dépenses annuelles de voyage à l’étranger pour le ministre et son personnel.


---




## Appendix

### Choice Sets Summary (All Resources)
| Choice Set | Field(s) | Values | Standalone Doc |
|------------|----------|--------|----------------|


### Generation Metadata

- Generated: 2025-08-24T01:39:58 (UTC)
- Source: dictionaries/travela.json
- Commit: `ece18ac`
- Tool Version: simple-1

### Validation

- JSON Schema Validation: **PASSED**


### Notes

This documentation is auto-generated. Do not hand-edit; instead update the source recombinant JSON and re-run generation.