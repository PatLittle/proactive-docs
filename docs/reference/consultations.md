
# Open Dialogue - Consultations / Dialogue ouvert - Consultations

**Dataset Type:** `consultations`  
**Last Generated:** 2025-09-14T01:24:41 (UTC)  
**Source:** dictionaries/consultations.json  
**Commit:** `322574e`

Access, upload and modify consultation reports for your organization / Accès, téléversement et modifications des rapports sur les consultations pour votre organisation

---

## Resources


- [Open Dialogue - Consultations / Dialogue ouvert - Consultations](#consultations)


---


## Open Dialogue - Consultations / Dialogue ouvert - Consultations 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `registration_number` | Registration Number / Numéro d’enregistrement | `text` | Yes |  |  | This field is populated by the user. It is a unique reference number given to e… |
| `partner_departments` | Partner Department(s) / Ministère(s) partenaire(s) | `_text` | No |  | partner_departments | This field identifies the name(s) of the departments who are collaborating on t… |
| `subjects` | Subjects / Sujets | `_text` | Yes |  | subjects | This field indicates the different subjects related to the engagement process. |
| `title_en` | Consultation Title (English) / Titre de la consultation (en anglais) | `text` | Yes |  |  | This field identifies the complete name of the consultation in English. |
| `title_fr` | Consultation Title (French) / Titre de la consultation (en français) | `text` | Yes |  |  | This field identifies the complete name of the consultation in French. |
| `description_en` | Description (English) / Description (en anglais) | `text` | Yes |  |  | This field provides information regarding the nature of consultation and engage… |
| `description_fr` | Description (French) / Description (en français) | `text` | Yes |  |  | This field provides information regarding the nature of consultation and engage… |
| `target_participants_and_audience` | Target Participants and Audience / Participants visés et public cible | `_text` | Yes |  | target_participants_and_audience | This field provides information regarding the target participants and audience … |
| `start_date` | Start Date / Date de début | `date` | Yes |  |  | This field indicates when a planned consultation will begin to accept input fro… |
| `end_date` | End Date / Date de fin | `date` | Yes |  |  | This field indicates the end date of the consultation. The consultation is cons… |
| `status` | Status / État | `text` | Yes |  | status | The field indicates the current status of the engagement process. |
| `profile_page_en` | Link to Consultations Profile Page (English) / Lien vers la page du profil des consultations (en anglais) | `text` | Yes |  |  | This field provides the link to the English engagement information profile page. |
| `profile_page_fr` | Link to Consultations Profile Page (French) / Lien vers la page du profil des consultations (en français) | `text` | Yes |  |  | This field provides the link to the French engagement information profile page. |
| `report_available_online` | Report Available online / Rapport disponible en ligne | `text` | Yes |  | report_available_online | This field indicates if the “What we Heard” report is completed, published and … |
| `report_link_en` | Link to the “What we Heard” Report in English / Lien – rapport « Ce que nous avons entendu » en anglais | `text` | No |  |  | This field provides the link to the “What we Heard” report when it is available… |
| `report_link_fr` | Link to the “What we Heard” Report in French / Lien – rapport « Ce que nous avons entendu » en français | `text` | No |  |  | This field provides the link to the “What we Heard” report when it is available… |
| `high_profile` | High Profile / Haute visibilité | `text` | Yes |  | high_profile | This field indicates whether the consultation or public engagement initiative i… |
| `rationale` | Rationale / Raison | `_text` | Yes |  | rationale | The field indicates the rationale that prompted the public engagement initiativ… |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `registration_number` – Registration Number / Numéro d’enregistrement

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field is populated by the user. It is a unique reference number given to each line item in the spreadsheet. Having a unique identifier for each item will allow users locate a specific item in the registry should they need to modify or delete. The Registration Number should respect the following format: C-XXXXXXX.  
FR: Cette zone doit être remplie par l’utilisateur. Il s’agit d’un numéro de référence unique donné à chaque article de la feuille de calcul. Les utilisateurs peuvent ainsi trouver, dans un registre donné, un article précis à modifier ou à supprimer. Le numéro d’enregistrement doit respecter le format suivant : C-XXXXXXX.


---

#### `partner_departments` – Partner Department(s) / Ministère(s) partenaire(s)

**Type:** `_text`  
**Required:** No  
**Validation:** None / None  
**Choice Set:** partner_departments (49 values)  


**Description:**  
EN: This field identifies the name(s) of the departments who are collaborating on the identified engagement process. Please provide the numerical code associated to each department and separated by commas.  
FR: Cette zone indique le ministère ou les ministères qui collaborent au processus de participation en question. Il faut indiquer le nom complet des ministères (aucun acronyme).


##### Allowed Values (partner_departments)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `D110` | Science and Engineering Research Canada (SERC) | Recherche en sciences et génie du Canada (RSGC) |
| `D115` | Natural Ressources Canada (NRCan) | Ressources naturelles Canada (NRCan) |
| `D119` | Department of Justice Canada (JUS) | Ministère de la Justice Canda (JUS) |
| `D131` | Royal Canadian Mounted Police (RCMP) | Gendarmerie Royale du Canada (GRC) |
| `D135` | Public Health Agency of Canada (PHAC) | Agence de la santé publique du Canada (ADPC) |
| `D139` | Treasury Board Secretariat (TBS) | Secrétariat du Conseil du Trésor (SCT) |
| `D141` | Employment and Social Development Canada (ESDC) | Emploi et Dévelopement social Canada (EDSC) |
| `D143` | Polar Knowledge Canada (POLAR) | Savoir polaire Canada (POLAIRE) |
| `D147` | Status of Women Canada (SWC) | Condition féminine Canada (CFC) |
| `D154` | Parks Canada (PC) | Parcs Canada (PC) |
| `D157` | Department of Finance Canada (FIN) | Ministère des finances Canada (FIN) |
| `D16` | Canadian Heritage (PCH) | Patrimoine canadien (PCH) |
| `D169` | Canadian Coast Guards (CCG) | Garde côtière canadienne  (GCC) |
| `D172` | National Research Council Canada (NRCC) | Conseil national de recherches du Canada (CNRC) |
| `D173` | Privy Council Office (PCO) | Bureau du Conseil privé (BCP) |
| `D189` | Veterans Affairs Canada (VAC) | Anciens Combattants Canada (ACC) |
| `D193` | Correctional Services Canada | Service correctionnel du Canada |
| `D202` | Canada Science and Technology Museum (CSTM) | Musée des sciences et de la technologie du Canada (MSTC) |
| `D206` | Canadian Food Inspection Agency (CFIA) | Agence canadienne d’inspection des aliments (ACIA) |
| `D207` | Social Sciences and Humanities Research Council of Canada (SSHRC) | Conseil de recherches en sciences humaines du Canada (CRSHC) |
| `D214` | Public Safety Canada (PS) | Sécurité publique Canada (PS) |
| `D215` | Transportation Safety Board of Canada (TSB) | Bureau de la sécurité des transports du Canada (BST) |
| `D217` | Transport Canada (TC) | Transport Canada (TC) |
| `D229` | Canada Border Services Agency (CBSA) | Agence des services frontaliers du Canada (ASFC) |
| `D230` | Innovation,Science amd Econmic Development Canada (ISEDC) | Innovation, Sciences et Développement économique Canada (ISDEC) |
| `D231` | Law Commission of Canada | Commission du droit du Canada |
| `D235` | Agriculture and Agri-Food Canada (AAFC) | Agriculture et Agroalimentaire Canada (AAC) |
| `D236` | Canadian Institutes of Health Research (CIHR) | Instituts de recherche en santé du Canada (IRSC) |
| `D239` | Canada Energy Regulator (CER) | La Régie de l’énergie du Canada (REC) |
| `D249` | Indigenous and Northern Affairs Canada (INAC) | Affaires autochtones et du Nord Canada (AANC) |
| `D253` | Fisheries and Oceans Canada (DFO) | Pêches et Océans Canada (MPO) |
| `D256` | Statistics Canada (STATCAN) | Statistiques Canada (STATCAN) |
| `D262` | The National Battlefields Commission (NBC) | Commission des champs bataille nationaux (CCBN) |
| `D270` | Impact Assessment Agency of Canada (IAAC) | Agence d&#39;évaluation d&#39;impact du Canada (AEIC) |
| `D271` | Health Canada (HC) | Santé Canada (SC) |
| `D278` | Infrastructure Canada (INFC) | Infrastructure Canada (INFC) |
| `D32` | National Defence (DND) | Défense nationale (MDN) |
| `D35` | Canadian Centre for Occupational Health and Safety (CCOHS) | Centre canadien d’hygiène et de sécurité au travail (CCHST) |
| `D47` | Canada Revenue Agency (CRA) | Agence du revenu du Canada (ARC) |
| `D55` | Western Economic Diversification Canada (WD) | Diversification de l’économie de l’Ouest Canada (DEO) |
| `D64` | Global Affairs Canada (GAC) | Affaires mondiales Canada (AMC) |
| `D73` | Canadian School of Public Service (CSPS) | École de la fonction publique du Canada (EFPC) |
| `D81` | Public Services and Procurement Canada (PSPC) | Services publiques et Approvisionnement Canada (SPAC) |
| `D87` | Canada Mortgage and Housing Corporation | Société canadienne d&#39;hypothèques et de logement |
| `D90` | Canadian Security Intelligence Service (CSIS) | Service canadien de renseignement de sécurité (SCRS) |
| `D92` | Shared Services Canada (SSC) | Services partagés Canada (SPC) |
| `D93` | Economic Development Agency of Canada for the Regions of Quebec (CED) | Agence de développement économique du Canada pour les régions du Québec (DEC) |
| `D94` | Immigration, Refugees and Citizenship Canada (IRCC) | Immigration, Réfugiés et Citoyenneté Canada (IRCC) |
| `D99` | Environment and Climate Change Canada (ECCC) | Environnement et Changement climatique Canada (ECCC) |




---

#### `subjects` – Subjects / Sujets

**Type:** `_text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  
**Choice Set:** subjects (54 values)  


**Description:**  
EN: This field indicates the different subjects related to the engagement process.  
FR: Cette zone indique les différents sujets sur lesquels porte le processus de participation.


##### Allowed Values (subjects)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `AA` | Arts | Arts |
| `AD` | Advertising / Marketing | Publicité et Marketing |
| `AG` | Agriculture | Agriculture |
| `AM` | Amendments | Modifications |
| `AN` | Animals | Animaux |
| `CD` | Children | Enfants |
| `CM` | Communication | Communication |
| `CR` | Copyright / Trademarks / Patents | Droit d’auteur/Marques de commerce/Brevets |
| `CU` | Culture | Culture |
| `DV` | Development | Développement |
| `EC` | Economy | Économie |
| `ED` | Economic development | Développement économique |
| `EM` | Employment | Emploi |
| `EN` | Environment | Environnement |
| `EU` | Education | Éducation |
| `EX` | Exporting / Importing | Exportation/Importation |
| `FA` | Financial assistance and entitlements | Aide financière et droits |
| `FD` | Food and drug | Aliments et drogues |
| `FI` | Finance | Finances |
| `FO` | Foreign affairs | Affaires étrangères |
| `FS` | Fisheries | Pêches |
| `GBA` | Gender Based Analysis | Analyse comparative entre les sexes |
| `GE` | Gender | Sexes |
| `GP` | Government procurement | Marché public |
| `HL` | Housing | Logement |
| `HP` | Heritage | Patrimoine |
| `HR` | Human resources | Ressources humaines |
| `HS` | Health | Santé |
| `IM` | Immigration | Immigration |
| `IN` | Industry | Industrie |
| `IP` | Indigenous Peoples | Peuples autochtones |
| `IT` | International | Internationaux |
| `JL` | Justice and the Law | Justice et Loi |
| `LT` | Labour | Travail |
| `ND` | National Defence | Défense nationale |
| `NR` | Natural resources | Ressources naturelles |
| `PD` | Persons with disabilities | Personnes handicapées |
| `PL` | Plants | Végétaux |
| `PO` | Policy | Politique |
| `PR` | Private sector | Secteur privé |
| `PS` | Public safety | Sécurité publique |
| `RE` | Regulations | Règlements |
| `RL` | Recreation | Loisirs |
| `RU` | Rural and remote services | Services aux régions rurales et isolées |
| `SA` | Seniors | Aînés |
| `SE` | Service | Service |
| `SO` | Society | Société |
| `SP` | Sport | Sport |
| `ST` | Science and technology | Sciences et technologie |
| `TC` | Trade | Commerce |
| `TF` | Training and careers | Formation et carrières |
| `TR` | Transportation | Transport |
| `TX` | Taxes | Impôts et taxes |
| `YJ` | Youth | Jeunes |




---

#### `title_en` – Consultation Title (English) / Titre de la consultation (en anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field identifies the complete name of the consultation in English.  
FR: Cette zone indique le titre, en anglais, de la consultation.


---

#### `title_fr` – Consultation Title (French) / Titre de la consultation (en français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field identifies the complete name of the consultation in French.  
FR: Cette zone indique le titre, en français, de la consultation.


---

#### `description_en` – Description (English) / Description (en anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field provides information regarding the nature of consultation and engagement activities in English. This includes a description of the main objectives and expected outcomes of the engagement process. Users are invited to explain how the engagement activities, methods and/or tools will help meet the consultation’s objectives.  
FR: Cette zone fournit de l’information, en anglais, sur la nature des activités de consultation et de participation. On y trouve notamment une description des principaux objectifs et des résultats attendus du processus de participation. On invite les utilisateurs à expliquer en quoi les activités, les méthodes et les outils permettront d’atteindre les objectifs de la consultation.


---

#### `description_fr` – Description (French) / Description (en français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field provides information regarding the nature of consultation and engagement activities in French. This includes a description of the main objectives and expected outcomes of the engagement process. Users are invited to explain how the engagement activities, methods and/or tools will help meet the consultation’s objectives.  
FR: Cette zone fournit de l’information, en français, sur la nature des activités de consultation et de participation. On y trouve notamment une description des principaux objectifs et des résultats attendus du processus de participation. On invite les utilisateurs à expliquer en quoi les activités, les méthodes et les outils permettront d’atteindre les objectifs de la consultation.


---

#### `target_participants_and_audience` – Target Participants and Audience / Participants visés et public cible

**Type:** `_text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  
**Choice Set:** target_participants_and_audience (76 values)  


**Description:**  
EN: This field provides information regarding the target participants and audience of the engagement process.  
FR: Cette zone précise les participants visés et le public cible du processus de participation.


##### Allowed Values (target_participants_and_audience)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `AA` | Arts and Culture Institutions | Institutions artistiques et culturelles |
| `AC` | Academics | Universitaires |
| `AD` | Advocacy | Groupes de défense des intérêts |
| `AG` | Agriculture Production | Production agricole |
| `BS` | Business and Industry Associations | Associations commerciales et industrielles |
| `CA` | Canadians Living Abroad | Canadiens vivant à l’étranger |
| `CC` | Canadians | Canadiens |
| `CH` | Charities | Organismes caritatifs |
| `CI` | Cultural Industries | Industries culturelles |
| `CO` | Consumers | Consommateurs |
| `CS` | Construction Companies | Entreprises de construction |
| `CU` | Colleges and Universities | Collèges et universités |
| `EI` | Mining, Quarrying, Oil and Gas Extraction Industry | Industrie des mines, des carrières et de l’extraction pétrolière et gazière |
| `ET` | Ethnic groups/minorities | Groupes/minorités ethniques |
| `FA` | Family and Community Services | Services à la famille et à la communauté |
| `FC` | Foreign Countries | Pays étrangers |
| `FI` | Financial and Insurance Institutions | Établissements financiers et compagnies d’assurance |
| `FM` | Food Manufacturers | Fabricants de produits alimentaires |
| `FN` | First Nations | Premières Nations |
| `FW` | Foreign Workers | Travailleurs étrangers |
| `GP` | General Public | Grand public |
| `HC` | Health Care Providers and Social Assistance Services | Fournisseurs de soins de santé et services d’assistance sociale |
| `IB` | Indigenous governing bodies | Organismes de gouvernance autochtones |
| `IG` | International Governments | Gouvernement internationale |
| `IM` | Immigrants | Immigrants |
| `IO` | Indigenous Organizations | Organisations autochtones |
| `IP` | Indigenous Peoples | Peuples autochtones |
| `IT` | IT and Security Industry | Industrie de la TI et de la sécurité |
| `IU` | Inuit | Inuit |
| `JM` | Journalists/Media | Journalistes/Médias |
| `LA` | Law Enforcement Bodies | Organismes d’application de la loi |
| `LF` | Low-income families | Familles à faible revenu |
| `LM` | Linguistic minorities | Minorités lingustiques |
| `LP` | Land and Property Owners | Propriétaires fonciers et immobiliers |
| `LU` | Labour Associations and Unions | Associations de travailleurs et syndicats |
| `MA` | Manufacturers | Fabricants |
| `MT` | Métis | Métis |
| `MU` | Municipalities | Municipalités |
| `NG` | NGOs and Not for Profit | ONG et organisations à but non lucratif |
| `NI` | International NGOs and Not-for-profit | ONG et organisations à but non lucratif internationales |
| `NR` | Natural Resources Industry | Industrie des ressources naturelles |
| `NT` | Northerners | Habitants du Nord |
| `NW` | Newcomers | Nouveaux arrivants |
| `OD` | Other Federal Departments and Agencies | Autres ministères et organismes fédéraux |
| `OI` | International Organizations | Organisations internationales |
| `PA` | Parliamentarians | Parlementaires |
| `PC` | Parents and Caregivers | Parents et proches aidants |
| `PD` | People with disabilities | Personnes ayant un handicap |
| `PP` | Patients | Patients |
| `PR` | Permanent Residents | Résidents permanents |
| `PS` | Public Servants | Fonctionnaires |
| `PT` | Provinces/Territories | Provinces/Territoires |
| `RC` | Researchers | Chercheurs |
| `RE` | Real Estate Companies | Sociétés immobilières |
| `RF` | Refugees | Réfugiés |
| `RG` | Regulatory Body | Organismes de réglementation |
| `RO` | Research Organizations | Organisations de recherche |
| `RP` | Regulatory and Professional Associations | Organismes de réglementation et associations profesionnelles |
| `RT` | Retail Trade Companies | Entreprises de commerce au détail |
| `RU` | Rural Residents | Résidents des régions rurales |
| `SE` | Seniors | Aînés |
| `SL` | Scientific Labs | Laboratoires scientifiques |
| `SM` | Small and Medium Businesses | Petites et moyennes entreprises |
| `SP` | Service Providers | Fournisseurs de services |
| `ST` | Students | Étudiants |
| `TO` | Transportation Organizations | Organisations de transport |
| `TR` | Treaty rights and self-government agreement holders | Détenteurs de droits issus des traités |
| `TT` | Think Tanks | Groupes de réflexion |
| `UI` | Urban Indigenous Peoples | Autochtones vivant en milieu urbain |
| `UP` | Unions and/or Professional Associations | Syndicats et / ou associations professionnelles |
| `UR` | Urban Residents | Populations urbaines |
| `VV` | Veterans | Vétérans et anciens combattants |
| `WF` | Women | Femmes |
| `WM` | Waste Management Services | Services de gestion des déchets |
| `WT` | Wholesale Trade Organizations | Organisations de commerce de gros |
| `YJ` | Youth | Jeunes |




---

#### `start_date` – Start Date / Date de début

**Type:** `date`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field indicates when a planned consultation will begin to accept input from participants.  
FR: Ce champ indique quand une séance de planification prévue commencera à accepter les commentaires des participants.


---

#### `end_date` – End Date / Date de fin

**Type:** `date`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field indicates the end date of the consultation. The consultation is considered closed when no more engagement activities will take place and/or when a department begins analysing the input received during the engagement process.  
FR: Ce champ indique la date à laquelle la consultation a pris fin. Une consultation est terminée lorsqu’il n’y a plus d’activités de participation qui se tiendront et/ou lorsqu’un ministère entreprend l’analyse des commentaires reçus dans le cadre du processus de participation.


---

#### `status` – Status / État

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  
**Choice Set:** status (6 values)  


**Description:**  
EN: The field indicates the current status of the engagement process.  
FR: Cette zone indique l’état d’avancement du processus de participation.


##### Allowed Values (status)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `CA` | Closed – Analyzing Input | Fermée – Analyse en cours |
| `CN` | Closed – No Report Expected | Fermée – Aucun rapport en attente |
| `CR` | Closed – Report Available | Fermée – Rapport disponible |
| `NF` | Not Going Forward | Ne va pas de l&#39;avant |
| `O` | Open – Accepting Input | Ouverte – Avis acceptés |
| `P` | Planned | Prévue |




---

#### `profile_page_en` – Link to Consultations Profile Page (English) / Lien vers la page du profil des consultations (en anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field provides the link to the English engagement information profile page.  
FR: Cette zone contient le lien vers la page de profil (en anglais) qui donne des renseignements sur le processus de participation du public.


---

#### `profile_page_fr` – Link to Consultations Profile Page (French) / Lien vers la page du profil des consultations (en français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  


**Description:**  
EN: This field provides the link to the French engagement information profile page.  
FR: Cette zone contient le lien vers la page profil française qui contient des renseignements sur le processus de participation.


---

#### `report_available_online` – Report Available online / Rapport disponible en ligne

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  
**Choice Set:** report_available_online (2 values)  


**Description:**  
EN: This field indicates if the “What we Heard” report is completed, published and made available online on the Consulting with Canadians website.  
FR: Cette zone indique si le rapport intitulé « Ce que nous avons entendu » est terminé, publié et disponible sur le site Web « Consultations auprès des Canadiens ».


##### Allowed Values (report_available_online)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `N` | No | Non |
| `Y` | Yes | Oui |




---

#### `report_link_en` – Link to the “What we Heard” Report in English / Lien – rapport « Ce que nous avons entendu » en anglais

**Type:** `text`  
**Required:** No  
**Validation:** None / None  


**Description:**  
EN: This field provides the link to the “What we Heard” report when it is available online.  
FR: Cette zone contient le lien vers le rapport intitulé « Ce que nous avons entendu » en anglais après que le rapport est affiché en ligne.


---

#### `report_link_fr` – Link to the “What we Heard” Report in French / Lien – rapport « Ce que nous avons entendu » en français

**Type:** `text`  
**Required:** No  
**Validation:** None / None  


**Description:**  
EN: This field provides the link to the “What we Heard” report when it is available online.  
FR: Cette zone contient le lien vers le rapport intitulé « Ce que nous avons entendu » après que le rapport est affiché en ligne.


---

#### `high_profile` – High Profile / Haute visibilité

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  
**Choice Set:** high_profile (2 values)  


**Description:**  
EN: This field indicates whether the consultation or public engagement initiative is considered high profile. The consultation is considered high profile if it meets one or more of the criteria in the ‘Rationale’ field.  
FR: Cette zone indique si la consultation ou initiative de participation est à haute visibilité. La consultation est considérée comme de haute visibilité si elle réponde à un ou plus de critères à la zone 'Raison'.


##### Allowed Values (high_profile)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `N` | No | Non |
| `Y` | Yes | Oui |




---

#### `rationale` – Rationale / Raison

**Type:** `_text`  
**Required:** Yes  
**Validation:** This field must not be empty / Ce champ ne doit pas être vide  
**Choice Set:** rationale (7 values)  


**Description:**  
EN: The field indicates the rationale that prompted the public engagement initiative. This field includes only criteria that define high profile public engagement.  
FR: Cette zone comprend le(s) motif(s) de l’activité de participation du public. Cette zone inclut uniquement les critères qui définissent une consultation ou participation public de profil élevé.


##### Allowed Values (rationale)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `BG` | Budget | Budget |
| `IN` | International Commitment | Engagement international |
| `LC` | Duty to Consult | Obligation de consulter |
| `ML` | Mandate Letter | Lettre de mandat |
| `MP` | Minister and/or Parliamentary Secretary Involvement and/or announcement | Implication ou annonce du ministre ou du secrétaire parlementaire |
| `PC` | Parliament Committee | Comité parlementaire |
| `ST` | Speech of the Throne | Discours du Trône |




---




## Appendix

### Choice Sets Summary (All Resources)
| Choice Set | Field(s) | Values | Standalone Doc |
|------------|----------|--------|----------------|


### Generation Metadata

- Generated: 2025-09-14T01:24:41 (UTC)
- Source: dictionaries/consultations.json
- Commit: `322574e`
- Tool Version: simple-1

### Validation

- JSON Schema Validation: **PASSED**


### Notes

This documentation is auto-generated. Do not hand-edit; instead update the source recombinant JSON and re-run generation.