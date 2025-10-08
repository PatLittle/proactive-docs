
# Proactive Publication - Hospitality Expenses / Publication proactive - Dépenses d'accueil

**Dataset Type:** `hospitalityq`  
**Last Generated:** 2025-10-08T20:10:33 (UTC)  
**Source:** dictionaries/hospitalityq.json  
**Commit:** `6af3f8d`

Access, upload and modify the quarterly hospitality expenses for your organization / Accès, téléversement et modification des dépenses trimestriellement liées à l’accueil pour votre organisation

---

## Resources


- [Proactive Publication - Hospitality Expenses / Publication proactive - Dépenses d'accueil](#hospitalityq)

- [Proactive Publication - Hospitality Nothing to Report / Publication proactive - Dépenses d'accueil (Rien à signaler)](#hospitalityq-nil)


---


## Proactive Publication - Hospitality Expenses / Publication proactive - Dépenses d'accueil 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `ref_number` | Reference Number / Numéro de référence | `text` | Yes |  |  | This field is populated by the organization. It is a unique reference number gi… |
| `disclosure_group` | Disclosure Group / Groupe de divulgation | `text` | No |  | disclosure_group | This field will display the group to which the individual belongs. |
| `title_en` | Title (English) / Titre (anglais) | `text` | Yes |  |  | This field will display, in English, the position title of the individual who i… |
| `title_fr` | Title (French) / Titre (français) | `text` | Yes |  |  | This field will display, in French, the position title of the individual who in… |
| `name` | Name / Nom | `text` | Yes |  |  | This field will display the name of the individual who incurred the hospitality… |
| `description_en` | Purpose of hospitality activity (English) / But de l’activité d’accueil (anglais) | `text` | Yes |  |  | This will cover both the forms (for example, breakfast, refreshment, lunch, rec… |
| `description_fr` | Purpose of hospitality activity (French) / But de l’activité d’accueil (français) | `text` | Yes |  |  | This will cover both the forms (for example, breakfast, refreshment, lunch, rec… |
| `start_date` | Start Date / Date de début | `date` | Yes |  |  | The start date on which the hospitality was provided. |
| `end_date` | End Date / Date de fin | `date` | Yes |  |  | The end date on which the hospitality was provided. (can be the same as start date) |
| `location_en` | Municipality where the hospitality activity took place (English) / Municipalité où l’activité d’accueil a eu lieu (anglais) | `text` | Yes |  |  | Must include the Municipality where hospitality was provided, in English |
| `location_fr` | Municipality where the hospitality activity took place (French) / Municipalité où l’activité d’accueil a eu lieu (français) | `text` | Yes |  |  | Must include the Municipality where hospitality was provided, in French. |
| `vendor_en` | Name of the first commercial establishment or vendor involved in the hospitality activity (English) / Nom du premier établissement commercial ou fournisseur impliqué dans l’activité d’accueil (anglais) | `text` | Yes |  |  | Must include the name of the first commercial establishment or vendor that prov… |
| `vendor_fr` | Name of the first commercial establishment or vendor involved in the hospitality activity (French) / Nom du premier établissement commercial ou fournisseur impliqué dans l’activité d’accueil (français) | `text` | Yes |  |  | Must include the name of the first commercial establishment or vendor that prov… |
| `vendor_2_en` | Name of the second commercial establishment or vendor involved in the hospitality activity (English) / Nom du deuxième établissement commercial ou fournisseur impliqué dans l’activité d’accueil (anglais) | `text` | No |  |  | Must include the name of the second commercial establishment or vendor that pro… |
| `vendor_2_fr` | Name of the second commercial establishment or vendor involved in the hospitality activity (French) / Nom du deuxième établissement commercial ou fournisseur impliqué dans l’activité d’accueil (français) | `text` | No |  |  | Must include the name of the second commercial establishment or vendor that pro… |
| `vendor_other_en` | Name of any other commercial establishments or vendors involved in the hospitality activity (English) / Nom de tout autre établissement commercial ou fournisseur impliqué dans l’activité d’accueil (anglais) | `text` | No |  |  | Must include the names of any other commercial establishments or vendors that p… |
| `vendor_other_fr` | Name of any other commercial establishments or vendors involved in the hospitality activity (French) / Nom de tout autre établissement commercial ou fournisseur impliqué dans l’activité d’accueil (français) | `text` | No |  |  | Must include the name of any other commercial establishments or vendors that pr… |
| `employee_attendees` | Attendees (Government of Canada Officials) / Participants (Nombre de représentants du gouvernement du Canada) | `int` | Yes |  |  | The total number of attendees (Government of Canada Officials). For any clarifi… |
| `guest_attendees` | Attendees (Guests) / Participants (Nombre d’invités) | `int` | Yes |  |  | The total number of attendees (Guests) |
| `total` | Total cost / Total des coûts | `money` | Yes |  |  | Total Amount of the expenses for the hospitality activity |
| `additional_comments_en` | Additional comments (English) / Commentaires additionnels (anglais) | `text` | No |  |  | This field may be populated with additional explanatory comments, in English. |
| `additional_comments_fr` | Additional comments (French) / Commentaires additionnels (français) | `text` | No |  |  | This field may be populated with additional explanatory comments, in French. |


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
**Validation:** Required if "End Date" is on or after April 1st 2025 / Requis si la "date de fin" est le 1er avril 2025 ou après  
**Choice Set:** disclosure_group (2 values)  


**Description:**  
EN: This field will display the group to which the individual belongs.  
FR: Ce champ indique le groupe auquel appartient l’individu.


##### Allowed Values (disclosure_group)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `MPSES` | Minister/Ministerial advisor / Ministerial Staff / Parliamentary Secretary/Exempt Staff | Ministre / Conseiller ministériel / Personnel ministériel / Secrétaire parlementaire / Personnel exonéré |
| `SLE` | Senior officer or employees | Cadre supérieur ou employé |




---

#### `title_en` – Title (English) / Titre (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field will display, in English, the position title of the individual who incurred the hospitality expenses (the hospitality expenses were charged to their responsibility centre).  
FR: Cette zone indique, en anglais, le titre du poste de la personne qui a engagé les dépenses d’accueil (les dépenses d’accueil ont été imputées à leur centre de responsabilité).


---

#### `title_fr` – Title (French) / Titre (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field will display, in French, the position title of the individual who incurred the hospitality expenses (the hospitality expenses were charged to their responsibility centre).  
FR: Cette zone indique, en français, le titre du poste de la personne qui a engagé les dépenses d’accueil (les dépenses d’accueil ont été imputées à leur centre de responsabilité).


---

#### `name` – Name / Nom

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field will display the name of the individual who incurred the hospitality expenses (the hospitality expenses were charged to their responsibility centre).  
FR: Ce champ affiche le nom de la personne qui a engagé les dépenses d’accueil (les dépenses d’accueil ont été imputées à leur centre de responsabilité.


---

#### `description_en` – Purpose of hospitality activity (English) / But de l’activité d’accueil (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This will cover both the forms (for example, breakfast, refreshment, lunch, reception, dinner and other forms of hospitality) and circumstances (the purpose) of the hospitality, in English.  
FR: Cette zone comprend la forme d’accueil (par exemple, déjeuner, rafraîchissement, dîner, réception, souper, et autres formes d’accueil) et les circonstances (le but) de l’accueil, en anglais.


---

#### `description_fr` – Purpose of hospitality activity (French) / But de l’activité d’accueil (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This will cover both the forms (for example, breakfast, refreshment, lunch, reception, dinner and other forms of hospitality) and circumstances (the purpose) of the hospitality, in French.  
FR: Cette zone comprend la forme d’accueil (par exemple, déjeuner, rafraîchissement, dîner, réception, souper, et autres formes d’accueil) et les circonstances (le but) de l’accueil, en français.


---

#### `start_date` – Start Date / Date de début

**Type:** `date`  
**Required:** Yes  
**Validation:** This field must not be empty.
Date can’t be in the future.
 / Ce champ ne doit pas être vide.
La date ne doit pas être dans le futur.
  


**Description:**  
EN: The start date on which the hospitality was provided.  
FR: La date du début auxquelles les activités d’accueil ont eu lieu.


---

#### `end_date` – End Date / Date de fin

**Type:** `date`  
**Required:** Yes  
**Validation:** This field must not be empty.
Date can’t be in the future.
 / Ce champ ne doit pas être vide.
La date ne doit pas être dans le futur.
  


**Description:**  
EN: The end date on which the hospitality was provided. (can be the same as start date)  
FR: La date de fin auxquelles les activités d’accueil ont eu lieu. (peut être la même date du début)


---

#### `location_en` – Municipality where the hospitality activity took place (English) / Municipalité où l’activité d’accueil a eu lieu (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: Must include the Municipality where hospitality was provided, in English  
FR: Comprend la municipalité où les services d’accueil ont été fournis, en anglais


---

#### `location_fr` – Municipality where the hospitality activity took place (French) / Municipalité où l’activité d’accueil a eu lieu (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: Must include the Municipality where hospitality was provided, in French.  
FR: Comprend la municipalité où les services d’accueil ont été fournis, en français.


---

#### `vendor_en` – Name of the first commercial establishment or vendor involved in the hospitality activity (English) / Nom du premier établissement commercial ou fournisseur impliqué dans l’activité d’accueil (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: Must include the name of the first commercial establishment or vendor that provided the hospitality (for example, restaurant, hotel or other location) and/or vendor (for example, a caterer), in English.
  
FR: Doit inclure le nom du premier établissement commercial ou fournisseur qui a fourni l’accueil (par exemple, restaurant, hôtel ou autre lieu) et/ou du fournisseur (par exemple, un traiteur), en anglais.



---

#### `vendor_fr` – Name of the first commercial establishment or vendor involved in the hospitality activity (French) / Nom du premier établissement commercial ou fournisseur impliqué dans l’activité d’accueil (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: Must include the name of the first commercial establishment or vendor that provided the hospitality (for example, restaurant, hotel or other location) and/or vendor (for example, a caterer), in French.
  
FR: Doit inclure le nom du premier établissement commercial ou fournisseur qui a fourni l’accueil (par exemple, restaurant, hôtel ou autre lieu) et/ou du fournisseur (par exemple, un traiteur), en français.



---

#### `vendor_2_en` – Name of the second commercial establishment or vendor involved in the hospitality activity (English) / Nom du deuxième établissement commercial ou fournisseur impliqué dans l’activité d’accueil (anglais)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: Must include the name of the second commercial establishment or vendor that provided the hospitality (for example, restaurant, hotel or other location) and/or vendor (for example, a caterer), in English.
  
FR: Doit inclure le nom du deuxième établissement commercial ou fournisseur qui a fourni l’accueil (par exemple, restaurant, hôtel ou autre lieu) et/ou du fournisseur (par exemple, un traiteur), en anglais.



---

#### `vendor_2_fr` – Name of the second commercial establishment or vendor involved in the hospitality activity (French) / Nom du deuxième établissement commercial ou fournisseur impliqué dans l’activité d’accueil (français)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: Must include the name of the second commercial establishment or vendor that provided the hospitality (for example, restaurant, hotel or other location) and/or vendor (for example, a caterer), in French.
  
FR: Doit inclure le nom du deuxième établissement commercial ou fournisseur qui a fourni l’accueil (par exemple, restaurant, hôtel ou autre lieu) et/ou du fournisseur (par exemple, un traiteur), en français.



---

#### `vendor_other_en` – Name of any other commercial establishments or vendors involved in the hospitality activity (English) / Nom de tout autre établissement commercial ou fournisseur impliqué dans l’activité d’accueil (anglais)

**Type:** `text`  
**Required:** No  
**Validation:** Must be in the format of <Vendor Name>;<Vendor 2 Name> / Doit être au format <nom du fournisseur>;<nom du fournisseur 2>  


**Description:**  
EN: Must include the names of any other commercial establishments or vendors that provided the hospitality (for example, restaurant, hotel or other location) and/or vendor (for example, a caterer), in English. Note, use the format {Vendor Name};{Vendor 2 Name} (e.g. Les Impertinentes;Les Street Monkeys)
  
FR: Doit inclure le nom de tout autre établissement commercial ou fournisseur ayant fourni l’accueil (par exemple, restaurant, hôtel ou autre lieu) et/ou du fournisseur (par exemple, un traiteur), en anglais. Remarque : Utilisez le format <nom du fournisseur>;<nom du fournisseur 2> (par exemple : Les Impertinentes;Les Street Monkeys)



---

#### `vendor_other_fr` – Name of any other commercial establishments or vendors involved in the hospitality activity (French) / Nom de tout autre établissement commercial ou fournisseur impliqué dans l’activité d’accueil (français)

**Type:** `text`  
**Required:** No  
**Validation:** Must be in the format of <Vendor Name>;<Vendor 2 Name> / Doit être au format <nom du fournisseur>;<nom du fournisseur 2>  


**Description:**  
EN: Must include the name of any other commercial establishments or vendors that provided the hospitality (for example, restaurant, hotel or other location) and/or vendor (for example, a caterer), in French. Note, use the format <Vendor Name>;<Vendor 2 Name> (e.g. Les Impertinentes;Les Street Monkeys)
  
FR: Doit inclure le nom de tout autre établissement commercial ou fournisseur ayant fourni l’accueil (par exemple, restaurant, hôtel ou autre lieu) et/ou du fournisseur (par exemple, un traiteur), en français. Remarque : Utilisez le format {nom du fournisseur};{nom du fournisseur 2} (par exemple : Les Impertinentes;Les Street Monkeys)'



---

#### `employee_attendees` – Attendees (Government of Canada Officials) / Participants (Nombre de représentants du gouvernement du Canada)

**Type:** `int`  
**Required:** Yes  
**Validation:** This field must not be empty.
Zero is an invalid entry.
 / Ce champ ne doit pas être vide.
Zéro est une entrée invalide.
  


**Description:**  
EN: The total number of attendees (Government of Canada Officials). For any clarification regarding Government of Canada Officials, please refer to Table 2 of the Guide to the Proactive Publication of Travel and Hospitality Expenses- Canada.ca (https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32660).
  
FR: Nombre total de participants (représentants du gouvernement du Canada). Pour toute clarification concernant les représentants du gouvernement du Canada, veuillez référer au table 2 du Guide de publication proactive des frais de voyage et d’accueil- Canada.ca (https://www.tbs-sct.canada.ca/pol/doc-fra.aspx?id=32660).



---

#### `guest_attendees` – Attendees (Guests) / Participants (Nombre d’invités)

**Type:** `int`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: The total number of attendees (Guests)  
FR: Nombre total de participants (invités)


---

#### `total` – Total cost / Total des coûts

**Type:** `money`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: Total Amount of the expenses for the hospitality activity  
FR: Montant total des dépenses pour l’activité d’accueil


---

#### `additional_comments_en` – Additional comments (English) / Commentaires additionnels (anglais)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: This field may be populated with additional explanatory comments, in English.  
FR: Ce champ peut indiquer des commentaires explicatifs additionnels, en anglais.


---

#### `additional_comments_fr` – Additional comments (French) / Commentaires additionnels (français)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: This field may be populated with additional explanatory comments, in French.  
FR: Ce champ peut indiquer des commentaires explicatifs additionnels, en français.


---



## Proactive Publication - Hospitality Nothing to Report / Publication proactive - Dépenses d'accueil (Rien à signaler) 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `year` | Year / Année | `year` | Yes |  |  | This tab / field in the template is only populated if there are no hospitality … |
| `month` | Month / mois | `text` | Yes |  | month | This tab / field in the template is only populated if there are no hospitality … |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `year` – Year / Année

**Type:** `year`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This tab / field in the template is only populated if there are no hospitality expenses for the reporting period. This field should be populated with the year of the reporting period.  
FR: Cet onglet/champ du modèle n’est rempli que s'il n'y a pas de frais d'accueil pour la période d’établissement de rapports. Ce champ doit être rempli avec l’année de la période d’établissement de rapports.


---

#### `month` – Month / mois

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  
**Choice Set:** month (12 values)  


**Description:**  
EN: This tab / field in the template is only populated if there are no hospitality expenses for the reporting period. This field should be populated with the month of the reporting period.  
FR: Cet onglet/champ du modèle n’est rempli que s'il n'y a pas de frais d'accueil pour la période d’établissement de rapports. Ce champ doit être rempli avec le mois de la période d’établissement de rapports.


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

- Generated: 2025-10-08T20:10:33 (UTC)
- Source: dictionaries/hospitalityq.json
- Commit: `6af3f8d`
- Tool Version: simple-1

### Validation

- JSON Schema Validation: **PASSED**


### Notes

This documentation is auto-generated. Do not hand-edit; instead update the source recombinant JSON and re-run generation.