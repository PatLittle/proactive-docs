
# Proactive Publication - Acts of Founded Wrongdoing / Publication proactive - Dossiers sur les actes répréhensibles fondés

**Dataset Type:** `wrongdoing`  
**Last Generated:** 2026-01-18T01:50:04 (UTC)  
**Source:** dictionaries/wrongdoing.json  
**Commit:** `4793aa3`

Access, upload and modify the Acts of Founded Wrongdoing reports for your organization / Accès, téléversement et modifications des dossiers sur les actes répréhensibles fondés pour votre organisation

---

## Resources


- [Proactive Publication - Founded Wrongdoing / Publication proactive - Dossiers sur les actes répréhensibles fondés](#wrongdoing)


---


## Proactive Publication - Founded Wrongdoing / Publication proactive - Dossiers sur les actes répréhensibles fondés 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `ref_number` | Reference Number / Numéro de référence | `text` | Yes |  |  | This field is populated by the user. It is a unique reference number given to e… |
| `file_id_number` | File Identification Number / Numéro d’identification du fichier | `text` | Yes |  |  | This field will contain the file identification number of the founded wrongdoin… |
| `file_id_date` | File Identification date / Date d’identification du ficher | `date` | Yes |  |  | This field will provide the date that the file was created/received. |
| `case_description_en` | English Case Description / Description anglaise | `text` | Yes |  |  | The field will contain the case description, in English. |
| `case_description_fr` | French Case Description / Description française | `text` | Yes |  |  | This field will contain the case description, in French. |
| `findings_conclusions` | Findings and Conclusions / Constatations et Conclusions | `_text` | Yes |  | findings_conclusions | The field will contain value(s) a – f, separated by commas if more than one value. |
| `recommendations_corrective_measures_en` | English Recommendations and Corrective Measures / Recommendations et mesures Correctives anglaises | `text` | Yes |  |  | The Field will contain the Recommendations and Corrective Measures as per the a… |
| `recommendations_corrective_measures_fr` | French Recommendations and Corrective Measures / Recommendations et mesures Correctives françaises | `text` | Yes |  |  | The Field will contain the Recommendations and Corrective Measures as per the a… |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `ref_number` – Reference Number / Numéro de référence

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: This field is populated by the user. It is a unique reference number given to each line item in the spreadsheet. Having a unique identifier for each item will allow users locate a specific item in the registry should they need to modify or delete.  
FR: Cette zone est remplie par chaque organisation. Un identificateur unique est attribué à chaque poste dans le tableur. Un identificateur unique pour chaque poste permettra aux utilisateurs de repérer un article en particulier s’ils doivent le modifier ou le supprimer.


---

#### `file_id_number` – File Identification Number / Numéro d’identification du fichier

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: This field will contain the file identification number of the founded wrongdoing file.  
FR: Cette zone renferme le numéro d’identification du dossier de l’acte répréhensible constaté.


---

#### `file_id_date` – File Identification date / Date d’identification du ficher

**Type:** `date`  
**Required:** Yes  


**Description:**  
EN: This field will provide the date that the file was created/received.  
FR: Cette zone renferme la date à laquelle le dossier a été créé ou reçu.


---

#### `case_description_en` – English Case Description / Description anglaise

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: The field will contain the case description, in English.  
FR: Cette zone renferme la description du cas en anglais.


---

#### `case_description_fr` – French Case Description / Description française

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: This field will contain the case description, in French.  
FR: Cette zone renferme la description du cas en français.


---

#### `findings_conclusions` – Findings and Conclusions / Constatations et Conclusions

**Type:** `_text`  
**Required:** Yes  
**Choice Set:** findings_conclusions (6 values)  


**Description:**  
EN: The field will contain value(s) a – f, separated by commas if more than one value.  
FR: Le champ contiendra une (des) valeur(s) a – f, séparées par une virgule s´il y en a plus d´une.


##### Allowed Values (findings_conclusions)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `a` | a contravention of any Act of Parliament or of the legislature of a province, or of any regulations made under any such Act, other than a contravention of section 19 of this Act | la contravention d’une loi fédérale ou provinciale ou d’un règlement pris sous leur régime, à l’exception de la contravention de l’article 19 de la présente loi |
| `b` | a misuse of public funds or a public asset | l’usage abusif des fonds ou des biens publics |
| `c` | a gross mismanagement in the public sector | les cas graves de mauvaise gestion dans le secteur public |
| `d` | an act or omission that creates a substantial and specific danger to the life, health or safety of persons, or to the environment, other than a danger that is inherent in the performance of the duties or functions of a public servant | le fait de causer — par action ou omission — un risque grave et précis pour la vie, la santé ou la sécurité humaines ou pour l’environnement, à l’exception du risque inhérent à l’exercice des attributions d’un fonctionnaire |
| `e` | a serious breach of a code of conduct established under section 5 or 6 | la contravention grave d’un code de conduite établi en vertu des articles 5 ou 6 |
| `f` | knowingly directing or counselling a person to commit a wrongdoing set out in any of paragraphs (a) to (e) | le fait de sciemment ordonner ou conseiller à une personne de commettre l’un des actes répréhensibles visés aux alinéas a) à e) |




---

#### `recommendations_corrective_measures_en` – English Recommendations and Corrective Measures / Recommendations et mesures Correctives anglaises

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: The Field will contain the Recommendations and Corrective Measures as per the article 11 of the Public Servants Disclosure Protection Act, in English.  
FR: Cette zone renferme les recommandations et mesures correctives en anglais, en conformité à l’article 11 de la Loi sur la protection des fonctionnaires divulgateurs d’actes répréhensibles.


---

#### `recommendations_corrective_measures_fr` – French Recommendations and Corrective Measures / Recommendations et mesures Correctives françaises

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: The Field will contain the Recommendations and Corrective Measures as per the article 11 of the Public Servants Disclosure Protection Act, in French.  
FR: Cette zone renferme les recommandations et mesures correctives en français, en conformité à l’article 11 de la Loi sur la protection des fonctionnaires divulgateurs d’actes répréhensibles.


---




## Appendix

### Choice Sets Summary (All Resources)
| Choice Set | Field(s) | Values | Standalone Doc |
|------------|----------|--------|----------------|


### Generation Metadata

- Generated: 2026-01-18T01:50:04 (UTC)
- Source: dictionaries/wrongdoing.json
- Commit: `4793aa3`
- Tool Version: simple-1

### Validation

- JSON Schema Validation: **PASSED**


### Notes

This documentation is auto-generated. Do not hand-edit; instead update the source recombinant JSON and re-run generation.