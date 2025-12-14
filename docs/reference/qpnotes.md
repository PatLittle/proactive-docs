
# Proactive Publication - Question Period Notes / Publication proactive - Notes pour la période des questions

**Dataset Type:** `qpnotes`  
**Last Generated:** 2025-12-14T01:45:09 (UTC)  
**Source:** dictionaries/qpnotes.json  
**Commit:** `ddfad99`

Access, upload and modify Question Period notes for your organization / Accès, téléversement et modifications des notes de la période de questions pour votre organisation

---

## Resources


- [Proactive Publication - Question Period Notes / Publication proactive - Notes pour la période des questions](#qpnotes)

- [Proactive Publication - Question Period Notes Nothing to Report / Publication proactive - Notes pour la période des questions rien à signaler](#qpnotes-nil)


---


## Proactive Publication - Question Period Notes / Publication proactive - Notes pour la période des questions 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `reference_number` | Reference Number / Numéro de référence | `text` | Yes |  |  | This field is populated by the user with the reference number of the Question P… |
| `title_en` | Title (English) / Titre (anglais) | `text` | Yes |  |  | This field is populated by the user with the official title of the Question Per… |
| `title_fr` | Title (French) / Titre (français) | `text` | Yes |  |  | This field is populated by the user with the official title of the Question Per… |
| `minister` | Title of Minister / Titre du ministre | `text` | Yes |  | minister | This field will display the title of the Minister for whom the Question Period … |
| `question_en` | Issue/Question (English) / Enjeu ou question (anglais) | `text` | No |  |  | This section will display the issue or question the Minister is responding to, … |
| `question_fr` | Issue/Question (French) / Enjeu ou question (français) | `text` | No |  |  | This section will display the issue or question the Minister is responding to, … |
| `date_received` | Date Provided to the Minister&#39;s Office / Date de fourniture au bureau du minister | `date` | Yes |  |  | This field will display the date on which the Question Period Note was provided… |
| `response_en` | Suggested Response (English) / Réponse suggérée (anglais) | `text` | Yes |  |  | This field will display the Suggested Response section of the Question Period N… |
| `response_fr` | Suggested Response (French) / Réponse suggérée (français) | `text` | Yes |  |  | This field will display the Suggested Response section of the Question Period N… |
| `background_en` | Background (English) / Contexte (anglais) | `text` | Yes |  |  | This field should display the background section of the Question Period note, I… |
| `background_fr` | Background (French) / Contexte (français) | `text` | Yes |  |  | This field should display the background section of the Question Period note, I… |
| `additional_information_en` | Additional Information (English) / Renseignements supplémentaires (anglais) | `text` | No |  |  | This field will display any additional information, as deemed necessary, in English. |
| `additional_information_fr` | Additional Information (French) / Renseignements supplémentaires (français) | `text` | No |  |  | This field will display any additional information, as deemed necessary, in French. |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `reference_number` – Reference Number / Numéro de référence

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field is populated by the user with the reference number of the Question Period Note. This number is a mandatory system requirement when publishing a template.  
FR: Ce champ est rempli par l’utilisateur avec le numéro de référence de la note pour la période de questions. Le numéro est une exigence de système obligatoire pour la publication d’un modèle.


---

#### `title_en` – Title (English) / Titre (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field is populated by the user with the official title of the Question Period Note, in English.  
FR: L’utilisateur indique le titre officiel en anglais de la note pour la période de questions dans ce champ.


---

#### `title_fr` – Title (French) / Titre (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field is populated by the user with the official title of the Question Period Note, in French.  
FR: L’utilisateur indique le titre officiel en français de la note pour la période de questions dans ce champ.


---

#### `minister` – Title of Minister / Titre du ministre

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  
**Choice Set:** minister (111 values)  


**Description:**  
EN: This field will display the title of the Minister for whom the Question Period Note was created.  
FR: Ce champ affichera le titre du ministre pour qui la note pour la période de questions a été créée.


##### Allowed Values (minister)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `AGC` | Attorney General of Canada | Procureur général du Canada |
| `AMF` | Associate Minister of Finance | Ministre associée des Finances |
| `AMH` | Associate Minister of Health | Ministre associée de la santé |
| `AMND` | Associate Minister of National Defence | Ministre associé de la Défense nationale |
| `AMPS` | Associate Minister of Public Safety | Ministre associée de la sécurité publique |
| `CGW` | Chief government whip | Whip en chef du gouvernement |
| `DPM` | Deputy Prime Minister | Vice-première ministre |
| `LGHC` | Leader of the Government in the House of Commons | Leader du gouvernement à la Chambre des communes |
| `MAA` | Minister of Agriculture and Agri-Food | Ministre de l&#39;Agriculture et de l&#39;Agroalimentaire |
| `MAARED` | Minister of Agriculture and Agri-Food and Rural Economic Development | Ministre de l’agriculture et de l’agroalimentaire et du développement économique rural |
| `MAIDI` | Minister of Artificial Intelligence and Digital Innovation | Ministre de l’intelligence artificielle et de l’innovation numérique |
| `MCCIPC` | Minister of Canadian Culture and Identity, Parks Canada | Ministre de la culture et de l’identité canadiennes, parcs canada |
| `MCH` | Minister of Canadian Heritage | Ministre du Patrimoine canadien |
| `MCIC` | Minister of Canadian Identity and Culture | Ministre de l’identité et de la culture canadiennes |
| `MCR` | Minister of Crown-Indigenous Relations | Ministre des Relations Couronne-Autochtones |
| `MCRNA` | Minister of Crown-Indigenous Relations and Northern Affairs | Ministre des relations couronne-autochtones et des affaires du nord |
| `MCS` | Minister of Citizens’ Services | Ministre des services aux citoyens |
| `MDG` | Minister of Digital Government | Ministre du Gouvernement numérique |
| `MDI` | Minister of Democratic Institutions | Ministre des institutions démocratiques |
| `MDIPD` | Minister of Diversity, Inclusion and Persons with Disabilities | Ministre de la diversité, de l’inclusion et des personnes en situation de handicap |
| `MDIY` | Minister of Diversity and Inclusion and Youth | Ministre de la Diversité et de l’Inclusion et de la Jeunesse |
| `MECC` | Minister of Environment and Climate Change | Ministre de l&#39;Environnement et du Changement climatique |
| `MED` | Minister of Economic Development | Ministre du Développement économique |
| `MEMCR` | Minister of Emergency Management and Community Resilience | Ministre de la gestion des urgences et de la résilience des communautés |
| `MENR` | Minister of Energy and Natural Resources | Ministre de l’énergie et des ressources naturelles |
| `MEP` | Minister of Emergency Preparedness | Ministre de la protection civile |
| `MEPITED` | Minister of Export Promotion, International Trade and Economic Development | Ministre de la promotion des exportations, du commerce international et du développement économique |
| `MEWDDI` | Minister of Employment, Workforce Development and Disability Inclusion | Ministre de l’Emploi, du Développement de la main-d’œuvre et de l&#39;Inclusion des personnes handicapées |
| `MEWDL` | Minister of Employment, Workforce Development and Labour | Ministre de l’emploi, du développement de la main-d’œuvre et du travail |
| `MEWDOL` | Minister of Employment, Workforce Development and Official Languages | Ministre de l’emploi, du développement de la main-d’œuvre et des langues officielles |
| `MF` | Minister of Finance | Ministre des Finances |
| `MF1` | Minister of Fisheries | Ministre des pêches |
| `MFA` | Minister of Foreign Affairs | Ministre des Affaires étrangères |
| `MFAID` | Minister of Foreign Affairs and International Development | Ministre des affaires étrangères et du développement international |
| `MFCSD` | Minister of Families, Children and Social Development | Ministre de la Famille, des Enfants et du Développement social |
| `MFNR` | Minister of Finance and National Revenue | Ministre des finances et du revenu national |
| `MFOCCG` | Minister of Fisheries, Oceans and the Canadian Coast Guard | Ministre des Pêches, des Océans et de la Garde côtière canadienne |
| `MGTPSP` | Minister of Government Transformation, Public Services and Procurement | Ministre de la transformation du gouvernement, des services publics et de l’approvisionnement |
| `MGTPWP` | Minister of Government Transformation, Public Works and Procurement | Ministre de la transformation du gouvernement, des travaux publics et de l’approvisionnement |
| `MH` | Minister of Health | Ministre de la Santé |
| `MHDI` | Minister of Housing and Diversity and Inclusion | Ministre du logement et de la diversité et de l’inclusion |
| `MHI` | Minister of Housing and Infrastructure | Ministre du logement et de l’infrastructure |
| `MHIC` | Minister of Housing, Infrastructure and Communities | Ministre du logement, de l’infrastructure et des collectivités |
| `MI` | Minister of Industry | Ministre de l’industrie |
| `MIA` | Minister of Intergovernmental Affairs | Ministre des Affaires intergouvernementales |
| `MIAIC` | Minister of Intergovernmental Affairs, Infrastructure and Communities | Ministre des affaires intergouvernementales, de l’infrastructure et des collectivités |
| `MIC` | Minister of Infrastructure and Communities | Ministre de l&#39;Infrastructure et des Collectivités |
| `MID` | Minister of International Development | Ministre du Développement international |
| `MIRC` | Minister of Immigration, Refugees and Citizenship | Ministre de l’Immigration, des Réfugiés et de la Citoyenneté |
| `MIS` | Minister of Indigenous Services | Ministre des Services aux Autochtones |
| `MISI` | Minister of Innovation, Science and Industry | Ministre de l&#39;Innovation, des Sciences et de l&#39;Industrie |
| `MIT` | Minister of International Trade | Ministre du Commerce international |
| `MITEPSBED` | Minister of International Trade, Export Promotion, Small Business and Economic Development | Ministre du commerce international, de la promotion des exportations, de la petite entreprise et du développement économique |
| `MITIA` | Minister of International Trade and Intergovernmental Affairs | Ministre du commerce international et des affaires intergouvernementales |
| `MJ` | Minister of Justice | Ministre de la Justice |
| `MJF` | Minister of Jobs and Families | Ministre de l’emploi et des familles |
| `ML` | Minister of Labour | Ministre du Travail |
| `MLS` | Minister of Labour and Seniors | Ministre du travail et des aînés |
| `MMCP` | Minister of Middle Class Prosperity | Ministre de la Prospérité de la classe moyenne |
| `MMHA` | Minister of Mental Health and Addictions | Ministre de la santé mentale et des dépendances |
| `MNA` | Minister of Northern Affairs | Ministre des Affaires du Nord |
| `MNAA` | Minister of Northern and Arctic Affairs | Ministre des affaires du nord et de l’arctique |
| `MND` | Minister of National Defence | Ministre de la Défense nationale |
| `MNR` | Minister of National Revenue | Ministre du Revenu national |
| `MNR1` | Minister of Natural Resources | Ministre des Ressources naturelles |
| `MOL` | Minister of Official Languages | Ministre des Langues officielles |
| `MPS` | Minister of Public Safety | Ministre de la sécurité publique |
| `MPSDIIA` | Minister of Public Safety, Democratic Institutions and Intergovernmental Affairs | Ministre de la sécurité publique, des institutions démocratiques et des affaires intergouvernementales |
| `MPSEP` | Minister of Public Safety and Emergency Preparedness | Ministre de la Sécurité publique et de la Protection civile |
| `MPSP` | Minister of Public Services and Procurement | Ministre des Services publics et de l’Approvisionnement |
| `MRACOA` | Minister responsible for the Atlantic Canada Opportunities Agency | Ministre responsable de l’agence de promotion économique du canada atlantique |
| `MRCEDQR` | Minister responsible for Canada Economic Development for Quebec Regions | Ministre responsable de développement économique canada pour les régions du québec |
| `MRCNEDA` | Minister responsible for the Canadian Northern Economic Development Agency | Ministre responsable de l’agence canadienne de développement économique du nord |
| `MRCRA` | Minister responsible for the Canada Revenue Agency | Ministre responsable de l’agence du revenu du canada |
| `MRCTIAOCE` | Minister responsible for Canada-U.S. Trade, Intergovernmental Affairs and One Canadian Economy | Ministre responsable du commerce canada–états-unis, des affaires intergouvernementales et de l’unité de l’économie canadienne |
| `MRED` | Minister of Rural Economic Development | Ministre du Développement économique rural |
| `MREDACRQ` | Minister responsible for the Economic Development Agency of Canada for the Regions of Quebec | Ministre responsable de l’agence de développement économique du canada pour les régions du québec |
| `MRFEDANO` | Minister responsible for the Federal Economic Development Agency for Northern Ontario | Ministre responsable de l’agence fédérale de développement économique pour le nord de l’ontario |
| `MRFEDASO` | Minister responsible for the Federal Economic Development Agency for Southern Ontario | Ministre responsable de l’agence fédérale de développement économique pour le sud de l’ontario |
| `MROL` | Minister responsible for Official Languages | Ministre responsable des langues officielles |
| `MRPEDAC` | Minister responsible for the Pacific Economic Development Agency of Canada | Ministre responsable de l’agence de développement économique du pacifique canada |
| `MRPEDC` | Minister responsible for Prairies Economic Development Canada | Ministre responsable de développement économique canada pour les prairies |
| `MRPEDC1` | Minister responsible for Pacific Economic Development Canada | Ministre responsable de développement économique canada pour le pacifique |
| `MS` | Minister of Seniors | Ministre des Aînés |
| `MS1` | Minister of Sport | Ministre des sports |
| `MSB` | Minister of Small Business | Ministre de la petite entreprise |
| `MSBEP` | Minister of Small Business and Export Promotion | Ministre de la Petite Entreprise et de la Promotion des exportations |
| `MSPA` | Minister of Sport and Physical Activity | Ministre des sports et de l’activité physique |
| `MT` | Minister of Transport | Ministre des Transports |
| `MT1` | Minister of Tourism | Ministre du tourisme |
| `MTIT` | Minister of Transport and Internal Trade | Ministre des transports et du commerce intérieur |
| `MVA` | Minister of Veterans Affairs | Ministre des Anciens Combattants |
| `MWGE` | Minister for Women and Gender Equality | Ministre des Femmes et de l’Égalité des genres |
| `MWGE1` | Minister of Women and Gender Equality | Ministre des femmes et de l’égalité des genres |
| `MWGEY` | Minister for Women and Gender Equality and Youth | Ministre des femmes et de l’égalité des genres et de la jeunesse |
| `PKPCC` | President of the King’s Privy Council for Canada | Président du conseil privé du roi pour le canada |
| `PM` | Prime Minister | Premier ministre |
| `PQPCC` | President of the Queen’s Privy Council for Canada | Président du Conseil privé de la Reine pour le Canada |
| `PTB` | President of the Treasury Board | Président du Conseil du Trésor |
| `SRP` | Special Representative for the Prairies | Représentant spécial pour les Prairies |
| `SSCC` | Secretary of State (Combatting Crime) | Secrétaire d’état (lutte contre la criminalité) |
| `SSCRAFI` | Secretary of State (Canada Revenue Agency and Financial Institutions) | Secrétaire d’état (agence du revenu du canada et institutions financières) |
| `SSCY` | Secretary of State (Children and Youth) | Secrétaire d’état (enfance et jeunesse) |
| `SSDP` | Secretary of State (Defence Procurement) | Secrétaire d’état (approvisionnement en matière de défense) |
| `SSID` | Secretary of State (International Development) | Secrétaire d’état (développement international) |
| `SSL` | Secretary of State (Labour) | Secrétaire d’état (travail) |
| `SSN` | Secretary of State (Nature) | Secrétaire d’état (nature) |
| `SSRD` | Secretary of State (Rural Development) | Secrétaire d’état (développement rural) |
| `SSS` | Secretary of State (Seniors) | Secrétaire d’état (aînés) |
| `SSS1` | Secretary of State (Sport) | Secrétaire d’état (sports) |
| `SSSBT` | Secretary of State (Small Business and Tourism) | Secrétaire d’état (petites entreprises et tourisme) |




---

#### `question_en` – Issue/Question (English) / Enjeu ou question (anglais)

**Type:** `text`  
**Required:** No  
**Validation:** None / None  


**Description:**  
EN: This section will display the issue or question the Minister is responding to, in English.  
FR: Cette section affichera en anglais la question ou l’enjeu auquel répond le ministère.


---

#### `question_fr` – Issue/Question (French) / Enjeu ou question (français)

**Type:** `text`  
**Required:** No  
**Validation:** None / None  


**Description:**  
EN: This section will display the issue or question the Minister is responding to, in French.  
FR: Cette section affichera en français la question ou l’enjeu auquel répond le ministère.


---

#### `date_received` – Date Provided to the Minister's Office / Date de fourniture au bureau du minister

**Type:** `date`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field will display the date on which the Question Period Note was provided to the Minister's Office.  
FR: Ce champ affichera la date à laquelle la note pour la période de questions a été fournie au ministre aux fins d’utilisation au cours d’une période de questions.


---

#### `response_en` – Suggested Response (English) / Réponse suggérée (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field will display the Suggested Response section of the Question Period Note, in English.  
FR: Ce champ affichera la section de la réponse suggérée de la note pour la période de questions en anglais.


---

#### `response_fr` – Suggested Response (French) / Réponse suggérée (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field will display the Suggested Response section of the Question Period Note, in French.  
FR: Ce champ affichera la section de la réponse suggérée de la note pour la période de questions en français.


---

#### `background_en` – Background (English) / Contexte (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field should display the background section of the Question Period note, In English.  
FR: Ce champ devrait afficher en anglais la section du contexte de la note pour la période de questions.


---

#### `background_fr` – Background (French) / Contexte (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field should display the background section of the Question Period note, In French.  
FR: Ce champ devrait afficher en français la section du contexte de la note pour la période de questions.


---

#### `additional_information_en` – Additional Information (English) / Renseignements supplémentaires (anglais)

**Type:** `text`  
**Required:** No  
**Validation:** None / None  


**Description:**  
EN: This field will display any additional information, as deemed necessary, in English.  
FR: Ce champ affichera tout renseignement supplémentaire, en anglais, selon les besoins.


---

#### `additional_information_fr` – Additional Information (French) / Renseignements supplémentaires (français)

**Type:** `text`  
**Required:** No  
**Validation:** None / None  


**Description:**  
EN: This field will display any additional information, as deemed necessary, in French.  
FR: Ce champ affichera tout renseignement supplémentaire, en français, selon les besoins.


---



## Proactive Publication - Question Period Notes Nothing to Report / Publication proactive - Notes pour la période des questions rien à signaler 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `year` | Year / Année | `year` | Yes |  |  | This tab / field in the template is only populated if there are no question per… |
| `reporting_period` | Reporting Period / Période de déclaration | `text` | Yes |  | reporting_period | This tab / field in the template is only populated if there are no briefing not… |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `year` – Year / Année

**Type:** `year`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This tab / field in the template is only populated if there are no question period notes for the reporting period. This field should be populated with the year of the reporting period.  
FR: Cet onglet/champ du modèle n’est rempli que s'il n'y a pas de notes pour la période de questions pour la période d’établissement de rapports. Ce champ doit être rempli avec l’année de la période d’établissement de rapports.


---

#### `reporting_period` – Reporting Period / Période de déclaration

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  
**Choice Set:** reporting_period (2 values)  


**Description:**  
EN: This tab / field in the template is only populated if there are no briefing notes for the reporting period. This field should be populated with the reporting period.  
FR: Cet onglet/champ du modèle n’est rempli que s'il n'y a pas de note pour la période de questions pour la période d’établissement de rapports. Ce champ doit être rempli avec la période d’établissement de rapports.


##### Allowed Values (reporting_period)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `P01` | Jan. - June | jan. - juin |
| `P02` | July - Dec. | juil. - déc. |




---




## Appendix

### Choice Sets Summary (All Resources)
| Choice Set | Field(s) | Values | Standalone Doc |
|------------|----------|--------|----------------|


### Generation Metadata

- Generated: 2025-12-14T01:45:09 (UTC)
- Source: dictionaries/qpnotes.json
- Commit: `ddfad99`
- Tool Version: simple-1

### Validation

- JSON Schema Validation: **PASSED**


### Notes

This documentation is auto-generated. Do not hand-edit; instead update the source recombinant JSON and re-run generation.