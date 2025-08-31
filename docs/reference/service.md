
# Service Inventory / Répertoire de services

**Dataset Type:** `service`  
**Last Generated:** 2025-08-31T01:26:25 (UTC)  
**Source:** dictionaries/service.json  
**Commit:** `24250a1`

Access, upload and modify the Service Inventory of external and internal enterprise services for your organization / Accèder, téléverser et modifier le catalogue des service internes intégrés et externes pour votre organisation

---

## Resources


- [Service Identification Information & Metrics / Information et paramètres sur l’identification des services](#service)

- [Service Standards & Performance Results / Normes de service et résultats du rendement](#service-std)


---


## Service Identification Information & Metrics / Information et paramètres sur l’identification des services 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `fiscal_yr` | Fiscal Year / Année financière | `text` | Yes |  | fiscal_yr | Identifies the fiscal year (April 1 to March 31) during which service activitie… |
| `service_id` | Service ID Number / Numéro d&#39;identification du service | `text` | Yes |  |  | The unique number assigned to a service in the inventory to make it easier to r… |
| `service_name_en` | Service Name (English) / Nom du service (en anglais) | `text` | Yes |  |  | Identifies the official name of the service. |
| `service_name_fr` | Service Name (French) / Nom du service (en français) | `text` | Yes |  |  | Identifies the official name of the service. |
| `service_description_en` | Service Description (English) / Description du service (en anglais) | `text` | Yes |  |  | Provides a brief description of the service, in plain language. |
| `service_description_fr` | Service Description (French) / Description du service (en français) | `text` | Yes |  |  | Provides a brief description of the service, in plain language. |
| `service_type` | Service Type / Type de service | `_text` | Yes |  | service_type | Identifies the service type as outlined in the Guideline on Service and Digital… |
| `service_recipient_type` | Service Recipient Type / Type de bénéficiaire du service | `text` | Yes |  | service_recipient_type | Targeted, client-based services: serve specific clients or groups, such as peop… |
| `service_scope` | Service Scope / Étendue du service | `_text` | Yes |  | service_scope | Indicates whether the service is external or internal to government. Multiple v… |
| `client_target_groups` | Client/Target Groups / Clients/groupes cibles | `_text` | Yes |  | client_target_groups | Identifies the clients or target groups of the service. Multiple values must be… |
| `program_id` | Program ID Code / Code d&#39;identification du programme | `_text` | Yes |  | program_id | Identifies the unique program code associated with program elements for all str… |
| `client_feedback_channel` | Client Feedback, by Channel / Commentaires des clients, par canal | `_text` | Yes |  | client_feedback_channel | Identifies which channels, if any, provide users of a service an opportunity to… |
| `automated_decision_system` | Automated Decision System / Système décisionnel automatisé | `text` | Yes |  | automated_decision_system | An automated decision system is defined in the Directive on Automated Decision-… |
| `automated_decision_system_description_en` | Automated Decision System Description (English) / Description du système décisionnel automatisé (anglais) | `text` | No |  |  | Describe what the system does. Include: the name or title of the system, the ro… |
| `automated_decision_system_description_fr` | Automated Decision System Description (French) / Description du système décisionnel automatisé (français) | `text` | No |  |  | Describe what the system does. Include: the name or title of the system, the ro… |
| `service_fee` | Service Fees / Frais de service | `text` | Yes |  | service_fee | Identifies whether a service fee is collected for the provision of the service. |
| `os_account_registration` | Online Services: Account Registration/Enrollment / Services en ligne : Enregistrement/inscription du compte | `text` | Yes |  | os_account_registration | Identifies whether a client can register or enroll for a personal account where… |
| `os_authentication` | Online Services: Authentication / Services en ligne : Authentification | `text` | Yes |  | os_authentication | Identifies whether a client can authenticate their identity online. |
| `os_application` | Online Services: Application / Services en ligne : Demande | `text` | Yes |  | os_application | Identifies whether a client can apply for a service online. |
| `os_decision` | Online Services: Decision / Services en ligne : Décision | `text` | Yes |  | os_decision | Identifies whether a client can be notified online of the outcome of their requ… |
| `os_issuance` | Online Services: Issuance / Services en ligne : Émission | `text` | Yes |  | os_issuance | Identifies whether a client can receive the service online, perhaps in the form… |
| `os_issue_resolution_feedback` | Online Services: Issue Resolution and Feedback / Services en ligne : Solution de problème et rétroaction | `text` | Yes |  | os_issue_resolution_feedback | Identifies whether a client can seek resolution to their issues or provide feed… |
| `os_comments_client_interaction_en` | Comments on Online Services - Client Interaction Points (English) / Commentaires sur les services électroniques - points d&#39;interaction avec les clients (anglais) | `text` | No |  |  | Comments related to online services - client Interaction points (English). For … |
| `os_comments_client_interaction_fr` | Comments on Online Services - Client Interaction Points (French) / Commentaires sur les services électroniques - points d&#39;interaction avec les clients (français) | `text` | No |  |  | Comments related to online services - client Interaction points (French). For a… |
| `last_service_review` | Year of last service review / Année du dernier examen de service | `text` | No |  | last_service_review | Identifies the fiscal year when the most recent service review was completed. |
| `last_service_improvement` | Year of last service improvement based on client feedback / Année de la dernière amélioration du service sur la base de la rétroaction du client | `text` | No |  | last_service_improvement | What was the most recent year in which this service was improved based on clien… |
| `sin_usage` | Use of Social Insurance Number / Utilisation du numéro d&#39;assurance sociale (NAS) | `text` | Yes |  | sin_usage | Identifies whether the Social Insurance Number (SIN) is used in the delivery of… |
| `cra_bn_identifier_usage` | Use of CRA Business Number as Standard Identifier / Utilisation du numéro d’entreprise de l’ARC en tant qu’identificateur standard | `text` | Yes |  | cra_bn_identifier_usage | Identifies whether the Canada Revenue Agency's Business Number is used in the d… |
| `num_phone_enquiries` | Number of Telephone Enquiries Received / Nombre des demandes téléphoniques reçus | `text` | Yes |  |  | Identifies the number of enquiries about the service received in this fiscal ye… |
| `num_applications_by_phone` | Number of Applications Submitted by Telephone / Nombre de demandes soumises par téléphone | `text` | Yes |  |  | Identifies the number of applications submitted in a fiscal year for the teleph… |
| `num_website_visits` | Number of Website Visits / Nombre de visites sur le site Web | `text` | Yes |  |  | Identifies the number of visits to the service's website in a fiscal year. A va… |
| `num_applications_online` | Number of Applications Submitted Online / Nombre de demandes soumises en ligne | `text` | Yes |  |  | Identifies the number of applications submitted in a fiscal year for the online… |
| `num_applications_in_person` | Number of Applications Submitted In-Person / Nombre de demandes soumises en personne | `text` | Yes |  |  | Identifies number of applications received in-person in a fiscal year for the s… |
| `num_applications_by_mail` | Number of Applications Submitted via Postal Mail / Nombre de demandes soumises par la poste | `text` | Yes |  |  | Identifies the number of applications received through postal mail in a fiscal … |
| `num_applications_by_email` | Number of Applications Submitted by Email / Nombre de demandes soumises par courriel | `text` | Yes |  |  | Identifies the number of applications received through email in a fiscal year f… |
| `num_applications_by_fax` | Number of Applications Submitted by Fax / Nombre de demandes soumises par fax | `text` | Yes |  |  | Identifies the number of applications received through fax in a fiscal year for… |
| `num_applications_by_other` | Number of Applications Submitted via other channels / Nombre de demandes soumises par les autre modes de prestations | `text` | Yes |  |  | Identifies the number of applications received through other channels not liste… |
| `special_remarks_en` | Special Remarks (English) / Remarques spéciales (anglais) | `text` | No |  |  | Provides additional space for comments related to volumetrics information. Plea… |
| `special_remarks_fr` | Special Remarks (French) / Remarques spéciales (français) | `text` | No |  |  | Provides additional space for comments related to volumetrics information. Plea… |
| `service_uri_en` | URL to Service (English) / URL du service (anglais) | `text` | No |  |  | Identifies the departmental webpage where the service is described and/or accessed. |
| `service_uri_fr` | URL to Service (French) / URL du service (français) | `text` | No |  |  | Identifies the departmental webpage where the service is described and/or accessed. |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `fiscal_yr` – Fiscal Year / Année financière

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** fiscal_yr (25 values)  


**Description:**  
EN: Identifies the fiscal year (April 1 to March 31) during which service activities took place. For example, records for fiscal year 2023-2024 should include applications received from April 1, 2023, to March 31, 2024.
  
FR: Indique l'exercice financier (1 avril au 31 mars) durant lequel les activités du service ont eu lieu. Par exemple, les données pour l’exercice financier 2023-2024 devrait inclure les demandes de service qui ont été reçues entre le 1 avril 2023 et le 31 mars 2024.



##### Allowed Values (fiscal_yr)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `2005-2006` | 2005-2006 | 2005-2006 |
| `2006-2007` | 2006-2007 | 2006-2007 |
| `2007-2008` | 2007-2008 | 2007-2008 |
| `2008-2009` | 2008-2009 | 2008-2009 |
| `2009-2010` | 2009-2010 | 2009-2010 |
| `2010-2011` | 2010-2011 | 2010-2011 |
| `2011-2012` | 2011-2012 | 2011-2012 |
| `2012-2013` | 2012-2013 | 2012-2013 |
| `2013-2014` | 2013-2014 | 2013-2014 |
| `2014-2015` | 2014-2015 | 2014-2015 |
| `2015-2016` | 2015-2016 | 2015-2016 |
| `2016-2017` | 2016-2017 | 2016-2017 |
| `2017-2018` | 2017-2018 | 2017-2018 |
| `2018-2019` | 2018-2019 | 2018-2019 |
| `2019-2020` | 2019-2020 | 2019-2020 |
| `2020-2021` | 2020-2021 | 2020-2021 |
| `2021-2022` | 2021-2022 | 2021-2022 |
| `2022-2023` | 2022-2023 | 2022-2023 |
| `2023-2024` | 2023-2024 | 2023-2024 |
| `2024-2025` | 2024-2025 | 2024-2025 |
| `2025-2026` | 2025-2026 | 2025-2026 |
| `2026-2027` | 2026-2027 | 2026-2027 |
| `2027-2028` | 2027-2028 | 2027-2028 |
| `2028-2029` | 2028-2029 | 2028-2029 |
| `2029-2030` | 2029-2030 | 2029-2030 |




---

#### `service_id` – Service ID Number / Numéro d'identification du service

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field cannot contain commas.
 / Ce champ ne doit pas être vide.
Ce champ ne peut pas contenir de virgules.
  


**Description:**  
EN: The unique number assigned to a service in the inventory to make it easier to refer to specific services.  
FR: Le numéro unique attribué à un service dans le répertoire afin de faciliter le référencement à des services précis.


---

#### `service_name_en` – Service Name (English) / Nom du service (en anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field has a maximum length of 350 characters.
 / Ce champ ne doit pas être vide.
Ce champ ne peut excéder une longueur maximale de 350 caractères.
  


**Description:**  
EN: Identifies the official name of the service.  
FR: Indique le nom officiel du service.


---

#### `service_name_fr` – Service Name (French) / Nom du service (en français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field has a maximum length of 350 characters.
 / Ce champ ne doit pas être vide.
Ce champ ne peut excéder une longueur maximale de 350 caractères.
  


**Description:**  
EN: Identifies the official name of the service.  
FR: Indique le nom officiel du service.


---

#### `service_description_en` – Service Description (English) / Description du service (en anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field has a maximum length of 1800 characters.
 / Ce champ ne doit pas être vide.
Ce champ ne peut excéder une longueur maximale de 1800 caractères.
  


**Description:**  
EN: Provides a brief description of the service, in plain language.  
FR: Offre une brève description du service, en langage simple.


---

#### `service_description_fr` – Service Description (French) / Description du service (en français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field has a maximum length of 1800 characters.
 / Ce champ ne doit pas être vide.
Ce champ ne peut excéder une longueur maximale de 1800 caractères.
  


**Description:**  
EN: Provides a brief description of the service, in plain language.  
FR: Offre une brève description du service, en langage simple.


---

#### `service_type` – Service Type / Type de service

**Type:** `_text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** service_type (8 values)  


**Description:**  
EN: Identifies the service type as outlined in the Guideline on Service and Digital. Multiple values must be separated by a comma (,).  
FR: Indique le type de service tel qu'indiqué dans la Ligne directrice sur les services et le numérique. Séparez les entrées par une virgule (,) s’il y en a plusieurs qui s’appliquent.


##### Allowed Values (service_type)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `APIR` | Agreements, Permissions, Inspections, Rulings | Accords, autorisations, inspections, décisions |
| `CER` | Care, Education, Recreation | Soins, éducation, loisirs |
| `GNC` | Grants and Contributions | Subventions et contributions |
| `INFO` | Information | Informations |
| `LRP` | Legislation, Regulation, Policy | Législation, réglementation, politique |
| `PPI` | Penalties, Protection, Intervention | Pénalités, protection, interventions |
| `REG_VOL` | High Volume Regulatory Transactions | Opérations réglementaires à demande élevée |
| `RES` | Resources | Ressources |




---

#### `service_recipient_type` – Service Recipient Type / Type de bénéficiaire du service

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** service_recipient_type (2 values)  


**Description:**  
EN: Targeted, client-based services: serve specific clients or groups, such as people, businesses, GC employees. Untargeted, Societal-based Service: serve society, not distinct people or groups, such as military, pure science.
  
FR: Services ciblés axés sur les clients : Répondent aux besoins de clients ou de groupes particuliers, par exemple les personnes, les entreprises ou les employés du GC. Services non ciblés axés sur la société : Répondent aux besoins de la société en général et non aux besoins de personnes ou de groupes distincts, par exemple les forces armées ou la science pure.



##### Allowed Values (service_recipient_type)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `CLIENT` | Targeted, Client-based service | Service ciblé, axé sur les clients |
| `SOCIETY` | Untargeted, Societal-based service | Service non-ciblé, axé sur la société |




---

#### `service_scope` – Service Scope / Étendue du service

**Type:** `_text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** service_scope (4 values)  


**Description:**  
EN: Indicates whether the service is external or internal to government. Multiple values must be separated by a comma (,).  
FR: Indique si le service est offert aux clients externes ou internes au gouvernement. Séparez les entrées par une virgule (,) s’il y en a plusieurs qui s’appliquent.


##### Allowed Values (service_scope)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `CLUSTER` | Internal Cluster Service | Service cluster interne |
| `ENTERPRISE` | Internal Enterprise Service | Service interne intégré |
| `EXTERN` | External Service | Service externe |
| `INTERN` | Internal Service | Service interne |




---

#### `client_target_groups` – Client/Target Groups / Clients/groupes cibles

**Type:** `_text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** client_target_groups (6 values)  


**Description:**  
EN: Identifies the clients or target groups of the service. Multiple values must be separated by a comma (,).  
FR: Identifie les clients ou les groupes de services cibles. Séparez les entrées par une virgule (,) s’il y en a plusieurs qui s’appliquent.


##### Allowed Values (client_target_groups)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `ECONOM` | Economic Segments (Businesses) | Segments économiques (entreprises) |
| `FOR` | Foreign Entities | Entités étrangères |
| `INTERN_GOV` | Internal to Government | Interne au gouvernement |
| `NGO` | Non Profit Institutions and Organizations | Institutions et organismes sans but lucratif |
| `PERSON` | Persons | Particuliers |
| `PTC` | Provinces, Territories or Communities | Provinces, territoires et collectivités |




---

#### `program_id` – Program ID Code / Code d'identification du programme

**Type:** `_text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** program_id (1079 values)  


**Description:**  
EN: Identifies the unique program code associated with program elements for all strategic outcomes, programs, sub-programs, and sub-sub-programs. The Program codes in the government-wide Chart of Accounts can be used. Corporate planners in the department/agency who are responsible for the Policy on Results can assist in identifying this, if needed. Multiple values must be separated by a comma (,).
  
FR: Indique le code de programme unique associé aux éléments de programme pour tous les résultats stratégiques, les programmes, les sous-programmes et les sous-sous-programmes. Les planificateurs ministériels du ministère ou de l'organisme responsables de la Politique sur les résultats peuvent aider à déterminer le code d'identification du programme, au besoin. Séparez les entrées par une virgule (,) s’il y en a plusieurs qui s’appliquent.



##### Allowed Values (program_id)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `BCZ01` | Data Partnerships and Pan-Canadian Collaboration | Partenariats de données et Collaboration pancanadienne |
| `BCZ02` | Marketing | Marketing |
| `BCZ03` | Investor Services | Services aux investisseurs |
| `BED01` | Inclusive Communities | Collectivités inclusives |
| `BED02` | Diversified Communities | Collectivités diversifiées |
| `BED03` | Research and Development and Commercialization | Recherche-développement et commercialisation |
| `BED04` | Innovation Ecosystem | Écosystème d&#39;innovation |
| `BED05` | Business Growth | Croissance des entreprises |
| `BED06` | Trade and Investment | Commerce et investissement |
| `BED07` | Policy Research and Engagement | Recherche stratégique et mobilisation |
| `BEE01` | Registry Services | Service de greffe |
| `BEE02` | Legal Services | Services juridiques |
| `BEE03` | Mandate and Members Services | Services liés aux mandats et aux membres |
| `BEG01` | Judicial Services | Services judiciaires |
| `BEG02` | Registry Services | Services de greffe |
| `BEG03` | E-Courts | Tribunaux électroniques |
| `BEG04` | Security | Sécurité |
| `BEZ01` | Copyright Tariff Setting and Issuance of Licences | Établissement de tarifs et délivrance de licences pour l&#39;utilisation des droits d&#39;auteur |
| `BFO01` | Maintenance of infrastructure and security | Entretien des infrastructures et sécurité |
| `BFY01` | Educational, cultural and heritage activities | Activités pédagogiques, culturelles et patrimoniales |
| `BFZ01` | Occupational health and safety information and services | Services et renseignements sur la santé et la sécurité au travail |
| `BGB01` | Grain Quality | Qualité des grains |
| `BGB02` | Grain Research | Recherches sur les grains |
| `BGB03` | Safeguards for Grain Farmers | Mesures de protection des producteurs de grain |
| `BGC01` | Refugee Protection Decisions | Décisions relatives à la protection des réfugiés |
| `BGC02` | Refugee Appeal Decisions | Décisions relatives aux appels des réfugiés |
| `BGC03` | Admissibility and Detention Decisions | Décisions relatives aux enquêtes et à la détention |
| `BGC04` | Immigration Appeal Decisions | Décisions relatives aux appels en matière d&#39;immigration |
| `BGD01` | Visitors | Visiteurs |
| `BGD02` | International Students | Étudiants étrangers |
| `BGD03` | Temporary Workers | Travailleurs temporaires |
| `BGE01` | Federal Economic Immigration | Immigration économique fédérale |
| `BGE02` | Regional Economic Immigration | Immigration économique régionale |
| `BGE03` | Family Reunification | Regroupement familial |
| `BGE04` | Humanitarian/Compassionate and Discretionary Immigration | Immigration pour considérations d&#39;ordre humanitaire et discrétionnaire |
| `BGE05` | Refugee Resettlement | Réinstallation des réfugiés |
| `BGE06` | Asylum | Asile |
| `BGE07` | Settlement | Établissement |
| `BGF01` | Citizenship | Citoyenneté |
| `BGF02` | Passport | Passeports |
| `BGG01` | Voting Services Delivery and Field Management | Prestation des services de vote et gestion en région |
| `BGG02` | National Register of Electors and Electoral Geography | Registre national des électeurs et géographie électorale |
| `BGG03` | Public Education and Information | Éducation et information du public |
| `BGG04` | Electoral Integrity and Regulatory Oversight | Intégrité électorale et surveillance réglementaire |
| `BGH01` | Protection of Official Languages Rights | Protection des droits liés aux langues officielles |
| `BGI01` | Advancement of Official Languages | Avancement des langues officielles |
| `BGM01` | Reaching Home | Vers un chez-soi |
| `BGM02` | Social Development Partnerships Program | Programme de partenariats pour le développement social |
| `BGM03` | New Horizons for Seniors Program | Programme Nouveaux Horizons pour les aînés |
| `BGM04` | Enabling Accessibility Fund | Fonds pour l&#39;accessibilité |
| `BGM05` | Early Learning and Child Care | Apprentissage et garde des jeunes enfants |
| `BGM06` | Canadian Benefit for Parents of Young Victims of Crime | Allocation canadienne aux parents de jeunes victimes de crimes |
| `BGM07` | Indigenous Early Learning Child Care Transformation Initiative | Initiative de transformation de l&#39;apprentissage et de la garde des jeunes enfants autochtones |
| `BGM08` | Sustainable Development Goals Funding Program | Programme de financement des Objectifs de développement durable |
| `BGM09` | Accessible Canada Initiative | Canada Accessible |
| `BGM10` | Social Innovation and Social Finance Strategy | Stratégie d&#39;innovation sociale et de finance sociale |
| `BGM11` | Strategic Engagement and Research Program | Programme stratégique de mobilisation des partenaires et de recherche |
| `BGM12` | Black-led Philanthropic Endowment Fund | Le Fonds de dotation philanthropique dirigé par des Noirs |
| `BGM13` | National School Food Program | Programme national d&#39;alimentation dans les écoles |
| `BGN01` | Old Age Security | Sécurité de la vieillesse |
| `BGN02` | Canada Disability Savings Program | Programme canadien pour l&#39;épargne-invalidité |
| `BGN03` | Canada Pension Plan | Régime de pensions du Canada |
| `BGO01` | Employment Insurance | Assurance-emploi |
| `BGO02` | Workforce Development Agreements | Ententes sur le développement de la main-d&#39;œuvre |
| `BGO03` | Labour Market Development Agreements | Ententes sur le développement du marché du travail |
| `BGO04` | Opportunities Fund for Persons with Disabilities | Fonds d&#39;intégration pour les personnes handicapées |
| `BGO05` | Job Bank | Guichet-Emplois |
| `BGO06` | Youth Employment and Skills Strategy | Stratégie emploi et compétences jeunesse |
| `BGO07` | Canada Service Corps | Service jeunesse Canada |
| `BGO08` | Skills and Partnership Fund | Fonds pour les compétences et les partenariats |
| `BGO09` | Skills for Success | Compétences pour réussir |
| `BGO10` | Indigenous Skills and Employment Training (ISET) Program | Programme de formation pour les compétences et l&#39;emploi destiné aux Autochtones |
| `BGO11` | Student Work Placement Program | Programme de stages pratiques pour étudiants |
| `BGO12` | Union Training and Innovation Program | Programme pour la formation et l&#39;innovation en milieu syndical |
| `BGO13` | Sectoral Workforce Solutions Program | Programme de solutions pour la main-d&#39;œuvre sectorielle |
| `BGO14` | Temporary Foreign Worker Program | Programme des travailleurs étrangers temporaires |
| `BGO15` | Foreign Credential Recognition Program | Programme de reconnaissance des titres de compétences étrangers |
| `BGO16` | Enabling Fund for Official Language Minority Communities | Fonds d&#39;habilitation pour les communautés de langue officielle en situation minoritaire |
| `BGO17` | Canada Student Financial Assistance Program and Canada Apprentice Loans | Programme canadien d&#39;aide financière aux étudiants et prêts aux apprentis |
| `BGO18` | Canada Education Savings Program | Programme canadien pour l&#39;épargne-études |
| `BGO19` | Skilled Trades and Apprenticeship (Red Seal Program) | Métiers spécialisés et apprentissage (programme du Sceau rouge) |
| `BGO20` | Apprenticeship Grants | Subvention aux apprentis |
| `BGO21` | Future Skills | Compétences futures |
| `BGO22` | Skilled Trades Awareness and Readiness (STAR) Program | Programme de sensibilisation et de préparation aux métiers spécialisés (PSPMS) |
| `BGO23` | Supports for Student Learning | Soutien à l&#39;apprentissage des étudiants |
| `BGO24` | Canada Emergency Response Benefit | Prestation canadienne d&#39;urgence |
| `BGO25` | Canada Recovery Benefits | Prestations canadiennes de relance économique |
| `BGO26` | Apprenticeship Service | Service d&#39;apprentissage |
| `BGO27` | Community Workforce Development Program | Le programme de développement de la main-d&#39;œuvre des communautés |
| `BGO28` | Canada Worker Lockdown Benefit | Prestation canadienne pour les travailleurs en cas de confinement |
| `BGO29` | Canadian Apprenticeship Strategy | Stratégie canadienne de formation en apprentissage |
| `BGP01` | Labour Relations | Relations de travail |
| `BGP02` | Federal Workers&#39; Compensation | Service fédéral d&#39;indemnisation des accidentés du travail |
| `BGP03` | Occupational Health and Safety | Santé et sécurité au travail |
| `BGP04` | Workplace Equity | Équité en milieu de travail |
| `BGP05` | Labour Standards | Normes du travail |
| `BGP06` | Wage Earner Protection Program | Programme de protection des salariés |
| `BGP07` | International Labour Affairs | Affaires internationales du travail |
| `BGQ01` | Government of Canada Telephone General Enquiries Services | Services téléphoniques de renseignements généraux du gouvernement du Canada |
| `BGQ02` | Government of Canada Internet Presence | Présence du gouvernement du Canada sur Internet |
| `BGQ03` | Citizen Service Network | Réseau de service aux citoyens |
| `BGQ04` | Passport | Passeport |
| `BGQ05` | Service Delivery Partnerships | Partenariats de prestation de services |
| `BGQ06` | Canadian Digital Service | Service numérique canadien |
| `BGR01` | Clean Growth and Climate Change Mitigation | Croissance propre et atténuation des changements climatiques |
| `BGR02` | International Environment and Climate Action | Action internationale sur l&#39;environnement et le climat |
| `BGR03` | Climate Change Adaptation | Adaptation aux changements climatiques |
| `BGS01` | Air Quality | Qualité de l&#39;air |
| `BGS02` | Water Quality and Ecosystems Partnerships | Qualité de l&#39;eau et partenariat sur les ecosystèmes |
| `BGS03` | Community and Sustainability | Communauté et durabilité |
| `BGS04` | Aquatic Ecosystems Health, Substances and Waste Management | Santé des écosystèmes aquatiques et gestion des substances et des déchets |
| `BGS05` | Compliance Promotion and Enforcement - Pollution | Promotion de la conformité et application de la loi - Pollution |
| `BGS06` | Canada Water Agency Program | Programme de l&#39;Agence canadienne de l&#39;eau |
| `BGT01` | Species at Risk | Espèces en péril |
| `BGT02` | Migratory Birds and Other Wildlife | Oiseaux migrateurs et autres espèces sauvages |
| `BGT03` | Habitat Conservation and Protection | Conservation et protection des habitats |
| `BGT04` | Biodiversity Policy and Partnerships | Politiques et partenariats sur la biodiversité |
| `BGT05` | Environmental Assessment | Évaluation environnementale |
| `BGT06` | Compliance Promotion and Enforcement - Wildlife | Promotion de la conformité et application de la loi - Faune |
| `BGU01` | Weather and Environmental Observations, Forecasts and Warnings | Observations, prévisions et avertissements météorologiques et environnementaux |
| `BGU02` | Hydrological Services | Services hydrologiques |
| `BGV01` | Impact Assessment Policy Development | Élaboration de politiques en matière d&#39;évaluation d&#39;impact |
| `BGV02` | Assessment Delivery | Réalisation des évaluations |
| `BGV03` | Assessment Administration, Conduct, and Monitoring | Administration, réalisation et surveillance de l&#39;évaluation |
| `BGV04` | Indigenous Relations and Engagement | Relations avec les Autochtones et participation des Autochtones |
| `BGW01` | Heritage Places Establishment | Création de lieux patrimoniaux |
| `BGW02` | Heritage Places Conservation | Conservation des lieux patrimoniaux |
| `BGW03` | Heritage Places Promotion and Public Support | Promotion des lieux patrimoniaux et soutien du public |
| `BGW04` | Visitor Experience | Expérience du visiteur |
| `BGW05` | Heritage Canals, Highways and Townsites Management | Gestion des canaux patrimoniaux, des routes et des lotissements urbains |
| `BGX01` | Legislative Audit | Audit législatif |
| `BLL01` | Business innovation and growth | Innovation et croissance des entreprises |
| `BLL02` | Vitality of communities | Vitalité des collectivités |
| `BLL03` | Targeted or temporary support | Soutien ponctuel ou ciblé |
| `BLL04` | Regional Innovation | Innovation régionale |
| `BLM01` | Space Exploration | Exploration spatiale |
| `BLM02` | Space Utilization | Utilisation de l&#39;espace |
| `BLM03` | Space Capacity Development | Développement de la capacité spatiale |
| `BNL01` | Community Development | Développement communautaire |
| `BNL02` | Business Development | Expansion des entreprises |
| `BNL03` | Policy and Advocacy | Politiques et défense des intérêts |
| `BNL04` | Northern Projects Management | Gestion des projets nordiques |
| `BNM01` | Advanced Manufacturing | Fabrication de pointe |
| `BNM02` | Commercialization Partnerships | Partenariats de commercialisation |
| `BNM03` | Business Growth and Productivity | Croissance et productivité des entreprises |
| `BNM04` | Business Investment | Investissement dans les entreprises |
| `BNM05` | Business Services | Services aux entreprises |
| `BNM06` | Community Futures Program | Programme de développement des collectivités |
| `BNM07` | Eastern Ontario Development Program | Programme de développement de l&#39;Est de l&#39;Ontario |
| `BNM08` | Official Languages Minority Communities | Communautés de langue officielle en situation minoritaire |
| `BNM09` | Regional Diversification | Diversification régionale |
| `BNM10` | Business Scale Up and Productivity | Accroissement d&#39;échelle et productivité des entreprises |
| `BNM11` | Regional Innovation Ecosystem | Écosystème d&#39;innovation régional |
| `BNM12` | Community Economic Development and Diversification | Développement économique et diversification des collectivités |
| `BNN01` | Talent Development | Développement des talents |
| `BNN02` | Support for Underrepresented Entrepreneurs | Soutien aux entrepreneurs sous-représentés |
| `BNN03` | Bridging Digital Divides | Combler le fossé numérique |
| `BNN04` | Economic Development in Northern Ontario | Développement économique du Nord de l&#39;Ontario |
| `BNN05` | Consumer Affairs | Programme des consommateurs |
| `BNO01` | Science and Research | Sciences et recherche |
| `BNO02` | Horizontal Science, Research and Technology Policy | Politique horizontale sur les sciences, la recherche et la technologie |
| `BNO03` | Innovation Superclusters Initiative | Initiative des supergrappes d&#39;innovation |
| `BNO04` | Support to External Advisors | Soutien aux conseillers externes |
| `BNP01` | Business Innovation | L&#39;innovation en entreprises |
| `BNP02` | Support for Small Business | Aide pour les petites entreprises |
| `BNP03` | Business Policy and Analysis | Politique de l&#39;entreprise et analyse |
| `BNP04` | Economic Outcomes from Procurement | Retombées économiques de l&#39;approvisionnement |
| `BNP05` | Digital Service | Services numériques |
| `BNP06` | Spectrum and Telecommunications | Spectre et télécommunications |
| `BNP07` | Clean Technology and Clean Growth | Technologies et croissance propres |
| `BNP08` | Communication Technologies, Research and Innovation | Recherche et innovation dans le domaine des technologies des communications |
| `BNP09` | Business Conditions Policy | Politique sur les conditions commerciales |
| `BNP10` | Insolvency | Insolvabilité |
| `BNP11` | Intellectual Property | Propriété intellectuelle |
| `BNP12` | Competition Law Enforcement and Promotion | Promotion et application du droit de la concurrence |
| `BNP13` | Federal Incorporation | Constitution en société sous le régime fédéral |
| `BNP14` | Investment Review | Examen des investissements |
| `BNP15` | Trade Measurement | Mesure commerciale |
| `BNP16` | Tourism | Tourisme |
| `BNP17` | Talent Development | Développement des talents |
| `BNP18` | Marketplace Protection and Promotion | Protection et promotion du marché |
| `BNQ01` | Aerospace | Aérospatiale |
| `BNQ02` | Aquatic and Crop Resource Development | Développement des cultures et des ressources aquatiques |
| `BNQ03` | Automotive and Surface Transportation | Automobile et Transports de surface |
| `BNQ04` | Construction | Construction |
| `BNQ05` | Energy, Mining and Environment | Énergie, mines et environnement |
| `BNQ06` | Herzberg Astronomy &amp; Astrophysics | Herzberg, Astronomie et astrophysique |
| `BNQ07` | Human Health Therapeutics | Thérapeutiques en santé humaine |
| `BNQ08` | Industrial Research Assistance Program | Programme d&#39;aide à la recherche industrielle |
| `BNQ09` | Information and Communications Technologies | Technologies de l&#39;information et des communications |
| `BNQ10` | International Affiliations | Affiliations internationales |
| `BNQ11` | Metrology | Métrologie |
| `BNQ12` | Medical Devices | Dispositifs médicaux |
| `BNQ13` | Nanotechnology | Nanotechnologie |
| `BNQ14` | National Science Library | Bibliothèque scientifique nationale |
| `BNQ15` | Ocean, Coastal and River Engineering | Génie océanique, côtier et fluvial |
| `BNQ16` | Security and Disruptive Technologies | Technologies de sécurité et de rupture |
| `BNQ17` | TRIUMF | TRIUMF |
| `BNQ18` | Business Management Support (Enabling) | Soutien à la gestion des affaires (fonction habilitante) |
| `BNQ19` | Design &amp; Fabrication Services (Enabling) | Services de conception et de fabrication (fonction habilitante) |
| `BNQ20` | Research Information Technology Platforms (Enabling) | Technologies spécialisées d&#39;information en R-D (fonction habilitante) |
| `BNQ21` | Special Purpose Real Property (Enabling) | Biens immobiliers à vocation particulière (fonction habilitante) |
| `BNQ22` | Collaborative Science, Technology and Innovation Program | Programme de collaboration en science, en technologie et en innovation |
| `BNQ23` | Advanced Electronics and Photonics | Électronique et photonique avancées |
| `BNQ24` | Digital Technologies | Technologies numériques |
| `BNQ25` | Genomics Research and Development Initiative Shared Priority Projects | Projets à priorité partagée de l&#39;Initiative de recherche et développement en génomique |
| `BNQ26` | Biologics Manufacturing Centre | Centre de production de produits biologiques |
| `BNQ27` | Canadian Photonics Fabrication Centre | Centre de fabrication pour la photonique du Canada |
| `BNQ28` | Quantum and Nanotechnologies | Quantique et nanotechnologies |
| `BNR01` | Discovery Research | Recherche axée sur la découverte |
| `BNR02` | Research Training and Talent Development | Formation en recherche et perfectionnement des compétences |
| `BNR03` | Research Partnerships | Partenariats de recherche |
| `BNT01` | Insight Research | Recherche axée sur la connaissance |
| `BNT02` | Research Training and Talent Development | Formation en recherche et perfectionnement des compétences |
| `BNT03` | Research Partnerships | Partenariats de recherche |
| `BNT04` | New Frontiers in Research Fund | Fonds Nouvelles frontières en recherche |
| `BNT05` | Canada Research Continuity Emergency Fund | Fonds d&#39;urgence pour la continuité de la recherche au Canada |
| `BNT06` | Canada Biomedical Research Fund | Fonds de recherche biomédicale du Canada |
| `BNU01` | Research Support Fund | Fonds de soutien à la recherche |
| `BNV01` | Economic and Environmental Statistics | Statistique économique et environnementale |
| `BNV02` | Socio-economic Statistics | Statistique socioéconomique |
| `BNV03` | Censuses | Recensements |
| `BNV04` | Cost-Recovered Statistical Services | Services statistiques à frais recouvrables |
| `BNV05` | Centres of Expertise | Centres d&#39;expertise |
| `BNW01` | Innovation | Innovation |
| `BNW02` | Business Growth | Croissance des entreprises |
| `BNW03` | Business Services | Services aux entreprises |
| `BNW04` | Community Initiatives | Initiatives communautaires |
| `BNX01` | Litigation Services | Services de contentieux |
| `BNX02` | Legislative Services | Services législatifs |
| `BNX03` | Advisory Services | Services de consultation juridique |
| `BNY01` | Legal Policies, Laws and Governance | Politiques juridiques, lois et gouvernance |
| `BNY02` | Legal Representation | Représentation juridique |
| `BNY03` | Contraventions Regime | Régime de contraventions |
| `BNY04` | Drug Treatment Court Funding Program | Programme de financement des tribunaux de traitement de la toxicomanie |
| `BNY05` | Victims of Crime | Victimes d&#39;actes criminels |
| `BNY06` | Youth Justice | Justice pour les jeunes |
| `BNY07` | Family Justice | Justice pour la famille |
| `BNY08` | Indigenous Justice | Justice pour les autochtones |
| `BNY09` | Justice System Partnerships | Partenariats avec le système de justice |
| `BNY10` | Ombudsman for Victims of Crime | Ombudsman des victimes d&#39;actes criminels |
| `BNZ01` | Payments pursuant to the Judges Act | Paiements en application de la Loi sur les juges |
| `BNZ02` | Federal Judicial Affairs | Commissariat à la magistrature fédérale |
| `BNZ03` | Canadian Judicial Council | Conseil canadien de la magistrature |
| `BRA01` | Tax Services and Processing | Services fiscaux et traitement |
| `BRA02` | Returns Compliance | Observation en matière de production des déclarations |
| `BRA03` | Collections | Recouvrements |
| `BRA04` | Domestic Compliance | Observation nationale |
| `BRA05` | International and Large Business Compliance and Criminal Investigations | Observation du secteur international et grandes entreprises et enquêtes criminelles |
| `BRA06` | Objections and Appeals | Oppositions et appels |
| `BRA07` | Taxpayer Relief | Allègement pour les contribuables |
| `BRA08` | Service Feedback | Rétroaction sur le service |
| `BRA09` | Charities | Organismes de bienfaisance |
| `BRA10` | Registered Plans | Régimes enregistrés |
| `BRA11` | Policy, Rulings, and Interpretations | Politique, décisions et interprétations |
| `BRA12` | Reporting Compliance | Observation en matière d&#39;exactitude des déclarations |
| `BRB01` | Benefits | Prestations |
| `BRC01` | Taxpayers&#39; Ombudsperson | Ombudsman des contribuables |
| `BRD01` | Federal Prosecutions | Poursuites fédérales |
| `BRD02` | Regulatory Offences and Economic Crime Prosecution Program | Programme de poursuites des infractions réglementaires et des crimes économiques |
| `BRE01` | Compliance and Enforcement | Observation et contrôle d&#39;application |
| `BRF01` | Compliance with access to information obligations | Conformité avec les obligations prévues à la Loi sur l&#39;accès à l&#39;information |
| `BRG01` | Promotion Program | Programme de promotion |
| `BRG02` | Compliance Program | Programme de conformité |
| `BRH01` | Court administration | Administration de la Cour |
| `BRH02` | Administration of the Judges Act for the Judges of the Supreme Court of Canada | Administration de la Loi sur les juges pour les juges de la Cour suprême du Canada |
| `BRT01` | Support for Canadian Content Creation | Soutien pour la création de contenu canadien |
| `BRT02` | Connection to the Communications System | Connexion au système de communication |
| `BRT03` | Protection Within the Communications System | Protection au sein du système de communication |
| `BSA01` | Promotion Program | Programme de promotion |
| `BSB01` | Protection Program | Programme de protection |
| `BSC01` | Audit Program | Programme d&#39;audit |
| `BSD01` | Arts | Arts |
| `BSD02` | Cultural Marketplace Framework | Cadre du marché culturel |
| `BSD03` | Cultural Industries Support and Development | Soutien et développement des industries culturelles |
| `BSE01` | National Celebrations, Commemorations and Symbols | Célébrations, commémorations, symboles nationaux |
| `BSE02` | Community Engagement and Heritage | Engagement communautaire et patrimoine |
| `BSE03` | Preservation of and Access to Heritage | Préservation et accès au patrimoine |
| `BSE04` | Learning About Canadian History | Apprentissage de l&#39;histoire canadienne |
| `BSF01` | Sport Development and High Performance | Développement du sport et performance de haut niveau |
| `BSG01` | Multiculturalism and Anti-Racism | Multiculturalisme et lutte contre le racisme |
| `BSG02` | Human Rights | Droits de la personne |
| `BSG03` | Indigenous Languages | Langues autochtones |
| `BSG04` | Youth Engagement | Engagement des jeunes |
| `BSH01` | Official Languages | Langues officielles |
| `BSI01` | Acquisition and processing of government records | Acquisition et traitement de documents gouvernementaux |
| `BSI02` | Acquisition and processing of published heritage | Acquisition et traitement du patrimoine publié |
| `BSI03` | Acquisition and processing of private archives | Acquisition et traitement d&#39;archives privées |
| `BSI04` | Preservation | Préservation |
| `BSJ01` | Public services | Services publics |
| `BSJ02` | Outreach and support to communities | Sensibilisation et soutien aux collectivités |
| `BSJ03` | Access to information and privacy | Accès à l&#39;information et protection des renseignements personnels |
| `BSM01` | Audiovisual programming and production | Programmation et production audiovisuelles |
| `BSP01` | Distribution of works and audience engagement | Distribution des œuvres et interaction avec les auditoires |
| `BSP02` | Promotion of works and National Film Board outreach | Promotion des œuvres et rayonnement de l&#39;Office national du film |
| `BSP03` | Preservation, conservation and digitization of works | Préservation, conservation et numérisation des œuvres |
| `BTA01` | Infrastructure, Tolls and Export Applications | Demandes relatives aux infrastructures, aux droits et aux exportations |
| `BTA02` | Participant Funding | Aide financière aux participants |
| `BTB01` | Company Performance | Rendement des sociétés |
| `BTB02` | Management System and Industry Performance | Système de gestion et rendement du secteur |
| `BTB03` | Emergency Management | Gestion des situations d&#39;urgence |
| `BTB04` | Regulatory Framework | Cadre de réglementation |
| `BTC01` | Energy System Information | Information sur les filières énergétiques |
| `BTC02` | Pipeline Information | Information sur les pipelines |
| `BTD01` | Stakeholder Engagement | Mobilisation des parties prenantes |
| `BTD02` | Indigenous Engagement | Mobilisation des Autochtones |
| `BTF01` | Fisheries Management | Gestion des pêches |
| `BTF02` | Aboriginal Programs and Treaties | Programmes Autochtones et traités |
| `BTF03` | Aquaculture Management | Gestion de l&#39;aquaculture |
| `BTF04` | Salmonid Enhancement | Mise en valeur des salmonidés |
| `BTF05` | International Engagement | Engagement à l&#39;échelle internationale |
| `BTF06` | Small Craft Harbours | Ports pour petits bateaux |
| `BTF07` | Conservation and Protection | Conservation et protection |
| `BTF08` | Aquatic Animal Health | Santé des animaux aquatiques |
| `BTF09` | Biotechnology and Genomics | Biotechnologie et génomique |
| `BTF10` | Aquaculture Science | Sciences de l&#39;aquaculture |
| `BTF11` | Fisheries Science | Sciences halieutiques |
| `BTF12` | Economics and Statistics | Économie et statistiques |
| `BTF13` | Fish and Seafood Sector | Secteur du poisson et des fruits de mer |
| `BTG01` | Fish and Fish Habitat Protection | Programme de protection du poisson et de son habitat |
| `BTG02` | Aquatic Invasive Species | Espèces aquatiques envahissantes |
| `BTG03` | Species at Risk | Espèces en péril |
| `BTG04` | Marine Planning and Conservation | Planification et conservation marines |
| `BTG05` | Aquatic Ecosystem Science | Science liée aux écosystèmes aquatiques |
| `BTG06` | Oceans and Climate Change Science | Science liée aux océans et au changement climatique |
| `BTG07` | Aquatic Ecosystems Economics | Économie liée aux écosystèmes aquatiques |
| `BTH01` | Icebreaking Services | Services de déglaçage |
| `BTH02` | Aids to Navigation | Aides à la navigation |
| `BTH03` | Waterways Management | Gestion des voies navigables |
| `BTH04` | Marine Communications and Traffic Services | Services de communications et de trafic maritimes |
| `BTH05` | Shore-based Asset Readiness | État de préparation des actifs terrestres |
| `BTH06` | Hydrographic Services, Data and Science | Services hydrographiques, données et sciences |
| `BTI01` | Search and Rescue | Recherche et sauvetage |
| `BTI02` | Marine Environmental and Hazards Response | Réponse aux Intervention environnementale et dangers maritimes |
| `BTI03` | Maritime Security | Sécurité maritime |
| `BTI04` | Fleet Operational Capability | Capacité opérationnelle de la flotte |
| `BTI05` | Fleet Maintenance | Entretien de la flotte |
| `BTI06` | Fleet Procurement | Acquisitions de la flotte |
| `BTI07` | Canadian Coast Guard College | Collège de la Garde côtière canadienne |
| `BTI08` | Marine Operations Economics | Économie liée aux opérations maritimes |
| `BTJ01` | Nuclear Fuel Cycle Program | Programme de cycle du combustible nucléaire |
| `BTJ02` | Nuclear Reactors Program | Programme des réacteurs nucléaires |
| `BTJ03` | Nuclear Substances and Prescribed Equipment Program | Programme des substances nucléaires et de l&#39;équipement réglementé |
| `BTJ04` | Nuclear Non-Proliferation Program | Programme de non prolifération nucléaire |
| `BTJ05` | Scientific, Regulatory and Public Information Program | Programme de renseignements scientifiques, réglementaires et publics |
| `BTK01` | Investing in Canada Phase 1 – Funding Allocations for Provinces and Territories | Phase 1 du plan Investir dans le Canada – Allocations de financement pour les provinces et les territoires |
| `BTK02` | Investing in Canada Phase 1 – Funding for Federation of Canadian Municipalities | Phase 1 du plan Investir dans le Canada – Financement de la Fédération canadienne des municipalités |
| `BTK03` | Investing in Canada Infrastructure Program | Programme d&#39;infrastructure du plan Investir dans le Canada |
| `BTK04` | Gas Tax Fund – Permanent Funding for Municipalities | Fonds de la taxe sur l&#39;essence – Financement permanent pour les municipalités |
| `BTK05` | New Building Canada Fund – National Infrastructure Component | Nouveau Fonds Chantiers Canada – volet Infrastructures nationales |
| `BTK06` | New Building Canada Fund – Funding Allocations for Provinces and Territories | Nouveau Fonds Chantiers Canada – Allocations de financement pour les provinces et les territoires |
| `BTK07` | Historical Programs | Programmes déjà en place |
| `BTK08` | New Champlain Bridge Corridor Project | Projet de corridor du nouveau pont Champlain |
| `BTK09` | Gordie Howe International Bridge Team | Projet du pont international Gordie-Howe |
| `BTK10` | Toronto Waterfront Revitalization Initiative | Initiative de revitalisation du secteur riverain de Toronto |
| `BTK11` | Smart Cities Challenge | Défi des villes intelligentes |
| `BTK12` | Disaster Mitigation and Adaption Fund | Fonds d&#39;atténuation et d&#39;adaptation en matière de catastrophes |
| `BTK13` | Research and Knowledge Initiative | Initiative de recherche et de connaissances |
| `BTL01` | Canadian Geodetic Survey: Spatially Enabling Canada | Levés géodésiques du Canada : Le Canada à référence spatiale |
| `BTL02` | Geological Knowledge for Canada&#39;s Onshore and Offshore Land | Connaissances géologiques des terres côtières et extracôtières du Canada |
| `BTL03` | Core Geospatial Data | Données géospatiales essentielles |
| `BTL04` | Canada-US International Boundary Treaty | Traité de la frontière internationale entre le Canada et les États-Unis |
| `BTL05` | Canada Lands Survey System | Système d&#39;arpentage des terres du Canada |
| `BTL06` | Geoscience for Sustainable Development of Natural Resources | Géoscience pour la valorisation durable des ressources naturelles |
| `BTL07` | Pest Risk Management | Gestion des risques liés aux ravageurs |
| `BTL08` | Forest Climate Change | Changements climatiques liés aux forêts |
| `BTL09` | Climate Change Adaptation | Adaptation aux changements climatiques |
| `BTL10` | Explosives Safety and Security | Sécurité et sûreté des explosifs |
| `BTL11` | Geoscience to Keep Canada Safe | Géoscience pour assurer la sécurité des Canadiens |
| `BTL12` | Wildfire Risk Management | Gestion du risque de feux de végétation |
| `BTL13` | Polar Continental Shelf Program | Programme du plateau continental polaire |
| `BTM01` | Clean Energy Technology Policy, Research and Engagement | Politique, recherche et mobilisation en matière de technologies énergétiques propres |
| `BTM02` | Clean Growth in Natural Resource Sectors | Croissance propre dans les secteurs des ressources naturelles |
| `BTM03` | Energy Innovation Program | Programme d&#39;innovation énergétique |
| `BTM04` | Green Mining Innovation | Innovation Mines vertes |
| `BTM05` | Fibre Solutions | Solutions axées sur les fibres |
| `BTM06` | Sustainable Forest Management | Aménagement forestier durable |
| `BTM07` | Cumulative Effects | Effets cumulatifs |
| `BTM08` | Lower Carbon Transportation | Transport faible en carbone |
| `BTM09` | Electricity Resources | Ressources en électricité |
| `BTM10` | Energy Efficiency | Efficacité énergétique |
| `BTM11` | Energy and Climate Change Policy | Politique en matière d&#39;énergie et de changements climatiques |
| `BTM12` | Innovative Geospatial Solutions | Solutions géospatiales novatrices |
| `BTM13` | Energy Innovation and Clean Technology (EICT) | Innovation énergétique et technologies propres (IETP) |
| `BTO01` | Forest Sector Competitiveness | Compétitivité du secteur forestier |
| `BTO02` | Provision of Federal Leadership in the Minerals and Metals Sector | Prestation d&#39;un leadership fédéral dans le secteur des minéraux et des métaux |
| `BTO03` | Energy Safety and Security, and Petroleum Resources | Sûreté et sécurité énergétique, et ressources pétrolières |
| `BTO04` | International Energy Engagement | Mobilisation au titre de l&#39;énergie à l&#39;échelle internationale |
| `BTO05` | Statutory Offshore Payments | Paiements législatifs pour les hydrocarbures extracôtiers |
| `BTO06` | Indigenous Partnerships Office | Bureau des partenariats avec les Autochtones |
| `BTO07` | Nòkwewashk | Nòkwewashk |
| `BTO08` | Youth Employment and Skills Strategy - Science and Technology Internship Program (Green Jobs) | La Stratégie emploi et compétences jeunesse - Programme de stages en sciences et technologie (Emplois verts) |
| `BTO09` | Indigenous Reconciliation and Regulatory Coordination | Réconciliation avec les peuples autochtones et coordination réglementaire |
| `BTR01` | Learning | Apprentissage |
| `BTS01` | Disclosure and Reprisal Management | Gestion des divulgations et des représailles |
| `BTT01` | Analysis and Outreach | Analyse et liaison |
| `BTT02` | Dispute Resolution | Règlement des différends |
| `BTT03` | Determinations and Compliance | Déterminations et conformité |
| `BTW01` | Aviation Safety Regulatory Framework | Cadre réglementaire de la sécurité aérienne |
| `BTW02` | Aviation Safety Oversight | Surveillance de la sécurité aérienne |
| `BTW03` | Aviation Safety Certification | Certification de la sécurité aérienne |
| `BTW04` | Aviation Security Regulatory Framework | Cadre réglementaire de la sûreté aérienne |
| `BTW05` | Aviation Security Oversight | Surveillance de la sûreté aérienne |
| `BTW06` | Aircraft Services | Services aériens |
| `BTW07` | Marine Safety Regulatory Framework | Cadre réglementaire de la sécurité maritime |
| `BTW08` | Marine Safety Oversight | Surveillance de la sécurité maritime |
| `BTW09` | Marine Safety Certification | Certification de la sécurité maritime |
| `BTW10` | Marine Security Regulatory Framework | Cadre réglementaire de la sûreté maritime |
| `BTW11` | Marine Security Oversight | Surveillance de la sûreté maritime |
| `BTW12` | Navigation Protection Program | Programme de protection de la navigation |
| `BTW13` | Rail Safety Regulatory Framework | Cadre réglementaire de la sécurité ferroviaire |
| `BTW14` | Rail Safety Oversight | Surveillance de la sécurité ferroviaire |
| `BTW15` | Rail Safety Improvement Program | Programme d&#39;amélioration de la sécurité ferroviaire |
| `BTW16` | Multi-Modal and Road Safety Regulatory Framework | Cadre réglementaire du transport multimodal et de la sécurité de l&#39;automobile |
| `BTW17` | Multi-Modal and Road Safety Oversight | Surveillance du transport multimodal et de la sécurité de l&#39;automobile |
| `BTW18` | Intermodal Surface Security Regulatory Framework | Cadre réglementaire de la sûreté intermodale du transport terrestre |
| `BTW19` | Intermodal Surface Security Oversight | Surveillance de la sûreté intermodale du transport terrestre |
| `BTW20` | Transportation of Dangerous Goods Regulatory Framework | Cadre réglementaire pour le transport des marchandises dangereuses |
| `BTW21` | Transportation of Dangerous Goods Oversight | Surveillance du transport des marchandises dangereuses |
| `BTW22` | Transportation of Dangerous Goods Technical Support | Soutien technique du transport des marchandises dangereuses |
| `BTW23` | Multimodal Safety &amp; Security Services | Services de la sécurité et la sûreté multimodales |
| `BTW24` | Security Screening Certification | Programmes de filtrage de sûreté |
| `BTW25` | Emergency Management | Gestion des urgences |
| `BTX01` | Climate Change and Clean Air | Changement climatique et qualité de l&#39;air |
| `BTX02` | Protecting Oceans and Waterways | Protéger les océans et les voies navigables |
| `BTX03` | Environmental Stewardship of Transportation | Gérance environnementale des transports |
| `BTX04` | Transportation Innovation | Innovation dans le secteur des transports |
| `BTX05` | Indigenous Partnerships and Engagement | Partenariats avec les Autochtones et mobilisation |
| `BTX06` | Navigation Protection Program | Programme de protection de la navigation |
| `BTY01` | Transportation Marketplace Frameworks | Cadres qui appuient le marché des transports |
| `BTY02` | Transportation Analysis | Analyse du secteur des transports |
| `BTY03` | Transportation Infrastructure | Infrastructure de transport |
| `BTY04` | National Trade Corridors | Corridors commerciaux nationaux |
| `BUA01` | Conditional Release Decisions | Décisions relatives à la mise en liberté sous condition |
| `BUB01` | Conditional Release Openness and Accountability | Application transparente et responsable du processus de mise en liberté sous condition |
| `BUC01` | Record Suspension Decisions/Clemency Recommendations | Décisions relatives à la suspension du casier et recommandations concernant la clémence |
| `BUE01` | Reviews | Examens |
| `BUF01` | Targeting | Ciblage |
| `BUF02` | Intelligence Collection and Analysis | Collecte et analyse du renseignement |
| `BUF03` | Security Screening | Filtrage de sécurité |
| `BUF04` | Traveller Facilitation and Compliance | Facilitation de la circulation et conformité des voyageurs |
| `BUF05` | Commercial Facilitation and Compliance | Facilitation et conformité des opérations commerciales |
| `BUF06` | Anti-Dumping and Countervailing | Antidumping et compensation |
| `BUF07` | Trusted Traveller | Voyageurs fiables |
| `BUF08` | Trusted Trader | Négociants fiables |
| `BUF09` | Recourse | Recours |
| `BUF10` | Force Generation | Constitution des forces |
| `BUF11` | Buildings and Equipment | Immeubles et d&#39;équipements |
| `BUF12` | Field Technology Support | Support technologique |
| `BUF13` | Trade Facilitation and Compliance | Facilitation et conformité des échanges commerciaux |
| `BUG01` | Immigration Investigations | Enquêtes en matière d&#39;immigration |
| `BUG02` | Detentions | Détentions |
| `BUG03` | Hearings | Audiences |
| `BUG04` | Removals | Renvois |
| `BUG05` | Criminal Investigations | Enquêtes criminelles |
| `BUH01` | Setting Rules for Plant Health | Établissement des règles pour la protection des végétaux |
| `BUH02` | Plant Health Compliance Promotion | Promotion de la conformité en matière de protection des végétaux |
| `BUH03` | Monitoring and Enforcement for Plant Health | Surveillance et application de la loi en matière de protection des végétaux |
| `BUH04` | Permissions for Plant Products | Autorisations pour les produits d&#39;origine végétale |
| `BUH05` | Setting Rules for Animal Health | Établissement des règles pour la santé animale |
| `BUH06` | Animal Health Compliance Promotion | Promotion de la conformité en matière de santé animale |
| `BUH07` | Monitoring and Enforcement for Animal Health | Surveillance et application de la loi en matière de santé animale |
| `BUH08` | Permissions for Animal Products | Autorisations pour les produits d&#39;origine animale |
| `BUH09` | Setting Rules for Food Safety and Consumer Protection | Établissement de règles pour la salubrité des aliments et la protection des consommateurs |
| `BUH10` | Food Safety and Consumer Protection Compliance Promotion | Promotion de la conformité en matière de salubrité des aliments et de protection des consommateurs |
| `BUH11` | Monitoring and Enforcement for Food Safety and Consumer Protection | Surveillance et application de la loi en matière de salubrité des aliments et de protection des consommateurs |
| `BUH12` | Permissions for Food Products | Autorisations pour les produits alimentaires |
| `BUH13` | International Standards Setting | Définition de normes internationales |
| `BUH14` | International Regulatory Cooperation and Science Collaboration | Coopération internationale en matière de réglementation et collaboration scientifique |
| `BUH15` | Market Access Support | Soutien à l&#39;accès aux marchés |
| `BUI01` | Investigator-Initiated Research | Recherche libre |
| `BUI02` | Training and Career Support | Formation et soutien professionnel |
| `BUI03` | Research in Priority Areas | Recherche priorisée |
| `BUJ01` | Institutional Management and Support | Gestion et soutien en établissement |
| `BUJ02` | Supervision | Surveillance |
| `BUJ03` | Drug Enforcement | Lutte antidrogue |
| `BUJ04` | Clinical Services and Public Health | Services cliniques et de santé publique |
| `BUJ05` | Mental Health Services | Services de santé mentale |
| `BUJ06` | Food Services | Services d&#39;alimentation |
| `BUJ07` | Accommodation Services | Services de logement |
| `BUJ08` | Preventive Security and Intelligence | Sécurité préventive et renseignement |
| `BUK01` | Offender Case Management | Gestion des cas des délinquants |
| `BUK02` | Community Engagement | Engagement des collectivités |
| `BUK03` | Chaplaincy Services | Services d&#39;aumônerie |
| `BUK04` | Elder Services | Services d&#39;aînés |
| `BUK05` | Correctional Program Readiness | Préparation aux programmes correctionnels |
| `BUK06` | Correctional Programs | Programmes correctionnels |
| `BUK07` | Correctional Program Maintenance | Programme de maintien des acquis |
| `BUK08` | Offender Education | Éducation des délinquants |
| `BUK09` | CORCAN Employment and Employability | CORCAN – Emploi et employabilité |
| `BUK10` | Social Program | Programme social |
| `BUK11` | Correctional Programs | Programmes correctionnels |
| `BUL01` | Community Management and Security | Sécurité et gestion dans la collectivité |
| `BUL02` | Community-Based Residential Facilities | Établissements résidentiels communautaires |
| `BUL03` | Community Correctional Centres | Centres correctionnels communautaires |
| `BUL04` | Community Health Services | Services de santé dans la collectivité |
| `BUM01` | Foreign Signals Intelligence | Renseignement électromagnétique étranger |
| `BUM02` | Cyber Security and Information Assurance | Cybersécurité et assurance de l&#39;information |
| `BUM03` | Foreign Cyber Operations | Cyber opérations étrangères |
| `BUM04` | Operations Enablement | Soutien aux opérations |
| `BUN01` | Operations in Canada | Opérations au Canada |
| `BUN02` | Operations in North America | Opérations en Amérique du Nord |
| `BUN03` | International Operations | Opérations internationales |
| `BUN04` | Global Engagement | Engagement mondial |
| `BUN05` | Cyber Operations | Cyberopérations |
| `BUN06` | Command, Control and Sustainment of Operations | Commandement, contrôle et poursuite prolongée des opérations |
| `BUN07` | Special Operations | Opérations spéciales |
| `BUO01` | Strategic Command and Control | Commandement et contrôle stratégiques |
| `BUO02` | Ready Naval Forces | Forces navales prêtes au combat |
| `BUO03` | Ready Land Forces | Forces terrestres prêtes au combat |
| `BUO04` | Ready Air and Space Forces | Forces aériennes et spatiales prêtes au combat |
| `BUO05` | Ready Special Operations Forces | Forces d&#39;opérations spéciales prêtes au combat |
| `BUO06` | Ready Cyber and Joint Communication Information Systems (CIS) Forces | Cyberforces et systèmes de communication et d&#39;information (SCI) interarmées prêts au combat |
| `BUO07` | Ready Intelligence Forces | Forces du renseignement prêtes au combat |
| `BUO08` | Ready Joint and Combined Forces | Forces interarmées et multinationales prêtes au combat |
| `BUO09` | Ready Health, Military Police and Support Forces | Soins de santé, police militaire et forces de soutien prêts à l&#39;action |
| `BUO10` | Equipment Support | Soutien de l&#39;équipement |
| `BUO11` | Canadian Forces Liaison Council and Employer Support | Conseil de liaison des Forces canadiennes et appui des employeurs |
| `BUP01` | Recruitment | Recrutement |
| `BUP02` | Individual Training and Professional Military Education | Instruction individuelle et formation professionnelle militaire |
| `BUP03` | Total Health Care | Gamme complète des soins de santé |
| `BUP04` | Defence Team Management | Gestion de l&#39;Équipe de la Défense |
| `BUP05` | Military Transition | Transition de la vie militaire à la vie civile |
| `BUP06` | Military Member and Family Support | Soutien fourni au militaire et à sa famille |
| `BUP07` | Military History and Heritage | Histoire et patrimoine militaires |
| `BUP08` | Military Law Services/Military Justice Superintendence | Services du droit militaire/Exercice de l&#39;autorité de justice militaire |
| `BUP09` | Ombudsman | Ombudsman |
| `BUP10` | Cadets and Junior Canadian Rangers (Youth Program) | Cadets et Rangers juniors canadiens (Programme jeunesse) |
| `BUQ01` | Joint Force Development | Développement des forces interarmées |
| `BUQ02` | Naval Force Development | Développement de la force navale |
| `BUQ03` | Land Force Development | Développement de la force terrestre |
| `BUQ04` | Air and Space Force Development | Développement de la force aérienne et spatiale |
| `BUQ05` | Special Operations Force Development | Développement des forces d&#39;opérations spéciales |
| `BUQ06` | Cyber and Joint Communication Information Systems (CIS) Force Development | Développement de la cyberforce et de la force du systèmes d&#39;information et communications (SIC) interarmées |
| `BUQ07` | Intelligence Force Development | Développement de la force du renseignement |
| `BUQ08` | Science, Technology and Innovation | Sciences, technologie et innovation |
| `BUR01` | Maritime Equipment Acquisition | Acquisition d&#39;équipements maritimes |
| `BUR02` | Land Equipment Acquisition | Acquisition d&#39;équipements terrestres |
| `BUR03` | Aerospace Equipment Acquisition | Acquisition d&#39;équipements aérospatiaux |
| `BUR04` | Defence Information Technology Systems Acquisition, Design and Delivery | Acquisition, conception et livraison de systèmes de technologie de l&#39;information de la Défense |
| `BUR05` | Defence Materiel Management | Gestion du matériel de la Défense |
| `BUS01` | Defence Infrastructure Program Management | Gestion du Programme d&#39;infrastructure de la Défense |
| `BUS02` | Defence Infrastructure Construction, Recapitalization and Investment | Infrastructure de la Défense : construction, réfection et investissement |
| `BUS03` | Defence Infrastructure Maintenance, Support and Operations | Infrastructure de la Défense : entretien, soutien et opérations |
| `BUS04` | Defence Residential Housing | Logements résidentiels de la Défense |
| `BUS05` | Defence Information Systems, Services and Programme Management | Gestion des programmes, systèmes et services d&#39;information de la Défense |
| `BUS06` | Environment and Sustainable Management | Environnement et gestion durable |
| `BUS07` | Indigenous Affairs | Affaires autochtones |
| `BUS08` | Naval Bases | Bases navales |
| `BUS09` | Land Bases | Bases terrestres |
| `BUS10` | Air and Space Wings | Escadres aérospatiales |
| `BUS11` | Joint, Common and International Bases | Bases interarmées, communes et internationales |
| `BUS12` | Military Police Institutional Operations | Opérations institutionnelles de la Police militaire |
| `BUS13` | Safety | Sécurité |
| `BUT01` | Supervision and Enforcement | Surveillance et mise en application |
| `BUT02` | Research, Policy and Education | Recherche, politique et éducation |
| `BUU01` | Financial Literacy | Littératie financière |
| `BUV01` | Tax Policy and Legislation | Politique et législation fiscales |
| `BUV02` | Economic and Fiscal Policy, Planning and Forecasting | Politiques économique et budgétaire, planification et prévisions |
| `BUV03` | Economic Development Policy | Politique de développement économique |
| `BUV04` | Federal-Provincial Relations and Social Policy | Relations fédérales-provinciales et politique sociale |
| `BUV05` | Financial Sector Policy | Politique du secteur financier |
| `BUV06` | International Trade and Finance Policy | Politique des finances et échanges internationaux |
| `BUV07` | Canada Health Transfer | Transfert canadien en matière de santé |
| `BUV08` | Fiscal Arrangements with Provinces and Territories | Arrangements fiscaux avec les provinces et les territoires |
| `BUV09` | Tax Collection and Administration Agreements | Accords de perception fiscale et d&#39;administration fiscale |
| `BUV10` | Commitments to International Financial Organizations | Engagements envers les organisations financières internationales |
| `BUV11` | Market Debt and Foreign Reserves Management | Dette contractée sur les marchés et gestion des réserves de change |
| `BUW01` | Compliance Program | Programme de conformité |
| `BUW02` | Strategic Policy and Reviews | Politique stratégique et examens |
| `BUX01` | Financial Intelligence Program | Programme du renseignement financier |
| `BUX02` | Strategic Intelligence, Research and Analytics | Renseignements stratégiques, recherche et analyse |
| `BUZ01` | Independent review of military grievances | Examen indépendant des griefs militaires |
| `BVA01` | Registry of Lobbyists | Registre des lobbyistes |
| `BVA02` | Outreach and Education | Sensibilisation et éducation |
| `BVA03` | Compliance and Enforcement | Conformité et exécution |
| `BVA04` | Registration, education and compliance | Enregistrement, éducation et conformité |
| `BVB01` | International Policy Coordination | Coordination des politiques internationales |
| `BVB02` | Trade, Investment and International Economic Policy | Politique sur le commerce, l&#39;investissement et l&#39;économie internationale |
| `BVB03` | Multilateral Policy | Politiques multilatérales |
| `BVB04` | International Law | Droit international |
| `BVB05` | The Office of Protocol | Le Bureau du Protocole |
| `BVB06` | Europe, Arctic, Middle East and Maghreb Policy &amp; Diplomacy | Politique et diplomatie en Europe, dans l&#39;Arctique, au Moyen-Orient et au Maghreb |
| `BVB07` | Americas Policy &amp; Diplomacy | Politique et diplomatie pour les Amériques |
| `BVB08` | Asia Pacific Policy &amp; Diplomacy | Politique et diplomatie en Asie-Pacifique |
| `BVB09` | Sub-Saharan Africa Policy &amp; Diplomacy | Politique et diplomatie en Afrique subsaharienne |
| `BVB10` | Geographic Coordination and Mission Support | Coordination géographique et appui aux missions |
| `BVB11` | Gender Equality and the Empowerment of Women and Girls | L&#39;égalité des genres et le renforcement du pouvoir des femmes et des filles |
| `BVB12` | Humanitarian Action | Action humanitaire |
| `BVB13` | Human Development: Health &amp; Education | Développement de la personne: Santé et éducation  |
| `BVB14` | Growth that works for everyone | Une croissance au service de tous |
| `BVB15` | Environment and Climate Action | Environnement et l&#39;action pour le climat |
| `BVB16` | Human Rights, Governance, Democracy &amp; Inclusion | Droits de la personne, gouvernance, démocratie et inclusion |
| `BVB17` | Peace and Security Policy | Politique liée à la Paix et sécurité |
| `BVB18` | Inclusive Governance | Gouvernance inclusive |
| `BVB19` | International Security Policy and Diplomacy | Politique de sécurité internationale et diplomatie |
| `BVB20` | International Assistance Policy | Politique d&#39;aide internationale |
| `BVC01` | Trade Policy, Agreements, Negotiations and Disputes | Politiques et négociations commerciales, accords et différends |
| `BVC02` | Trade Controls | Réglementation commerciale |
| `BVC03` | International Business Development | Développement du commerce international |
| `BVC04` | International Innovation and Investment | Innovation et investissement international |
| `BVC05` | Europe, Arctic, Middle East and Maghreb Trade | Commerce en Europe, dans l&#39;Arctique, au Moyen-Orient et au Maghreb |
| `BVC06` | Americas Trade | Commerce dans les Amériques |
| `BVC07` | Asia Pacific Trade | Commerce en Asie-Pacifique |
| `BVC08` | Sub-Saharan Africa Trade | Commerce en Afrique subsaharienne |
| `BVD01` | International Assistance Operations | Opérations d&#39;aide internationale |
| `BVD02` | Humanitarian Assistance | Aide humanitaire |
| `BVD03` | Partnerships for Development Innovation | Partenariats pour innovation dans le développement |
| `BVD04` | Multilateral International Assistance | Aide internationale multilatérale |
| `BVD05` | Peace and Stabilization Operations | Stabilisation et opérations de paix |
| `BVD06` | Anti-Crime and Counter-Terrorism Capacity Building | Programmes visant à renforcer les capacités de lutte contre la criminalité et le terrorisme |
| `BVD07` | Weapons Threat Reduction | Réduction des menaces d&#39;armes |
| `BVD08` | Canada Fund for Local Initiatives | Fonds canadien d&#39;initiatives locales |
| `BVD09` | Europe, Arctic, Middle East and Maghreb International Assistance | Aide internationale en Europe, dans l&#39;Arctique, au Moyen-Orient et au Maghreb |
| `BVD10` | Americas International Assistance | Aide internationale dans les Amériques |
| `BVD11` | Asia Pacific International Assistance | Aide internationale en Asie-Pacifique |
| `BVD12` | Sub-Saharan Africa International Assistance | Aide internationale en Afrique subsaharienne |
| `BVD13` | Grants and Contributions Policy and Operations | Politiques et opérations concernant les subventions et les contributions |
| `BVD14` | Office of Human Rights, Freedom and Inclusion (OHRFI) Programming | Programmation du Bureau des droits de la personne, des libertés et de l&#39;inclusion (BDPLI) |
| `BVE01` | Consular Assistance and Services for Canadians Abroad | Aide consulaire et les services aux Canadiens à l&#39;étranger |
| `BVE02` | Emergency Preparedness and Response | Préparation et intervention en cas d&#39;urgence |
| `BVF01` | Platform Corporate Services | Services ministériels au niveau de la plateforme |
| `BVF02` | Foreign Service Directives | Directives sur le service extérieur |
| `BVF03` | Client Relations and Mission Operations | Relations avec les clients et opérations des missions |
| `BVF04` | Locally Engaged Staff Services | Services aux employés recrutés sur place |
| `BVF05` | Real Property Planning and Stewardship | Planification et intendance des biens immobiliers |
| `BVF06` | Real Property Project Delivery, Professional and Technical Services | Services professionnels et techniques pour l&#39;exécution des projets de biens immobiliers |
| `BVF07` | Mission Readiness and Security | Préparation et sécurité de la mission |
| `BVF08` | Mission Network IM/IT | Gestion de l&#39;information et technologie de l&#39;information du réseau des missions |
| `BVG01` | Health Care Systems Analysis and Policy | Analyse et politique des systèmes de soins de santé |
| `BVG02` | Access, Affordability, and Appropriate Use of Drugs and Medical Devices | Accessibilité, abordabilité et usage approprié des médicaments et des instruments médicaux |
| `BVG03` | Home, Community and Palliative Care | Soins à domicile, en milieu communautaire et palliatifs |
| `BVG04` | Mental Health | Santé Mentale |
| `BVG05` | Substance Use and Addictions | Dépendances et usage de substances |
| `BVG06` | Digital Health | Santé numérique |
| `BVG07` | Health Information | Information sur la Santé |
| `BVG08` | Canada Health Act | Loi canadienne sur la santé |
| `BVG09` | Medical Assistance in Dying | Aide médicale à mourir |
| `BVG10` | Cancer Control | Lutte contre le cancer |
| `BVG11` | Patient Safety | Sécurité des patients |
| `BVG12` | Organs, Tissues and Blood | Organes, tissus et sang |
| `BVG13` | Promoting Minority Official Languages in the Health Care Systems | Promotion des langues officielles des minorités dans le système de santé |
| `BVG14` | Brain Research | Recherche sur le cerveau |
| `BVG15` | Thalidomide | Thalidomide |
| `BVG16` | Territorial Health Investment Fund | Fonds d&#39;investissement-santé pour les territoires |
| `BVG21` | Responsive Health Care Systems | Systèmes de soins de santé adaptés |
| `BVG22` | Healthy People and Communities | Personnes et communautés en santé |
| `BVG23` | Quality Health Science, Data and Evidence | Science, données et preuves de qualité sur la santé |
| `BVH01` | Pharmaceutical Drugs | Produits pharmaceutiques |
| `BVH02` | Biologic and Radiopharmaceutical Drugs | Médicaments biologiques et radiopharmaceutiques |
| `BVH03` | Medical Devices | Matériels médicaux |
| `BVH04` | Natural Health Products | Produits de santé naturels |
| `BVH05` | Food &amp; Nutrition | Aliments et nutrition |
| `BVH06` | Air Quality | Qualité de l&#39;air |
| `BVH07` | Climate Change | Changements climatiques |
| `BVH08` | Water Quality | Qualité de l&#39;eau |
| `BVH09` | Health Impacts of Chemicals | Incidence des produits chimiques sur la santé |
| `BVH10` | Consumer Product Safety | Sécurité des produits de consommation |
| `BVH11` | Workplace Hazardous Products | Matières dangereuses utilisées au travail |
| `BVH12` | Tobacco Control | Lutte antitabac (y compris le vapotage) |
| `BVH13` | Controlled Substances | Substances contrôlées |
| `BVH14` | Cannabis | Cannabis |
| `BVH15` | Radiation Protection | Radioprotection |
| `BVH16` | Pesticides | Pesticides |
| `BVH17` | Health Canada Specialized Services | Services spécialisés de Santé Canada |
| `BVJ01` | Complaints Resolution | Règlement des plaintes |
| `BVK01` | The Communications Security Establishment Commissioner&#39;s Review Program | Programme d&#39;examen du commissaire du Centre de la sécurité des télécommunications |
| `BVL01` | Ombuds for federally sentenced individuals | Ombuds pour les personnes purgeant une peine de ressort fédérale |
| `BVM01` | Patented Medicine Price Regulation Program | Le programme de réglementation du prix des médicaments brevetés |
| `BVM02` | Pharmaceutical Trends Program | Le programme sur les tendances relatives aux produits pharmaceutiques |
| `BVN01` | Risk Assessment and Intervention – Federally Regulated Financial Institutions | Évaluation des risques et prise de mesures – Institutions financières fédérales |
| `BVN02` | Regulation and Guidance of Federally Regulated Financial Institutions | Réglementation et établissement de consigne à l&#39;intention des Institutions financières fédérales |
| `BVN03` | Regulatory Approvals and Legislative Precedents | Approbations réglementaires et précédents législatifs |
| `BVN04` | Federally Regulated Private Pension Plans | Régimes de retraite privés fédéraux |
| `BVO01` | Actuarial Valuation and Advice | Évaluation actuarielle et conseils |
| `BVP01` | Health Promotion | Promotion de la santé |
| `BVP02` | Chronic Disease Prevention | Prévention des maladies chroniques |
| `BVP03` | Evidence for Health Promotion, and Chronic Disease and Injury Prevention | Données probantes liées à la promotion de la santé et à la prévention des maladies chroniques et des blessures |
| `BVQ01` | Laboratory Science Leadership and Services | Services et leadership en matière de science en laboratoire |
| `BVQ02` | Communicable Disease and Infection Control | Contrôle des maladies transmissibles et des infections |
| `BVQ03` | Vaccination | Vaccination |
| `BVQ04` | Foodborne and Zoonotic Diseases | Maladies zoonotiques et d&#39;origine alimentaire |
| `BVR01` | Emergency Preparedness and Response | Préparation et intervention en cas d&#39;urgence |
| `BVR02` | Biosecurity | Biosécurité |
| `BVR03` | Border and Travel Health | Santé des voyageurs et santé transfrontalière |
| `BVS01` | National Security Leadership | Leadership en matière de sécurité nationale |
| `BVS02` | Critical Infrastructure | Infrastructures essentielles |
| `BVS03` | Cyber Security | Cybersécurité |
| `BVT01` | Crime Prevention | Prévention du crime |
| `BVT02` | Law Enforcement and Policing | Application de la loi et police |
| `BVT03` | Serious and Organized Crime | Crime organisé et crimes graves |
| `BVT04` | Border Policy | Politique frontalière |
| `BVT05` | Indigenous Policing | Services de police autochtones |
| `BVT06` | Corrections | Services correctionnels |
| `BVU01` | Emergency Prevention/Mitigation | Prévention et atténuation des urgences |
| `BVU02` | Emergency Preparedness | Préparation aux urgences |
| `BVU03` | Emergency Response/Recovery | Intervention d&#39;urgence et rétablissement |
| `BVV01` | Procurement Leadership | Leadership en matière d&#39;approvisionnement |
| `BVV02` | Procurement Services | Services d&#39;approvisionnement |
| `BVV03` | Procurement Program | Programme des approvisionnements |
| `BVW01` | Federal Pay Administration | Administration de la paye fédérale |
| `BVW02` | Federal pension Administration | Administration de la pension fédérale |
| `BVW03` | Payments Instead of Property Taxes to Local Governments | Paiements en remplacement d&#39;impôts aux administrations locales |
| `BVW04` | Payments and Revenue Collection | Paiements et perception des recettes |
| `BVW05` | Government-Wide Accounting and Reporting | Comptabilité et production de rapports à l&#39;échelle du gouvernement |
| `BVW06` | Cape Breton Operations (CBO) – HR Legacy Benefits | Opérations du Cap-Breton (OCB) – Avantages des legs en matière de RH |
| `BVX01` | Federal Accommodation and Infrastructure | Locaux fédéraux et Infrastructure |
| `BVX02` | Real Property Services | Services immobiliers |
| `BVX03` | Parliament Hill and Surroundings | Colline du Parlement et ses environs |
| `BVX04` | Cape Breton Operations (CBO) – Portfolio Management | Opérations du Cap-Breton (OCB) – Gestion du portefeuille |
| `BVY01` | Linguistic services | Services linguistiques |
| `BVY02` | Communication Services | Services de communication |
| `BVY03` | Government-wide Corporate Services | Services organisationnels pangouvernementaux |
| `BVY04` | Document Imaging Services | Services d&#39;imagerie documentaire |
| `BVY05` | Asset Disposal | Aliénation des biens |
| `BVY06` | Service Management | Gestion des services |
| `BVY07` | Canadian General Standards Board | Office des normes générales du Canada |
| `BVY08` | Security and Oversight Services | Services de sécurité et de surveillance |
| `BVZ01` | Procurement Ombudsman | Ombudsman de l&#39;approvisionnement |
| `BWA01` | Aviation occurrence investigations | Enquêtes d&#39;événements aéronautiques |
| `BWA02` | Marine occurrence investigations | Enquêtes d&#39;événements maritimes |
| `BWA03` | Rail Occurrence Investigations | Enquêtes d&#39;événements ferroviaires |
| `BWA04` | Pipeline occurrence investigations | Enquêtes d&#39;événements de pipeline |
| `BWB01` | Policy Direction and Support | Soutien et orientation en matière de politiques |
| `BWB02` | Recruitment and Assessment Services | Services de recrutement et d&#39;évaluation |
| `BWB03` | Oversight and Monitoring | Surveillance |
| `BWC01` | Email Services | Services liés au courriel |
| `BWC02` | Hardware Provisioning | Achat de matériel |
| `BWC03` | Software Provisioning | Achat de logiciels |
| `BWC04` | Workplace Technology Services | Services de technologie en milieu de travail |
| `BWC05` | Digital Communications | Communications numériques |
| `BWC06` | Workplace Technologies | Technologies en milieu de travail |
| `BWD01` | Bulk Print | Impression en bloc |
| `BWD02` | File and Print | Fichiers et impression |
| `BWD03` | Middleware &amp; Database | Intergiciels et bases de données |
| `BWD04` | Data Centre Facility | Installations des centres de données |
| `BWD05` | High Performance  Computing Solution | Solution informatique de haute performance |
| `BWD06` | Mid-Range | Milieu de gamme |
| `BWD07` | Mainframe | Ordinateur central |
| `BWD08` | Storage | Entreposage |
| `BWD09` | Cloud | Infonuagique |
| `BWD10` | Data Centre Information Technology Operations | Opérations en technologies de l&#39;information des centres de données |
| `BWE01` | Local Area Network | Réseau local |
| `BWE02` | Wide Area Network | Réseau étendu |
| `BWE03` | Internet | Internet |
| `BWE04` | Satellite | Services satellites |
| `BWE05` | Mobile Devices and Fixed-Line Phones | Appareils mobiles et téléphones fixes |
| `BWE06` | Conferencing Services | Services de conférence |
| `BWE07` | Contact Centre Infrastructure | Infrastructure du centre de contact |
| `BWE08` | Toll-Free Voice | Services de voix sans frais |
| `BWE09` | Telecommunications | Télécommunications |
| `BWE10` | Networks | Réseaux |
| `BWF01` | Identity and Access Management | Identité et gestion de l&#39;accès |
| `BWF02` | Secret Infrastructure | Infrastructure secrète |
| `BWF03` | Infrastructure Security | Sécurité de l&#39;infrastructure |
| `BWF04` | Cyber Security Strategic Planning | Planification stratégique de la cybersécurité |
| `BWF05` | Security Management and Governance | Gestion et gouvernance de la sécurité |
| `BWF06` | Secure Remote Access | Accès à distance protégé |
| `BWF07` | Security | Sécurité |
| `BWG01` | Strategic Direction | Orientation stratégique |
| `BWG02` | Service Management | Gestion des services |
| `BWG03` | Customer Relationships | Relations avec les clients |
| `BWG04` | Enterprise Services Design and Delivery | Conception et prestation des services d&#39;entreprise |
| `BWH01` | Expertise and Outreach | Expertise et information |
| `BWH02` | Community Action and Innovation | Action communautaire et innovation |
| `BWI01` | Disability Pension Benefits and Allowances | Avantages et allocations pour pensions d&#39;invalidité |
| `BWI02` | Disability Awards, Critical Injury and Death Benefits | Indemnités d&#39;invalidité, avantages pour blessure grave et de décès |
| `BWI03` | Earnings Loss Benefit | Allocation pour perte de revenus |
| `BWI04` | Career Impact Allowance | Allocation pour incidence sur la carrière |
| `BWI05` | Retirement Benefits | Prestations de retraite |
| `BWI06` | Health Care Benefits | Avantages pour soins de santé |
| `BWI07` | Transition Services | Services de transition |
| `BWI08` | Long Term Care | Soins de longue durée |
| `BWI09` | Veterans Independence Program | Programme pour l&#39;autonomie des anciens combattants |
| `BWI10` | Caregiver Recognition Benefit | Allocation de reconnaissance des aidants naturels |
| `BWI11` | War Veterans Allowance | Allocation aux anciens combattants |
| `BWI12` | Income Support | Soutien du revenu |
| `BWI13` | Veterans Emergency Fund | Fonds d&#39;urgence pour les vétérans |
| `BWI14` | Centre of Excellence on Post Traumatic Stress Disorder and Related Mental Health Conditions | Centre d&#39;excellence sur le trouble de stress post-traumatique et les états de santé mentale connexes |
| `BWI15` | Veteran and Family Well Being Fund | Fonds pour le bien être des vétérans et de leur famille |
| `BWI16` | Disability Benefits | Prestations d&#39;invalidité |
| `BWI17` | Research Funding | Financement de la recherche |
| `BWI18` | Research and Innovation | Recherche et innovation |
| `BWJ01` | Canada Remembers Program | Programme Le Canada se souvient |
| `BWJ02` | Funeral and Burial Program | Programme de funérailles et d&#39;inhumation |
| `BWK01` | Veterans Ombudsperson | Ombudsman des vétérans |
| `BWL01` | Review and Appeal | Révision et appel |
| `BWM01` | Statutory, Legislative and Policy Support to First Nations Governance | Soutien statutaire, législatif et politique à la gouvernance autochtone |
| `BWM02` | Negotiations of Claims and Self-Government Agreements | Négociation des accords en matière de revendications et d&#39;autonomie gouvernementale |
| `BWM03` | Specific Claims | Revendications particulières |
| `BWM04` | Management and Implementation of Agreements and Treaties | Gestion et mise en oeuvre des accords et traités |
| `BWM05` | Consultation and Accommodation | Consultation et accommodement |
| `BWM06` | Consultation and Policy Development | Consultation et élaboration de politiques |
| `BWM07` | Federal Interlocutor&#39;s Contribution Program | Programme de contribution de l&#39;Interlocuteur fédéral |
| `BWM08` | Basic Organizational Capacity | Capacité organisationnelle de base |
| `BWM09` | Other Claims | Autres revendications |
| `BWM10` | First Nation Jurisdiction over Land and Fiscal Management | Juridiction des Premières Nations en matière de terre et de gestion fiscale |
| `BWM11` | Northern and Arctic Governance and Partnerships | Gouvernance et partenariats dans le Nord et l&#39;Arctique |
| `BWM12` | Individual Affairs | Affaires individuelles |
| `BWM13` | Indian Residential Schools Settlement Agreement | Convention de règlement relative aux pensionnats indiens |
| `BWM14` | Residential Schools Legacy | Séquelles des pensionnats |
| `BWM15` | Indigenous Engagement and Capacity Support | Mobilisation et soutien de la capacité des Autochtones |
| `BWM16` | Indigenous-led Services | Services dirigés par les Autochtones |
| `BWN01` | Trade and Market Expansion | Croissance du commerce et des marchés |
| `BWN02` | Sector Engagement and Development | Mobilisation et développement du secteur |
| `BWN03` | Farm Products Council of Canada | Conseil des produits agricoles du Canada |
| `BWN04` | Supply Management Initiatives | Initiatives de gestion de l&#39;offre |
| `BWN05` | Canadian Pari-Mutuel Agency | Agence canadienne du pari mutuel |
| `BWN06` | Water Infrastructure | Infrastructure hydraulique |
| `BWN07` | Federal, Provincial and Territorial Cost-shared Markets and Trade | Programmes à frais partagés fédéral, provinciaux et territoriaux reliés aux marchés et au commerce |
| `BWN08` | Community Pastures | Pâturages communautaires |
| `BWN09` | Food Policy Initiatives | Initiatives relatives à la politique alimentaire |
| `BWN10` | Water Infrastructure Divesture | Cession des infrastructures hydrauliques |
| `BWO01` | Foundational Science and Research | Science et recherche fondamentales |
| `BWO02` | AgriScience | Agri-science |
| `BWO03` | AgriInnovate | Agri-innover |
| `BWO04` | Environment and Climate Change Programs | Programmes en matière d&#39;environnement et de changements climatiques |
| `BWO05` | Canadian Agricultural Strategic Priorities Program | Programme canadien des priorités stratégiques de l&#39;agriculture |
| `BWO06` | Federal, Provincial and Territorial Cost-shared Science, Research, Innovation and Environment | Programmes à frais partagés fédéral, provinciaux et territoriaux reliés à la science, à la recherche, à l&#39;innovation et à l&#39;environnement |
| `BWP01` | AgriStability | Agri-stabilité |
| `BWP02` | AgriInvest | Agri-investissement |
| `BWP03` | AgriRecovery | Agri-relance |
| `BWP04` | AgriInsurance | Agri-protection |
| `BWP05` | AgriRisk | Agri-risques |
| `BWP06` | Loan Guarantee Programs | Programmes de garantie de prêts |
| `BWP07` | Farm Debt Mediation Service | Service de médiation en matière d&#39;endettement agricole |
| `BWP08` | Pest Management | Lutte antiparasitaire |
| `BWP09` | Assurance Program | Programme d&#39;assurance |
| `BWP10` | Federal, Provincial and Territorial Cost-shared Assurance | Programmes à frais partagés fédéral, provinciaux et territoriaux reliés à l&#39;assurance |
| `BWP11` | Return of Payments | Retour de paiements |
| `BWP12` | Mandatory Isolation Support for Temporary Foreign Workers Program | Programme d&#39;aide pour l&#39;isolement obligatoire des travailleurs étrangers temporaires |
| `BWP13` | African Swine Fever Response | Intervention en cas d&#39;éclosion de la peste porcine africaine |
| `BWP14` | Livestock Price Insurance Program | Programme d&#39;assurance des prix du bétail |
| `BWQ01` | Oversee and regulate the planning and construction of the Canadian portion of the Alaska Highway Natural Gas Pipeline Project | Surveiller et réglementer la planification et la construction de la partie canadienne du projet de gazoduc de la route de l&#39;Alaska |
| `BWR01` | Indigenous Entrepreneurship and Business Development | Entreprenariat et développement des entreprises autochtones |
| `BWR02` | Economic Development Capacity and Readiness | Capacité de développement économique et disponibilité |
| `BWR03` | Land, Natural Resources and Environmental Management | Gestion des terres, des ressources naturelles et de l&#39;environnement |
| `BWR04` | Climate Change Adaptation and Clean Energy | Adaptation aux changements climatiques et énergie propre |
| `BWR05` | Northern Strategic and Science Policy | Politique stratégique et scientifique du Nord |
| `BWR06` | Northern Regulatory and Legislative Frameworks | Cadres réglementaires et législatifs du Nord |
| `BWR07` | Northern and Arctic Environmental Sustainability | Durabilité environnementale dans le Nord et l&#39;Arctique |
| `BWR08` | Northern Contaminated Sites | Sites contaminés dans le Nord |
| `BWR09` | Canadian High Arctic Research Station | Station canadienne de recherche dans l&#39;Extrême-Arctique |
| `BWR10` | Nutrition North | Nutrition Nord |
| `BWR11` | Northern and Arctic Governance and Partnerships | Gouvernance et partenariats dans le Nord et l&#39;Arctique |
| `BWS01` | Education | Éducation |
| `BWS02` | Income Assistance | Aide au revenu |
| `BWS03` | Assisted Living | Aide à la vie autonome |
| `BWS04` | First Nations Child and Family Services | Services d&#39;aide à l&#39;enfance et à la famille des Premières Nations |
| `BWS05` | Family Violence Prevention | Prévention de la violence familiale |
| `BWS06` | Urban Programming for Indigenous | Programmes urbains pour les peuples Autochtones |
| `BWT01` | Indigenous Governance and Capacity | Gouvernance autochtone et capacités |
| `BWT02` | Water and Wastewater | L&#39;eau et les eaux usées |
| `BWT03` | Education Facilities | Installations d&#39;enseignement |
| `BWT04` | Housing | Logement |
| `BWT05` | Other Community Infrastructure and Activities | Autres infrastructures et activités communautaires |
| `BWT06` | Emergency Management Assistance | Aide à la gestion des urgences |
| `BWU01` | Clinical and Client Care | Pratique clinique et soins aux clients |
| `BWU02` | Home and Community Care | Soins à domicile et en milieu communautaire |
| `BWU03` | Communicable Diseases Control and Management | Contrôle et gestion des maladies transmissibles |
| `BWU04` | Mental Wellness | Bien-Être mental |
| `BWU05` | Healthy Living | Vie saine |
| `BWU06` | Healthy Child Development | Développement des enfants en santé |
| `BWU07` | Child First Initiative – Jordan&#39;s Principle | Initiative du principe de Jordan – Principe de l&#39;enfant d&#39;abord |
| `BWU08` | Supplementary Health Benefits | Prestations supplémentaires en Santé |
| `BWU09` | Health Planning, Quality Management and Systems Integration | Planification de la santé, gestion de la qualité et intégration des systèmes |
| `BWU10` | Health Human Resources | Ressources humaines en santé |
| `BWU11` | Health Facilities | Établissements de santé |
| `BWU12` | e-Health Infostructure | Infostructure cybersanté |
| `BWU13` | British Columbia Tripartite Health Governance | Gouvernance tripartite de la Colombie-Britannique en matière de santé |
| `BWU14` | Environmental Public Health | Hygiène du milieu |
| `BWV01` | Conference Services | Services aux conférences |
| `BWW01` | Senior Personnel and Public Service Renewal | Personnel supérieur et renouvellement de la fonction publique |
| `BWW02` | International Affairs and National Security | Affaires internationales et sécurité nationale |
| `BWW03` | Planning and Operation of Cabinet | Planification et Opérations du Cabinet |
| `BWW04` | Commissions of Inquiry | Commissions d&#39;enquête |
| `BWW05` | Youth | Jeunesse |
| `BWW06` | Legislative and Parliamentary Governance | Gouvernance législative et parlementaire |
| `BWW07` | Results, Delivery, Impact and Innovation | Résultats, livraison, impact et innovation |
| `BWW08` | Intergovernmental Affairs | Affaires intergouvernementales |
| `BWW09` | Social and Economic Policy | Politique économique et sociale |
| `BWX01` | Science and Technology | Science et technologie |
| `BWX02` | Knowledge Management and Engagement | Gestion des connaissances et mobilisation |
| `BWY01` | Review of Canadian Security Intelligence Service operations | Examen des opérations du Service canadien du renseignement de sécurité |
| `BWY02` | Investigation of complaints against the Canadian Security Intelligence Service | Enquêtes sur les plaintes contre le Service canadien du renseignement de sécurité |
| `BXA01` | Oversight and Treasury Board Support | Surveillance et soutien au Conseil du Trésor |
| `BXA02` | Expenditure Data, Analysis, Results, and Reviews | Données, analyses, résultats et examens des dépenses |
| `BXA03` | Results and Performance Reporting Policies and Initiatives | Initiatives et politiques relatives aux rapports sur les résultats et le rendement |
| `BXA04` | Government-wide Funds | Fonds pangouvernementaux |
| `BXB01` | Financial Management Policies and Initiatives | Politiques et initiatives liées à la gestion financière |
| `BXB02` | Digital Policy | Politique numérique |
| `BXB03` | Digital Strategy, Planning, and Oversight | Stratégie, planification et surveillance du numérique |
| `BXB04` | Management Accountability Framework | Cadre de responsabilisation de gestion |
| `BXB05` | Acquired Services and Assets Policies and Initiatives | Politiques et initiatives sur les biens et services acquis |
| `BXB06` | Digital Comptrollership Program | Programme de la fonction de contrôle numérique |
| `BXB07` | Internal Audit Policies and Initiatives | Politiques et initiatives sur la vérification interne |
| `BXB08` | Communications and Federal Identity Policies and Initiatives | Politiques et initiatives sur les communications et l&#39;image de marque du GC |
| `BXB09` | Canadian Digital Service | Service numérique canadien |
| `BXB10` | Greening Government Operations | Écologisation des activités gouvernementales |
| `BXB11` | Public Service Accessibility | Accessibilité de la fonction publique |
| `BXB12` | Comptrollership Program | Programme de la fonction de contrôleur |
| `BXB13` | Digital Government Program | Programme du gouvernement numérique |
| `BXC01` | Employee Relations and Total Compensation | Relations avec les employés et de la rémunération globale |
| `BXC02` | Pension and Benefits Management | Gestion des pensions et des avantages sociaux |
| `BXC03` | Workplace Policies and Services | Politiques et services en milieu de travail |
| `BXC04` | Public Service Employer Payments | Paiements en tant qu&#39;employeur de la fonction publique |
| `BXC05` | Executive and Leadership Development | Perfectionnement des cadres supérieurs et en leadership |
| `BXC06` | People Management Systems and Processes | Systèmes et processus de gestion des personnes |
| `BXC07` | Research, Planning and Renewal | Recherche, planification et renouvellement |
| `BXC08` | Employer Program | Programme d&#39;employeur |
| `BXD01` | Regulatory Policy, Oversight, and Cooperation | Politique, surveillance et coopération réglementaires |
| `BXD02` | Regulatory Cooperation | Coopération en matière de réglementation |
| `BXE01` | Export Development Canada (Canada Account) | Exportation et développement Canada (Compte du Canada) |
| `BXF01` | Public Complaints | Plaintes du public |
| `BXF02` | Investigations | Enquêtes |
| `BXF03` | Public Education | Éducation du public |
| `BXG01` | Federal Policing Investigations | Enquêtes de la Police fédérale |
| `BXG02` | Intelligence | Renseignement |
| `BXG03` | Protective Services | Services de protection |
| `BXG04` | Federal Policing Prevention and Engagement | Prévention et engagement de la Police fédérale |
| `BXG05` | International Policing | Police internationale |
| `BXG06` | Federal Operations Support | Soutien aux opérations fédérales |
| `BXG07` | Governance | Gouvernance |
| `BXH01` | Canadian Firearms Investigative and Enforcement Services | Services d&#39;enquête et d&#39;application de la loi en matière d&#39;armes à feu |
| `BXH02` | Criminal Intelligence Service Canada | Service canadien de renseignements criminels |
| `BXH03` | Forensic Science and Identification Services | Services des sciences judiciaires et de l&#39;identité |
| `BXH04` | Canadian Police College | Collège canadien de police |
| `BXH05` | Sensitive and Specialized Investigative Services | Services d&#39;enquêtes spécialisées et de nature délicate |
| `BXH06` | RCMP Specialized Technical Investigative Services | Services spécialisés d&#39;enquêtes techniques de la GRC |
| `BXH07` | RCMP Departmental Security | Sécurité ministérielle de la GRC |
| `BXH08` | RCMP Operational IM/IT Services | Services opérationnels de la GI-TI de la GRC |
| `BXH09` | Firearms Licensing and Registration | Délivrance de permis et enregistrement des armes à feu |
| `BXH10` | National Cybercrime Coordination Unit | Groupe national de coordination contre la cybercriminalité |
| `BXI01` | Provincial/Territorial Policing | Services de police provinciaux et territoriaux |
| `BXI02` | Municipal Policing | Services de police municipaux |
| `BXI03` | Indigenous Policing | Services de police autochtones |
| `BXI04` | Contract and Indigenous Policing Operations Support | Soutien aux opérations des Services de police contractuels et autochtones |
| `BXI05` | Force Generation | Mise sur pied de la force |
| `BXJ01` | Appeal case reviews | Examen d&#39;appels |
| `BXK01` | Leaders&#39; Debates | Débats des chefs |
| `BXL01` | Supplementary Health Benefits | Prestations supplémentaires en santé |
| `BXL02` | Clinical and Client Care | Pratique clinique et soins aux clients |
| `BXL03` | Community Oral Health Services | Services communautaires en santé buccodentaire |
| `BXL04` | Individual Affairs | Affaires individuelles |
| `BXM01` | Jordan&#39;s Principle and the Inuit Child First Initiative | Principe de Jordan et l&#39;Initiative: les enfants Inuits d&#39;abord |
| `BXM02` | Mental Wellness | Bien-être mental |
| `BXM03` | Healthy Living | Vie saine |
| `BXM04` | Healthy Child Development | Développement des enfants en santé |
| `BXM05` | Home and Community Care | Soins à domicile et en milieu communautaire |
| `BXM06` | Health Human Resources | Ressources humaines en santé |
| `BXM07` | Environmental Public Health | Hygiène du milieu |
| `BXM08` | Communicable Disease Control and Management | Contrôle et gestion des maladies transmissibles |
| `BXM09` | Education | Éducation |
| `BXM10` | Income Assistance | Le programme d&#39;aide au revenu |
| `BXM11` | Assisted Living | Le Programme d&#39;aide à la vie autonome |
| `BXM12` | First Nations Child and Family Services | Programme des services à l&#39;enfance et à la famille des Premières Nations |
| `BXM13` | Family Violence Prevention | Le Programme de prévention de la violence familiale |
| `BXM14` | Urban Programming for Indigenous Peoples | Programmes urbains pour les peuples autochtones |
| `BXP01` | Health Facilities | Établissements de santé |
| `BXP02` | e-Health Infostructure | Infostructure cybersanté |
| `BXP03` | Health Planning, Quality Management and Systems Integration | Planification de la santé, gestion de la qualité et intégration des systèmes |
| `BXP04` | Indigenous Governance and Capacity | Gouvernance et capacités autochtones |
| `BXP05` | Water and Wastewater | L&#39;eau et les eaux usées |
| `BXP06` | Education Facilities | Installations d&#39;enseignement |
| `BXP07` | Housing | Logement |
| `BXP08` | Other Community Infrastructure and Activities | Autres infrastructures et activités communautaires |
| `BXP09` | Emergency Management Assistance | Aide à la gestion des urgences |
| `BXP10` | Indigenous Entrepreneurship and Business Development | Entreprenariat et développement des entreprises autochtones |
| `BXP11` | Economic Development Capacity and Readiness | Capacité de développement économique et disponibilité |
| `BXP12` | Lands, Natural Resources and Environmental Management | Gestion des terres, des ressources naturelles et de l&#39;environnement |
| `BXP13` | Statutory, Legislative and Policy Support to First Nations Governance | Soutien statutaire, législatif et politique à la gouvernance autochtone |
| `BXQ01` | New Fiscal Relationship | Nouvelle relation financière |
| `BXQ02` | Self-Determined Services | Services autodéterminés |
| `BXQ03` | British Columbia Tripartite Health Governance | Gouvernance tripartite de la Colombie-Britannique en matière de santé |
| `BXR01` | Expertise and Outreach | Expertise et information |
| `BXR02` | Community Action and Innovation | Action communautaire et innovation |
| `BXS01` | Quasi-judicial Review Program | Programme d&#39;examen quasi judiciaire |
| `BXT01` | Company Performance | Rendement des sociétés |
| `BXT02` | Management System and Industry Performance | Système de gestion et rendement du secteur |
| `BXT03` | Emergency Management | Gestion des situations d&#39;urgence |
| `BXT04` | Regulatory Framework | Cadre de réglementation |
| `BXU01` | Energy System Information | Information sur les filières énergétiques |
| `BXU02` | Pipeline Information | Information sur les pipelines |
| `BXV01` | Stakeholder Engagement | Mobilisation des parties prenantes |
| `BXV02` | Indigenous Engagement | Mobilisation des Autochtones |
| `BXW01` | National security and intelligence activity reviews and complaints investigations | Surveillance des activités de sécurité nationale et de renseignement et enquêtes sur les plaintes |
| `BXX01` | Compliance and Enforcement | Observation et contrôle d&#39;application |
| `BXY01` | Infrastructure, Tolls and Export Applications | Demandes relatives aux infrastructures, aux droits et aux exportations |
| `BXY02` | Participant Funding | Aide financière aux participants |
| `BXZ01` | Standards Development | Élaboration des normes |
| `BXZ02` | Outreach and Knowledge Application | Sensibilisation et application des connaissances |
| `BYB01` | Allocation-based and Direct Funding Stewardship | Gérance du financement fondé sur l&#39;allocation et du financement direct |
| `BYB02` | Major Bridges Oversight | Surveillance des grands ponts |
| `BYB03` | Alternative Financing Oversight | Surveillance du financement alternatif |
| `BYB04` | Homelessness Funding Oversight | Surveillance du financement en matière d&#39;itinérance |
| `BYC01` | Alternative Financing Investment | Investissement de financement alternatif |
| `BYC02` | Public Infrastructure and Communities Investment | Investissement dans les infrastructures publiques et les collectivités |
| `BYC03` | Major Bridges Investment | Investissement dans les grands ponts |
| `BYC04` | Homelessness Investment | Investissements en matière d&#39;itinérance |
| `BYD01` | Rural Economic Development Policy | Politique de développement économique rural |
| `BYD02` | Major Bridges Policy | Politique des grands ponts |
| `BYD03` | Public Infrastructure and Communities Policy | Politique sur les infrastructures publiques et les collectivités |
| `BYD04` | Alternative Financing Policy | Politique de financement alternatif |
| `BYD05` | Homelessness Policy | Politiques en matière d&#39;itinérance |
| `BYE01` | Workplace Technologies | Technologies en milieu de travail |
| `BYE02` | Cloud | Infonuagique |
| `BYE03` | Data Centre Information Technology Operations | Opérations en technologies de l&#39;information des centres de données |
| `BYE04` | Telecommunications | Télécommunications |
| `BYE05` | Networks | Réseaux |
| `BYE06` | Security | Sécurité |
| `BYE07` | Enterprise Services Design and Delivery | Conception et prestation des services d&#39;entreprise |
| `BYG01` | Electoral Boundaries Readjustment Administration | Révision des limites des circonscriptions électorales |
| `BYI01` | Voting Services | Services de vote |
| `BYI02` | Field Management | Gestion des activités en région |
| `BYI03` | Public Education and Information | Éducation et information du public |
| `BYI04` | Electoral Data Services | Services liés aux données électorales |
| `BYJ01` | Office of the Commissioner of Canada Elections | Bureau du commissaire aux élections fédérales |
| `BYJ02` | Political Entities Regulatory Compliance | Conformité régulatoire des entités politiques |
| `BYJ03` | Electoral Integrity and Regulatory Policy | Intégrité électorale et politique réglementaire |
| `BYK01` | Innovation | Innovation |
| `BYK02` | Business Growth | Croissance des entreprises |
| `BYK03` | Business Services | Services aux entreprises |
| `BYK04` | Community Initiatives | Initiatives communautaires |
| `BYL01` | Business Development | Développement des affaires |
| `BYL02` | Regional Innovation Ecosystem | Écosystème régional de l&#39;innovation |
| `BYL03` | Community Economic Development and Diversification | Développement et diversification économiques des collectivités |
| `BYM01` | Innovation | Innovation |
| `BYM02` | Business Growth | Croissance des entreprises |
| `BYM03` | Business Services | Services aux entreprises |
| `BYM04` | Community Initiatives | Initiatives communautaires |
| `BYO01` | Law Review | Examen du droit |
| `BYP01` | Public Health Promotion and Disease Prevention | Promotion de la santé publique et prévention des maladies |
| `BYP02` | Home and Long-Term Care | Soins à domicile et soins de longue durée |
| `BYP03` | Primary Health Care | Soins de santé primaires |
| `BYP04` | Health Systems Support | Soutien aux systèmes de santé |
| `BYP05` | Supplementary Health Benefits | Prestations supplémentaires en santé |
| `BYP06` | Jordan&#39;s Principle and the Inuit Child First Initiative | Principe de Jordan et Initiative : Les enfants inuits d&#39;abord |
| `BYP07` | Safety and Prevention Services | Services de sécurité et de prévention |
| `BYP08` | Child and Family Services | Services à l&#39;enfance et à la famille |
| `BYP09` | Income Assistance | Le programme d&#39;aide au revenu |
| `BYP10` | Urban Programming for Indigenous Peoples | Programmes urbains pour les peuples autochtones |
| `BYP11` | Elementary and Secondary Education | Éducation primaire et secondaire |
| `BYP12` | Post-Secondary Education | Éducation postsecondaire |
| `BYP13` | Community Infrastructure | Infrastructures communautaires |
| `BYP14` | Communities &amp; The Environment | Communautés et environnement |
| `BYP15` | Emergency Management Assistance | Aide à la gestion des urgences |
| `BYP16` | Community Economic Development | Développement économique communautaire |
| `BYP17` | Indigenous Entrepreneurship and Business Development | Entrepreneuriat et développement des entreprises autochtones |
| `BYP18` | Indigenous Governance and Capacity Supports | Gouvernance autochtone et soutien des capacités |
| `ISS01` | Management and Oversight Services | Services de gestion et de surveillance |
| `ISS02` | Communications Services | Services de communication |
| `ISS03` | Legal Services | Services juridiques |
| `ISS04` | Human Resources Management Services | Services de gestion des ressources humaines |
| `ISS05` | Financial Management Services | Services de gestion financière |
| `ISS06` | Information Management Services | Services de gestion de l&#39;information |
| `ISS07` | Information Technology Services | Services de la technologie de l&#39;information |
| `ISS08` | Real Property Management Services | Services de gestion des biens immobiliers |
| `ISS09` | Materiel Management Services | Services de gestion du matériel |
| `ISS0Z` | Acquisition Management Services | Services de gestion des acquisitions |
| `ISS11` | Management and Oversight Services | Services de gestion et de surveillance |
| `ISS12` | Communications Services | Services de communication |
| `ISS13` | Legal Services | Services juridiques |
| `ISS14` | Human Resources Management Services | Services de gestion des ressources humaines |
| `ISS15` | Financial Management Services | Services de gestion financière |
| `ISS16` | Information Management Services | Services de gestion de l&#39;information |
| `ISS17` | Information Technology Services | Services de la technologie de l&#39;information |
| `ISS18` | Real Property Management Services | Services de gestion des biens immobiliers |
| `ISS19` | Materiel Management Services | Services de gestion du matériel |
| `ISS1Z` | Acquisition Management Services | Services de gestion des acquisitions |
| `ISSA1` | Management and Oversight Services | Services de gestion et de surveillance |
| `ISSA2` | Communications Services | Services de communication |
| `ISSA3` | Legal Services | Services juridiques |
| `ISSA4` | Human Resources Management Services | Services de gestion des ressources humaines |
| `ISSA5` | Financial Management Services | Services de gestion financière |
| `ISSA6` | Information Management Services | Services de gestion de l&#39;information |
| `ISSA7` | Information Technology Management Services | Services de gestion de la technologie de l&#39;information |
| `ISSA8` | Real Property Management Services | Services de gestion des biens immobiliers |
| `ISSA9` | Materiel Management Services | Services de gestion du matériel |
| `ISSAZ` | Acquisition Management Services | Services de gestion des acquisitions |




---

#### `client_feedback_channel` – Client Feedback, by Channel / Commentaires des clients, par canal

**Type:** `_text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** client_feedback_channel (8 values)  


**Description:**  
EN: Identifies which channels, if any, provide users of a service an opportunity to provide feedback on their level of satisfaction with the service. Multiple values must be separated by a comma (,).
  
FR: Détermine quels canaux, s'il y a lieu, offrent aux utilisateurs d'un service l'occasion de donner une rétroaction sur leur niveau de satisfaction à l'égard du service. Séparez les entrées par une virgule (,) s’il y en a plusieurs qui s’appliquent.



##### Allowed Values (client_feedback_channel)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `EML` | Email | Courriel |
| `FAX` | Fax | Télécopieur |
| `NON` | No feedback collected | Aucune rétroaction possible |
| `ONL` | Online | En ligne |
| `OTH` | Other channel not listed | Autre option qui n&#39;est pas sur la liste |
| `PERSON` | In-Person | En personne |
| `POST` | Postal Mail | Courrier postal |
| `TEL` | Telephone | Téléphone |




---

#### `automated_decision_system` – Automated Decision System / Système décisionnel automatisé

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** automated_decision_system (2 values)  


**Description:**  
EN: An automated decision system is defined in the Directive on Automated Decision-Making and means any technology that either assists or replaces the judgment of human decision-makers, such as those that draw from fields like statistics, linguistics and computer science, and use techniques such as rules-based systems, regression, predictive analytics, machine learning, deep learning, and neural networks.
  
FR: Un système décisionnel automatisé est défini dans la Directive sur la prise de décisions automatisée et désigne toute technologie qui assiste ou remplace le jugement des décideurs humains, comme ceux qui proviennent de domaines tels que les statistiques, la linguistique et les sciences informatiques, et utilisent des techniques telles que les systèmes basés sur des règles, la régression, l’analytique prédictive, l’apprentissage automatique, l’apprentissage en profondeur et les réseaux neuronaux.



##### Allowed Values (automated_decision_system)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `N` | No | Non |
| `Y` | Yes | Oui |




---

#### `automated_decision_system_description_en` – Automated Decision System Description (English) / Description du système décisionnel automatisé (anglais)

**Type:** `text`  
**Required:** No  
**Validation:** This field is required due to a response in a different field.
This field has a maximum length of 1800 characters.
 / Ce champ est requis en raison d'une réponse présente dans un autre champ.
Ce champ ne peut excéder une longueur maximale de 1800 caractères.
  


**Description:**  
EN: Describe what the system does. Include: the name or title of the system, the role of the system in the decision, whether it is full or partial automation, and how officers use the system to make or inform the decision.
  
FR: Décrivez ce que fait le système. Inclure : le nom ou titre du système, le rôle du système dans la prise de décision, s'il s'agit d'une automatisation complète ou partielle, et comment les agents utilisent le système pour prendre ou informer la décision.



---

#### `automated_decision_system_description_fr` – Automated Decision System Description (French) / Description du système décisionnel automatisé (français)

**Type:** `text`  
**Required:** No  
**Validation:** This field is required due to a response in a different field.
This field has a maximum length of 1800 characters.
 / Ce champ est requis en raison d'une réponse présente dans un autre champ.
Ce champ ne peut excéder une longueur maximale de 1800 caractères.
  


**Description:**  
EN: Describe what the system does. Include: the name or title of the system, the role of the system in the decision, whether it is full or partial automation, and how officers use the system to make or inform the decision.
  
FR: Décrivez ce que fait le système. Inclure : le nom ou titre du système, le rôle du système dans la prise de décision, s'il s'agit d'une automatisation complète ou partielle, et comment les agents utilisent le système pour prendre ou informer la décision.



---

#### `service_fee` – Service Fees / Frais de service

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** service_fee (2 values)  


**Description:**  
EN: Identifies whether a service fee is collected for the provision of the service.  
FR: Indique si des frais de service sont perçus pour la prestation du service.


##### Allowed Values (service_fee)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `N` | No | Non |
| `Y` | Yes | Oui |




---

#### `os_account_registration` – Online Services: Account Registration/Enrollment / Services en ligne : Enregistrement/inscription du compte

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** os_account_registration (3 values)  


**Description:**  
EN: Identifies whether a client can register or enroll for a personal account where they can make use of other interaction points (applying for services, providing information, seeing their status, submitting feedback, etc.).
  
FR: Indique si un client peut s'inscrire ou s'inscrire à un compte personnel où il peut utiliser d'autres points d'interaction (demander des services, fournir des renseignements, voir son statut, soumettre des commentaires, etc.).



##### Allowed Values (os_account_registration)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `N` | No (This interaction point is applicable to the service but is not currently online) | Non (Ce point d&#39;interaction s&#39;applique au service, mais il n&#39;est pas en ligne présentement) |
| `NA` | N/A (This interaction point is not applicable to the service) | S.O. (Ce point d&#39;interaction ne s&#39;applique pas au service) |
| `Y` | Yes (This interaction point is applicable to the service and is online) | Oui (Ce point d&#39;interaction s&#39;applique au service et est en ligne) |




---

#### `os_authentication` – Online Services: Authentication / Services en ligne : Authentification

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** os_authentication (3 values)  


**Description:**  
EN: Identifies whether a client can authenticate their identity online.  
FR: Indique si un client peut confirmer son identité en ligne.


##### Allowed Values (os_authentication)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `N` | No (This interaction point is applicable to the service but is not currently online) | Non (Ce point d&#39;interaction s&#39;applique au service, mais il n&#39;est pas en ligne présentement) |
| `NA` | N/A (This interaction point is not applicable to the service) | S.O. (Ce point d&#39;interaction ne s&#39;applique pas au service) |
| `Y` | Yes (This interaction point is applicable to the service and is online) | Oui (Ce point d&#39;interaction s&#39;applique au service et est en ligne) |




---

#### `os_application` – Online Services: Application / Services en ligne : Demande

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** os_application (3 values)  


**Description:**  
EN: Identifies whether a client can apply for a service online.  
FR: Indique si un client peut présenter une demande de service en ligne.


##### Allowed Values (os_application)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `N` | No (This interaction point is applicable to the service but is not currently online) | Non (Ce point d&#39;interaction s&#39;applique au service, mais il n&#39;est pas en ligne présentement) |
| `NA` | N/A (This interaction point is not applicable to the service) | S.O. (Ce point d&#39;interaction ne s&#39;applique pas au service) |
| `Y` | Yes (This interaction point is applicable to the service and is online) | Oui (Ce point d&#39;interaction s&#39;applique au service et est en ligne) |




---

#### `os_decision` – Online Services: Decision / Services en ligne : Décision

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** os_decision (3 values)  


**Description:**  
EN: Identifies whether a client can be notified online of the outcome of their request for this service.  
FR: Indique si un client peut être informé en ligne du résultat de sa demande de ce service.


##### Allowed Values (os_decision)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `N` | No (This interaction point is applicable to the service but is not currently online) | Non (Ce point d&#39;interaction s&#39;applique au service, mais il n&#39;est pas en ligne présentement) |
| `NA` | N/A (This interaction point is not applicable to the service) | S.O. (Ce point d&#39;interaction ne s&#39;applique pas au service) |
| `Y` | Yes (This interaction point is applicable to the service and is online) | Oui (Ce point d&#39;interaction s&#39;applique au service et est en ligne) |




---

#### `os_issuance` – Online Services: Issuance / Services en ligne : Émission

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** os_issuance (3 values)  


**Description:**  
EN: Identifies whether a client can receive the service online, perhaps in the form of permits, certificates, money or information.  
FR: Indique si un client peut recevoir le service en ligne, peut-être sous forme de permis, de certificats, d'argent ou d'information.


##### Allowed Values (os_issuance)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `N` | No (This interaction point is applicable to the service but is not currently online) | Non (Ce point d&#39;interaction s&#39;applique au service, mais il n&#39;est pas en ligne présentement) |
| `NA` | N/A (This interaction point is not applicable to the service) | S.O. (Ce point d&#39;interaction ne s&#39;applique pas au service) |
| `Y` | Yes (This interaction point is applicable to the service and is online) | Oui (Ce point d&#39;interaction s&#39;applique au service et est en ligne) |




---

#### `os_issue_resolution_feedback` – Online Services: Issue Resolution and Feedback / Services en ligne : Solution de problème et rétroaction

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** os_issue_resolution_feedback (3 values)  


**Description:**  
EN: Identifies whether a client can seek resolution to their issues or provide feedback online.  
FR: Indique si un client peut demander une résolution à leur problèmes avec le service ou fournir de la rétroaction en ligne.


##### Allowed Values (os_issue_resolution_feedback)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `N` | No (This interaction point is applicable to the service but is not currently online) | Non (Ce point d&#39;interaction s&#39;applique au service, mais il n&#39;est pas en ligne présentement) |
| `NA` | N/A (This interaction point is not applicable to the service) | S.O. (Ce point d&#39;interaction ne s&#39;applique pas au service) |
| `Y` | Yes (This interaction point is applicable to the service and is online) | Oui (Ce point d&#39;interaction s&#39;applique au service et est en ligne) |




---

#### `os_comments_client_interaction_en` – Comments on Online Services - Client Interaction Points (English) / Commentaires sur les services électroniques - points d'interaction avec les clients (anglais)

**Type:** `text`  
**Required:** No  
**Validation:** This field is required due to a response in a different field.
This field has a maximum length of 1000 characters.
 / Ce champ est requis en raison d'une réponse présente dans un autre champ.
Ce champ ne peut excéder une longueur maximale de 1000 caractères.
  


**Description:**  
EN: Comments related to online services - client Interaction points (English). For any interaction points reported as "Not Applicable", comments have to be provided.
  
FR: Commentaires en lien avec les services électroniques - points d'interaction avec les clients (anglais). Pour tout points d'interaction signalés comme « sans objet », des commentaires doivent être fournis.



---

#### `os_comments_client_interaction_fr` – Comments on Online Services - Client Interaction Points (French) / Commentaires sur les services électroniques - points d'interaction avec les clients (français)

**Type:** `text`  
**Required:** No  
**Validation:** This field is required due to a response in a different field.
This field has a maximum length of 1000 characters.
 / Ce champ est requis en raison d'une réponse présente dans un autre champ.
Ce champ ne peut excéder une longueur maximale de 1000 caractères.
  


**Description:**  
EN: Comments related to online services - client Interaction points (French). For any interaction points reported as "Not Applicable", comments have to be provided.
  
FR: Commentaires en lien avec les services électroniques - points d'interaction avec les clients (français). Pour tout points d'interaction signalés comme « sans objet », des commentaires doivent être fournis.



---

#### `last_service_review` – Year of last service review / Année du dernier examen de service

**Type:** `text`  
**Required:** No  
**Choice Set:** last_service_review (25 values)  


**Description:**  
EN: Identifies the fiscal year when the most recent service review was completed.  
FR: Identifie l’exercice lors duquel le plus récent examen de service a été mené.


##### Allowed Values (last_service_review)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `2005-2006` | 2005-2006 | 2005-2006 |
| `2006-2007` | 2006-2007 | 2006-2007 |
| `2007-2008` | 2007-2008 | 2007-2008 |
| `2008-2009` | 2008-2009 | 2008-2009 |
| `2009-2010` | 2009-2010 | 2009-2010 |
| `2010-2011` | 2010-2011 | 2010-2011 |
| `2011-2012` | 2011-2012 | 2011-2012 |
| `2012-2013` | 2012-2013 | 2012-2013 |
| `2013-2014` | 2013-2014 | 2013-2014 |
| `2014-2015` | 2014-2015 | 2014-2015 |
| `2015-2016` | 2015-2016 | 2015-2016 |
| `2016-2017` | 2016-2017 | 2016-2017 |
| `2017-2018` | 2017-2018 | 2017-2018 |
| `2018-2019` | 2018-2019 | 2018-2019 |
| `2019-2020` | 2019-2020 | 2019-2020 |
| `2020-2021` | 2020-2021 | 2020-2021 |
| `2021-2022` | 2021-2022 | 2021-2022 |
| `2022-2023` | 2022-2023 | 2022-2023 |
| `2023-2024` | 2023-2024 | 2023-2024 |
| `2024-2025` | 2024-2025 | 2024-2025 |
| `2025-2026` | 2025-2026 | 2025-2026 |
| `2026-2027` | 2026-2027 | 2026-2027 |
| `2027-2028` | 2027-2028 | 2027-2028 |
| `2028-2029` | 2028-2029 | 2028-2029 |
| `2029-2030` | 2029-2030 | 2029-2030 |




---

#### `last_service_improvement` – Year of last service improvement based on client feedback / Année de la dernière amélioration du service sur la base de la rétroaction du client

**Type:** `text`  
**Required:** No  
**Choice Set:** last_service_improvement (25 values)  


**Description:**  
EN: What was the most recent year in which this service was improved based on client feedback?  
FR: Quelle a été l'année la plus récente au cours de laquelle ce service a été amélioré en fonction des commentaires des clients?


##### Allowed Values (last_service_improvement)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `2005-2006` | 2005-2006 | 2005-2006 |
| `2006-2007` | 2006-2007 | 2006-2007 |
| `2007-2008` | 2007-2008 | 2007-2008 |
| `2008-2009` | 2008-2009 | 2008-2009 |
| `2009-2010` | 2009-2010 | 2009-2010 |
| `2010-2011` | 2010-2011 | 2010-2011 |
| `2011-2012` | 2011-2012 | 2011-2012 |
| `2012-2013` | 2012-2013 | 2012-2013 |
| `2013-2014` | 2013-2014 | 2013-2014 |
| `2014-2015` | 2014-2015 | 2014-2015 |
| `2015-2016` | 2015-2016 | 2015-2016 |
| `2016-2017` | 2016-2017 | 2016-2017 |
| `2017-2018` | 2017-2018 | 2017-2018 |
| `2018-2019` | 2018-2019 | 2018-2019 |
| `2019-2020` | 2019-2020 | 2019-2020 |
| `2020-2021` | 2020-2021 | 2020-2021 |
| `2021-2022` | 2021-2022 | 2021-2022 |
| `2022-2023` | 2022-2023 | 2022-2023 |
| `2023-2024` | 2023-2024 | 2023-2024 |
| `2024-2025` | 2024-2025 | 2024-2025 |
| `2025-2026` | 2025-2026 | 2025-2026 |
| `2026-2027` | 2026-2027 | 2026-2027 |
| `2027-2028` | 2027-2028 | 2027-2028 |
| `2028-2029` | 2028-2029 | 2028-2029 |
| `2029-2030` | 2029-2030 | 2029-2030 |




---

#### `sin_usage` – Use of Social Insurance Number / Utilisation du numéro d'assurance sociale (NAS)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** sin_usage (3 values)  


**Description:**  
EN: Identifies whether the Social Insurance Number (SIN) is used in the delivery of the service.  
FR: Indique si le numéro d'assurance sociale (NAS) est utilisé dans la prestation du service.


##### Allowed Values (sin_usage)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `N` | No | Non |
| `NA` | N/A (not a service to individuals) | S.O. (N&#39;est pas un service aux particuliers) |
| `Y` | Yes | Oui |




---

#### `cra_bn_identifier_usage` – Use of CRA Business Number as Standard Identifier / Utilisation du numéro d’entreprise de l’ARC en tant qu’identificateur standard

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** cra_bn_identifier_usage (3 values)  


**Description:**  
EN: Identifies whether the Canada Revenue Agency's Business Number is used in the delivery of the service as the standard identifier in accordance with the Directive on the Business Number.
  
FR: Indique si le numéro d’entreprise de l’Agence du revenu du Canada est utilisé dans la prestation des services en tant qu’identificateur standard, conformément à la Directive sur le numéro d’entreprise.



##### Allowed Values (cra_bn_identifier_usage)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `N` | No | Non |
| `NA` | N/A (not a service to businesses) | S.O. (N&#39;est pas un service aux entreprises) |
| `Y` | Yes | Oui |




---

#### `num_phone_enquiries` – Number of Telephone Enquiries Received / Nombre des demandes téléphoniques reçus

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field must be either a number, "NA", or "ND"
This value must not be negative.
 / Ce champ ne doit pas être vide.
Ce champ doit être un chiffre, "NA", ou "ND"
Cette valeur ne doit être négative.
  


**Description:**  
EN: Identifies the number of enquiries about the service received in this fiscal year. Note: This field represents only requests for information about the service. Report service requests or applications submitted by telephone in the "telephone applications" field. A value of 0 means no calls were received; ND means no data was collected; and NA means it is not possible to submit telephone enquiries.
  
FR: Indique le nombre de demandes d'information reçues par téléphone au cours d'un exercice financier. Remarque : Ce champ indique seulement le nombre de demandes d'information au sujet d'un service. Servez-vous du champ "telephone applications" pour les demandes de prestation de service reçues par téléphone.



---

#### `num_applications_by_phone` – Number of Applications Submitted by Telephone / Nombre de demandes soumises par téléphone

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field must be either a number, "NA", or "ND"
This value must not be negative.
 / Ce champ ne doit pas être vide.
Ce champ doit être un chiffre, "NA", ou "ND"
Cette valeur ne doit être négative.
  


**Description:**  
EN: Identifies the number of applications submitted in a fiscal year for the telephone channel. A value of 0 means no applications were received for this channel; ND means there is no data collected for this channel; and NA means no applications can be submitted through this channel.
  
FR: Indique le nombre de demandes reçues par téléphone au cours d'un exercice. La valeur 0 signifie qu'aucune demande n'a été reçue via ce mode de prestation, aucune donnée (ND) signifie qu'aucune donnée n’est disponible, et sans objet (NA) signifie que le service n’est pas offert au moyen de ce mode de prestation.



---

#### `num_website_visits` – Number of Website Visits / Nombre de visites sur le site Web

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field must be either a number, "NA", or "ND"
This value must not be negative.
 / Ce champ ne doit pas être vide.
Ce champ doit être un chiffre, "NA", ou "ND"
Cette valeur ne doit être négative.
  


**Description:**  
EN: Identifies the number of visits to the service's website in a fiscal year. A value of 0 means there were no visits; ND means there is no data collected website visits; and NA means there is no associated public website.
  
FR: Indique le nombre de de visites au site web du service lors d'un exercice financier. La valeur 0 signifie qu'aucune visite au site web n’a été enregistrée, aucune donnée (ND) signifie que le nombre de visites n’est pas mesuré, et sans objet (NA) signifie qu’il n’y a aucune site web à visiter.



---

#### `num_applications_online` – Number of Applications Submitted Online / Nombre de demandes soumises en ligne

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field must be either a number, "NA", or "ND"
This value must not be negative.
 / Ce champ ne doit pas être vide.
Ce champ doit être un chiffre, "NA", ou "ND"
Cette valeur ne doit être négative.
  


**Description:**  
EN: Identifies the number of applications submitted in a fiscal year for the online channel. A value of 0 means no applications were received for this channel; ND means there is no data collected for this channel; and NA means no applications can be submitted through this channel.
  
FR: Indique le nombre de demandes reçues en ligne au cours d'un exercice. La valeur 0 signifie qu'aucune demande n'a été reçue via ce mode de prestation, aucune donnée (ND) signifie qu'aucune donnée n’est disponible, et sans objet (NA) signifie que le service n’est pas offert au moyen de ce mode de prestation.



---

#### `num_applications_in_person` – Number of Applications Submitted In-Person / Nombre de demandes soumises en personne

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field must be either a number, "NA", or "ND"
This value must not be negative.
 / Ce champ ne doit pas être vide.
Ce champ doit être un chiffre, "NA", ou "ND"
Cette valeur ne doit être négative.
  


**Description:**  
EN: Identifies number of applications received in-person in a fiscal year for the service. A value of 0 means no applications were received for this channel; ND means there is no data collected for this channel; and NA means no applications can be submitted through this channel.
  
FR: Indique le nombre de demandes reçues en personne au cours d'un exercice. La valeur 0 signifie qu'aucune demande n'a été reçue via ce mode de prestation, aucune donnée (ND) signifie qu'aucune donnée n’est disponible, et sans objet (NA) signifie que le service n’est pas offert au moyen de ce mode de prestation.



---

#### `num_applications_by_mail` – Number of Applications Submitted via Postal Mail / Nombre de demandes soumises par la poste

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field must be either a number, "NA", or "ND"
This value must not be negative.
 / Ce champ ne doit pas être vide.
Ce champ doit être un chiffre, "NA", ou "ND"
Cette valeur ne doit être négative.
  


**Description:**  
EN: Identifies the number of applications received through postal mail in a fiscal year. A value of 0 means no applications were received for this channel; ND means there is no data collected for this channel; and NA means no applications can be submitted through this channel.
  
FR: Indique le nombre de demandes reçues par la poste au cours d'un exercice. La valeur 0 signifie qu'aucune demande n'a été reçue via ce mode de prestation, aucune donnée (ND) signifie qu'aucune donnée n’est disponible, et sans objet (NA) signifie que le service n’est pas offert au moyen de ce mode de prestation.



---

#### `num_applications_by_email` – Number of Applications Submitted by Email / Nombre de demandes soumises par courriel

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field must be either a number, "NA", or "ND"
This value must not be negative.
 / Ce champ ne doit pas être vide.
Ce champ doit être un chiffre, "NA", ou "ND"
Cette valeur ne doit être négative.
  


**Description:**  
EN: Identifies the number of applications received through email in a fiscal year for the service. A value of 0 means no applications were received for this channel; ND means there is no data collected for this channel; and NA means no applications can be submitted through this channel.
  
FR: Indique le nombre de demandes reçues par courriel au cours d'un exercice. La valeur 0 signifie qu'aucune demande n'a été reçue via ce mode de prestation, aucune donnée (ND) signifie qu'aucune donnée n’est disponible, et sans objet (NA) signifie que le service n’est pas offert au moyen de ce mode de prestation.



---

#### `num_applications_by_fax` – Number of Applications Submitted by Fax / Nombre de demandes soumises par fax

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field must be either a number, "NA", or "ND"
This value must not be negative.
 / Ce champ ne doit pas être vide.
Ce champ doit être un chiffre, "NA", ou "ND"
Cette valeur ne doit être négative.
  


**Description:**  
EN: Identifies the number of applications received through fax in a fiscal year for the service. A value of 0 means no applications were received for this channel; ND means there is no data collected for this channel; and NA means no applications can be submitted through this channel.
  
FR: Indique le nombre de demandes reçues par télécopieur au cours d'un exercice. La valeur 0 signifie qu'aucune demande n'a été reçue via ce mode de prestation, aucune donnée (ND) signifie qu'aucune donnée n’est disponible, et sans objet (NA) signifie que le service n’est pas offert au moyen de ce mode de prestation.



---

#### `num_applications_by_other` – Number of Applications Submitted via other channels / Nombre de demandes soumises par les autre modes de prestations

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field must be either a number, "NA", or "ND"
This value must not be negative.
 / Ce champ ne doit pas être vide.
Ce champ doit être un chiffre, "NA", ou "ND"
Cette valeur ne doit être négative.
  


**Description:**  
EN: Identifies the number of applications received through other channels not listed in a fiscal year for the service. A value of 0 means no applications were received for this channel; ND means there is no data collected for this channel; and NA means no applications can be submitted through this channel.
  
FR: Indique le nombre de demandes reçues par des modes de prestations qui ne sont pas énumérés dans ce gabarit au cours d'un exercice. La valeur 0 signifie qu'aucune demande n'a été reçue via ce mode de prestation, aucune donnée (ND) signifie qu'aucune donnée n’est disponible, et sans objet (NA) signifie que le service n’est pas offert au moyen de ce mode de prestation.



---

#### `special_remarks_en` – Special Remarks (English) / Remarques spéciales (anglais)

**Type:** `text`  
**Required:** No  
**Validation:** This field has a maximum length of 2000 characters. / Ce champ ne peut excéder une longueur maximale de 2000 caractères.  


**Description:**  
EN: Provides additional space for comments related to volumetrics information. Please refer to associated Field ID, where applicable. For comments related to other fields, departments can create and publish an explanatory note on their website with a link to the GC Service Inventory dataset. This field is mandatory if there is an amount reported under “Number of applications submitted via other channels”
  
FR: Fournit de l'espace supplémentaire pour les commentaires relatifs aux renseignements sur les volumes. Veuillez vous reporter au code d'identification de la zone, s'il y a lieu. Pour les commentaires relatifs à d'autres zones, les ministères peuvent publier une note explicative sur leur site Web suivi d'un lien vers l'ensemble de données du Répertoire des services du GC. Ce champ est requis s’il y a un montant rapporté sous le champ « Nombre de demandes soumises par les autres modes de prestation »



---

#### `special_remarks_fr` – Special Remarks (French) / Remarques spéciales (français)

**Type:** `text`  
**Required:** No  
**Validation:** This field has a maximum length of 2000 characters. / Ce champ ne peut excéder une longueur maximale de 2000 caractères.  


**Description:**  
EN: Provides additional space for comments related to volumetrics information. Please refer to associated Field ID, where applicable. For comments related to other fields, departments can create and publish an explanatory note on their website with a link to the GC Service Inventory dataset. This field is mandatory if there is an amount reported under “Number of applications submitted via other channels”
  
FR: Fournit de l'espace supplémentaire pour les commentaires relatifs aux renseignements sur les volumes. Veuillez vous reporter au code d'identification de la zone, s'il y a lieu. Pour les commentaires relatifs à d'autres zones, les ministères peuvent publier une note explicative sur leur site Web suivi d'un lien vers l'ensemble de données du Répertoire des services du GC. Ce champ est requis s’il y a un montant rapporté sous le champ « Nombre de demandes soumises par les autres modes de prestation »



---

#### `service_uri_en` – URL to Service (English) / URL du service (anglais)

**Type:** `text`  
**Required:** No  
**Validation:** This field has a maximum length of 1500 characters. / Ce champ ne peut excéder une longueur maximale de 1500 caractères.  


**Description:**  
EN: Identifies the departmental webpage where the service is described and/or accessed.  
FR: Indique la page Web du ministère où le service est décrit et/ou peut être lancé.


---

#### `service_uri_fr` – URL to Service (French) / URL du service (français)

**Type:** `text`  
**Required:** No  
**Validation:** This field has a maximum length of 1500 characters. / Ce champ ne peut excéder une longueur maximale de 1500 caractères.  


**Description:**  
EN: Identifies the departmental webpage where the service is described and/or accessed.  
FR: Indique la page Web du ministère où le service est décrit et/ou peut être lancé.


---



## Service Standards & Performance Results / Normes de service et résultats du rendement 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `fiscal_yr` | Fiscal Year / Année financière | `text` | Yes |  | fiscal_yr | Identifies the fiscal year (April 1 to March 31) during which service activitie… |
| `service_id` | Service ID Number / Numéro d&#39;identification du service | `text` | Yes |  |  | The unique number assigned to a service in the inventory to make it easier to r… |
| `service_name_en` | Service Name (English) / Nom du service (en anglais) | `text` | Yes |  |  | Identifies the official name of the service. |
| `service_name_fr` | Service Name (French) / Nom du service (en français) | `text` | Yes |  |  | Identifies the official name of the service. |
| `service_standard_id` | Service Standard ID / Numéro d&#39;identification de la norme relative aux services | `text` | Yes |  |  | Identifies the unique number assigned to each service standard for that service… |
| `service_standard_en` | Service Standard (English) / Norme relative aux services (anglais) | `text` | Yes |  |  | Identifies the service standard related to a particular service. See Guideline … |
| `service_standard_fr` | Service Standard (French) / Norme relative aux services (français) | `text` | Yes |  |  | Identifies the service standard related to a particular service. See Guideline … |
| `type` | Service Standard Type / Type de norme relative aux services | `text` | Yes |  | type | Identifies the type of service standard as defined in the Guideline on Service … |
| `channel` | Service Standard Channel / Mode de prestation de la norme de service | `text` | Yes |  | channel | Identifies the service channel to which the service standard applies |
| `channel_comments_en` | Comments on the service standard channel (English) / Commentaires sur le mode de prestation de la norme de service (anglais) | `text` | No |  |  | Comments related to the service standard channel and provides explanation of "O… |
| `channel_comments_fr` | Comments on the service standard channel (French) / Commentaires sur le mode de prestation de la norme de service (Francais) | `text` | No |  |  | Comments related to the service standard channel and provides explanation of "O… |
| `target` | Service Standard Target / Cible de la norme relative aux services | `numeric` | No |  |  | The frequency that the organization expects to meet service standard (reported … |
| `volume_meeting_target` | Business Volume That Met Service Standard Target / Volume d&#39;activités qui respectent la cible de la norme relative aux services | `bigint` | No |  |  | Identifies the number of final outputs issued appropriate to the service (eg. p… |
| `total_volume` | Total Volume / Volumes totaux | `bigint` | No |  |  | Identifies the total number of final outputs issued appropriate to the service … |
| `comments_en` | Comments on the service standard in general (English) / Commentaires sur la norme de service en general (anglais) | `text` | No |  |  | Comments related to the service standard in general. |
| `comments_fr` | Comments on the service standard in general (French) / Commentaires sur la norme de service en general (Francais) | `text` | No |  |  | Comments related to the service standard in general. |
| `standards_targets_uri_en` | URL to Service Standards and Targets (English) / URL vers les normes relatives aux services et les cibles (anglais) | `text` | Yes |  |  | Identifies the departmental webpage (Canada.ca) where the service standards and… |
| `standards_targets_uri_fr` | URL to Service Standards and Targets (French) / URL vers les normes relatives aux services et les cibles (français) | `text` | Yes |  |  | Identifies the departmental webpage (Canada.ca) where the service standards and… |
| `performance_results_uri_en` | URL to Real-Time Performance Results (English) / URL aux résultats de rendement en temps réel (anglais) | `text` | No |  |  | Identifies the departmental webpage where the real-time performance results for… |
| `performance_results_uri_fr` | URL to Real-Time Performance Results (French) / URL aux résultats de rendement en temps réel (français) | `text` | No |  |  | Identifies the departmental webpage where the real-time performance results for… |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `fiscal_yr` – Fiscal Year / Année financière

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** fiscal_yr (25 values)  


**Description:**  
EN: Identifies the fiscal year (April 1 to March 31) during which service activities took place. For example, records for fiscal year 2023-2024 should include applications received from April 1, 2023, to March 31, 2024.
  
FR: Indique l'exercice financier (1 avril au 31 mars) durant lequel les activités du service ont eu lieu. Par exemple, les données pour l’exercice financier 2023-2024 devrait inclure les demandes de service qui ont été reçues entre le 1 avril 2023 et le 31 mars 2024.



##### Allowed Values (fiscal_yr)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `2005-2006` | 2005-2006 | 2005-2006 |
| `2006-2007` | 2006-2007 | 2006-2007 |
| `2007-2008` | 2007-2008 | 2007-2008 |
| `2008-2009` | 2008-2009 | 2008-2009 |
| `2009-2010` | 2009-2010 | 2009-2010 |
| `2010-2011` | 2010-2011 | 2010-2011 |
| `2011-2012` | 2011-2012 | 2011-2012 |
| `2012-2013` | 2012-2013 | 2012-2013 |
| `2013-2014` | 2013-2014 | 2013-2014 |
| `2014-2015` | 2014-2015 | 2014-2015 |
| `2015-2016` | 2015-2016 | 2015-2016 |
| `2016-2017` | 2016-2017 | 2016-2017 |
| `2017-2018` | 2017-2018 | 2017-2018 |
| `2018-2019` | 2018-2019 | 2018-2019 |
| `2019-2020` | 2019-2020 | 2019-2020 |
| `2020-2021` | 2020-2021 | 2020-2021 |
| `2021-2022` | 2021-2022 | 2021-2022 |
| `2022-2023` | 2022-2023 | 2022-2023 |
| `2023-2024` | 2023-2024 | 2023-2024 |
| `2024-2025` | 2024-2025 | 2024-2025 |
| `2025-2026` | 2025-2026 | 2025-2026 |
| `2026-2027` | 2026-2027 | 2026-2027 |
| `2027-2028` | 2027-2028 | 2027-2028 |
| `2028-2029` | 2028-2029 | 2028-2029 |
| `2029-2030` | 2029-2030 | 2029-2030 |




---

#### `service_id` – Service ID Number / Numéro d'identification du service

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field cannot contain commas.
 / Ce champ ne doit pas être vide.
Ce champ ne peut pas contenir de virgules.
  


**Description:**  
EN: The unique number assigned to a service in the inventory to make it easier to refer to specific services.  
FR: Le numéro unique attribué à un service dans le répertoire afin de faciliter le référencement à des services précis.


---

#### `service_name_en` – Service Name (English) / Nom du service (en anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field has a maximum length of 350 characters.
 / Ce champ ne doit pas être vide.
Ce champ ne peut excéder une longueur maximale de 350 caractères.
  


**Description:**  
EN: Identifies the official name of the service.  
FR: Indique le nom officiel du service.


---

#### `service_name_fr` – Service Name (French) / Nom du service (en français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field has a maximum length of 350 characters.
 / Ce champ ne doit pas être vide.
Ce champ ne peut excéder une longueur maximale de 350 caractères.
  


**Description:**  
EN: Identifies the official name of the service.  
FR: Indique le nom officiel du service.


---

#### `service_standard_id` – Service Standard ID / Numéro d'identification de la norme relative aux services

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field cannot contain commas.
 / Ce champ ne doit pas être vide.
Ce champ ne peut pas contenir de virgules.
  


**Description:**  
EN: Identifies the unique number assigned to each service standard for that service. Makes it easier for reference purposes as one service may have multiple standards.
  
FR: Indique le numéro unique attribué à chaque norme relative aux services pour ce service. Facilite le référencement, car un service peut avoir de multiples normes.



---

#### `service_standard_en` – Service Standard (English) / Norme relative aux services (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field has a maximum length of 500 characters.
 / Ce champ ne doit pas être vide.
Ce champ ne peut excéder une longueur maximale de 500 caractères.
  


**Description:**  
EN: Identifies the service standard related to a particular service. See Guideline on Service and Digital for format to be used when defining service standards.
  
FR: Indique la norme relative aux services ayant trait à un service en particulier. Voir la Ligne directrice sur les services et le numérique afin de connaître le format à utiliser pour définir les normes relatives aux services.



---

#### `service_standard_fr` – Service Standard (French) / Norme relative aux services (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field has a maximum length of 500 characters.
 / Ce champ ne doit pas être vide.
Ce champ ne peut excéder une longueur maximale de 500 caractères.
  


**Description:**  
EN: Identifies the service standard related to a particular service. See Guideline on Service and Digital for format to be used when defining service standards.
  
FR: Indique la norme relative aux services ayant trait à un service en particulier. Voir la Ligne directrice sur les services et le numérique afin de connaître le format à utiliser pour définir les normes relatives aux services.



---

#### `type` – Service Standard Type / Type de norme relative aux services

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** type (4 values)  


**Description:**  
EN: Identifies the type of service standard as defined in the Guideline on Service and Digital. Access: a commitment outlining the ease and convenience the client should experience when attempting to access a service. Accuracy: a commitment stipulating that the client will receive a service that is up to date, free of errors, and complete. Timeliness: a commitment stating how long the client should expect to wait to receive a service once the service has been accessed.
  
FR: Indique le type de norme relative aux services défini dans la Ligne directrice sur les services et le numérique. Accès: un engagement qui décrit la facilité et la convivialité que devrait connaître le client lorsqu'il essaie d'accéder à un service. Exactitude: un engagement qui stipule que le client recevra un service complet et à jour qui est exempt d'erreurs. Délai: un engagement qui indique le temps d'attente que devrait connaître le client pour recevoir un service une fois qu'il y a accédé.



##### Allowed Values (type)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `ACS` | Access | Accès |
| `ACY` | Accuracy | Exactitude |
| `OTH` | Other | Autre |
| `TML` | Timeliness | Délai |




---

#### `channel` – Service Standard Channel / Mode de prestation de la norme de service

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** channel (7 values)  


**Description:**  
EN: Identifies the service channel to which the service standard applies  
FR: Identifie à quelle mode de prestation de service la norme de service s'applique


##### Allowed Values (channel)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `EML` | Email | Courriel |
| `FAX` | Fax | Télécopieur |
| `ONL` | Online | En ligne |
| `OTH` | Other channel not listed | Autre option qui n’est pas sur la liste |
| `PERSON` | In-Person | En personne |
| `POST` | Postal Mail | Courrier postal |
| `TEL` | Telephone | Téléphone |




---

#### `channel_comments_en` – Comments on the service standard channel (English) / Commentaires sur le mode de prestation de la norme de service (anglais)

**Type:** `text`  
**Required:** No  
**Validation:** This field has a maximum length of 1500 characters. / Ce champ ne peut excéder une longueur maximale de 1500 caractères.  


**Description:**  
EN: Comments related to the service standard channel and provides explanation of "Other" channel selection.  
FR: Commentaires en lien au mode de prestation de la norme de service et fournit une explication de la sélection des modes de prestation « Autre ».


---

#### `channel_comments_fr` – Comments on the service standard channel (French) / Commentaires sur le mode de prestation de la norme de service (Francais)

**Type:** `text`  
**Required:** No  
**Validation:** This field has a maximum length of 1500 characters. / Ce champ ne peut excéder une longueur maximale de 1500 caractères.  


**Description:**  
EN: Comments related to the service standard channel and provides explanation of "Other" channel selection.  
FR: Commentaires en lien au mode de prestation de la norme de service et fournit une explication de la sélection des modes de prestation « Autre ».


---

#### `target` – Service Standard Target / Cible de la norme relative aux services

**Type:** `numeric`  
**Required:** No  
**Validation:** This field must be a single number between 0 and 1 representing a percentage. / Ce champ doit inscrire un seul et unique chiffre entre 0 et 1 représentant un pourcentage.  


**Description:**  
EN: The frequency that the organization expects to meet service standard (reported as a percentage).  
FR: Fréquence à laquelle l'organisation s'attend à respecter sa norme de service (exprimée en pourcentage).


---

#### `volume_meeting_target` – Business Volume That Met Service Standard Target / Volume d'activités qui respectent la cible de la norme relative aux services

**Type:** `bigint`  
**Required:** No  
**Validation:** This value must not be negative. / Cette valeur ne doit être négative.  


**Description:**  
EN: Identifies the number of final outputs issued appropriate to the service (eg. payments issued, requests completed, etc) during the fiscal year that met a particular service standard target for a service. Blank indicates no information available, while 0 indicates that no final outputs issued met service standard targets.
  
FR: Indique le nombre d'opérations de service effectuées (p. ex. les appels auxquels on a répondu, les paiements émis, les demandes traitées, etc.) au cours de l'exercice qui ont respecté une norme relative aux services particulière à un service. Un champ vide indique qu'aucune information n'est disponible, tandis que 0 indique qu'aucun résultat final n'a été émis qui a atteint les objectifs de la norme de service.



---

#### `total_volume` – Total Volume / Volumes totaux

**Type:** `bigint`  
**Required:** No  
**Validation:** This value must not be negative. / Cette valeur ne doit être négative.  


**Description:**  
EN: Identifies the total number of final outputs issued appropriate to the service (eg. payments issued, requests completed, etc) during the fiscal year. Blank indicates no information available, while 0 indicates no final outputs issued.
  
FR: Indique le nombre total d'opérations de service effectuées (p. ex. les paiements émis, les demandes traitées, etc.) relativement à un service au cours de l'exercice. Un champ vide indique qu'aucune information n'est disponible, tandis que 0 indique qu'aucune opération n'a été effectuée.



---

#### `comments_en` – Comments on the service standard in general (English) / Commentaires sur la norme de service en general (anglais)

**Type:** `text`  
**Required:** No  
**Validation:** This field has a maximum length of 2000 characters. / Ce champ ne peut excéder une longueur maximale de 2000 caractères.  


**Description:**  
EN: Comments related to the service standard in general.  
FR: Commentaires en lien à la norme de service en general.


---

#### `comments_fr` – Comments on the service standard in general (French) / Commentaires sur la norme de service en general (Francais)

**Type:** `text`  
**Required:** No  
**Validation:** This field has a maximum length of 2000 characters. / Ce champ ne peut excéder une longueur maximale de 2000 caractères.  


**Description:**  
EN: Comments related to the service standard in general.  
FR: Commentaires en lien à la norme de service en general.


---

#### `standards_targets_uri_en` – URL to Service Standards and Targets (English) / URL vers les normes relatives aux services et les cibles (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field has a maximum length of 1500 characters.
 / Ce champ ne doit pas être vide.
Ce champ ne peut excéder une longueur maximale de 1500 caractères.
  


**Description:**  
EN: Identifies the departmental webpage (Canada.ca) where the service standards and targets are published.  
FR: Indique la page Web ministérielle (Canada.ca) où les normes relatives aux services et les cibles sont publiées.


---

#### `standards_targets_uri_fr` – URL to Service Standards and Targets (French) / URL vers les normes relatives aux services et les cibles (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field has a maximum length of 1500 characters.
 / Ce champ ne doit pas être vide.
Ce champ ne peut excéder une longueur maximale de 1500 caractères.
  


**Description:**  
EN: Identifies the departmental webpage (Canada.ca) where the service standards and targets are published.  
FR: Indique la page Web ministérielle (Canada.ca) où les normes relatives aux services et les cibles sont publiées.


---

#### `performance_results_uri_en` – URL to Real-Time Performance Results (English) / URL aux résultats de rendement en temps réel (anglais)

**Type:** `text`  
**Required:** No  
**Validation:** This field has a maximum length of 1500 characters. / Ce champ ne peut excéder une longueur maximale de 1500 caractères.  


**Description:**  
EN: Identifies the departmental webpage where the real-time performance results for a service are published.  
FR: Identifie la site Web du service sur laquelle les résultats de performance en temps réel d'un service sont publiés.


---

#### `performance_results_uri_fr` – URL to Real-Time Performance Results (French) / URL aux résultats de rendement en temps réel (français)

**Type:** `text`  
**Required:** No  
**Validation:** This field has a maximum length of 1500 characters. / Ce champ ne peut excéder une longueur maximale de 1500 caractères.  


**Description:**  
EN: Identifies the departmental webpage where the real-time performance results for a service are published.  
FR: Identifie la site Web du service sur laquelle les résultats de performance en temps réel d'un service sont publiés.


---




## Appendix

### Choice Sets Summary (All Resources)
| Choice Set | Field(s) | Values | Standalone Doc |
|------------|----------|--------|----------------|


### Generation Metadata

- Generated: 2025-08-31T01:26:25 (UTC)
- Source: dictionaries/service.json
- Commit: `24250a1`
- Tool Version: simple-1

### Validation

- JSON Schema Validation: **PASSED**


### Notes

This documentation is auto-generated. Do not hand-edit; instead update the source recombinant JSON and re-run generation.