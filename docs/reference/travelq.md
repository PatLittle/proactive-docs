
# Proactive Publication - Travel Expenses / Publication proactive - Dépenses de voyage

**Dataset Type:** `travelq`  
**Last Generated:** 2025-10-08T20:10:34 (UTC)  
**Source:** dictionaries/travelq.json  
**Commit:** `6af3f8d`

Access, upload and modify the monthly travel expense reports for your organization / Accès, téléversement et modification des rapports mensuels sur les frais de déplacement pour votre organisation

---

## Resources


- [Proactive Publication - Travel Expenses / Publication proactive - Dépenses de voyage](#travelq)

- [Proactive Publication - Travel Expenses Nothing to Report / Publication proactive - Dépenses de voyage (Rien à signaler)](#travelq-nil)


---


## Proactive Publication - Travel Expenses / Publication proactive - Dépenses de voyage 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `ref_number` | Reference Number / Numéro de référence | `text` | Yes |  |  | This field is populated by the organization. It is a unique reference number gi… |
| `disclosure_group` | Disclosure Group / Groupe de divulgation | `text` | No |  | disclosure_group | This field will display the group to which the individual belongs. |
| `title_en` | Title (English) / Titre (anglais) | `text` | Yes |  |  | This field will display the position title of the person who travelled, in English |
| `title_fr` | Title (French) / Titre (français) | `text` | Yes |  |  | This field will display the position title of the person who travelled, in French. |
| `name` | Name / Nom | `text` | Yes |  |  | This field will display the name of the  person who travelled |
| `purpose_en` | Purpose of Travel (English) / But du déplacement (anglais) | `text` | Yes |  |  | A short description, in English, of the reason for the trip. The description sh… |
| `purpose_fr` | Purpose of Travel (French) / But du déplacement (français) | `text` | Yes |  |  | A short description, in French, of the reason for the trip. The description sho… |
| `start_date` | Travel Start Date / Date de début du voyage | `date` | Yes |  |  | To cover the date the travel started |
| `end_date` | Travel End Date / Date de fin du voyage | `date` | Yes |  |  | To cover the date the travel ended (can be the same as travel start date) |
| `destination_en` | Place visited (English) / Endroits visités (anglais) | `text` | Yes |  |  | To include name of the first place visited during the trip in question, in English. |
| `destination_fr` | Place visited (French) / Endroits visités (français) | `text` | Yes |  |  | To include name of the first place visited during the trip in question, in French. |
| `destination_2_en` | Second place visited (English) / Deuxième lieu visité (anglais) | `text` | No |  |  | To include name of second place visited during the trip in question, in English. |
| `destination_2_fr` | Second place visited (French) / Deuxième lieu visité (français) | `text` | No |  |  | To include name of second place visited during the trip in question, in French. |
| `destination_other_en` | Other places visited (English) / Autres lieux visités (anglais) | `text` | No |  |  | To include names of all other places visited during the trip in question, in English. |
| `destination_other_fr` | Other places visited (French) / Autres lieux visités (français) | `text` | No |  |  | To include names of all other places visited during the trip in question, in French. |
| `airfare` | Airfare / Tarif aérien | `money` | No |  |  | Total cost of any airline tickets, if applicable. |
| `other_transport` | Other transportation / Autres moyens de transport | `money` | No |  |  | Total cost of any other forms of transportation (for example, train, bus, vehic… |
| `lodging` | Lodging / Hébergement | `money` | Yes |  |  | Total cost of accommodation |
| `meals` | Meals and incidentals / Frais de repas et frais accessoires | `money` | Yes |  |  | Total cost of meals and incidentals expenses. |
| `other_expenses` | Other expenses / Autres dépenses | `money` | No |  |  | Total cost of all other items that are not covered by the above fields (for exa… |
| `total` | Total Amount / Montant total | `money` | Yes |  |  | The total of the amount listed above. |
| `additional_comments_en` | Additional Comments English / Additional Comments English | `text` | No |  |  | This field may be populated with additional comments in English. |
| `additional_comments_fr` | Additional Comments French / Additional Comments French | `text` | No |  |  | This field may be populated with additional comments in French. |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `ref_number` – Reference Number / Numéro de référence

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field is populated by the organization. It is a unique reference number given to each line item in the spreadsheet. Having a unique identifier for each item will allow users locate a specific item in the registry should they need to modify or delete.
  
FR: Cette zone est remplie par chaque organisation. Un identificateur unique est attribué à chaque poste dans le tableur. Un identificateur unique pour chaque poste permettra aux utilisateurs de repérer un article en particulier s’ils doivent le modifier ou le supprimer.



---

#### `disclosure_group` – Disclosure Group / Groupe de divulgation

**Type:** `text`  
**Required:** No  
**Validation:** Required if "Travel End Date" is on or after April 1st 2025 / Requis si la "date de fin du voyage" est le 1er avril 2025 ou après  
**Choice Set:** disclosure_group (2 values)  


**Description:**  
EN: This field will display the group to which the individual belongs.  
FR: Ce champ indique le groupe auquel appartient l’individu.


##### Allowed Values (disclosure_group)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `MPSES` | Minister/Ministerial adviser/Ministerial staff/Parliamentary Secretary/Exempt Staff | Ministre/Conseiller ministériel/Personnel ministériel/Secrétaire parlementaires/Personnel exonéré |
| `SLE` | Senior officer or employee | Cadre supérieur ou employé |




---

#### `title_en` – Title (English) / Titre (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field will display the position title of the person who travelled, in English  
FR: Cette zone indique le titre du poste de la personne qui a voyagé, en anglais.


---

#### `title_fr` – Title (French) / Titre (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field will display the position title of the person who travelled, in French.  
FR: Cette zone indique le titre du poste de la personne qui a voyagé, en français.


---

#### `name` – Name / Nom

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field will display the name of the  person who travelled  
FR: Ce champ affiche le nom de la personne qui a voyagé


---

#### `purpose_en` – Purpose of Travel (English) / But du déplacement (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: A short description, in English, of the reason for the trip. The description should be succinct (one line if possible) and provide users with a general sense of the trip's purpose. Use of acronyms should be avoided.
  
FR: Brève description de la raison du voyage, en anglais. La description doit être brève (une ligne dans la mesure du possible) et donner une indication générale aux utilisateurs du but du voyage. Il faut éviter d’utiliser des acronymes.



---

#### `purpose_fr` – Purpose of Travel (French) / But du déplacement (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: A short description, in French, of the reason for the trip. The description should be succinct (one line if possible) and provide users with a general sense of the trip's purpose. Use of acronyms should be avoided.
  
FR: Brève description de la raison du voyage, en français. La description doit être brève (une ligne dans la mesure du possible) et donner une indication générale aux utilisateurs du but du voyage. Il faut éviter d’utiliser des acronymes.



---

#### `start_date` – Travel Start Date / Date de début du voyage

**Type:** `date`  
**Required:** Yes  
**Validation:** This field must not be empty.
Date can’t be in the future.
 / Ce champ ne doit pas être vide.
La date ne doit pas être dans le futur.
  


**Description:**  
EN: To cover the date the travel started  
FR: Date de début du voyage


---

#### `end_date` – Travel End Date / Date de fin du voyage

**Type:** `date`  
**Required:** Yes  
**Validation:** This field must not be empty.
Date can’t be in the future.
 / Ce champ ne doit pas être vide.
La date ne doit pas être dans le futur.
  


**Description:**  
EN: To cover the date the travel ended (can be the same as travel start date)  
FR: Date de fin du voyage (peut être la même date que la date du début du voyage)


---

#### `destination_en` – Place visited (English) / Endroits visités (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty
Must be in the format of <City Name>, <State/Province Name>, <Country Name> for Canada and US, or <City Name>, <Country Name> for international
 / Ce champ ne doit pas être vide
Doit être au format <Nom de la ville>, <Nom de l'État/de la province>, <Nom du pays> pour le Canada et les États-Unis, ou <Nom de la ville>, <Nom du pays> pour l'international (p. ex. Ottawa, Ontario, Canada ou Londres, Angleterre)
  


**Description:**  
EN: To include name of the first place visited during the trip in question, in English.  
FR: Inclure le nom du premier lieu visité lors du voyage en question, en anglais.


---

#### `destination_fr` – Place visited (French) / Endroits visités (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty
Must be in the format of <City Name>, <State/Province Name>, <Country Name> for Canada and US, or <City Name>, <Country Name> for international
 / Ce champ ne doit pas être vide
Doit être au format <Nom de la ville>, <Nom de l'État/de la province>, <Nom du pays> pour le Canada et les États-Unis, ou <Nom de la ville>, <Nom du pays> pour l'international
  


**Description:**  
EN: To include name of the first place visited during the trip in question, in French.  
FR: Inclure le nom du premier lieu visité lors du voyage en question, en français.


---

#### `destination_2_en` – Second place visited (English) / Deuxième lieu visité (anglais)

**Type:** `text`  
**Required:** No  
**Validation:** Must be in the format of <City Name>, <State/Province Name>, <Country Name> for Canada and US, or <City Name>, <Country Name> for international
 / Doit être au format <Nom de la ville>, <Nom de l'État/de la province>, <Nom du pays> pour le Canada et les États-Unis, ou <Nom de la ville>, <Nom du pays> pour l'international
  


**Description:**  
EN: To include name of second place visited during the trip in question, in English.  
FR: Inclure le nom du deuxième lieu visité au cours du voyage en question, en anglais.


---

#### `destination_2_fr` – Second place visited (French) / Deuxième lieu visité (français)

**Type:** `text`  
**Required:** No  
**Validation:** Must be in the format of <City Name>, <State/Province Name>, <Country Name> for Canada and US, or <City Name>, <Country Name> for international
 / Doit être au format <Nom de la ville>, <Nom de l'État/de la province>, <Nom du pays> pour le Canada et les États-Unis, ou <Nom de la ville>, <Nom du pays> pour l'international
  


**Description:**  
EN: To include name of second place visited during the trip in question, in French.  
FR: Inclure le nom du deuxième lieu visité au cours du voyage en question, en français.


---

#### `destination_other_en` – Other places visited (English) / Autres lieux visités (anglais)

**Type:** `text`  
**Required:** No  
**Validation:** Must be in the format of <City Name>, <State/Province Name>, <Country Name>;<City 2 Name>, <Country 2 Name>
 / Doit être au format <Nom de la ville>, <Nom de l'État/de la province>, <Nom du pays>;<Nom de la ville 2>, <Nom du pays 2>
  


**Description:**  
EN: To include names of all other places visited during the trip in question, in English.  
FR: Inclure les noms de tous les autres lieux visités au cours du voyage en question, en anglais.


---

#### `destination_other_fr` – Other places visited (French) / Autres lieux visités (français)

**Type:** `text`  
**Required:** No  
**Validation:** Must be in the format of <City Name>, <State/Province Name>, <Country Name>;<City 2 Name>, <Country 2 Name>
 / Doit être au format <Nom de la ville>, <Nom de l'État/de la province>, <Nom du pays>;<Nom de la ville 2>, <Nom du pays 2>
  


**Description:**  
EN: To include names of all other places visited during the trip in question, in French.  
FR: Inclure les noms de tous les autres lieux visités au cours du voyage en question, en français.


---

#### `airfare` – Airfare / Tarif aérien

**Type:** `money`  
**Required:** No  


**Description:**  
EN: Total cost of any airline tickets, if applicable.  
FR: Coût total des billets d’avion, s’il y a lieu.


---

#### `other_transport` – Other transportation / Autres moyens de transport

**Type:** `money`  
**Required:** No  


**Description:**  
EN: Total cost of any other forms of transportation (for example, train, bus, vehicle rental, private vehicle, taxis, etc), if applicable.  
FR: Coût total de toutes autres forme de transport (par exemple, train, autobus, véhicule loué, véhicule particulier, taxis), s’il y a lieu.


---

#### `lodging` – Lodging / Hébergement

**Type:** `money`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: Total cost of accommodation  
FR: Coût total de l’hébergement


---

#### `meals` – Meals and incidentals / Frais de repas et frais accessoires

**Type:** `money`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: Total cost of meals and incidentals expenses.  
FR: Total des frais de repas et accessoires


---

#### `other_expenses` – Other expenses / Autres dépenses

**Type:** `money`  
**Required:** No  


**Description:**  
EN: Total cost of all other items that are not covered by the above fields (for example. special passport, visas, associated photos, calls to the office or home, dependant care where applicable, etc.).  
FR: Coût total de tous les autres éléments qui ne sont pas couverts par les champs ci-dessus (par exemple, passeport spécial, visas, photos connexes, appels au bureau ou à la maison, soin aux personnes à charge, le cas échéant)


---

#### `total` – Total Amount / Montant total

**Type:** `money`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: The total of the amount listed above.  
FR: Le total des montants énumérés ci-dessus


---

#### `additional_comments_en` – Additional Comments English / Additional Comments English

**Type:** `text`  
**Required:** No  


**Description:**  
EN: This field may be populated with additional comments in English.  
FR: Ce champ peut indiquer des commentaires supplémentaires en anglais.


---

#### `additional_comments_fr` – Additional Comments French / Additional Comments French

**Type:** `text`  
**Required:** No  


**Description:**  
EN: This field may be populated with additional comments in French.  
FR: Ce champ peut indiquer des commentaires supplémentaires en français.


---



## Proactive Publication - Travel Expenses Nothing to Report / Publication proactive - Dépenses de voyage (Rien à signaler) 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `year` | Year / Année | `year` | Yes |  |  | This tab / field in the template is only populated if there are no travel expen… |
| `month` | Month / mois | `text` | Yes |  | month | This tab / field in the template is only populated if there are no travel expen… |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `year` – Year / Année

**Type:** `year`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This tab / field in the template is only populated if there are no travel expenses for the reporting period. This field should be populated with the year of the reporting period.
  
FR: Cet onglet/champ du modèle n’est rempli que s'il n'y a pas de frais de voyage pour la période d’établissement de rapports. Ce champ doit être rempli avec l’année de la période d’établissement de rapports.



---

#### `month` – Month / mois

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  
**Choice Set:** month (12 values)  


**Description:**  
EN: This tab / field in the template is only populated if there are no travel expenses for the reporting period. This field should be populated with the month of the reporting period.
  
FR: Cet onglet/champ du modèle n’est rempli que s'il n'y a pas de frais de voyage pour la période d’établissement de rapports. Ce champ doit être rempli avec le mois de la période d’établissement de rapports.



##### Allowed Values (month)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `01` | January | janvier |
| `02` | February | février |
| `03` | March | mars |
| `04` | April | avril |
| `05` | May | mai |
| `06` | June | juin |
| `07` | July | juillet |
| `08` | August | août |
| `09` | September | septembre |
| `10` | October | octobre |
| `11` | November | novembre |
| `12` | December | décembre |




---




## Appendix

### Choice Sets Summary (All Resources)
| Choice Set | Field(s) | Values | Standalone Doc |
|------------|----------|--------|----------------|


### Generation Metadata

- Generated: 2025-10-08T20:10:34 (UTC)
- Source: dictionaries/travelq.json
- Commit: `6af3f8d`
- Tool Version: simple-1

### Validation

- JSON Schema Validation: **PASSED**


### Notes

This documentation is auto-generated. Do not hand-edit; instead update the source recombinant JSON and re-run generation.