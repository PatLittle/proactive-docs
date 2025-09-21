
# ATI Summaries / Accès à l’information sommaires complétés

**Dataset Type:** `ati`  
**Last Generated:** 2025-09-21T01:26:38 (UTC)  
**Source:** dictionaries/ati.json  
**Commit:** `63dfd98`

Access, upload and modify the monthly ATI Summaries and ATI Nothing to Report for your organization / Accès, téléversement et modification des sommaires mensuels des demandes d’accès à l’information et des demandes d’accès pour lesquelles rien n’est à signaler pour votre organisation

---

## Resources


- [ATI Summaries / Accès à l’information sommaires complétés](#ati)

- [ATI Nothing to Report / Accès à l’information rien à signaler](#ati-nil)


---


## ATI Summaries / Accès à l’information sommaires complétés 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `year` | Year / Année | `year` | Yes |  |  | This field must be populated with the four-digit calendar year that the request… |
| `month` | Month (1-12) / Mois (1-12) | `month` | Yes |  |  | This field must be populated with a numerical representation of the month durin… |
| `request_number` | Request Number / Numero de la demande | `text` | Yes |  |  | Your institution’s request file number of the completed Access to Information r… |
| `summary_en` | English Summary / Sommaire de la demande en anglais | `text` | Yes |  |  | A descriptive summary of the completed Access to Information request in English. |
| `summary_fr` | French Summary / Sommaire de la demande en français | `text` | Yes |  |  | A descriptive summary of the completed Access to Information request in French. |
| `disposition` | Disposition / Disposition | `text` | Yes |  | disposition | The response disposition of the completed Access to Information request |
| `pages` | Number of Pages / Nombre de pages | `int` | Yes |  |  | The number of pages released in response to the completed Access to Information… |
| `comments_en` | Comments English / Commentaires en anglais | `text` | No |  |  | This field may be populated with additional or contextual comments in English. |
| `comments_fr` | Comments French / Commentaires en français | `text` | No |  |  | This field may be populated with additional or contextual comments in French. |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `year` – Year / Année

**Type:** `year`  
**Required:** Yes  
**Validation:** Must be not be in the future or before 2011 / Ne peux pas être dans le futur ni avant 2011  


**Description:**  
EN: This field must be populated with the four-digit calendar year that the request was closed.  
FR: Ce champ doit être complété avec l’année civile à quatre chiffres durant laquelle la demande a été complétée.


---

#### `month` – Month (1-12) / Mois (1-12)

**Type:** `month`  
**Required:** Yes  
**Validation:** Must be in the range of 1-12 (representing January-December). / Doit être dans la gamme de 1-12 (représente janvier-décembre)  


**Description:**  
EN: This field must be populated with a numerical representation of the month during which the request was closed.  
FR: Ce champ doit être complété avec la représentation numérique du mois durant lequel la demande a été complétée.


---

#### `request_number` – Request Number / Numero de la demande

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: Your institution’s request file number of the completed Access to Information request.  
FR: Numéro de dossier de demande de votre institution de la demande d’accès à l’information complétée.


---

#### `summary_en` – English Summary / Sommaire de la demande en anglais

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: A descriptive summary of the completed Access to Information request in English.  
FR: Un résumé descriptif de la demande d’accès à l’information en anglais.


---

#### `summary_fr` – French Summary / Sommaire de la demande en français

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: A descriptive summary of the completed Access to Information request in French.  
FR: Un résumé descriptif de la demande d’accès à l’information en français.


---

#### `disposition` – Disposition / Disposition

**Type:** `text`  
**Required:** Yes  
**Choice Set:** disposition (5 values)  


**Description:**  
EN: The response disposition of the completed Access to Information request  
FR: La disposition de la réponse de la demande d’accès à l’information complétée.


##### Allowed Values (disposition)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `DA` | All disclosed | Communication totale |
| `DP` | Disclosed in part | Communication partielle |
| `EC` | All excluded | Exclusion totale |
| `EX` | All exempted | Exception totale |
| `NE` | No records exist | Aucun document n’existe |




---

#### `pages` – Number of Pages / Nombre de pages

**Type:** `int`  
**Required:** Yes  
**Validation:** This value must not be negative / Cette valeur ne doit pas être négatif  


**Description:**  
EN: The number of pages released in response to the completed Access to Information request. If no records were released, enter a value of “0”.  
FR: Le nombre de pages publiées en réponse à la demande d’accès à l’information. Si aucun enregistrement n’a été publié, entrez la valeur « 0 ».


---

#### `comments_en` – Comments English / Commentaires en anglais

**Type:** `text`  
**Required:** No  


**Description:**  
EN: This field may be populated with additional or contextual comments in English.  
FR: Ce champ peut être rempli avec des commentaires supplémentaires ou contextuels en anglais.


---

#### `comments_fr` – Comments French / Commentaires en français

**Type:** `text`  
**Required:** No  


**Description:**  
EN: This field may be populated with additional or contextual comments in French.  
FR: Ce champ peut être rempli avec des commentaires supplémentaires ou contextuels en français.


---



## ATI Nothing to Report / Accès à l’information rien à signaler 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `year` | Year / Année | `year` | Yes |  |  | Four-digit calendar year of the month for which you are reporting no summaries … |
| `month` | Month (1-12) / Mois (1-12) | `month` | Yes |  |  | A numerical representation of the month for which you are reporting no summarie… |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `year` – Year / Année

**Type:** `year`  
**Required:** Yes  
**Validation:** Must be not be in the future or before 2011 / Ne peux pas être dans le futur ni avant 2011  


**Description:**  
EN: Four-digit calendar year of the month for which you are reporting no summaries to publish.  
FR: Année civile a quatre chiffres du mois pour lequel vous ne signalez aucun résumé à publier.


---

#### `month` – Month (1-12) / Mois (1-12)

**Type:** `month`  
**Required:** Yes  
**Validation:** Must be in the range of 1-12 (representing January-December). / Doit être dans la gamme de 1-12 (représente janvier-décembre)  


**Description:**  
EN: A numerical representation of the month for which you are reporting no summaries to publish.  
FR: Une représentation numérique du mois pour lequel vous ne signalez aucun résumé a publier.


---




## Appendix

### Choice Sets Summary (All Resources)
| Choice Set | Field(s) | Values | Standalone Doc |
|------------|----------|--------|----------------|


### Generation Metadata

- Generated: 2025-09-21T01:26:38 (UTC)
- Source: dictionaries/ati.json
- Commit: `63dfd98`
- Tool Version: simple-1

### Validation

- JSON Schema Validation: **PASSED**


### Notes

This documentation is auto-generated. Do not hand-edit; instead update the source recombinant JSON and re-run generation.