
# Proactive Publication - Use of Administrative Aircraft / Publication proactive - Utilisation des avions d'affaires

**Dataset Type:** `adminaircraft`  
**Last Generated:** 2025-11-02T01:36:56 (UTC)  
**Source:** dictionaries/adminaircraft.json  
**Commit:** `fadc35e`

Access, upload and modify government administrative aircraft use / Accès, téléversement et modifications des rapports sur la utilisation des avions d'affaires

---

## Resources


- [Proactive Publication - Use of Administrative Aircraft / Publication proactive - Utilisation des avions d'affaires](#adminaircraft)


---


## Proactive Publication - Use of Administrative Aircraft / Publication proactive - Utilisation des avions d'affaires 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `reference_number` | Reference Number / Numéro de référence | `text` | Yes |  |  | This field is populated by the user with the reference number of the trip. This… |
| `minister` | Title of Minister / Titre du ministre | `text` | Yes |  | minister | This field will display the title of the Minister who requested the trip. |
| `purpose_en` | Purpose of the trip (English) / But du voyage (anglais) | `text` | Yes |  |  | A description of the reason for the government trip in question. The descriptio… |
| `purpose_fr` | Purpose of the trip (French) / But du voyage (français) | `text` | Yes |  |  | A description, in French, of the reason for the government trip in question. Th… |
| `start_date` | Travel start date / Date du début du voyage | `date` | Yes |  |  | The date the travel started. |
| `end_date` | Travel end date / Date de fin du voyage | `date` | Yes |  |  | The date the travel ended (can be the same as travel start date). |
| `locations_en` | Location(s) visited (English) / Endroit(s) visité (anglais) | `text` | Yes |  |  | To include names of all places visited to conduct government business during th… |
| `locations_fr` | Location(s) visited (French) / Endroit(s) visité (français) | `text` | Yes |  |  | To include names of all places visited to conduct government business during th… |
| `hours` | Number of hours flown / Le nombre d’heures de vol | `numeric` | Yes |  |  | The number of hours flown. |
| `passengers` | Passenger names / Nom des passagers | `text` | Yes |  |  | Full list of flight passengers. (Comma seperated) |
| `additional_information_en` | Additional Information (English) / Renseignements supplémentaires (anglais) | `text` | No |  |  | This field will display any additional information, as deemed necessary, in English. |
| `additional_information_fr` | Additional Information (French) / Renseignements supplémentaires (français) | `text` | No |  |  | This field will display any additional information, as deemed necessary, in French. |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `reference_number` – Reference Number / Numéro de référence

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field is populated by the user with the reference number of the trip. This number is a mandatory system requirement when publishing a template.  
FR: Ce champ est rempli par l’utilisateur avec le numéro de référence du voyage. Le numéro est une exigence de système obligatoire pour la publication d’un modèle.


---

#### `minister` – Title of Minister / Titre du ministre

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  
**Choice Set:** minister (112 values)  


**Description:**  
EN: This field will display the title of the Minister who requested the trip.  
FR: Ce champ affichera le titre du ministre qui a demandé le voyage.


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
| `GG` | The Governor General of Canada | La gouverneure générale du Canada |
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

#### `purpose_en` – Purpose of the trip (English) / But du voyage (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: A description of the reason for the government trip in question. The description should be succinct (one line if possible) and provide users with a general sense of the trip's purpose. Use of acronyms should be avoided, in English.  
FR: Description de la raison du voyage, en anglais, en service commandé visé. La description doit être brève (une ligne dans la mesure du possible) et donner une indication générale aux utilisateurs du but du voyage. Il faut éviter d’utiliser des acronymes.


---

#### `purpose_fr` – Purpose of the trip (French) / But du voyage (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: A description, in French, of the reason for the government trip in question. The description should be succinct (one line if possible) and provide users with a general sense of the trip's purpose. Use of acronyms should be avoided, in French  
FR: Description de la raison du voyage, en français, en service commandé visé. La description doit être brève (une ligne dans la mesure du possible) et donner une indication générale aux utilisateurs du but du voyage. Il faut éviter d’utiliser des acronymes.


---

#### `start_date` – Travel start date / Date du début du voyage

**Type:** `date`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: The date the travel started.  
FR: Date du début du voyage.


---

#### `end_date` – Travel end date / Date de fin du voyage

**Type:** `date`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: The date the travel ended (can be the same as travel start date).  
FR: Date de fin du voyage (peut être la même date que la date du début du voyage).


---

#### `locations_en` – Location(s) visited (English) / Endroit(s) visité (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: To include names of all places visited to conduct government business during the trip in question, in English. (separate multiple locations with semicolons)  
FR: Cette zone indique, en anglais, le nom de tous les lieux qui ont été visités dans le cadre du voyage en question réalisé pour le compte du gouvernement. (séparer plusieurs emplacements avec des points-virgules)


---

#### `locations_fr` – Location(s) visited (French) / Endroit(s) visité (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: To include names of all places visited to conduct government business during the trip in question, in french. (separate multiple locations with semicolons)  
FR: Cette zone indique, en français, le nom de tous les lieux qui ont été visités dans le cadre du voyage en question réalisé pour le compte du gouvernement. (séparer plusieurs emplacements avec des points-virgules)


---

#### `hours` – Number of hours flown / Le nombre d’heures de vol

**Type:** `numeric`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: The number of hours flown.  
FR: Le nombre d’heures de vol.


---

#### `passengers` – Passenger names / Nom des passagers

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: Full list of flight passengers. (Comma seperated)  
FR: Liste complète des passagers du vol. (séparées par des virgules)


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




## Appendix

### Choice Sets Summary (All Resources)
| Choice Set | Field(s) | Values | Standalone Doc |
|------------|----------|--------|----------------|


### Generation Metadata

- Generated: 2025-11-02T01:36:56 (UTC)
- Source: dictionaries/adminaircraft.json
- Commit: `fadc35e`
- Tool Version: simple-1

### Validation

- JSON Schema Validation: **PASSED**


### Notes

This documentation is auto-generated. Do not hand-edit; instead update the source recombinant JSON and re-run generation.