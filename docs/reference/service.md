
# Service Inventory / Répertoire de services

**Dataset Type:** `service`  
**Last Generated:** 2026-10-04T04:26:54 (UTC)  
**Source:** dictionaries/service.json  
**Commit:** `22ad121`

Access, upload and modify the Service Inventory of external and internal enterprise services for your organization / Accèder, téléverser et modifier le catalogue des service internes intégrés et externes pour votre organisation

---

## Resources


- [Service Identification Information & Metrics / Renseignements sur l'identification des services, données volumétriques](#service)

- [Service Standards & Performance Results / Normes de service et résultats de rendement](#service-std)


---


## Service Identification Information & Metrics / Renseignements sur l'identification des services, données volumétriques 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `fiscal_yr` | Fiscal Year / Exercice financier | `text` | Yes |  | fiscal_yr | Identifies the fiscal year (April 1 to March 31) during which service activitie… |
| `service_id` | Service ID Number / Numéro d&#39;identification du service | `text` | Yes |  | service_id | The unique number assigned to a service in the inventory to make it easier to r… |
| `service_name_en` | Service Name (English) / Nom du service (anglais) | `text` | Yes |  |  | Identifies the official name of the service. |
| `service_name_fr` | Service Name (French) / Nom du service (français) | `text` | Yes |  |  | Identifies the official name of the service. |
| `service_description_en` | Service Description (English) / Description du service (anglais) | `text` | Yes |  |  | Provides a brief description of the service, in plain language. |
| `service_description_fr` | Service Description (French) / Description du service (français) | `text` | Yes |  |  | Provides a brief description of the service, in plain language. |
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
| `last_service_improvement` | Year of last service improvement based on client feedback / Année de la dernière amélioration du service sur la base de la rétroaction du client | `text` | No |  | last_service_improvement | Identifies the most recent year in which this service was improved based on cli… |
| `sin_usage` | Use of Social Insurance Number / Utilisation du numéro d&#39;assurance sociale (NAS) | `text` | Yes |  | sin_usage | Identifies whether the Social Insurance Number (SIN) is used in the delivery of… |
| `cra_bn_identifier_usage` | Use of CRA Business Number as Standard Identifier / Utilisation du numéro d’entreprise de l’ARC en tant qu’identificateur standard | `text` | Yes |  | cra_bn_identifier_usage | Identifies whether the Canada Revenue Agency's Business Number is used in the d… |
| `num_phone_enquiries` | Number of Telephone Enquiries Received / Nombre de demandes de renseignements reçues par telephone | `text` | Yes |  |  | Identifies the number of enquiries about the service received in this fiscal ye… |
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


#### `fiscal_yr` – Fiscal Year / Exercice financier

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** fiscal_yr (13 values)  


**Description:**  
EN: Identifies the fiscal year (April 1 to March 31) during which service activities took place. For example, records for fiscal year 2023-2024 should include applications received from April 1, 2023, to March 31, 2024.
  
FR: Indique l'exercice financier (1 avril au 31 mars) durant lequel les activités du service ont eu lieu. Par exemple, les données pour l’exercice financier 2023-2024 devraient inclure les demandes de service qui ont été reçues entre le 1er avril 2023 et le 31 mars 2024.



##### Allowed Values (fiscal_yr)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
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




---

#### `service_id` – Service ID Number / Numéro d'identification du service

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field cannot contain commas.
 / Ce champ ne doit pas être vide.
Ce champ ne peut pas contenir de virgules.
  
**Choice Set:** service_id (2673 values)  


**Description:**  
EN: The unique number assigned to a service in the inventory to make it easier to refer to specific services.  
FR: Le numéro unique attribué à un service dans le répertoire afin de faciliter le référencement à des services précis.


##### Allowed Values (service_id)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `1` | Permit to Operate a Rendering Plant | Permis d&#39;exploitation d&#39;une usine de traitement |
| `10` | Procurement | Approvisionnement |
| `1000` | Reconciliation | Réconciliation |
| `1001` | Old Age Security (OAS) Benefits | Prestations de la Sécurité de la vieillesse |
| `1002` | Research Data Centres (RDC) | Centres de données de recherche (CDR) |
| `1003` | Employment Insurance (EI) Benefits | Prestations d’assurance-emploi |
| `1004` | Canada Nature Fund for Aquatic Species at Risk | Le Fonds de la nature du Canada pour les espèces aquatiques en péril |
| `1005` | Canadian Benefit for Parents of Young Victims of Crime | Allocation canadienne aux parents de jeunes victimes de crimes |
| `1006` | Catch Certification Program | Programme de certification des captures |
| `1007` | Canada Apprenticeship Grants | Subventions aux apprentis du Canada |
| `1008` | Aquatic Ecosystems Restoration Fund (AERF) | Fonds de restauration des écosystèmes aquatiques (FREA) |
| `1009` | Fisheries Act Authorizations | Autorisations en vertu de la Loi sur les pêches |
| `1010` | Fisheries and Aquaculture Clean Technology Adoption Program (FACTAP) | Programme d&#39;adoption des technologies propres pour les pêches et l&#39;aquaculture (PTPPA) |
| `1011` | Habitat Stewardship Program for Aquatic Species at Risk | Programme d&#39;intendance de l&#39;habitat pour les espèces aquatiques en péril |
| `1012` | Intergovernmental and International Relations | Relations intergouvernementales et internationales |
| `1013` | Introduction and Transfer Licensing Application Review | Processus d&#39;évaluation de permis d&#39;introduction et de transfert |
| `1014` | National Indigenous Representative Organizations | Organisations autochtones représentatives nationale |
| `1015` | MPA Activity Plan Application Process - Anguniaqvia niqiqyuam MPA | Processus de demande d&#39;activités pour la ZPM - Anguniaqvia niqiqyuam |
| `1016` | MPA Activity Plan Application Process - SGaan Kinghlas-Bowie Seamount MPA | Processus de demande d&#39;activités pour la ZPM - Mont sous-marin SGaan Kinghlas-Bowie |
| `1017` | MPA Activity Plan Application Process - Eastport MPA | Processus de demande d&#39;activités pour la ZPM - Eastport |
| `1018` | MPA Activity Plan Application Process - Endeavour Hydrothermal Vents | Processus de demande d&#39;activités pour la ZPM - Champ hydrothermal Endeavour |
| `1019` | Métis Housing | Logement des Métis |
| `1020` | MPA Activity Plan Application Process - Gilbert Bay MPA | Processus de demande d&#39;activités pour la ZPM - Baie Gilbert |
| `1021` | MPA Activity Plan Application Process - Gully MPA | Processus de demande d&#39;activités pour la ZPM - Gully |
| `1022` | MPA Activity Plan Application Process - Hecate Strait/Queen Charlotte Sound Glas | Processus de demande d&#39;activités pour la ZPM - Détroit d&#39;Hécate |
| `1023` | Inuit Housing | Logement des Inuit |
| `1024` | MPA Activity Plan Application Process - Musquash Estuary MPA | Processus de demande d&#39;activités pour la ZPM - Estuaire de la Musquash |
| `1025` | MPA Activity Plan Application Process - St. Anns Bank MPA | Processus de demande d&#39;activités pour la ZPM - Banc de Sainte-Anne |
| `1026` | National Online License System (NOLS) | Système national d&#39;émission de permis en ligne (SNEPL) |
| `1027` | National Recreational Licensing System (NRLS) (Pacific Only) | Système national d&#39;émission de permis de pêche récréative (SNDPP) |
| `1028` | Observer Designation Application and Renewal Processing | demandes de désignation d&#39;observateur et des demandes de renouvellement |
| `1029` | Oceans Management Contribution Program in support of oceans conservation and management | Programme de contributions pour la gestion des océans pour appuyer l&#39;élaboration et la mise en œuvre d&#39;activités de conservation et de gestion des océans |
| `1030` | Oceans Management Program - Grants in support Indigenous Groups in the Development and Implementation of Oceans Conservation and Management Activities | Programme de gestion des océans - Subventions à l’appui des groupes autochtones dans l’élaboration et la mise en œuvre d’activités de conservation et de gestion des océans |
| `1031` | Recreational Fisheries Conservation Partnerships Program Contribution Agreements | Programme de partenariats relatifs à la conservation des pêches récréatives |
| `1032` | Salmon Conservation Stamp | Timbre de protection du saumon |
| `1033` | Small Craft Harbours Class Contribution Program | Programme de contribution du MPO aux ports pour petits bateaux |
| `1034` | Small Craft Harbours Divestiture Class Grant Program | Programme de dessaisissement des ports pour petits bateaux |
| `1035` | Species at Risk Act Permits | Les permis de la Loi sur les espèces en péril |
| `1036` | Marine Environmental and Hazards Response | Intervention en cas de dangers et d’incidents environnementaux maritimes |
| `1037` | Icebreaking | Déglaçage |
| `1038` | Provision of Distress and Safety Communications | Prestation de services de communication de détresse et de sécurité |
| `1039` | Provision of Marine Information | Diffusion de renseignements maritimes |
| `1040` | Provision of Radio Communications and Public Correspondence Service | Prestation de services de correspondance publique et de communications radio |
| `1041` | Search and Rescue Coordination | Recherche et sauvetage Coordination |
| `1042` | Orientation sessions for persons with a priority entitlement. | Droit de priorité: Séances d&#39;orientation pour les bénéficiares d&#39;un droit de priorité |
| `1043` | Search and Rescue Response | Recherche et sauvetage |
| `1044` | Vessel Screening and Regulation of Vessel Traffic Movements | Contrôle des navires et réglementation des mouvements du trafic maritime |
| `1045` | Waterways Management | Gestion des voies navigables |
| `1046` | Release of Statistical Data on International Trade | Diffusion de données statistiques sur le commerce international |
| `1047` | Release of Statistical Data on Balance of Payment | Diffusion de données statistiques sur la balance de paiement |
| `1048` | Ministerial Designations for Protective Services by the RCMP | Désignations ministérielles pour les Services de la protection par la GRC |
| `1050` | Cadet Online Registration | Inscription en ligne pour les cadets |
| `1051` | Military History and Heritage | Histoire et patrimoine militaires |
| `1052` | Access to Information and Privacy | Accès à l&#39;information et de la protection des renseignements personnels |
| `1053` | Assistance connecting with foreign markets | Aide pour accéder aux marchés étrangers |
| `1054` | Acquiring Surplus Equipment | Acquisition De Biens Excédentaires |
| `1055` | Drugs and Medical Devices: Permission to Market | Médicaments et instruments médicaux : Autorisation de mise en marché |
| `1056` | Executrek Program | Programme ExécuTrek |
| `1057` | Legacy Sites Unexploded Explosive Ordnance (UXO) Program | Programme des munitions explosives non explosées (UXO) sur le anciens sites |
| `1058` | Compensation for Employers of Reservists Program (CERP) | Programme de Dédommagement des Employeurs de Réservistes |
| `1059` | Natural Health Products: Permission to Market | Produits de santé naturels : Autorisation de mise en marché |
| `1060` | Natural Health Products: Permission to Operate | Produits de santé naturels : Autorisation d&#39;exploitation |
| `1062` | Drugs and Medical Devices: Right to Sell Domestically | Médicaments et instruments médicaux : Droit de vendre à l&#39;échelle nationale |
| `1064` | Innovation for Defence Excellence and Security (IDEaS) | Innovation pour la défense, l’excellence et la sécurité (IDEeS) |
| `1065` | Mobilizing Insights in Defence and Security (MINDS) | Mobilisation des idées nouvelles en matière de défense et de sécurité (MINDS) |
| `1066` | Ministerial Correspondence Unit | Unité de la correspondance ministérielle |
| `1088` | Special Access Programs | Programmes d&#39;accès spéciale |
| `1089` | Food Market Authorization and Standards | Autorisation et normes du marché alimentaire |
| `1090` | Wage Earner Protection Program | Programme de protection des salariés |
| `1091` | Analytical testing services | Services d’analyse |
| `1092` | Science Horizons Youth Internship Program | Programme de stages Horizons Sciences pour les jeunes |
| `1093` | General Enquiry and Referral Telephone Service (1-800 O Canada) | Demande de renseignements généraux et service d’aiguillage par téléphone (1-800 O Canada) |
| `1094` | People Information Management Automated Request Tracker - Information/Data Request Service | Renseignements de gestion des personnes et données sur les demandes de service |
| `1095` | National Print Services | Service d&#39;impression national |
| `1096` | Occupational Health and Safety Tribunal Canada | Tribunal de santé et sécurité au travail Canada |
| `1097` | Individual Income Tax Returns | Déclaration d&#39;impôt sur le revenus des particuliers |
| `1098` | Authorize a Representative | Autoriser un Représentant |
| `1099` | GST/HST Returns | Production d&#39;une déclaration de la TPS/TVH |
| `1100` | GST/HST Rulings | Décisions en matière de TPS/TVH |
| `1101` | T2 Corporation Income Tax Returns | Déclaration de revenus des sociétés T2 |
| `1102` | Excise Duty, Excise Tax, Air Travellers Security Charge, and Fuel Charge returns | Droits d&#39;accise, taxes d&#39;accise, droit pour la sécurité des passagers du transport aérien, et déclaration de la redevance sur les combustibles |
| `1103` | IT Interoperability - GC Interop | Interopérabilité TI - GC Interop |
| `1104` | Income Tax Rulings | Décisions en Impôt |
| `1105` | Charity Information Return Filing | Déclaration de renseignements des organismes de bienfaisance |
| `1106` | Partnership Information Returns | Déclaration de Renseignements des Sociétés de Personnes |
| `1107` | Canada child benefit (CCB) applications | Les demandes d&#39;Allocation canadienne pour enfants (ACE) |
| `1108` | Tax Credit Application | Demande de crédit d&#39;impôt |
| `1109` | Children&#39;s Special Allowances (CSA) applications | Les demandes d&#39;Allocations Spéciales pour Enfants (ASE) |
| `1110` | Advanced Canada workers benefit (ACWB) | Avance de l’allocation canadienne pour les travailleurs (AACT) |
| `1111` | Provincial and territorial tax credit payments | Les versements de crédits d&#39;impôt provinciaux et territoriaux |
| `1112` | Provincial and territorial child benefit program payments | Les versements provinciaux et territoriaux pour les programmes de prestations pour enfants |
| `1113` | Formal Review Request (Objections) | Demande de vérification officielle (Oppositions) |
| `1114` | Public Enquiries | Demandes de renseignement |
| `1115` | Trust Income Tax Returns | Dépôt des déclarations de revenus des fiducies |
| `1116` | Business Number (BN) Registration | Inscription d&#39;un Numéro d&#39;Entreprise (NE) |
| `1117` | Access to Information and Privacy | Accès à l&#39;information et à la protection des renseignements personnels |
| `1118` | Prime Minister&#39;s Email | Courriel du premier ministre |
| `1119` | Copyright Tariff Setting | Établissement de tarifs liés au droit d’auteur |
| `1120` | Issuance of licences for the use of copyright works when the owner is unlocatable | Délivrance de licences pour les oeuvres protégées par un droit d&#39;auteur lorsque le titulaire est introuvable |
| `1121` | Public Notices of funding opportunities | Avis publics concernant les possibilités de financement |
| `1122` | Public enquiries | Demandes de renseignements du publique |
| `1123` | Public Notices of Successful Funding Applications | Avis publics concernant les demandes de financement retenues |
| `1126` | Funding transfers to administering institutions | Transfert des fonds aux établissements administrateurs |
| `1127` | Direct funding payments | Versement direct des fonds |
| `1128` | Grants and Awards Management | Gestion des subventions et bourses |
| `1129` | Access to Information and Privacy | Loi sur l’accès à l’information et Loi sur la protection des renseignements personnels |
| `1130` | GCshare | GCpartage |
| `1131` | Funding Services | Services de financement |
| `1132` | Diagnostic Testing and Reference Services | Tests de diagnostic et Services de référence |
| `1133` | Training and Guidance on the Duty to Consult | Formation et conseils sur l&#39;obligation de consulter |
| `1134` | Aboriginal and Treaty Rights Information System (ATRIS) and Training on using the system. | Système d&#39;information sur les droits ancestraux et issus de traités (SIDAIT) et formation sur l&#39;utilisation du système. |
| `1135` | Modern Treaty Management Environment (MTME) | Environnement de gestion des traités modernes (EGTM) |
| `1136` | Consultation Protocols and Resource Centres | Protocoles de consultation et centres de ressources |
| `1137` | Executive Correspondence | Correspondance de haute gestion |
| `1138` | Training &amp; Education on Modern treaties &amp; Self-Government Agreements | Formation et éducation sur les traités modernes et les ententes sur l’autonomie gouvernementale |
| `1139` | Individual Tax Enquiries (Contact Centre) | Demandes de renseignements sur l&#39;impôt des particuliers (Centre de contact) |
| `1140` | The First Nations Fiscal Management Act and its institutions. | La Loi sur la gestion financière des Premières Nations et ses institutions. |
| `1141` | Business Enquiries (Contact Centre) | Demandes de renseignements des entreprises (Centre de contact) |
| `1142` | Microbiological Emergency Response Team | Équipe d&#39;intervention d&#39;urgence |
| `1143` | Benefit Enquiries (Contact Centre) | Demandes de renseignements sur les prestations (Centre de contact) |
| `1144` | Pay and Benefits | Rémunération et avantages sociaux |
| `1145` | Maintain and update the Indian Register | Tenir le Registre des Indiens et le mettre à jour |
| `1146` | Disability Tax Credit | Crédit d&#39;impôt pour personnes handicapées |
| `1147` | My Government of Canada Human Resources (MyGCHR) | Mes ressources humaines du gouvernement du Canada (MesRHGC) |
| `1148` | Secure Certificate of Indian Status | Certificat sécurisé de statut d&#39;Indien |
| `1149` | Canada.ca | Canada.ca |
| `1150` | Treaty Payments Events | Paiement événements dans les traités |
| `1151` | Treaty Annuity Payments | Paiement des annuités prévues dans les traités |
| `1153` | Complaint Management - Human Rights | Gestion des plaintes - Droits de la personne |
| `1154` | Registration of persons with a priority entitlement | Inscription des personnes bénéficiant d&#39;un droit de priorité |
| `1155` | Identification of persons with a priority entitlement to vacant positions | Identification des personnes ayant le droit de priorité aux postes vacants |
| `1156` | Process permission requests from public servants seeking to be a candidate in an election | Traiter les demandes de permission des fonctionnaires souhaitant se porter candidats à une élection |
| `1157` | Targeted Contribution Funding to Support Climate Change Projects | Fonds de contribution ciblés pour soutenir les projets liés aux changements climatiques |
| `1158` | Official Language proficiency: Exclusions on medical grounds | Compétence en matière de langues officielles : Exemptions pour des raisons d&#39;ordre médical |
| `1159` | Provide minerals prospecting permits | Délivrer des permis de prospection |
| `1160` | Provide mineral claims | Délivrer des claims miniers |
| `1161` | Provide mining leases | Délivrer des baux miniers |
| `1162` | Provide licenses to prospect for minerals | Délivrer des licences de prospection des minéraux |
| `1163` | Provide coal exploration licenses, location permits and leases | Délivrer des permis de recherche de gisement de houille, des permis et des concessions d&#39;un emplacement |
| `1164` | Provide Crown land use permits | Fournir des permis d&#39;utilisation des terres de la Couronne |
| `1165` | Provide Crown land surface leases | Fournir des baux de surface pour les terres de la Couronne. |
| `1166` | Northern Participant Funding Program | Programme d&#39;aide financière aux participants du Nord |
| `1167` | Provide funding and advice to support Indigenous entrepreneurship and business d | Fournir du financement et des conseils pour soutenir l’entrepreneuriat autochtone et le développement des entreprises. |
| `1172` | FSWEP; Ongoing student recruitment inventory for hiring managers | Programme fédéral d&#39;expérience de travail étudiant: Répertoire d&#39;étudiants pour les gestionnaires |
| `1173` | Compliance - Employment Equity | Conformité - Équité en matière d&#39;emploi |
| `1176` | Post-secondary Co-op / Internship Program (CO-OP); Recruitment options for managers | Programme postsecondaire d&#39;enseignement coopératif / de stages: Options de recrutement pour les gestionnaires |
| `1178` | Provide funding and advice to support First Nation Economic Development Capacity | Fournir des conseils et du financement afin d’appuyer la capacité et la préparation du développement économique des Premières Nations. |
| `1179` | Research Affiliate Program (RAP); Recruitment options for managers | Programme des adjoints de recherche: Options de recrutement pour les gestionnaires |
| `1180` | Post-Secondary Recruitment Program (PSR); Recruitment options for managers | Programme de recrutement postsecondaire: Options de recrutement pour les gestionnaires |
| `1182` | Indian Land Registry | Registre des terres indiennes |
| `1183` | Recruitment of Policy leaders (RPL); Recruitment options for managers | Recrutement de leaders en politiques: Options de recrutement pour les gestionnaires |
| `1187` | Access to Information and Privacy Request Services | Service de demandes d&#39;accès à l&#39;information et protection des renseignements personnels |
| `1188` | With First Nation consent, administer and process additions to reserve applicati | Avec le consentement des Premières Nations, administrer et traiter les demandes d’ajout aux réserves afin de soutenir le développement communautaire et économique durable des Premières Nations. |
| `1190` | Additions to Reserve | Ajouts aux réserves |
| `1193` | Regulatory Development under the First Nations Commercial and Industrial Develop | Développement de règlements en vertu de la Loi sur le développement commercial et industriel des Premières Nations |
| `1195` | Public Service Resourcing System (PSRS); PSRS Help desk | Système de ressourcement de la fonction publique (SRFP): Service de dépannage du SRFP |
| `1196` | Procurement Strategy for Aboriginal Business and the Indigenous Business Directo | Stratégie d&#39;approvisionnement auprès des entreprises autochtones et Le répertoire des entreprises autochtones |
| `1197` | Indigenous Business Directory | Annuaire des entreprises autochtone |
| `1198` | Meeting Statutory/ Regulatory Obligations with Respect to Elections and Lawmakin | Respect des obligations statutaires ou réglementaires en matière d’élections et de législation |
| `1199` | Access to Capital | Accès au capital |
| `12` | Procurement Training Services | Services de formation sur l&#39;approvisionnement |
| `1200` | Prime Minister&#39;s Website | Site Web du premier ministre |
| `1202` | Personnel Psychology Centre; Assessment accommodation | Centre de psychologie du personnel: Mesures d&#39;adaptation en matière d&#39;évaluation |
| `1204` | Personnel Psychology Centre; Test Services | Centre de psychologie du personnel: Services d&#39;évaluation |
| `1208` | Environmental Funding - Community Interaction Program | Programme Interactions communautaires |
| `1210` | Personnel Psychology Centre;Consultation Services | Centre de psychologie du personnel: Services de consultation |
| `1211` | Measuring Device Prototype Approvals (new approvals) | Approbation des prototypes d&#39;appareils de mesure (nouvelles approbations) |
| `1212` | First Nation Land Management | Gestion des terres des Premières Nations |
| `1213` | Reserve Land and Environment Management Program | Programme de gestion de l&#39;environnement et des terres de réserves |
| `1214` | Matrimonial Real Property | Biens Immobiliers Matrimoniaux |
| `1215` | Land Use Planning | Planification de l&#39;utilisation des terres |
| `1216` | First Nations Solid Waste Management Initiative | Initiative de gestion des matières résiduelles des Premières Nations |
| `1217` | Environmental Review Process | Processus d&#39;évaluation environnementale |
| `1218` | Authorized Service Provider Accreditation, Registration and Renewal | Renouvellement d&#39;un fournisseur de services autorisé |
| `1219` | Contaminated Sites On Reserve Program | Programme des sites contaminés dans les réserves |
| `1220` | Approvals | Approbations |
| `1221` | Bankruptcy and Insolvency Records Search | Recherche de dossiers de faillite et d&#39;insolvabilité |
| `1222` | Licensed Insolvency Trustee (LIT) Licence Renewal | Renouvellement de Licence de syndics autorisés en insolvabilité (SAI) |
| `1223` | Heritage Designations | Désignation patrimoniales |
| `1225` | Federal Heritage Buildings Review Office | Bureau d&#39;examen des édifices fédéraux du patrimoine |
| `1228` | Rulings / Interpretations | Décisions / interprétations |
| `1229` | Amend, upon ministerial approval, Schedule I of The First Nation Oil And Gas And | Modifier, avec l’approbation ministérielle, l’annexe 1 de la Loi sur la gestion du pétrole et du gaz des fonds des Premières Nations pour y inclure les Premières Nations ayant tenu avec succès un vote visant à permettre l’exercice de la gouvernance a |
| `1230` | With First Nation consent, issue leases, permits or licenses to industry stakeho | Avec le consentement des Premières Nations, délivrer des baux, des permis ou des licences aux intervenants de l’industrie pour faciliter la prospection pétrolière et gazière et la mise en valeur des ressources sur les terres des Premières Nations. As |
| `1231` | Information and Transaction Services | Le service d&#39;information et de transaction |
| `1232` | Media Relations | Relations avec les médias |
| `1233` | Funding for Essential Community-Based Services: First Nations Child and Family Services | Financement des services essentiels communautaires: Services à l’enfance et à la famille des Premières Nations |
| `1234` | Licensed Insolvency Trustee (LIT) License Issuance Decisions | Décisions sur l&#39;octroi d&#39;une licence de syndic autorisé en insolvabilité (SAI) |
| `1235` | Incorporations | Incorporations |
| `1236` | Funding for Essential Community-Based Services: Assisted Living | Financement des services essentiels communautaires : aide à la vie autonome |
| `1237` | Nuans - Provide Corporate Name Search Report | Nuans-Générer un rapport de dénomination |
| `1238` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnel |
| `1239` | Funding for Essential Community-Based Services: Income Assistance | Financement des services essentiels communautaires : aide au revenu |
| `1240` | Futurpreneur Canada | Futurpreneur Canada |
| `1241` | Funding Essential Community-Based Services: Family Violence Prevention Shelter Program | Financement des services essentiels communautaires : Programme pour la prévention de la violence familiale |
| `1242` | Canadian Passport | Passeport canadien |
| `1243` | Canada Small Business Financing Program (CSBFP) | Programme de financement des petites entreprises du Canada (PFPEC) |
| `1244` | Merger Review - Competition Law Enforcement | Examen des fusions – Application du droit de la concurrence |
| `1245` | Funding for Essential Community-Based Services: Family Violence Prevention Shelt | Financement des services essentiels communautaires : Financement aux refuges pour la prévention de la violence familiale |
| `1246` | Information Centre - Law Enforcement | Centre d&#39;information - Application de la loi |
| `1247` | Funding for Essential Community-Based Services: Urban Programming for Indigenous Peoples | Financement des services essentiels communautaires : Programmes urbains pour les peuples autochtones |
| `1248` | CA Identification Number Application &amp; Updates | Numéro d&#39;identification CA Demande et mises à jour |
| `1249` | Copies of Corporate Documents and Certificates | Copies de documents constitutifs et certificats |
| `125` | Domestic Statistics and Market Information Web | Statistiques canadiennes et site Web d&#39;information sur les marchés |
| `1250` | Written Opinions | Avis écrits |
| `1251` | Capital Confirmations | Confirmations de la qualité des fonds propres |
| `1252` | In-Person Service | Service en personne |
| `1253` | Register Industrial Designs | Enregistrement de dessins industriels |
| `1254` | Office for Client Satisfaction | Bureau de la satisfaction des clients |
| `1255` | Register Copyrights | Enregistrement de droits d&#39;auteur |
| `1256` | Labour Market Impact Assessment | Études d’impact sur le marché du travail |
| `1257` | Disability Pension and Pain and Suffering Compensation | Pension d&#39;invalidité et indemnité pour douleur et souffrance |
| `1258` | Register Trademarks | Enregistrement de marques de commerce |
| `1260` | Canada Lands Survey System | Système d&#39;arpentage des terres du Canada |
| `1261` | Career Impact Allowance | Allocation pour incidence sur la carrière |
| `1262` | Exceptional Incapacity Allowance | Allocation d&#39;incapacité exceptionnelle |
| `1263` | Treatment Allowance | Allocation de traitement |
| `1264` | Attendance Allowance | Allocation pour soins |
| `1265` | IP Advisory Services | Service de conseils en PI |
| `1266` | Management of Grants and Contributions (Gs&amp;Cs) for Employment and Social Development Programs | Administration des subventions et contributions (S et C) pour les programmes d’Emploi et Développement social |
| `1267` | Grant Patents | Délivrance de brevets |
| `1268` | Connect to Innovate (CTI) | Brancher pour innover |
| `1269` | Financial Support for Long Term Care | Aide financière pour soins de longue durée |
| `127` | Canadian Soil Information Services (CanSIS) | Système d’information sur les sols du Canada (SISCan) |
| `1270` | Healthcare Costs and Supports | Coûts de soins de santé et soutien |
| `1271` | Veterans Independence Grants &amp; Reimbursements | Programme pour l&#39;autonomie des anciens combattants – Subventions et remboursements |
| `1272` | Educational Assistance for Children | Aide à l&#39;éducation pour les enfants |
| `1273` | War Veterans Allowance | Allocation aux anciens combattants |
| `1274` | Accessible Technology Development Program (ATP) | Programme de développement de la technologie accessible |
| `1275` | IRAP Grants and Contributions | Subventions et contributions du PARI |
| `1276` | Connecting Families Initiative (CFi), formerly Affordable Access Initiative | L&#39;initiative Familles branchées, anciennement l&#39;Initiative d&#39;accès abordable |
| `1277` | Care and Maintenance of Veterans&#39; Graves | Programme d&#39;entretien des stèles funéraires |
| `1278` | Earnings Loss Benefit | Allocation pour perte de revenus |
| `1279` | Public Recognition and Awareness | Reconnaissance et sensibilisation du public |
| `1280` | Commemorative Partnerships | Programme de partenariat pour la commémoration |
| `1281` | Funeral and Burial | Aide pour les funérailles et l&#39;inhumation |
| `1282` | Computers for School Plus (CFS+) | Ordinateurs pour les écoles et Plus (OPE+) |
| `1283` | Career Transition Services | Services de réorientation professionnelle |
| `1284` | Emergency Financial Support for Veterans | Aide financière d&#39;urgence pour les vétérans |
| `1286` | Veteran and Family Well-being Fund | Fonds pour le bien-être des vêtêrans et de leur famille |
| `1287` | Digital Literacy Exchange Program (DLEP) | Programme d&#39;échange en matière de littératie numérique |
| `1288` | Retirement Income Security Benefit | Allocation de sécurité du revenu de retraite |
| `1289` | Digital Skills for Youth (DS4Y) | Programme de compétences numériques pour les jeunes (CNJ) |
| `129` | Geospatial | Produits géospatiaux |
| `1290` | Work-Sharing | Travail partagé |
| `1291` | Contributions Program for Non-Profit Consumer and Voluntary Organizations | Programme de contributions pour les organisations sans but lucratif de consommateurs et de bénévoles |
| `1292` | Provision of a Social Insurance Number | Émission d’un numéro d’assurance sociale |
| `1293` | Job Bank - Find a Job | Guichet-Emplois– Trouver un emploi |
| `1294` | Job Bank for Employers | Guichet-Emplois pour les employeurs |
| `1295` | Labour Market Information | Information sur le marché du travail |
| `1296` | Canada Student Grants and Canada Student Loans | Bourses canadiennes pour étudiants et Prêts canadiens aux étudiants |
| `1297` | ATIP Online request platform | Plateforme de demande d’AIPRP en ligne |
| `1298` | Canada Apprentice Loans | Prêt canadien aux apprentis |
| `1299` | Contact Us- General Information to Data Users and Technical Support to Survey Respondents | Contactez-nous - Information générale aux utilisateurs des données et support technique aux répondants |
| `13` | Information and Education Services to Businesses | Services d&#39;information et de formation aux entreprises |
| `130` | Drought Watch | Guetter la sécheresse |
| `1300` | Funding Essential Community-Based Services: Elementary and Secondary Education | Financement des services essentiels communautaires : financement de l’éducation primaire et secondaire |
| `1301` | Clean Growth Hub | Carrefour de la croissance propre |
| `1302` | First Nations and Inuit Skills Link Program | Programme Connexion compétences à l’intention des Premières Nations et des Inuits |
| `1303` | Certification, Coordination, and Technical Analysis for Broadcast Radio and TV | Certification, coordination et analyse technique pour la radiodiffusion et la télévision |
| `1304` | Issuing Radio Operator Certificates | Délivrance de certificats d&#39;opérateur radio |
| `1305` | First Nations and Inuit Summer Work Experience Program | Programme Expérience d&#39;emploi d’été pour les étudiants inuits et des Premières Nations |
| `1306` | Issuing Radio/Spectrum Licences | Délivrance de licences radio et de spectre |
| `1307` | Strategic Innovation Fund (SIF) Online Application | Demande en ligne du Fonds stratégique pour l&#39;innovation (FSI) |
| `1308` | Grants and Contributions | Subventions et contributions |
| `1309` | My StatCan | Mon StatCan |
| `131` | Office of Intellectual Property and Commercialization | Bureau de la propriété intellectuelle et de la commercialisation (BPIC) |
| `1310` | First Nations and Inuit Cultural Education Centres Program Funding | Financement du Programme des centres éducatifs et culturels des Premières Nations et des Inuits |
| `1311` | Issuance of permits | Émission des permis |
| `1312` | Indspire | Indspire |
| `1313` | First Nations, Métis Nation and Inuit Post-Secondary Education Strategies | Stratégies d’éducation postsecondaire des Premières Nations, de la Nation métisse et des Inuits |
| `1314` | Métis Nation Post-Secondary Education Strategy | Stratégie d’éducation postsecondaire de la Nation métisse |
| `1315` | Radio and Terminal Equipment Certification | Homologation de l&#39;équipement radio et du matériel terminal |
| `1316` | Inuit Post-Secondary Strategy | Stratégie d’éducation postsecondaire des Inuits |
| `1317` | Release of Statistical Data on the Monthly Gross Domestic Product (GDP) by Industry | Diffusion de données statistiques sur le produit intérieur brut mensuel (PIB) par industrie |
| `1318` | Release of Statistical Data on the Quarterly Gross Domestic Product (GDP) | Diffusion de données statistiques sur le produit intérieur brut trimestriel (PIB) |
| `1319` | Release of Statistical Data on Manufacturing Sector | Diffusion de données statistiques sur le secteur de la fabrication |
| `132` | Saint-Hyacinthe Research and Development Centre&#39;s Industrial Program | Programme industriel du Centre de recherche et de développement de Saint-Hyacinthe |
| `1320` | Release of Statistical Data on Retail Trade | Diffusion de données statistiques sur le commerce de détail |
| `1321` | Release of Statistical Data on Enterprise Finances | Diffusion de données statistiques sur les finances des entreprises |
| `1322` | Canada Education Savings Grant and Canada Learning Bond | Subvention canadienne pour l’épargne-études et Bon d’études canadien |
| `1323` | CanCode | CodeCan |
| `1325` | Critical Injury Benefit | Indemnité pour blessure grave |
| `1326` | Capital Model Approvals | Approbation des modèles de fonds propres |
| `1327` | Release of Statistical Data on Wholesale Trade | Diffusion de données statistiques sur le commerce de gros |
| `1328` | Access to Information and Privacy | Accès à l&#39;information et de protection des renseignements personnels |
| `1329` | Actuarial Services | Services actuariels |
| `133` | AgriInvest | Agri-investissement |
| `1330` | Consumer Price Index (CPI) | l&#39;Indice des prix à la consommation (IPC) |
| `1331` | Canada Disability Savings Grant and Canada Disability Savings Bond | Subvention canadienne pour l’épargne-invalidité et Bon canadien pour l’épargne-invalidité |
| `1332` | ISED Citizen Services Centre | Centre de services aux citoyens d&#39;ISDE |
| `1333` | BizPal | PerLe |
| `1334` | Canadian Occupational Projection System | Système sur la projection des professions du Canada |
| `1335` | Business Benefits Finder | Outil de recherche d&#39;aide aux entreprise |
| `1336` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `1337` | Occupational Health and Safety Compliance and Enforcement (OHSCE) | Conformité et application de la Santé et sécurité au travail (CASST) |
| `1338` | Northern Ontario Development Program (NODP) | Programme de développement du Nord de l&#39;Ontario (PDNO) |
| `1339` | Client Service Centre (CSC) | Centre de services à la clientèle |
| `134` | AgriStability | Agri-stabilité |
| `1340` | Regional Economic Growth through Innovation (REGI) | Croissance économique régionale par l&#39;innovation (CERI) |
| `1341` | Merchant Seamen Compensation Act (MServCanA) | Loi sur l’indemnisation des marins marchands |
| `1342` | Women Entrepreneurship Strategy (WES) Ecosystem Fund | Fonds pour l&#39;écosystème de la SFE |
| `1343` | Release of Statistical Data on Industrial Product Index (IPPI) | Diffusion de données statistiques sur l&#39;Indice des prix des produits industriels (IPPI) |
| `1344` | Community Futures Program | Programme de développement des collectivités (PDC) |
| `1345` | Economic Development Initiative (EDI) | Initiative de développement économique (IDE) |
| `1346` | Innovation Superclusters Initiative | Initiative des supergrappes d&#39;innovation |
| `1347` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `1348` | Treasury Board of Canada Secretariat’s Claims Office | Bureau des réclamations du Secrétariat du Conseil du Trésor du Canada |
| `1349` | Open Government Portal - Access to data and information | Portail gouvernement ouvert – accès à l’information ouverte et données ouvertes. |
| `135` | Farm Debt Mediation Service | Service de médiation en matière d&#39;endettement agricole |
| `1350` | Classification Program | Programme de classification |
| `1351` | Release of Statistical Data on Census of Population | Diffusion de données statistiques sur le Recensement de la population |
| `1352` | Labour Force Survey | Enquête sur la population active |
| `1353` | Release of Statistical Data on Employment, Payroll and Hours | Diffusion de données statistiques sur l&#39;emploi, la rémunération et les heures de travail |
| `1354` | Client Services- Custom Products | Services au Client - Produits personnalisés |
| `1355` | Statistical Capacity Building – Workshops, Training and Conferences | Renforcement des capacités statistiques - Ateliers, formations et conférences |
| `1356` | National Allegations and Complaints | Plaintes et allégations nationales |
| `1357` | Assessment and Investigations | Services d&#39;examen et d&#39;enquêtes |
| `1358` | Fraud Awareness | Sensibilisation à la fraude |
| `1359` | National Allegations and Complaints | Plaintes et allégations nationales |
| `136` | AgriAssurance: National Industry Association Component | Programme Agri-assurance : Volet Associations nationales de l&#39;industrie |
| `1360` | Forensic Investigations | Enquêtes juricomptable |
| `1361` | Fraud Awareness Training | Formation de sensibilisation a la fraude |
| `1364` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels (AIPRP) |
| `1365` | Executive correspondence services | Services de la correspondance de la haute direction |
| `1366` | Departmental Library | Bibliothèque ministérielle |
| `1367` | Public Enquiries | Renseignements au public |
| `1368` | Canadian Forces Income Support Benefit | Allocation de soutien du revenu des Forces canadiennes |
| `1369` | Administration of Grants &amp; Contributions (Gs&amp;Cs) Service for the Labour Program | Administration des subventions et contributions (S et C) pour le Programme du travail |
| `137` | AgriMarketing Program: National Industry Association | Programme Agri-marketing : Volet Associations nationales de l&#39;industrie |
| `1370` | Labour Management Collaboration Program (also known as Workplace Harassment and | Programme de collaboration syndicale-patronale (aussi connu sous le nom de Fonds de prévention du harcèlement et de la violence en milieu de travail) |
| `1371` | Federal Workers&#39; Compensation | Service fédéral d’indemnisation des accidentés du travail |
| `1372` | Priority Entitlement; Support of medically released veterans with a priority entitlement | Droit de priorité: Soutien aux anciens combattants possédant un droit de priorité |
| `1373` | Federal Mediation and Conciliation Service (FMCS) | Service fédéral de médiation et de conciliation (SFMC) |
| `1374` | Labour Standards Compliance and Enforcement (LSCE) | Conformité et application des normes du travail (CANT) |
| `1375` | Legislated Employment Equity Program (LEEP) | Programme légiféré d&#39;équité en matière d&#39;emploi |
| `1376` | Federal Contractors Program (FCP) | Programme de contrats fédéraux |
| `1377` | Workplace Information Services | Services d’information sur les milieux de travail |
| `138` | AgriScience Program: Projects | Programme Agri-science - projets |
| `1380` | Supplementary Retirement Benefit | Prestation de retraite supplémentaire |
| `1383` | Administration of the Corrections and Conditional Release Regulations | Application du Règlement sur le système correctionnel et la mise en liberté sous condition |
| `1387` | Media enquiries | Demandes de renseignements des médias |
| `1388` | Public enquiries | Renseignements au public |
| `1389` | Orders in Council (OIC) | Décrets |
| `139` | AgriInnovate Program | Programme Agri-innover |
| `1391` | View our Reference Resources | Consultez nos ressources de références |
| `1393` | Read our Analysis | Lisez nos analyses |
| `1397` | Investigations; Conduct investigations on staffing irregularities and improper political activities. | Enquêtes: Mener des enquêtes sur les irrégularités en dotation et les activités politiques irrégulières |
| `14` | GC WAN | Réseau étendu du RGC |
| `140` | AgriRisk: Administrative Capacity Stream | Initiatives Agri-risques: Volet de renforcement des capacités administratives |
| `1403` | Monitoring Services: Surveys and analytical databases | Activités de surveillance: Sondages et bases de données analytiques |
| `1407` | Personal Information Requests Services | Services de demande d’accès à des renseignements personnels |
| `1410` | Grants and contributions | Subventions et contributions |
| `1411` | Leaders&#39; Debates Commission | La Commission aux débats des chefs |
| `1412` | Security Intelligence Review Committee (SIRC) | Le Comité de surveillance des activités de renseignement de sécurité (CSARS) |
| `1413` | National Security and Intelligence Committee of Parliamentarians (NSICOP) | Le Comité des parlementaires sur la sécurité nationale et le renseignement (CPSNR) |
| `1414` | Information about Surveys and for Survey Participants | Renseignements au sujet des enquêtes et pour les participants aux enquêtes |
| `1415` | Access our Statistical Data | Accédez à nos données statistiques |
| `1419` | Rehabilitation Services and Vocational Assistance | Services de réadaptation et d&#39;assistance professionnelle |
| `1420` | Temporary Foreign Workers - Application for Work Permit | Travailleurs étrangers temporaires - Demande de permis de travail |
| `1421` | International Mobility Program: Opinion and Enquires to Employers | Programme de mobilité internationale : Opinion et demandes de renseignements aux employeurs |
| `1422` | Electronic Travel Authorization | Autorisation de voyage électronique |
| `1423` | Temporary Resident Visa | Visa de résident temporaire |
| `1424` | Visitor Record (In-Canada) | Fiche du visiteur (au Canada) |
| `1425` | Restoration of status (In-Canada) | Rétablissement du statut (au Canada) |
| `1426` | Temporary Resident Permit | Permis de résident temporaire |
| `1427` | Temporary Resident Permit for Victims of Trafficking in Persons | Permis de résident temporaire pour les victimes de trafic de personnes |
| `1428` | Study Permit | Permis d&#39;études |
| `1429` | International Experience Canada - Application for Work Permit | Expérience internationale Canada - Demande d&#39;un permis de travail |
| `1430` | Federal Skilled Worker - Application for Permanent Residence | Travailleurs qualifiés (fédéral) - Demande de résidence permanente |
| `1431` | Federal Skilled Trades - Application for Permanent Residence | Travailleurs de métiers spécialisés (fédéral) - Demande de résidence permanente |
| `1432` | Provides a retail subsidy and a Harvesters Support Grant and Community Food Programs Fund to eligible communities | Fournit une subvention au commerce de détail et une subvention de soutien aux récoltants aux communautés éligibles. |
| `1433` | Canadian Experience Class - Application for Permanent Residence | Catégorie de l&#39;expérience canadienne - Demande de résidence permanente |
| `1434` | Start-up Visa - Application for Permanent Residence | Visa pour démarrage d&#39;entreprise - Demande de résidence permanente |
| `1435` | Immigrant Investor Venture Capital (IIVC) | Capital de risque pour les immigrants investisseurs (CRII) |
| `1436` | Federal Self employed - Application for Permanent Residence | Travailleurs autonomes (fédéral) - Demande de résidence permanente |
| `1437` | Live In Caregivers - Application for Permanent Residence | Aides familiaux résidants - Demande de résidence permanente |
| `1438` | Caring for Children or for People with High Medical Needs - Application for Perm | Garde d&#39;enfants ou soins aux personnes ayant des besoins médicaux élevés - Demande de résidence permanente |
| `1439` | Quebec Skilled Workers/Trades - Application for Permanent Residence | Travailleurs qualifiés – Québec - Demande de résidence permanente |
| `144` | AgriCompetitiveness | Programme Agri-compétitivité |
| `1440` | Quebec Business (Entrepreneur, Investor, Self-employed) - Application for Perma | Gens d&#39;affaires au Québec (entrepreneurs, investisseurs, travailleurs autonomes) - Demande de résidence permanente |
| `1441` | Provincial Nominees - Application for Permanent Residence | Candidats des provinces - Demande de résidence permanente |
| `1442` | Family Class Priority - Application for Permanent Residence | Demandes prioritaires de la catégorie du regroupement familial - Demande de résidence permanente |
| `1443` | Parents and Grandparents - Application for Permanent Residence | Parents et grands-parents - Demande de résidence permanente |
| `1444` | Other Relatives - Sponsorship for Permanent Residence | Autres membres de la famille - Parrainage pour la résidence permanente |
| `1445` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `1446` | Spouse or common-law partner in Canada - Application for Permanent Residence | Époux ou conjoints de fait au Canada - Demande de résidence permanente |
| `1447` | Temporary Resident Permit Holder - Application for Permanent Residence | Titulaire d&#39;un Permis de séjour temporaire - Demande de résidence permanente |
| `1449` | Humanitarian &amp; Compassionate - Application for Permanent Residence | Motifs d&#39;ordre humanitaire - Demande de résidence permanente |
| `145` | Youth Employment and Skills Program | Programme d’emploi et de compétences des jeunes |
| `1450` | Resettled Refugees - Permanent Residence | Réfugiés réinstallés - Résidence Permanente |
| `1451` | Humanitarian Public Policy - Application for resettlement to Canada | Politique d&#39;intérêt public humanitaire -Demande de réinstallation au Canada |
| `1452` | Fire Management | Gestion du Feu |
| `1453` | Immigration Loan | Prêts aux immigrants |
| `1454` | One-year window - Application for Permanent Residence of eligible dependants | Délai prescrit d&#39;un an - demande de résidence permanente de personnes à charge admissibles |
| `1455` | Protected Person &amp; Dependants - Permanent Residence | Personne protégée et personnes à charge - Résidence Permanente |
| `1456` | Search and Rescue | recherche et sauvetage |
| `1457` | In-Canada Asylum Claim | Octroi de l&#39;asile au Canada |
| `1458` | Access to information and privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1459` | The Issuance of a Danger Opinion | Émission d&#39;un avis de danger |
| `146` | Canadian Agricultural Strategic Priorities Program | Programme canadien des priorités stratégiques de l’agriculture |
| `1460` | Settlement Transfer Payments | Paiements de transfert, Programme d’établissement |
| `1461` | Federal Internship for Newcomers Program | Programme fédéral de stage pour les nouveaux arrivants |
| `1462` | Larkin Kerwin Library | Bibliothèque Larkin-Kerwin |
| `1463` | Pre-removal Risk Assessment | Examen des risques avant renvoi |
| `1464` | Permanent Resident Card Renewals &amp; Replacements | Renouvellement et remplacement de carte de résident permanent |
| `1465` | Issuance of a Permanent Resident Travel Document | Délivrance d&#39;un titre de voyage de résident permanent |
| `1466` | Resettlement Assistance Program Transfer Payments: Contributions to Service Provider Organisations | Paiements de transfert du Programme d&#39;aide à la réinstallation: Contributions aux fournisseurs de services |
| `1467` | Earth Observation Satellite Data services | Services des données satellitaires en observation de la terre |
| `1468` | The International Charter: Space and Major Disasters | Charte Internationale: espace et catastrophes majeures |
| `1469` | Space situational awareness (SSA) analysis reports (CRAMS) | Rapports d&#39;analyses de surveillance de l&#39;espace (CRAMS) |
| `147` | Agricultural Greenhouse Gas Program | Programme de lutte contre les gaz à effet de serre en agriculture |
| `1470` | Resettlement Assistance Program Transfer Payments: Income Support to Refugees in Canada | Paiements de transfert du Programme d&#39;aide à la réinstallation: Soutien du revenu aux réfugiés au Canada |
| `1471` | Interim Federal Health: Reimbursements to Health Care Professionals | Remboursement dans le cadre du programme fédéral de santé intérimaire |
| `1472` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1473` | Space Astronomy &amp; Space Situational Awareness Imagery | Imagerie spatiale pour la surveillance de l&#39;espace et l&#39;astronomie spatiale |
| `1474` | Satellite-based Automated Identification of Ships (S-AIS) Data Services | Services de données du système d&#39;identification automatique spatioporté (AIS) |
| `1475` | Climate Research Data | Données pour la recherche sur le climat |
| `148` | Canada Pavilion Program | Programme du pavillon du Canada |
| `1480` | Provision of Interim Federal Health Program coverage to eligible beneficiaries | Couverture pour les bénéficiaires admissibles au Programme fédéral de santé intérimaire |
| `1481` | Medical Surveillance Notification | Notification de la surveillance médicale |
| `1482` | Citizenship Grant- Application for Citizenship under Sections 5(1), 5(2), of the | Attribution de citoyenneté - Demande de citoyenneté au titre des articles 5 (1) et 5(2) de la Loi sur la citoyenneté |
| `1483` | Provide crown land quarry permits/leases | Fournir des permis ou des baux d&#39;exploitation de carrière sur des terres de la Couronne |
| `1484` | Application for Grant of Citizenship - Stateless Individual with a Canadian pare | Demande d&#39;attribution de citoyenneté aux personnes apatrides avec un parent canadien |
| `1485` | Application for Grant of Citizenship - Adopted Individual | Demande d&#39;attribution de citoyenneté à une personne adoptée |
| `1486` | Resumption of Citizenship | Réintégration de la citoyenneté |
| `1487` | Renunciation of Citizenship | Répudiation de la citoyenneté |
| `1488` | Proof of Citizenship | Preuve de citoyenneté |
| `1489` | Search of Citizenship Records | Recherche de documents de citoyenneté |
| `149` | Market Intelligence and Information Service | Services de renseignements sur les marchés |
| `1490` | Citizenship Education &amp; Outreach | Éducation et sensibilisation à la citoyenneté |
| `1491` | Issuance of a Regular Passport | Délivrance d&#39;un Passeport régulier |
| `1492` | Issuance of a Diplomatic Passport | Délivrance d&#39;un Passeport diplomatique |
| `1493` | Issuance of Special Passports | Délivrance de Passeport spécial |
| `1494` | Certificate of Identity | Certificat d&#39;identité |
| `1495` | Refugee Travel Document | Titre de voyage pour réfugiés |
| `1496` | Issuance of an Emergency Travel Document | Délivrance d&#39;un Titre de voyage d&#39;urgence |
| `1497` | Visa facilitation for Official Travel | Facilitation de l&#39;octroi des visas pour les voyages officiels |
| `1498` | Addition of a special stamp in a passport or other travel document | Ajout d&#39;une estampille spéciale sur le passeport ou un autre titre de voyage |
| `1499` | Addition of an observation in a passport or other travel document | Ajout d’une observation sur un passeport ou un autre titre de voyage |
| `15` | Mobile Devices | Gestion des appareils mobiles d’entreprise |
| `150` | Market Access Single Window | Guichet unique pour l&#39;accès aux marchés |
| `1500` | Certifying true copies of part of a passport or another travel document | Certifier les copies conformes d&#39;une partie d&#39;un passeport ou d&#39;un autre titre de voyage |
| `1501` | Verification of Status / Replacement of Immigration Document | Vérification du statut ou remplacement d&#39;un document d&#39;immigration |
| `1502` | Personnel Security | Service de sécurité aux employés |
| `1503` | Amendments to historical records or valid Temporary Resident documents | Modifications apportées à des dossiers historiques ou à des documents de résident temporaire valides |
| `1504` | Physical Security: Access Control | Sécurité physique: contrôle des accès |
| `1505` | Access to Information Request Services | Services d&#39;accès à l&#39;information |
| `1506` | NFB Archives | ONF Archives |
| `1507` | ATIP Consultative Services | Services consultatifs de l&#39;AIPRP |
| `1508` | Determination of Rehabilitation for criminality or serious criminality | Décision sur la réadaptation dans les cas de criminalité ou de grande criminalité |
| `1509` | ATIP Compliance Services | Services de conformité de l&#39;AIPRP |
| `1510` | Renunciation of Permanent Residency | Renonciation au statut de résident permanent |
| `1511` | Authorization to return to Canada | Autorisation de revenir au Canada |
| `1512` | IRCC Web Validation Portal | Portail de validation Web de l&#39;Immigration, réfugiés et Cittoyeneté Canada |
| `1513` | Global Assistance to Irregular Migrants | Aide mondiale aux migrants irréguliers |
| `1514` | Access to Information | Accès à l’information |
| `1515` | Ice Assistance Emergency Program | Programme d&#39;urgence d&#39;aide liée aux conditions des glaces |
| `1516` | Privacy | Protection des renseignements personnels |
| `1517` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1518` | Responses to queries from Authorized Representatives | Réponses aux questions des représentants |
| `1519` | Earth Observation Data Service | Service de données d&#39;observation de la Terre |
| `152` | Canada Brand | Guichet unique pour l&#39;accès aux marchés - Marque Canada |
| `1520` | Global Skills Strategy - Work Permit Application | Stratégie en matière de compétences mondiales - Demande de Permis de travail |
| `1521` | Canadian Hazards Information Service (Targeted) | Service canadien d&#39;information sur les risques (ciblé) |
| `1522` | Canadian Spatial Reference System | Système canadien de référence spatiale |
| `1523` | Atlantic Immigration Pilot - Application for Permanent Residence | Programme pilote d&#39;immigration au Canada atlantique - Demande de résidence permanente |
| `1524` | Canadian Wildland Fire Information System | Système canadien d&#39;information sur les feux de végétation |
| `1525` | Flight Operations | Operations Aériennes |
| `1526` | Public Screenings | Projections publiques |
| `1527` | Case Management | Gestion de cas |
| `1528` | Media Enquiries | Demandes des médias |
| `1529` | Media Enquiries | Demandes des médias |
| `153` | Access to Information and Privacy | L&#39;accès à l&#39;information et de la protection des renseignements personnels |
| `1530` | Industry Advisory Service / Northern Projects Management Office (NPMO) | Soutien de l&#39;industrie / Le Bureau de gestion des projets nordiques (BGPN) |
| `1531` | Social media responses to public enquiries | Réponses aux demandes de renseignements publiques dans les médias sociaux |
| `1532` | Funds to Support Education and Training for Veterans | Fonds pour appuyer les études et la formation des vétérans |
| `1533` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `1534` | Social Media Responses to Public Enquiries | Réponses aux demandes de renseignements publiques dans les médias sociaux |
| `1535` | Contribution Program for the Centre of Excellence for the Marine Transportation | Programme de contribution au Centre d’excellence pour le transport maritime des hydrocarbures et de gaz naturel liquéfié (GNL) |
| `1536` | Community Participation Funding Program | Programme de financement de la participation communautaire |
| `1537` | Program to Protect Canada&#39;s Coastlines and Waterways | Programme de protection du littoral et des voies navigables du Canada |
| `1538` | Building Canada Fund (Infrastructure Canada Program - TC manages agreements on b | Fonds Chantiers Canada (programme d&#39;Infrastructure Canada - TC gère des ententes pour le compte d&#39;Infrastructure Canada) |
| `1539` | Canada Strategic Infrastructure Fund (Infrastructure Canada Program - TC manages | Fonds canadien sur l&#39;infrastructure stratégique (programme d&#39;Infrastructure Canada - TC gère des ententes pour le compte d&#39;Infrastructure Canada) |
| `154` | Dairy Processing Investment Fund | Fonds d&#39;investissement dans la transformation des produits laitiers |
| `1540` | Border Infrastructure Fund (Infrastructure Canada Program - TC manages agreement | Fonds sur l&#39;infrastructure frontalière (programme d&#39;Infrastructure Canada - TC gère des ententes pour le compte d&#39;Infrastructure Canada) |
| `1541` | Gateways and Border Crossings Fund | Fonds pour les portes d&#39;entrée et les passages frontaliers |
| `1542` | Asia-Pacific Gateway and Corridor Transportation Infrastructure Fund | Fonds d&#39;infrastructure de transport de l&#39;Initiative de la Porte et du Corridor de l&#39;Asie-Pacifique |
| `1543` | National Trade Corridors Fund | Fonds national des corridors commerciaux |
| `1544` | Enforcement of Private Buoy Regulations for privately owned floating information | Règlement sur les bouées privées pour les balises d&#39;information flottantes appartenant à des particuliers en vertu de la Loi de 2001 sur la marine marchande du Canada. |
| `1545` | Receiver of Wreck Program under the Canada Shipping Act 2001 | Programme des receveur d&#39;épaves en vertu de la Loi de 2001 sur la marine marchande du Canada |
| `1546` | Management of exemptions of prohibited activities on navigable waterways | Gestion des exemption en lien avec des activités interdites sur les eaux navigables |
| `1547` | National Science Library | Bibliothèque scientifique nationale |
| `1548` | International Events and Convention Services Program (IECSP) | Programme des services aux événements internationaux et aux congrès (PSEIC) |
| `1549` | Federal Science Libraries Network (FSLN) | Réseau des bibliothèques scientifiques fédérales (RBSF) |
| `155` | CSC National Victim Services Program | Programme national de services aux victims du SCC |
| `1550` | Access to Information and Privacy Acts | Lois sur l&#39;accès à l&#39;information et la protection des renseignements personnels |
| `1551` | Technical Services | Services techniques |
| `1552` | Research Services | Services de recherches |
| `1553` | Codes Canada | Codes Canada |
| `1554` | Canada&#39;s official time | Heure officielle du Canada |
| `1555` | Instrument Calibration Services | Services d&#39;étalonnage d&#39;instruments |
| `1556` | Calibration laboratory assessment service | Service d&#39;évaluation des laboratoires d&#39;étalonnage |
| `1557` | Certified Reference Materials | Matériaux de référence certifiés |
| `1558` | IRAP Advisory Services to Firms | Services consultatifs du PARI aux entreprises |
| `156` | Dairy Farm Investment Program Producers | Programme d&#39;investissement pour fermes laitières |
| `1560` | IRAP Advisory Services through Contributions to Organizations | Services-conseils du PARI - contributions aux organismes |
| `1561` | Legal Advice, Counsel, and Representation for Veterans | Avis, conseils et représentation juridiques destinés aux vétérans |
| `1562` | Operating a federal railway | Exploitation d&#39;un chemin de fer fédéral |
| `1563` | Conduct outreach and training sessions for other government departments and Indi | Organiser des séances de sensibilisation et de formation pour les autres ministères et les entreprises autochtones. |
| `1564` | Rail Safety Improvement Program (RSIP) | Programme d&#39;amélioration de la sécurité ferroviaire (PASF) |
| `1565` | Rail security | Sûreté du transport ferroviaire |
| `1566` | Child car seat safety | Sécurité des sièges d&#39;auto pour enfants |
| `1567` | Defects and recalls of vehicles, tires and child car seats | Défauts et rappels de véhicules, de pneus et de sièges d&#39;auto pour enfants |
| `1568` | Driver Assistance Technologies | Technologies d&#39;aide à la conduite |
| `1569` | Safety standards for vehicles, tires and child car seats | Normes de sécurité pour véhicules, pneus et sièges d&#39;auto pour enfants |
| `157` | Access to Information and Privacy | Accès à l’information et de protection des renseignements personnels |
| `1570` | Stay safe when driving | Conduire en toute sécurité |
| `1571` | School bus safety activities | Activités de sécurité des autobus scolaires |
| `1572` | Vehicle Importation to and Manufacturing in Canada | Importation et fabrication de véhicules au Canada |
| `1573` | Innovative technologies | Technologies novatrices |
| `1574` | Motor Carriers, Commercial Vehicles and Drivers | Exigences pour véhicules utilitaires, transporteurs routiers et les conducteurs |
| `1575` | Research and testing on vehicles and child car seats | Sièges d&#39;auto pour enfant et véhicules : Recherche et mise à l&#39;essai |
| `1576` | Media Enquiries | Demandes des médias |
| `1577` | Road security | Sûreté routière |
| `1578` | Public Enquiries | Renseignements au public |
| `1579` | Road Safety Transfer Payment Program | Programme de paiement de transfert de sécurité routière |
| `158` | AgriAssurance: Small and Medium-sized Enterprise | Programme Agri-assurance : Volet Petites et moyennes entreprises |
| `1580` | Transportation of Dangerous Goods Program | Le programme du Transport des marchandises dangereuses |
| `1581` | Approval of Emergency Response Assistance Plans (ERAP) | l&#39;agrément des plans d&#39;intervention d&#39;urgence (PIU) |
| `1582` | CANUTEC - Canadian Transport Emergency Centre | CANUTEC - Centre canadien d&#39;urgence transport |
| `1583` | Major Project Management Office Tracker | Suivi des projets du Bureau de gestion des grands projets |
| `1584` | Airport Capital Assistance Program (ACAP) | Programme d&#39;aide aux immobilisations aéroportuaires |
| `1585` | Airport Operations and Maintenance Subsidy Program | Programme de subvention à l&#39;exploitation et à l&#39;entretien des aéroports |
| `1586` | Allowances to former employees of Newfoundland Railways, Steamships and Telecomm | Allocations aux anciens employés des services des chemins de fer, des navires à vapeur et des télécommunications de Terre-Neuve mutés aux Chemins de fer nationaux du Canada |
| `1587` | Ferry Services Contribution Program | Programme de contribution pour les services de traversier |
| `1588` | Issuance of Kimberley Process certificates for the export of rough diamonds | Délivrance des certificats du Processus de Kimberley pour l&#39;exportation des diamants bruts |
| `1589` | Grant to the Province of British Columbia in respect of the provision of ferry a | Subvention à la province de la Colombie-Britannique à l&#39;égard de la prestation de services de traversier et de cabotage pour marchandises et voyageurs |
| `1590` | Labrador Coastal Airstrips Restoration Program | Programme de réfection des bandes d&#39;atterrissage de la côte du Labrador |
| `1591` | Northumberland Strait Crossing subsidy payment under the Northumberland Strait C | Paiement de subvention pour l&#39;ouvrage de franchissement du détroit de Northumberland selon la Loi sur l&#39;ouvrage de franchissement du détroit de Northumberland (législatif). |
| `1592` | Outaouais Road Development Agreement | Entente d&#39;aménagement des routes de l&#39;Outaouais |
| `1593` | Payments to the Canadian National Railway Company in respect of the termination | Versements à la Compagnie des chemins de fer nationaux du Canada (CN) à la suite de l’abolition des péages sur le pont Victoria à Montréal et pour la réfection de la voie de circulation du pont (législatif) |
| `1594` | Ports Asset Transfer Program | Programme de transfert des installations portuaires |
| `1595` | Transportation Association of Canada | Association des transports du Canada |
| `1596` | Remote Passenger Rail Program | Programme de contributions pour les services ferroviaires voyageurs |
| `1597` | Media Enquiries | Demandes des médias |
| `1598` | Aircraft Parking | Stationnement des aéronefs |
| `1599` | Farm Products Council of Canada Reports and Publications | Rapports et publications du Conseil des produits agricoles du Canada |
| `16` | Videoconferencing | Vidéoconférence |
| `160` | Information Services | Services d&#39;information |
| `1600` | Vehicle Parking | Stationnement des véhicules |
| `1601` | Creation and distribution of Farm Products Council of Canada&#39;s Focus newsletter | Création et distribution du bulletin Focus du Conseil des produits agricoles du Canada |
| `1602` | General Terminal: Domestic and International | Accès à l&#39;aérogare : Vols intérieurs et internationaux |
| `1603` | Aircraft Landing – Domestic, International and Flying Training | Atterrissage d&#39;avions – Vols intérieurs, internationaux et instruction de vol |
| `1604` | Emergency Response Services Outside Normal Operating hours | Services d&#39;intervention d&#39;urgence en dehors des heures normales de service |
| `1605` | Annual Mobile Equipment Registration | L&#39;enregistrement annuelle d&#39;équipement mobile |
| `1606` | Management of obstructions to navigation | Gestion des obstacles à la navigation |
| `1607` | Harbour Dues | Service de port |
| `1608` | Approval of ‘works&#39; on Canada&#39;s navigable waterways under the Canadian Navigable | Approbation d&#39;ouvrages sur les voies navigables du Canada en vertu de la Loi sur la protection de la navigation. |
| `1609` | Marine security | Sûreté maritime |
| `161` | AgriDiversity | Programme Agri-diversité |
| `1610` | Marine accidents and investigations | Accidents maritimes et enquêtes |
| `1611` | Marine pollution and environmental response | Pollution marine et intervention environnementale |
| `1612` | Vessel design, construction and maintenance | Conception, construction et entretien des bâtiments |
| `1613` | Public Ports - Berthage | Service d&#39;amarrage |
| `1614` | Vessel licensing and registration | Permis et immatriculation des bateaux |
| `1615` | Public Ports - Storage | Service d&#39;entreposage |
| `1616` | Boating Safety Contribution Program | Programme de contributions pour la sécurité nautique |
| `1617` | Incident Management &amp; Response (Coast Guard reports, Duty Officer, PNR Arctic mo | Urgences maritimes |
| `1618` | Public Ports - Utilities and Other Services | Services publics et autres services |
| `1619` | Public Ports - Wharfage &amp; Transfer | Service de quayage et de transfert |
| `162` | Indigenous Agriculture and Food Systems Initiative | Initiative sur les systèmes agricoles et alimentaires autochtones |
| `1620` | Vessel inspection and certification | Inspection et certification des bâtiments |
| `1621` | Program to Advance Transportation Innovation: Program to Advance Connectivity an | Programme de promotion de l&#39;innovation en matière de transport : Programme de promotion de la connectivité et l&#39;automatisation du système de transports |
| `1622` | Marine training and certification of individuals | Formation et certification maritime |
| `1623` | Innovative Solutions Canada | Solutions Innovatrices Canada |
| `1624` | Program to Advance Indigenous Reconciliation | Programme visant à favoriser la réconciliation avec les peuples autochtones |
| `1625` | Transport Canada Situation Centre | Centre d&#39;intervention de Transports Canada |
| `1626` | Enforce the Coasting Trade Act - Penalties and Periods of Sanction | Application de la loi sur le cabotage - Sanctions et périodes de sanction |
| `1627` | Respond to designation requests by Canadian airlines | Répondre aux demandes de désignation des lignes aériennes canadiennes |
| `1628` | Financial Recognition for Veterans&#39; Caregivers | Reconnaissance financière pour les aidants de vétérans |
| `1629` | Ministerial and Deputy Correspondance | Correspondance ministérielle et du sous-ministre |
| `163` | Living Laboratories Initiative: Collaborative Program | Initiative des laboratoires vivants : Programme de collaboration |
| `1631` | Grants and Contributions to support the Northern Transportation Adaptation Initi | Subventions et contributions pour soutenir l&#39;initiative d&#39;adaptation du transport dans le nord |
| `1632` | Grants and Contributions to support the Transportation Assets Risk Assessment In | Subventions et contributions pour soutenir l&#39;initiative d&#39;évaluation des risques liés aux actifs de transport |
| `1633` | Veteran Family Program | Programme pour les familles des vétérans |
| `1634` | Grants and Contributions to Support Clean Transportation Initiatives | Subventions et contributions pour soutenir des initiatives de transport propre |
| `1635` | Grant to the International Civil Aviation Organization (ICAO) for Cooperative De | Subvention au Programme de développement coopératif de la sécurité opérationnelle et de maintien de la navigabilité de l&#39;Organisation de l&#39;aviation civile internationale (OACI) |
| `1636` | Payments to other governments or international agencies for the operation and ma | Versements aux autres gouvernements ou organismes internationaux pour l&#39;exploitation et l&#39;entretien des aéroports, des installations de navigation aérienne et des voies aériennes |
| `1637` | Commercial air services | Services aériens commerciaux |
| `1638` | Aircraft airworthiness | Navigabilité des aéronefs |
| `1639` | Provide Environmental Assessment Related Technical Advice | Fournir des conseils techniques connexes à l&#39;évaluation environnementale |
| `164` | AgriMarketing Program: Small and Medium-sized Enterprisers | Programme Agri-marketing : Volet Petites et moyennes entreprises |
| `1640` | Licences for the manufacture, storage and sale of explosives | Licences pour la fabrication, l&#39;entreposage et la vente des explosifs |
| `1641` | Authorization of explosives | Autorisation des explosifs |
| `1642` | Analysis and Certification of Explosives | Analyse et certification des explosifs |
| `1643` | National Fireworks Certification Program | Programme national de certification des artificiers |
| `1644` | Control of Explosives Precursor Chemicals (Restricted Components) | Contrôle des précurseurs chimique d’explosifs (composants d’explosif limités) |
| `1645` | Importing, Exporting and Transporting-in-Transit Permits | Permis d&#39;Importation, exportation et transport en transit |
| `1646` | Processing, by an employee of the Department of Transport, of a medical certific | Traitement par un employé du ministère des Transports d&#39;un certificat médical relativement à une licence de pilote ou à un permis de pilote, sauf un permis d&#39;élève-pilote |
| `1647` | Security Screening | Contrôle de sécurité |
| `1648` | Licensing for pilots and personnel | Délivrance de licences pour les pilotes et le personnel |
| `1649` | Registering and leasing aircraft | Immatriculation et location des aéronefs |
| `165` | Dispute Resolution | Règlement des Différends |
| `1650` | Air navigation services | Services de navigation aérienne |
| `1651` | Aviation accidents and investigations | Accidents d&#39;aviation et enquêtes |
| `1652` | Pipeline Arbitration Secretariat | Secrétariat d&#39;arbitrage des pipelines |
| `1653` | ENERGY STAR® Portfolio Manager Energy Benchmarking Tool | Outil d&#39;analyse comparative ENERGY STAR® Portfolio Manager |
| `1654` | Greening Government Services, and Federal Buildings Initiative | Services pour un gouvernement vert et l&#39;Initiative des bâtiments fédéraux |
| `1655` | General operating and flight rules | Règles générales d&#39;utilisation et de vol des aéronefs |
| `1656` | NRCan searchable product list for regulated and ENERGY STAR certified products | List de produts interrogeables de RNCan permettant de rechercher des produits réglementés et certifiés ENERGY STAR |
| `1657` | SmartWay Transportation Partnership | Partenariat de transport SmartWay |
| `1658` | Public enquiries | Demandes du public |
| `1659` | Training of pilots and aviation personnel | Instructeurs de vol et personnel de l&#39;aviation |
| `166` | Rule-Making | Prise de Règlements |
| `1660` | Licensing for aircraft maintenance engineers (AME) | Licences de technicien d&#39;entretien d&#39;aéronefs (TEA) |
| `1661` | Operating airports and aerodromes | Exploitation d&#39;aéroports et d&#39;aérodromes |
| `1662` | Aviation security | Sûreté aérienne |
| `1663` | Drone safety | Sécurité des drones |
| `1664` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1665` | Hangar and Ground Handling | Hangars et services au sol |
| `1666` | Aircraft Services Logistics | Logistique entourant le services des aéronefs |
| `1668` | Aircraft Engineering | Service de génie en aéronautique |
| `1669` | Aircraft Maintenance | Entretien des aéronefs |
| `167` | Determinations and Compliance | Déterminations et Conformité |
| `1670` | NDTCB: General Standards Board certification for non-destructive testing | Organisme de certification nationale en essais non destructifs de Ressources naturelles Canada : certification par l&#39;Office des normes générales du Canada en essais non destructifs |
| `1671` | Canadian Space Agency Class Grants and Contributions Program | Programme global des subventions et contributions de l&#39;Agence spatiale canadienne |
| `1672` | NDTCB: Portable tube-based X-ray fluorescence analyzer operator certification | Organisme de certification nationale en essais non destructifs de Ressources naturelles Canada : certification des opérateurs d&#39;analyseur à fluorescence rayons X à tube à rayons X portatif |
| `1673` | NDTCB: Written examination for the CNSC’s exposure device operator certification | Organisme de certification nationale en essais non destructifs de Ressources naturelles Canada : examen écrit de certification des opérateurs d&#39;appareils d&#39;exposition de la Commission canadienne de sûreté nucléaire |
| `1674` | Canadian Certified Reference Materials Project | Projet canadien des matériaux de référence certifiés |
| `1675` | Transportation Fuels website | Site Web Info-Carburant |
| `1676` | Diesel testing and certification | Essai et certification des moteurs diesel |
| `1677` | The Canadian Astronomy Data Centre (CADC) | Le Centre canadien de données astronomiques (CCDA) |
| `1678` | Grants and Contributions | Subventions et Contributions |
| `1679` | Canadian Impact Assessment Registry | Registre canadien d’évaluation d’impact |
| `168` | Information, Advice and Expertise | Information, Conseils et Expertise |
| `1680` | Physical Security Abroad – Security, Maintenance and Service Line Delivery | Sécurité Physique à l&#39;étranger - Sécurité, Entretien et Service d&#39;Exécution des Projets de ligne |
| `1681` | Engineering Services | Services d&#39;ingénierie |
| `1682` | Capital Project Delivery Services | Services de Réalisation de Projets immobiliers |
| `1683` | Missions Operations | Opérations des missions |
| `1684` | Real Property Transactions Services | Services de transactions immobilières |
| `1685` | International Project Delivery Services | Services internationaux de réalisation de projets |
| `1686` | Professional and Technical Services (e.g. architectural, engineering and interio | Services professionnels et techniques (services d’architecture, d’ingénierie et de design d’intérieur, par exemple) |
| `1688` | International Procurement and Contracting Services | Services internationaux d&#39;approvisionnement et de contrats |
| `1689` | Global Logistics Services | Services logistiques mondiaux |
| `169` | Funding Decisions for Scholarships and Fellowships | Décisions sur le financement des bourses |
| `1690` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `1691` | Grants and Contributions for International Assistance | Subventions et contributions pour l&#39;aide internationale |
| `1693` | Results-based management (RBM) and risk management information sessions provided | Appui fourni aux partenaires potentiels et existants en matière de gestion axée sur les résultats (GAR) et gestion du risque |
| `1694` | Results Based Management (RBM) resources (center of excellence) | Ressources en matière de Gestion axée sur les résultats (GAR) |
| `1695` | Canadian sanctions | Sanctions canadiennes |
| `1696` | Export Import Control Systems Support | Prise en charge des Systèmes des contrôles à l&#39;exportation et à l&#39;importation |
| `1697` | Jules Léger Library | Bibliothèque Jules-Léger |
| `1698` | Export and Import Permit Service | Service des licences d&#39;exportation et d&#39;importation |
| `1699` | Authentication of documents | Authentification des documents |
| `17` | Contact Centre | Centre de contact |
| `170` | Receiving Financial Transaction Reports | Réception de déclaration d&#39;opérations financières |
| `1700` | Intelligence Surveillance Reconnaissance | Renseignement, surveillance et reconnaissance |
| `1701` | Aircraft Operations and Maintenance Training | Formation sur les opérations et l&#39;entretien des aéronefs |
| `1702` | Parliamentary Affairs | Relations avec le Parlement |
| `1703` | Ministerial non-GIC appointments and GIC non-diplomatic appointments | Nominations ministérielles non effectuées par le gouverneur en conseil et nominations non diplomatiques effectuées par le gouverneur en conseil |
| `1704` | Strategic Governance, Ministerial Correspondence | Gouvernance stratégique, Correspondance ministérielle |
| `1705` | Corporate and common service management and delivery for DM and MIN offices | Services corporatif et services communs livré aux bureaux des ministres et des sous-ministres |
| `1706` | Access to Information and Privacy (ATIP) | Accès à l&#39;information et la protection des renseignements personnels |
| `1707` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1708` | Geo.ca | Geo.ca |
| `1709` | National Air Photo Library | Photothèque nationale de l&#39;air |
| `171` | Disclosures of Financial Intelligence | Communications de renseignements financiers |
| `1710` | Environmental Assessment done by Review Panels | Évaluation environnementale par une commission d&#39;examen |
| `1711` | Open Science &amp; Technology Repository (OSTR) | Dépôt ouvert des sciences &amp; technologies (DOST) |
| `1712` | Natural Resources Canada Library | Bibliothèque de Ressources naturelles Canada |
| `1713` | David Florida Laboratory: Spacecraft assembly, integration and testing centre | Laboratoire David-Florida : Centre d&#39;intégration, d&#39;assemblage et d&#39;essai d&#39;engins spatiaux |
| `1714` | Environmental Assessment done by the Agency | Évaluations environnementales réalisées par l&#39;Agence |
| `1715` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `1716` | ecoENERGY for Housing - Enquiries | écoÉNERGIE pour l&#39;habitation – Demandes de renseignements |
| `1717` | Access to Information and Privacy | Accès à l&#39;information et la protection des renseignements personnels |
| `1718` | Environmental Assessment done by Substitution | Évaluation environnementale par substitution |
| `1719` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `172` | Enquiries for Reporting Entities | Demandes de renseignements d&#39;entités déclarantes |
| `1720` | Request for assistance for outbreak or Federal public health surge support(s) | Demande d&#39;assistance pour de l&#39;aide en cas d&#39;éclosion ou la poussée fédérale de la santé soutient |
| `1721` | Respond to Correspondence Addressed to the Minister | Répondre aux correspondances adressées au ministre |
| `1722` | Respond to Correspondence Addressed to the President | Répondre aux correspondances adressées au président |
| `1724` | Jacob Finkelman Library | Bibliothèque Jacob Finkelman |
| `1725` | Social Security Tribunal Secretariat Call Centre | Centre d&#39;appels du secrétariat du Tribunal de la sécurité sociale |
| `1726` | Financial Literacy | Littératie financière |
| `1728` | Access to information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1729` | Federal On-Reserve School Operations and Funding | Financement et fonctionnement des écoles fédérales dans les réserves |
| `173` | Funding Decisions for Scholarships and Fellowships | Décisions sur le financement des bourses |
| `1731` | Enterprise Information and Records Management | Gestion des archives et de l&#39;information de l&#39;entreprise |
| `1732` | Personnel Security | Service de sécurité aux employés |
| `1733` | Physical Security: Access Control | Sécurité physique: contrôle des accès |
| `1734` | Departmental Library | Bibliothèque ministérielle |
| `1735` | Enterprise Information and Records Management (EIRM) | Gestion des archives et de l&#39;information de l&#39;entreprise (GAIE) |
| `1736` | Public Enquiries | Renseignements au public |
| `1737` | Aboriginal Aquatic Resource &amp; Ocean Management Contribution Agreements | Ententes de contribution du Programme autochtone de gestion des ressources aquatiques et océaniques |
| `1738` | Aboriginal Fisheries Strategy Food, Social and Ceremonial (FSC) Contribution Agr | Accords de contribution relatifs aux pêches autochtones à des fins alimentaires, sociales et rituelles (ASR) dans le cadre de la Stratégie relative aux pêches autochtones |
| `1739` | Aboriginal Fund for Species at Risk Contribution Agreements | Ententes de contribution des Fonds autochtones pour les espèces en péril (FAEP) |
| `1740` | Atlantic Integrated Fisheries Initiative Contribution Agreements | Ententes de contribution de l&#39;Initiative des pêches commerciales intégrées de l&#39;Atlantique (IPCIA) |
| `1741` | Access to information | Accès à l&#39;information |
| `1742` | Global oceanographic in situational data from the Global Telecommunication Syste | Données océanographiques dans situational mondiales du Système mondial de télécommunications |
| `1744` | Lake Ontario and St. Lawrence River water levels | Niveaux d&#39;eau du Lac Ontario et du fleuve Saint-Laurent |
| `1745` | Marine Environmental Data Section (MEDS) | Section des données sur le milieu marin |
| `1746` | Ministerial Correspondence | Correspondence ministerielle |
| `1747` | Nautical Charts and Publications | Cartes marines et services |
| `1748` | Northern Integrated Fisheries Initiative Contribution Agreements | Ententes de contribution de l&#39;InitiativeInitiative des pêches commerciales intégrées du Nord (IPCIN) |
| `1749` | Pacific Integrated Commercial Fisheries Initiative Contribution Agreements | Ententes de contribution de l’Initiative de pêche commerciale intégrée du Pacifique (IPCIP) |
| `1750` | Tides, Currents and Water Levels (CHS) | Marées, courants et niveaux d&#39;eau (SHC) |
| `1751` | Provide funding to First Nations for transfers of band moneys | Fournir des fonds aux Premières nations pour les transferts d&#39;argent de la bande |
| `1752` | Indian Moneys Expenditure Requests | Demandes de dépenses d&#39;argent des Indiens |
| `1753` | Living Estates: Individual trust account payout requests | Biens des personnes vivantes: Demandes de paiement d&#39;un compte individuel en fiducie |
| `1754` | Estates Management | Gestion des successions |
| `1755` | Band Support Funding | Financement du soutien des bandes |
| `1756` | Tribal Council Funding | Financement des conseils tribaux |
| `1757` | Employee Benefits | Avantages sociaux des employés |
| `1758` | Professional and Institutional Development | Dévelopement professionnel et institutionnel |
| `1759` | Emergency Management, Crisis &amp; Strategic Communications: First Nations Emergency Management Funding | Gestion des urgences, communications de crise et stratégiques : Financement de la gestion des urgences des Premières Nations |
| `1760` | On-Reserve Education Facilities Funding | Fonds d&#39;installations d&#39;enseignement pour les collectivités dans les réserves |
| `1761` | On-Reserve Education Facilities Policy and Technical Support | Politique et soutien technique en matière d&#39;installations d&#39;enseignement pour les collectivités dans les réserves |
| `1763` | On-Reserve Education Facilities Capacity Building | Renforcement des capacités pour les installations d&#39;enseignement pour les collectivités dans les réserves |
| `1764` | On-Reserve Water and Wastewater | L&#39;eau et les eaux usées dans les réserves |
| `1765` | On-Reserve Other Community Infrastructure Policy and Technical Support | Politique et soutien technique en matière d&#39;autres infrastructures communautaires pour les collectivités dans les réserves |
| `1766` | On-Reserve Water and Wastewater Infrastructure Capacity Building | Renforcement des capacités pour les Infrastructure d&#39;approvisionemet en eau et des eaux usées dans les réserves. |
| `1767` | On-Reserve Housing: Funding, Policy and Technical Support, and Capacity Building | Fonds d&#39;infrastructure du logement dans: le financement, soutien politique et technique, et renforcement des capacités |
| `1768` | On-Reserve Housing Policy and Technical Support | Politique de logement dans les réserves et soutien technique |
| `1769` | On-Reserve Housing Capacity Building | Renforcement des capacités en matière de logement dans les réserves |
| `1770` | On-Reserve Other Community Infrastructure Funding | Fonds d&#39;autres infrastructures communautaires pour les collectivités dans les réserves |
| `1771` | On-Reserve Water and Wastewater Infrastructure Policy and Technical Support | Politique et soutien technique en Matière d&#39;infrastructure d&#39;approvisionnement en eau et d&#39;assainissement des réserves |
| `1772` | Gas Tax Fund (GTF) | Fonds de la taxe sur l&#39;essence (FTE) |
| `1773` | New Building Canada Fund – Provincial-Territorial Infrastructure Component – Nat | Nouveau Fonds Chantiers Canada – volet Infrastructures provinciales-territoriales – Projets nationaux et régionaux (VIPT-PNR) |
| `1774` | New Building Canada Fund – Provincial-Territorial Infrastructure Component – Sma | Nouveau Fonds Chantiers Canada – volet Infrastructures provinciales-territoriales – Fonds des petites collectivités (VIPT-FPC) |
| `1775` | Public Transit Infrastructure Fund (PTIF) | Fonds pour l&#39;infrastructure de transport en commun (FITC) |
| `1776` | Clean Water and Wastewater Fund (CWWF) | Fonds pour l&#39;eau potable et le traitement des eaux usées (FEPTEU) |
| `1777` | Investing in Canada Infrastructure Program (ICIP) | Programme d&#39;infrastructure investir dans le Canada (PIIC) |
| `1778` | Supplementary Health Benefits - Direct Service Delivery | Prestations de santé supplémentaires – Prestation directe de services. |
| `1779` | Disaster Mitigation and Adaption Fund (DMAF) | Fonds d&#39;atténuation et d&#39;adaptation en matière de catastrophes (FAAC) |
| `178` | Funding Decisions for Grants to Researchers | Décisions sur le financement des subventions de recherche |
| `1780` | Municipal Asset Management Program (MAMP) | Programme de gestion des actifs municipaux (PGAM) |
| `1781` | Municipalities for Climate Innovation Program (MCIP) | Programme Municipalités pour l&#39;innovation climatique (PMIC) |
| `1782` | Smart Cities Challenge (SCC) | Défi des villes intelligentes |
| `1783` | Supplementary Health Benefits- Funding | Prestations de santé supplémentaires – Prestation directe de services. |
| `1784` | Ministerial and Deputy Correspondance | Correspondance ministérielle et du sous-ministre |
| `1785` | Access to Information and Privacy (ATIP) | Accès à l&#39;information et protection des renseignements personnels (AIPRP) |
| `1786` | Primary Health Care: Clinical and Client Care - Direct Service Delivery | Soins de santé primaires : soins cliniques et soins aux clients – prestation de services directe |
| `1789` | Media Enquiries | Relations des médias |
| `1790` | Public Enquiries | Requêtes du public |
| `1791` | Primary Health Care: Clinical and Client Care - Funding | Soins de santé primaires : soins cliniques et soins aux clients – Financement |
| `1792` | FSWEP; Inventory of student employment opportunities in Public Service | Programme fédéral d&#39;expérience de travail étudiant: Répertoire des possibilités d&#39;emploi pour étudiants dans la fonction publique |
| `1793` | Research Affiliate Program (RAP); Job opportunities for post-secondary students | Programme des adjoints de recherche: Offres d&#39;emploi pour les étudiants de niveau postsecondaire |
| `1794` | PSR; Job opportunities for college and university graduates | Programme de recrutement postsecondaire: Possibilités d&#39;emploi pour les diplômés des collèges et des universités |
| `1795` | Home and Long-Term Care: Home &amp; Community Care - Direct Service Delivery | Soins à domicile et de longue durée : Soins à domicile et en milieu communautaire – Prestation directe de services |
| `1796` | Recruitment of Policy Leaders (RPL); Job opportunities for professionals, academics and scientist | Recrutement de leaders en politiques: Opportunités d&#39;emplois pour les professionnels, diplômés universitaires et les scientifiques |
| `1797` | Home and Long-Term Care: Home and Community Care - Funding | Soins à domicile et de longue durée : Soins à domicile et en milieu communautaire – – Financement |
| `1798` | Primary Health Care: Community Oral Health Services - Direct Service Delivery | Soins de santé primaires : Services communautaires de santé bucco-dentaire – Prestation directe de services |
| `1799` | Primary Health Care: Community Oral Health Services - Funding | Soins de santé primaires : Services communautaires de santé bucco-dentaire – Financement |
| `18` | Learning Services ; access to the School&#39;s learning products | Services d&#39;apprentissage; accès aux produits d&#39;apprentissage de l&#39;école |
| `1800` | Public Health Promotion and Disease Prevention Direct Service Delivery | Prestation directe de services de promotion de la santé publique et de prévention des maladies |
| `1801` | Public Health Promotion and Disease Prevention Services Funding | Financement des services de promotion de la santé publique et de prévention des maladies |
| `1802` | Public Health Protection and Disease Prevention: Environmental Public Health - Direct Service Delivery | Protection de la santé publique et prévention des maladies : Hygiène du milieu - Prestation directe de services |
| `1803` | Public Health Protection and Disease Prevention: Environmental Public Health - Funding | Protection de la santé publique et prévention des maladies : Hygiène du milieu -Financement |
| `1804` | Jordan&#39;s Principle: Direct Service Delivery | Principe de Jordan: Prestation directe de services |
| `1805` | Jordan&#39;s Principle: Funds for Coordination under Canadian Human Rights Tribunal (CHRT 41) | Principe de Jordan :Fonds de coordination pour le Tribunal canadien des droits de la personne (TCDP 41) |
| `1806` | Public Health Promotion and Disease Prevention: Mental Wellness - Funding | Promotion de la santé publique et prévention des maladies: Bien-être mental – Financement |
| `1807` | Public Health Promotion and Disease Prevention: Healthy Child Development - Funding | Promotion de la santé publique et prévention des maladies : développement sain des enfants - Financement |
| `1808` | Public Health Promotion and Disease Prevention: Healthy Living - Funding | Promotion de la santé publique et prévention des maladies: Modes de vie sains - financement |
| `1809` | Public Health Promotion and Disease Prevention: Communicable Disease Control and Management - Funding | Promotion et prévention des maladies : Contrôle et gestion des maladies transmissibles - Financement |
| `1810` | Health Systems Support: Health Human Resources - Funding | Soutien aux systèmes de santé : Ressources humaines en santé – Financement |
| `1811` | Community Infrastructure: Health Facilities-Funding | Financement-Infrastructure communautaire : Établissements de santé |
| `1812` | Primary Health Care : eHealth Infostructure - Funding | Soins de santé primaires : Infostructure de cybersanté - Financement |
| `1813` | Health Systems Support: Health Planning, Quality Management and Systems Integration - Funding | Soutien aux systèmes de santé : planification des soins de santé, gestion de la qualité et intégration des systèmes - Financement |
| `1814` | Health Systems Support: British Columbia Tripartite and Health Systems Transformations - Funding | Soutien aux systèmes de santé : transformations tripartites et des systèmes de santé de la Colombie-Britannique – Financement |
| `1817` | Logistical services for FPT Conferences | Service de Logistique pour conférences FPT |
| `1818` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1821` | Access to information and privacy requests | Accès à l&#39;information et protection des renseignements personnels |
| `1822` | Public and media enquiries | Demandes de renseignements du public et des médias |
| `1823` | Investigate Federal Offender Concerns | Enquêter sur les préoccupations des délinquants fédéraux |
| `1824` | Access to Information and Privacy | Demande de d&#39;accès à l&#39;information et aux renseignements personnels |
| `1825` | Public and Media Enquiries | Demandes du publique et des médias |
| `1827` | Building Canada Fund - Major Infrastructure Component (BCF-MIC) | Fonds Chantiers Canada - Volet Grandes Infrastructures (FCC-VGI) |
| `1828` | New Building Canada Fund (NBCF) - National Infrastructure Component (NIC) | Nouveau Fonds Chantiers Canada (NFCC) - Volet Infrastructures Nationales (VIN) |
| `1829` | Green Infrastructure Fund (GIF) | Fonds d&#39;infrastructure verte (FIV) |
| `1830` | Toronto Waterfront Revitalization Initiative (TWRI) | Infrastructure Canada et l&#39;Initiative de revitalisation du secteur riverain de Toronto |
| `1831` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1832` | SECURITAS | SECURITAS |
| `1833` | Independent safety investigations | Enquêtes indépendantes de sécurité |
| `1834` | Smart Cities Community Support Program | Programme de soutien aux collectivités sur les villes intelligentes |
| `1835` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1836` | Evaluation Services and Learning Division | Direction des services à l’évaluation et de l’apprentissage |
| `1837` | Canada Periodical Fund - Aid to Publishers - Magazines | Fonds du Canada pour les périodiques - Aide aux éditeurs - magazines |
| `1839` | Evaluation Division | Division de l&#39;évaluation |
| `1840` | Canadian economic sanctions | Sanctions économiques canadiennes |
| `1844` | Public Opinion Research Report (PORR) | Rapports de recherches sur l&#39;opinion publique (RROP) |
| `1845` | Disposition Authorizations | Autorisations de disposition |
| `1848` | International Standard Book Number - ISBN | Numéro international normalisé du livre - ISBN |
| `1849` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1850` | International Standard Music Number - ISMN | Numéro international normalisé de la musique - ISMN |
| `1851` | International Standard Serial Number - ISSN | Numéro international normalisé des publications en série - ISSN |
| `1854` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `1855` | Travel Information Program | Programme de renseignements aux voyageurs |
| `1856` | Consular Assistance and Services for Canadians Abroad | Assistance consulaire et services pour les Canadiens à l&#39;étranger |
| `1857` | International trade and investment | Commerce international et investissements |
| `1858` | Importing into Canada | Importation au Canada |
| `1859` | International innovation | Innovation de portée internationale |
| `1860` | Trade Commissioner Service | Service des délégués commerciaux |
| `1861` | Canadian Technology Accelerators | Accélérateurs technologiques canadiens |
| `1862` | Public Enquiries | Demande d&#39;informations parvenant du public |
| `1863` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1866` | Law Enforcement Records Checks | Vérification des dossiers policiers |
| `1867` | Copy Services | Services de copies |
| `1868` | Documentary Heritage Communities Program - DHCP | Programme pour les collectivités du patrimoine documentaire - PCPD |
| `1869` | Reference | Référence |
| `1870` | Ship Sanitation Inspections | Inspections sanitaires de navire |
| `1871` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `1872` | Canadian Firearms Program (CFP) - Support to Law Enforcement | Programme canadien des armes à feu (PCAF) - Aide aux forces de l&#39;ordre |
| `1873` | Canadian Firearms Program (CFP) - Firearms Registration | Programme canadien des armes à feu (PCAF) - Enregistrement des armes à feu |
| `1874` | ATIP | AIPRP |
| `1875` | Canada&#39;s National Do Not Call List | Liste nationale de numéros de télécommunication exclus du Canada |
| `1876` | Voter Contact Registry | Registre de communication avec les élécteurs |
| `1877` | Payment of judges&#39; salaries and allowance claims | Paiement des salaires et indemnités des juges |
| `1879` | Administration of the federal judicial appointment process | Administration du processus de nomination des juges fédérale |
| `1880` | Judges&#39; Language Training | Formation linguistique des juges |
| `1881` | Federal Courts Reports | Recueil des décisions des Cours fédérales |
| `1882` | Review judges&#39; conduct complaints | Examiner les plaintes relatives à la conduite des juges |
| `1884` | Accreditation services for events | Services d&#39;accreditation pour les événements |
| `1885` | Event logistical services for media | Services logistiques pour les média lors d&#39;événements |
| `1886` | Ex gratia compensation program for events | Programme d&#39;indemnisation à titre gracieux lors d&#39;événements |
| `1887` | Client Services | Services à la clientèle |
| `1888` | Women Entrepreneurship Fund | Fonds pour les femmes en entrepreneuriat |
| `1889` | Administration of JUDICOM | Administration de JUDICOM |
| `1892` | Application for Record Suspension | Demande de suspension du casier |
| `1893` | Application for Clemency | Demande de clémence |
| `1894` | Decision Registry Requests | Demande d&#39;accès au Registre des décisions |
| `1895` | Request to Attend a Hearing | Demande pour assister à une audience |
| `1896` | Access to Information Requests | Demande d&#39;accès à l&#39;information |
| `1897` | Services for Victims: Providing information and registration services to victims | Services aux victimes : Prestation de services d’information et d’inscription aux victimes |
| `1898` | Services for Victims: Providing Audio Recordings to Registered Victims | Services aux victimes : Accès aux enregistrements sonores par les victimes inscrites |
| `1899` | Victims Complaints Mechanism | Mécanisme de plainte des victimes |
| `19` | Enterprise Requested Delivery | Demandes de livraison en organisation |
| `1900` | Application for Expungement | Demande de radiation |
| `1901` | Canada Book Fund - Support for Publishers- Business Development | Fonds du livre du Canada - Soutien aux éditeurs - développement des entreprises |
| `1902` | Creative Export Canada | Exporation créative Canada |
| `1903` | Canada Music Fund | Fonds de la musique du Canada |
| `1904` | Canadian Film or Video Production Tax Credit | Crédit d&#39;impôt pour production cinématographique ou magnétoscopique canadienne |
| `1905` | Film or Video Production Services Tax Credit | Crédit d&#39;impôt pour services de production cinématographique ou magnétoscopique |
| `1906` | Canada Arts Training Fund | Fonds du Canada pour la formation dans le secteur des arts |
| `1907` | Canada Cultural Investment Fund - Strategic Initiatives | Fonds du Canada pour l&#39;investissement en culture - Initiatives stratégiques |
| `1908` | Canada Arts Presentation Fund - Professional Arts Festivals and Performing Arts Series Presenters | Fonds du Canada pour la présentation des arts - Festivals artistiques et diffuseurs de saisons de spectacles professionnels |
| `1909` | Canada Cultural Spaces Fund | Fonds du Canada pour les espaces culturels |
| `1910` | Celebration and Commemoration - Celebrate Canada | Célébrations et commémorations - Le Canada en fête |
| `1911` | Museums Assistance - Access to Heritage | Aide aux musées - Accès au patrimoine |
| `1912` | Building Communities through Arts and Heritage - Local Festivals | Développement des communautés par le biais des arts et du patrimoine - Festivals locaux |
| `1913` | Canada History Fund | Fonds pour l’histoire du Canada |
| `1915` | Canadian Conservation Institute and Canadian Heritage Information Network - Conservation Services | Institut canadien de conservation et Réseau canadien d&#39;information sur le patrimoine - Services de conservation |
| `1916` | Canadian Conservation Institute and Canadian Heritage Information Network | Institut canadien de conservation et Réseau canadien d&#39;information sur le patrimoine |
| `1917` | Privacy Act Requests | Demandes en vertu de la Loi sur la protection des renseignements personnels. |
| `1919` | Support and assistance to athletes | Soutien et aide aux athlètes |
| `192` | RCMP- Contract &amp; Indigenous Policing (C &amp; IP) | (GRC) Services de police contractuels et autochtones (SPCA) |
| `1920` | Support for Hosting - Canada Games | Soutien pour l&#39;acceuil - Jeux du Canada |
| `1921` | Sport Support - National Sport Organization | Soutien au sport - Organismes nationaux de sport |
| `1922` | Indigenous Languages and Cultures - Indigenous Languages | Langues et cultures autochtones - Langues autochtones |
| `1923` | Multiculturalism and Anti-Racism Initiatives - Events | Multiculturalisme et la lutte contre le racisme - Événements |
| `1924` | Development of Official-Language Communities – Cooperation with the Community Sector | Développement des communautés de langue officielle - Collaboration avec le secteur communautaire |
| `1925` | Enhancement of Official Languages – Cooperation with the Non-Governmental Sector | Mise en valeur des langues officielles - Collaboration avec le secteur non gouvernemental |
| `1928` | Access to Information requests | Accès à l&#39;information et protection des renseignements personnels |
| `1929` | Privacy Requests | Demandes de protection des renseignements personnels |
| `1931` | Decision Registry: Research Requests | Registre des décisions: Demandes de recherche |
| `1932` | Status Confirmation Service (controlled substances) | Service de confirmation du statut (substances désignées) |
| `1933` | Importation of designated devices | Importation d&#39;instruments désignés |
| `1934` | Pharmacy Referrals to Provincial Regulatory Authorities for situations of non-co | Renvois aux autorités réglementaires provinciales pour les pharmacies en situations de non-conformité |
| `1935` | Referrals to Law Enforcement | Renvois aux organismes d&#39;application de la loi |
| `1936` | Approval of retained controlled substances by law enforcement | Approbation des substances désignées retenues par les organismes d&#39;application de la loi |
| `1937` | Responding to enquiries from law enforcement | Répondre aux demandes des organismes d&#39;application de la loi (Demandes d&#39;état et ordres de production) |
| `1938` | Responding to enquiries from external stakeholders | Répondre aux demandes des parties prenantes externes |
| `1939` | Responding to enquiries from internal stakeholders | Répondre aux demandes des parties prenantes internes |
| `1940` | Pre-Licence Inspection Packages | Trousses d&#39;inspection pré-licence |
| `1941` | Notices of Restriction for Pharmacists and Practitioners | Avis de restriction pour les pharmaciens et practiciens |
| `1942` | Substance Use and Addictions Program | Programme sur l&#39;usage et les dépendances aux substances |
| `1943` | Import-Export Permits | Permis d’importation-exportation |
| `1944` | Issuance of Industrial Hemp Import and Export Permits under the Cannabis Act and | Délivrance des permis d’importation et d’exportation de chanvre industriel en vertu de la Loi sur le cannabis et de ses règlements |
| `1945` | Issuance of licence for Analytical Testing under the Cannabis Act and its Regula | Délivrance de licences d&#39;essais analytiques en vertu de la Loi sur le cannabis et de ses règlements |
| `1946` | Issuance of Cannabis Drug Licences under the Cannabis Act and its Regulations | Délivrance de licences de drogues contenant du cannabis en vertu de la Loi sur le cannabis et de ses règlements |
| `1947` | Industrial Hemp Licences | Licences liée au chanvre industriel |
| `1948` | Issuance of licence for Research under the Cannabis Act and its Regulations | Délivrance de licences de recherche en vertu de la Loi sur le cannabis et de ses règlements |
| `1949` | Exemptions under the Cannabis Act | Exemptions en vertu de la Loi sur le cannabis |
| `195` | Money Services Businesses (MSBs) Registry - Registration | Registre des entreprises de services monétaires (ESM) – Inscription |
| `1950` | Tobacco Control Program - Enquiries and Complaints | Programme de lutte au tabagisme - Demandes et plaintes |
| `1951` | Compliance Promotion Activities | Activité de promotion de la conformité |
| `1952` | Review, assess and action compliance issues related to cannabis and hemp | Examiner, évaluer et traiter les questions de conformité liées au cannabis et au chanvre |
| `1953` | Cannabis Product Recalls | Rappels de produits du cannabis |
| `1954` | Initial Licensing | Octroi de licences initiales |
| `1955` | Renewals and Amendments | Renouvellements et modifications |
| `1956` | Security | Sécurité |
| `1957` | Personal Registration Certificates | Certificats d’inscription personnelle |
| `1958` | Client Services - Call Centre, Cannabis, Correspondence | Services à la clientèle — Centre d’appels, cannabis, correspondance |
| `1959` | Email: cannabis@canada.ca | Le courriel: cannabis@canada.ca |
| `1960` | Cannabis Police Services | Services à la clientèle - Services policiers relatifs au cannabis |
| `1961` | Issuance of Licences for controlled substances and precursor chemicals under the Controlled Drugs and Substances Act and its Regulations (New, Renewal, Amendment) (CSCB) | Délivrance de licences pour des substances réglementées et des précurseurs chimiques en vertu de la loi sur les drogues et les substances réglementées et de ses règlements (nouvelles licences, renouvellements, modifications) (DGSCC) |
| `1962` | Issuance of Import and Export Permits for Controlled Substances and Chemical Precursors under the Controlled Drugs and Substances Act and its Regulations (CSCB) | Délivrance de licences d&#39;importation et d&#39;exportation de substances réglementées et de précurseurs chimiques en vertu de la loi réglementant certaines drogues et autres substances et de son règlement d&#39;application (DGSCC) |
| `1963` | Issuance of Registrations for Class B Precursors | Inscriptions de précurseurs chimiques de catégorie B |
| `1964` | Issuance of Authorization Certificates for Preparations or Mixtures of Class A or Class B Precursors under the Controlled Drugs and Substances Act and its Regulations (CSCB) | Délivrance de certificats d&#39;autorisation pour les préparations ou mélanges de précurseurs de classe A ou B en vertu de la loi réglementant certaines drogues et autres substances et de son règlement d&#39;application (DGSCC) |
| `1965` | Exemptions to conduct research with controlled substances including clinical trials | Exemptions relatives a la recherche incluant les essais cliniques |
| `1966` | Exemptions to operate a supervised consumption site | Exemptions relatives aux sites de consommation supervisée |
| `1967` | Issuance of Test Kit Registrations under the Controlled Drugs and Substances Act and its Regulations | Octroi d&#39;enregistrements de nécessaires d&#39;essai pour les substances désignées |
| `1968` | Investor Services - Government Liaison | To be provided |
| `1969` | Investor Services - Proposals and Information Gathering | To be provided |
| `1970` | Investors Services - Advice and Support | To be provided |
| `1971` | Marketing - Outreach | To be provided |
| `1972` | Communications - Public &amp; Media Inquiries | To be provided |
| `1973` | Honours and Awards | Décorations et citations |
| `1975` | Canadian Centre for Climate Services | Centre canadien des services climatiques |
| `1976` | Process Verification | Vérification des processus |
| `1977` | Licences | Délivrance de licences |
| `1978` | Safe Food for Canadians Licence | Licence relatives à la salubrité des aliments au Canada |
| `1979` | Access to Information Request | Demande d&#39;accès à l&#39;information |
| `1980` | AgriRisk: Microgrants | Initiatives Agri-risques: Microsubventions |
| `1981` | AgriRisk: Research and Development Contribution Funding Stream | Initiatives Agri-risques: Volet de financement par contribution de recherche et développement |
| `1982` | Laboratory Testing | L&#39;analyse de laboratoire |
| `1984` | Agricultural Clean Technology Program: Adoption Stream | Programme des technologies propres en agriculture |
| `1985` | Local Food Infrastructure Fund | Fonds des infrastructures alimentaires locales |
| `1986` | Dairy Direct Payment Program | Programme de paiements directs pour les producteurs laitiers |
| `1987` | Solutions Integration Service | Service d&#39;intégration des solutions |
| `1988` | Responses to Access to Information and Privacy | Réponses aux demandes en vertu de la Loi sur l’accès à l’information ou de la Loi sur la protection des renseignements personnels |
| `1989` | Conferencing Services | Services de conférence |
| `1990` | Statistical, Research and Technical Publications | Publications statistiques, scientifiques et techniques |
| `1991` | Harvest Sample Crop Quality Results (Unofficial Results) | Programme d&#39;échantillons de récolte (résultats non officiels) |
| `1992` | Climate Change Funding Programs - Energy Savings Rebate program | Programme de remises écoénergétiques |
| `1993` | Climate Change Funding Programs - Climate Action Incentive Fund - SME | Fonds d’incitation à l’action pour le climat - PME |
| `1994` | Climate Change Funding Programs - Climate Action Incentive Fund - MUSH | Fonds d’incitation à l’action pour le climat - MUEH |
| `1995` | Public Weather | Météo publique |
| `1996` | Income Replacement Benefit | Prestation de remplacement du revenu |
| `1997` | Authorized Service Providers | Fournisseur de services autorisé |
| `1998` | Provision of Calibration Sets | Ensembles d&#39;étalonnage |
| `1999` | Documentation for Optional Inspection, Quality Assurance or Analytical Testing | Documents visant l&#39;inspection facultative, l&#39;assurance de la qualité ou les services d&#39;analyse |
| `2` | Import Live Animal, Hatching Eggs and Germplasm (Semen and Embryos) | Importation d&#39;animaux vivants, d&#39;oeufs d&#39;incubation et de germoplasme d&#39;animaux |
| `20` | High-performance Computing | Calcul de haute performance |
| `2000` | Certificate Final for Grain | Certificat final de grain |
| `2001` | Official CGC Sealed Sample with Certificate | Échantillon officiel scellé et certificat de la CCG |
| `2002` | Final Quality Determination for Grain Producers | Détermination définitive de la qualité pour les producteurs de grain |
| `2003` | Allocation of Producer Cars | Attribution des wagons de producteurs |
| `2004` | Payment Protection for Grain Producers | Protection du paiement à l&#39;intention des producteurs de grain |
| `2005` | Additional Pain and Suffering Compensation | Indemnité supplémentaire pour douleur et souffrance |
| `2006` | Responses to Public and Media Inquiries | Réponses aux demandes de renseignements du public et des médias |
| `2007` | Ice Warnings, Forecasts and Information | Avertissements, prévisions et informations sur les glaces |
| `2008` | State funeral | Funérailles d&#39;État |
| `2009` | Atmospheric Data and Information Service | Service de données et d&#39;informations atmosphériques |
| `2010` | New Fiscal Relationship (10 Year) Grant | Subvention nouvelle relation financière (de 10 ans) |
| `2013` | Canada Energy Regulator Management System Audits of Regulated Companies | Vérifications des systèmes de gestion des sociétés réglementées par la Régie de l&#39;énergie du Canada. |
| `2014` | Canada Energy Regulator Financial Audit of Regulated Companies. | Vérification des états financiers des sociétés réglementées par la Régie de l&#39;énergie du Canada. |
| `2015` | Client Service Centre | Centre de services à la clientèle |
| `2016` | Interchange Canada | Échanges Canada |
| `2017` | Management Accountability Framework | Cadre de responsabilisation de gestion |
| `2018` | General Inquiries | Demandes générales |
| `2019` | Directory of Federal Real Property (DFRP) | Répertoire des biens immobiliers fédéraux (RBIF) |
| `2020` | Federal Contaminated Sites Inventory (FCSI) | Inventaire des sites contaminés fédéraux (ISCF) |
| `2021` | IP Data | Données sur la PI |
| `2022` | Performance Management for Employees | Gestion du rendement pour les employés |
| `2023` | Processing Applications under the Canadian Energy Regulator Act, sections 183, 2 | Traitement des demandes aux termes de l&#39;article 183, 214, 262 ou 298 de la loi sur la Régie canadienne de l&#39;énergie. |
| `2024` | Treasury Board Submission Centre | Centre des présentations du Conseil du Trésor |
| `2025` | Provision of Grants and Contributions | Octroi de subventions et de contributions |
| `2028` | New Substances Notification | Déclaration de substances nouvelles |
| `2029` | Accessibility and Inclusivity in the Built Environment | Accessiblité et inclusivité dans l&#39;environnement bâti |
| `2030` | Green and Sustainable Government for Real Property | Gouvernement vert et durable pour les biens immobiliers |
| `2031` | Canadian Shellfish Sanitation Program (Emergency (bi-valve) shellfish area closu | Programme canadien de contrôle de la salubrité des mollusques (Recommandations pour la fermeture d&#39;urgence de la zone des mollusques) |
| `2032` | Athlete Assistance | Aide aux athlètes |
| `2033` | Appraisal and Valuation Services | Services d&#39;évaluation |
| `2034` | GC Talent Cloud | Nuage de talents du GC |
| `2035` | GCcollab | GCcollab |
| `2036` | Application Portfolio Management (APM) submission | Soumission du Plan de TI et gestion du portefeuille d&#39;applications (GPA) |
| `2038` | Permits for Migratory Bird Sanctuary Regulations | Permis en vertu du Règlement sur les refuges d&#39;oiseaux migrateurs |
| `204` | Money Services Businesses - Registry Search | Entreprises de services monétaires – Recherche d&#39;entités inscrites |
| `2041` | Treaty Annuity Payments | Paiements de rente conventionnelle |
| `2042` | Transfers of Band Moneys | Transferts d&#39;argent de bande |
| `2043` | Treaty Payments Events | Événements de paiement de traités |
| `2044` | Indian Moneys Expenditure Requests | Demandes de versement des fonds indiens |
| `2045` | Individual Trust Account Payout Requests | Demandes de paiement de compte en fiducie individuel |
| `2046` | Estates Management | Gestion des successions |
| `2047` | Indian Registry | Registre indien |
| `2048` | Issuance of the Secure Certificate of Indian Status | Délivrance du certificat sécurisé de statut d&#39;Indien |
| `2049` | Community-Based Services: First Nations Economic Development Capacity &amp; Readiness Funding | Services communautaires : financement de la capacité et de l’état de préparation en matière de développement économique des Premières Nations |
| `2050` | First Nations Commercial and Industrial Development Act | Loi sur le développement commercial et industriel des Premières nations |
| `2051` | Food Safety Investigation - Incident Response | Enquête sur la salubrité alimentaire - intervention en cas d’incident |
| `2052` | Amendments to Schedule I of The First Nation Oil And Gas And Moneys Management Act | Modifications à l’annexe 1 de la Loi sur la gestion du pétrole et du gaz et des fonds des Premières Nations |
| `2053` | Funding for Essential Community-Based Services: First Nation Land Management | Financement des services essentiels communautaires : gestion des terres des Premières Nations |
| `2054` | Interdepartmental Procurement Strategy for Aboriginal Businesses | Stratégie interministérielle d’approvisionnement auprès des entreprises autochtones |
| `2055` | Incentives for Zero-Emission Vehicles Program | Le programme incitatifs pour l&#39;achat de véhicules zéro émission |
| `2056` | Aboriginal Entrepreneurship Program - Access to Capital | Programme d&#39;entrepreneuriat autochtone - L’accès au capital |
| `2057` | Operation and Maintenance of First Nations and Inuit Health Facilities | Fonctionnement et l’entretien des établissements de santé des Premières Nations et des Inuits |
| `2058` | Procurement Strategy for Indigenous Business and the Indigenous Business Directory | Stratégie d’approvisionnement auprès des entreprises autochtones et Répertoire des entreprises autochtones |
| `2059` | Community Based On-Reserve Oil and Gas Management | Gestion communautaire du pétrole et du gaz sur les terres de réserve |
| `2060` | Indian Land Registry | Registre des terres indiennes |
| `2061` | Funding Community-Based Services: Reserve Land and Environment Management Program | Financement des services communautaires : Programme de gestion de l’environnement et des terres de réserve |
| `2062` | Contaminated Sites On-Reserve Program | Programme des sites contaminés dans les réserves |
| `2063` | Land Use Planning | Planification de l&#39;utilisation des terres |
| `2064` | First Nations Waste Management Initiative | Initiative des gestion des matières résiduelles des Premières Nations |
| `2065` | Environmental Review Process | Processus d&#39;examen environnemental |
| `2066` | Additions to Reserve | Ajouts aux réserves |
| `2067` | Sustainable On-Reserve First Nation Community and Economic Development | Développement économique et communautaire durable des Premières Nations dans les réserves |
| `2068` | Band Governance Management System | Système d&#39;information sur l&#39;administration des bandes |
| `2069` | Matrimonial Real Property | Biens immobiliers matrimoniaux dans les réserves |
| `2070` | Program to Address Disturbances from Vessel Traffic: Vessel slowdown | Programme de lutte contre les perturbations causées par le trafic maritime : Ralentissement du navire |
| `2071` | Animal Health Investigation - Incident Response | Enquête sur la salubrité des animaux - intervention en cas d’incident |
| `2072` | Quebec Fisheries Fund (QFF) | Fonds des pêches du Québec (FPQ) |
| `2073` | Program to Address Disturbances from Vessel Traffic: WhaleReport Alert System | Programme de lutte contre les perturbations causées par le trafic maritime : Système d&#39;alerte de rapport de baleine WhaleAlert |
| `2074` | Program to Protect Canada&#39;s Coastlines and Waterways: Abandoned Boats Program | Programme de protection du littoral et des voies navigables du Canada : Programme de bateaux abandonnés |
| `2075` | Program to Protect Canada&#39;s Coastlines and Waterways: Indigenous and Local Commu | Programme de protection du littoral et des voies navigables du Canada : Programme de partenariat et de mobilisation des collectivités autochtones et locales |
| `2076` | Program to Protect Canada&#39;s Coastlines and Waterways: Marine Training Program | Programme de protection du littoral et des voies navigables du Canada : Programme de formation dans le domaine maritime |
| `2077` | MPA Activity Plan Application Process - Laurentian Channel MPA | Processus de demande d&#39;activités pour la ZPM - Laurentian Channel |
| `2078` | MPA Activity Plan Application Process - Basin Head MPA | Processus de demande d&#39;activités pour la ZPM - Basin Head |
| `2079` | MPA Activity Plan Application Process - Banc-des-Americains MPA | Processus de demande d&#39;activités pour la ZPM - Banc-des-Americains |
| `208` | Management and Oversight | Gestion et Surveillance |
| `2080` | Canadian Industry Statistics | Statistiques relatives à l&#39;industrie canadienne |
| `2082` | Canadian Importers Database | Base de données sur les importateurs canadiens |
| `2083` | Trade Data Online | Données sur le commerce en direct. |
| `2084` | Financial Performance Data | Données sur la performance financière |
| `2085` | Program to Protect Canada&#39;s Coastlines and Waterways: Program to Enhance Maritim | Programme de protection du littoral et des voies navigables du Canada : Programme de sensibilisation accrue aux activités maritimes |
| `2086` | National Collision Database (NCDB) | Base nationale de données sur les collisions (BNDC) |
| `2087` | Indigenous Habitat Participation Program | Programme pour la participation autochtone sur les habitats |
| `2091` | BC Salmon Restoration and Innovation Fund (BCSRIF) | Fonds de restauration et d&#39;innovation pour le saumon de la Colombie-Britannique (FRISB) |
| `2092` | Marine Mammal Response Program | Programme d&#39;intervention auprès des mammifères marins |
| `2093` | TMX Accommodation Measure Salish Sea Initiative (SSI) | Initiative de la mer Salish (IMS) |
| `2094` | Enhanced Nature Legacy - Canada Target 1 Challenge Top-up | Complément du Défi de l’objectif 1 du Patrimoine naturel bonifié du Canada |
| `2095` | Canada Nature Fund - Community-nominated priority places for species at risk | Les lieux prioritaires désignés par les collectivités pour les espèces en péril du Fonds de la nature du Canada |
| `2096` | International Assistance Group | Service d&#39;entraide internationale |
| `2098` | Legal Services - Advisory | Services juridiques - Conseils |
| `2099` | Legal Services - Litigation | Services juridiques - Contentieux |
| `21` | Grants and Contribution Programs | Programmes de subventions et de contributions |
| `2100` | Legal Services - Legislative and Regulatory | Services juridiques – Législation et réglementation |
| `2101` | Investment Support | Soutien en matière d&#39;investissement |
| `2102` | Introductions | Présentations |
| `2103` | Roadmap | Feuille de route |
| `2104` | Women&#39;s Program | Programme de promotion de la femme |
| `2105` | Gender-Based Violence Program | Programme de financement de la lutte contre la violence fondée sur le sexe |
| `2106` | Equality for Sex, Sexual Orientation, Gender Identity and Expression Program | Programme de promotion de l&#39;égalité des sexes, de l&#39;orientation sexuelle, de l&#39;identité et de l&#39;expression de genre |
| `2107` | Client initiated request to transfer the file between offices in Canada | Demande initiée par le client pour transférer le dossier entre des bureaux au Canada |
| `2108` | Temporary Passport | Délivrance d&#39;un passeport provisoire |
| `2109` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `2110` | Family Orders and Agreement Enforcement Assistance | Aide à l&#39;exécution des ordonnances et des ententes familiales |
| `2112` | Ecosystems and Oceans Science Contribution Framework | Cadre de contribution de Sciences des écosystèmes et des océans |
| `2114` | Issuance of Authority – Air Licence, International Charter Permits and Wet Lease | Délivrance de l&#39;autorisation - Licence aérienne, permis d&#39;affrètement international et bail avec équipage |
| `2115` | introduction to and Advanced Training on the IAA | Introduction et formation avancée à la LEI |
| `2116` | Emergency Management Services | Services de gestion des urgences |
| `2117` | Impact Assessment done by Review Panels | Évaluation d&#39;impact par une commission d&#39;examen |
| `2118` | Impact Assessment done by Substitution | Évaluation d&#39;impact par substitution |
| `2119` | Monitoring and addressing events in the financial sector, response to liquidity | Surveillance et traitement des événements dans le secteur financier, réponse à la crise des liquidités |
| `2121` | Impact Assessment done by the Agency | Évaluation d&#39;impact réalisée par l&#39;Agence |
| `2122` | Northern Contaminants Program | Programme de lutte contre les contaminants dans le Nord |
| `2123` | Basic Organizational Capacity | Capacité organisationnelle de base |
| `2124` | Federal Interlocutor&#39;s Contribution Program(FICP) (Projects Stream) | Programme de contribution de l&#39;Interlocuteur fédéral |
| `2125` | Consultation and Policy Development | Consultations et de l&#39;élaboration des politiques |
| `2126` | Support in accordance with the Addition of Lands to Reserve and Reserve Creation Act, the First Nations Fiscal Management Act and the Framework Agreement on First Nation Land Management Act and the related institutions | Appui portant sur la Loi sur l’ajout de terres aux réserves et la création de réserves, la Loi sur la gestion financière des premières nations et la Loi sur l’Accord-cadre relatif à la gestion des terres de premières nations. |
| `2127` | List of First Nations managing their lands under the First Nations Land Management Act | Liste des Premières Nations qui gèrent leur terres sous la Loi sur la gestion des terres des Premières Nations |
| `2128` | Ministerial Correspondence | Correspondence ministérielle |
| `2129` | Indigenous Arts Centre | Centre d&#39;art autochtone |
| `2130` | Access to Information | Accès à l&#39;information |
| `2131` | Coordinate COVID-19 Funding Opportunities | Coordination des possibilités de financement liées à la COVID?19 |
| `2132` | Settlement Program Transfer Payments | Paiements de transfert du Programme d&#39;établissement |
| `2133` | Privacy | Protection des renseignements personnels |
| `2134` | Canada Energy Regulator (CER)&#39;s Emergency Response Procedures | Procedures d&#39;intervention d&#39;urgence de la Régie de l&#39;énergie du Canada |
| `2136` | Canadian Criminal Real Time Identification Services (CCRTIS) - Biometric Business Solutions (BBS) Certification Services. | Les Services canadiens d&#39;identification criminelle en temps réel (SCICTR) - Services de certification- Solutions biométriques d&#39;entreprise (SBE) |
| `2137` | Sensitive and Specialized Investigative Services (SSIS) | Services d&#39;enquêtes spécialisées et de nature délicate (SESND) |
| `2138` | Criminal Intelligence Service Canada (CISC) | Service canadian de renseignements criminels (SCRC) |
| `2139` | Departmental Correspondence Unit | Unité de la correspondance ministérielle |
| `2140` | Media Relations | Relations avec les médias |
| `2141` | Conservation management | Gestion de la conservation |
| `2142` | Highway Operations | Opérations de voirie |
| `2143` | Waterways Safety and Reporting | Services de sécurité et d&#39;information sur les voies navigables |
| `2144` | Alerts and advisories | Alertes et avis |
| `2145` | Government Resiliency and Continuity Management (Centre for Resiliency and Continuity Management) | Gestion de la continuité et de la résilience du gouvernement (Centre de gestion de la continuité et de la résilience) |
| `2146` | Accelerated Growth Service | Service de croissance accélérée |
| `2148` | Media relations | Relations avec les médias |
| `2149` | Stakeholder Relations | Stakeholder Relations |
| `2150` | Make a Complaint | Dépôt d&#39;une plainte |
| `2151` | Request a Review | Demande d&#39;examen |
| `2152` | Public Education and Outreach | Sensibilisation du public et liaison avec les collectivités |
| `2153` | Conduct a Review | Effectuer un examen |
| `2154` | Investigate a Complaint | Enquêter sur une plainte |
| `2155` | Funding Programs for Health Research and Training | Programmes de financement de la recherche et de la formation en santé |
| `2158` | Funding Programs | Programmes de financement |
| `2159` | Small Business Services and Public Enquiries | Services aux petites entreprises et demandes de renseignements pour le public |
| `22` | Web Inquiries | Demandes de renseignements sur le Web |
| `2201` | Mandatory Isolation Supports for Temporary Foreign Workers Program | Programme d&#39;aide pour l&#39;isolement obligatoire des travailleurs étrangers temporaires |
| `2213` | Emergency On-Farm Support Fund | Fonds d’urgence pour les mesures de soutien à la ferme |
| `2214` | Emergency Processing Fund | Le Fonds d&#39;urgence pour la transformation |
| `2215` | Surplus Food Rescue Program | Programme de récupération d’aliments excédentaires |
| `2216` | IP Education, tools, and resources | Éducation, outils et ressources en matière de PI |
| `2217` | Register Integrated Circuit Topography | Enregistrement de topographies de circuits intégrés |
| `2218` | Black Entrepreneurship Program | Programme pour l&#39;entrepreneuriat des communautés noires |
| `2219` | Women Entrepreneurship Knowledge Hub | Portal de connaissances pour les femmes en entrepreneuriat |
| `2220` | Rapid test kit provision | Fourniture de kit de test rapide |
| `2221` | COVID Alert | Alerte COVID |
| `2222` | Canada Digital Adoption Program - Grow Your Business Online | Programme canadien d’adoption du numérique - Développer vos activités commerciales en ligne |
| `2223` | Food Waste Reduction Challenge | Défi de réduction du gaspillage alimentaire |
| `2224` | AAFC Contact Centre | Centre d’appels de la Direction des programmes du revenu agricole (DPRA) |
| `2225` | Innovative Solutions Canada Program | Solutions innovatrices Canada (SIC) |
| `2226` | Safeguarding Your Research Portal | Portail Protégez Votre Recherche |
| `2227` | Strategic Science Fund (SSF) | Fonds stratégique des sciences (FSS) |
| `2228` | CRC-Intellectual Property Licensing | Licences de propriété intellectuelle |
| `2229` | Universal Broadband Fund (STS-CCB) | Fonds pour la large bande universelle |
| `2230` | COVID-19 Tracking System (CTS) | Système de suivi pour la COVID-19 (SSC) |
| `2233` | TBS IRIS (SAP) Corporate Financial Systems for the Central Agency Cluster Shared Systems (CAC-SS) | SCT IRIS (SAP) Systèmes financiers ministériels des Systèmes partagés du Regroupement des organismes centraux (SP-ROC) |
| `2234` | IC Contact Us: AGS Call Centre Service | Contactez-nous IC: Service de centre d&#39;appel |
| `2235` | Accelerated Growth Service | Service croissance accélérée |
| `2236` | The Accelerated Growth Service (AGS) | Le service de croissance accélérée |
| `2237` | ExploreIP | ExplorerPI |
| `2238` | Client Support Centre | Centre de soutien à la clientèle |
| `2239` | Expenditure Management Component | Le système de gestion des dépenses |
| `2240` | Issuance of Certificates of Qualification under the Floating Plant Clause (Coasting Trade Act) | Délivrance de certificats de qualification en vertu de la clause d&#39;outillage flottant (Loi sur le cabotage) |
| `2241` | Public Service Employee Survey (PSES) | Sondage auprès des fonctionnaires fédéraux (SAFF) |
| `2242` | Executive Talent Management | Gestion des talents des cadres supérieurs |
| `2243` | Canadian Experiences Fund | Fonds pour les expériences canadiennes |
| `2244` | Women Entrepreneurship Fund | Le Fonds pour les femmes en entrepreneuriat |
| `2245` | Women Entrepreneurship Strategy Ecosystem Fund | Le Fonds pour l&#39;écosystème de la Stratégie pour les femmes en entrepreneuriat |
| `2246` | Regional Relief and Recovery Fund | Fonds d&#39;aide et de relance régionale |
| `2247` | Large Employer Emergency Financing Facility (LEEFF) | Crédit d’urgence pour les grands employeurs (CUGE) |
| `2248` | Patent Collective Pilot Program (Gs&amp;Cs) | Programme pilote sur le Collectif de brevets |
| `2250` | Indigenous Intellectual Property Program Grant (Gs&amp;Cs) | Subvention du programme sur la propriété intellectuelle autochtone |
| `2251` | Intellectual Property Clinics Program (Gs&amp;Cs) | Programme de cliniques sur la propriété intellectuelle |
| `2253` | GC Integrated Planning submission | Soumission du Plan Intégrée GC |
| `2254` | COVID Vaccines Inventory Management | Gestion des inventaires vaccins COVID |
| `2255` | New Substances Program | Programme des substances nouvelles |
| `2256` | New Substances Notifications (Food and Drugs Act use) | Déclaration de substances nouvelles (usage en vertu de la Loi sur les aliments et drogues) |
| `2257` | Treasury Board Policy Suite Website | Site Web des politiques du Conseil du Trésor |
| `2259` | Early Retirement Incentive Program- A Unique Program (not associated with Receiver General Functions). Maintain pension services for employees of coal mines. | Programme d’encouragement à la retraite anticipée – Un programme unique (indépendant des fonctions du receveur général). Assurer les services de pensions pour les employés des mines de charbon. |
| `2260` | Investment Canada Act (ICA) Net Benefit Review, National Security Review | Loi sur Investissement Canda examen de l&#39;avantage net, examen relatif à la sécurité nationale |
| `2261` | Repository of Federal Public Sector (Core Public Administration) Collective Agreements | Répertoire des conventions collectives du secteur public fédéral (administration publique centrale) |
| `2262` | Project Risk and Complexity Assessment (Callipers) | L’Évaluation de la complexité et des risques des projets (Calibrage) |
| `2263` | Public Service Occupational Health Program COVID Response Division | Programme de santé au travail de la fonction publique - Division de l&#39;intervention liée à la COVID |
| `2264` | COVID-19 Mental Health Response | COVID-19: Intervention en santé mentale |
| `2265` | Travel Health Advice | Conseils de santé aux voyageurs |
| `2266` | GC-Wide Application Support Services | Services de soutien des applications à l&#39;échelle du GC |
| `2267` | Designated Quarantine Facilities | Installations de quarantaine désignées |
| `2268` | Central Notification System | Système de notification central |
| `2269` | Listeriosis Reference Service for Canada | Service de référence sur la listériose au Canada |
| `2270` | Measuring device approval services (non new approvals / revisions) | Services d&#39;approbation des dispositifs de mesure (non nouvelles approbations / révisions) |
| `2271` | Recruitment | Recrutement |
| `2274` | Prosecutorial Legal Advice | Conseils juridiques en matière de poursuites |
| `2275` | Respond to inquiries. | Répondre aux demandes de renseignements. |
| `2276` | Water/sewage treatment | Eau/traitement des eaux usées |
| `2277` | Emergency Support Function #10 | Fonction de soutien d&#39;urgence no. 10 |
| `2278` | National Fine Recovery Program (NFRP) | Programme national de recouvrement des amendes (PNRA) |
| `2280` | Class A Precursor Licences (New, Renewals, Amendments, Closures) | Octroi de licences de précurseurs chimiques de catégorie A (Nouvelles, renouvellements, modifications et fermetures) |
| `2281` | Cannabis Status Confirmation Service | Service de confirmation du statut en matiere du cannabis |
| `2283` | Amend Industrial Hemp Licences | Modifier les licences de chanvre en vertu de la Loi sur le cannabis et de ses règlements |
| `2284` | Fish Harvester Benefit and Grants program | Programme de Prestation et Subvention aux Pêcheurs |
| `2285` | One-Time Payment to Persons with Disabilities | Paiement Unique aux Personnes en Situation de Handicap |
| `2286` | Enquiries | Demande de renseignements |
| `2287` | Canadian Family Justice Fund | Fonds canadien de justice familiale |
| `2288` | Public Legal Education and Information | Éducation et information juridiques publiques |
| `2289` | Professional Training | Formation professionnelle |
| `2290` | Garnishment Registry of the National Capital Region (GAPDA) | Greffe de la saisie-arrêt de la région de la capitale nationale (LSADP) |
| `2291` | Central Registry of Divorce Proceedings (CRDP) | Bureau d&#39;enregistrement des actions en divorce (BEAD) |
| `2292` | Health Care Policy and Strategies Program | Programme des politiques et des stratégies en matière de soins de santé |
| `2293` | COVID-19 Public Enquiries | Demandes de renseignement sur la COVID-19 |
| `2294` | ArriveCAN Public Enquiries | Demandes de renseignement sur ArriveCAN |
| `2295` | COVID-19 Authorized Accommodations Toll-Free line | Ligne sans frais des hébergements autorisés COVID-19 |
| `2296` | Official Languages Health Program | Programme pour les langues officielles en santé |
| `2297` | Supporting the Canadian Red Cross&#39; Urgent Relief Efforts Related to COVID-19, Floods and Wildfires | Appuyer les efforts urgents de secours de la Croix-Rouge canadienne liés è la COVID-19, aux inondations et aux feux de forêt |
| `2298` | Botulism Reference Service for Canada | Service de référence pour le botulisme au Canada |
| `23` | Policy, Advocacy, and Coordination | Politique, représentation et coordination |
| `2300` | Canadian Travel Number (CTN) | Numéro canadien de voyages (NCV) |
| `2330` | Business Advisory Services. | Services-conseils à l&#39;entreprise. |
| `2358` | Youth Take Charge | Les jeunes s&#39;engagent |
| `2359` | Exchanges Canada - Youth Forums Canada | Échanges Canada - Forums Jeunesse Canada |
| `2360` | CNSC Emergency Management Duty Officer | Agente de service chargé de la gestion des urgences de la CCSN |
| `2361` | Radiological and Nuclear Expertise | Expertise nucléaire et radiologique |
| `2362` | Transportation Security Clearance | Habilitation de sécurité en matière de transport |
| `2363` | Program to Advance Transportation Innovation: Canadian Transportation Research F | Programme de promotion de l&#39;innovation en matière de transport : Groupe de recherches sur les transports au Canada |
| `2364` | Drone safety | Sécurité des drones |
| `2365` | Operating a federal railway | Exploitation d&#39;un chemin de fer fédéral |
| `2366` | Aviation Security - Issuing Exemptions | Sûreté aérienne - délivrance d&#39;exemptions |
| `2367` | Program to Address Disturbances from Vessel Traffic: Quiet Vessel Initiative | Programme de lutte contre les perturbations causées par le trafic maritime : Initiative pour des navires silencieux |
| `2368` | Issuance of AMOC/Exemption to the requirements of an Airworthiness Directive | Délivrance d&#39;un AMOC/Exemption aux exigences d&#39;une directive de navigabilité |
| `2369` | Contribution Program to Support Essential Air Services for Remote Communities | programme de contribution pour le programme de soutien aux services aériens essentiels aux collectivités éloignées |
| `2370` | Administration of the Marine War Risk Act and the agreement with the Canadian Sh | Administration de la Loi sur les risques de guerre en matière d&#39;assurance maritime et de l&#39;accord avec l&#39;Association pour assurance mutuelle d&#39;armateurs canadiens. |
| `2371` | Program to Protect Canada&#39;s Coastlines and Waterways: Safety Equipment and Basic | Programme de protection du littoral et des voies navigables du Canada : Initiative sur l&#39;équipement de sécurité et l&#39;infrastructure maritime de base dans les collectivités nordiques |
| `2372` | Program to Advance Indigenous Reconciliation: Program to Enhance Maritime Situat | Programme visant à favoriser la réconciliation avec les peuples autochtones : Programme de sensibilisation accrue aux activités maritimes |
| `2373` | Program to Advance Indigenous Reconciliation: Marine Safety Equipment and Traini | Programme visant à favoriser la réconciliation avec les peuples autochtones : Programme de formation et d&#39;équipement de sécurité maritime |
| `2374` | Inspecting a Railway | Inspection d&#39;un chemin de fer |
| `2375` | National Contact Centre Network (NCCN) | Réseau national des centres de contact (RNCC) |
| `2376` | Natural Infrastructure Fund (NIF) | Fonds pour les infrastructures naturelles (FIN) |
| `2377` | Green and Inclusive Community Buildings (GICB) | Bâtiments communautaires verts et inclusifs (BCVI) |
| `2378` | General Enquiry Services | Services de renseignements généraux (SRG) |
| `2379` | Cyber Security Assessments | Évaluations de la cybersécurité |
| `2380` | Canada Business App | l&#39;application Enterprises Canada |
| `243` | Species at Risk Act Permit System | Système de permis de la Loi sur les espèces en péril |
| `244` | Migratory Game Bird Hunting Permits | Permis de chasse aux oiseaux migrateurs considérés comme gibier |
| `2440` | Operational Communications Centre National Support Services (OCCNSS) | Services nationaux du soutien aux stations de transmissions opérationnelles (SNSSTO) |
| `2442` | RCMP Operations Coordination Centre (ROCC) | Centre de coordination des opérations de la GRC (CCOG) |
| `2443` | RCMP-Indigenous Relations Services (RIRS) | GRC services de relations avec les autochtones (GRC-SRA) |
| `2444` | Youth Officer Training (YOT) (online and in-person) | Formation des policiers éducateurs (FPE) (en ligne et en personne) |
| `2445` | RCMPTalks | Discussions GRC |
| `2446` | Youth Leadership Workshop (YLW) | Atelier de perfectionnement en leadership (APL) |
| `2447` | Indian Act Land Administration | Gestion des terres sous la Loi sur les Indiens |
| `2448` | Vulnerable Persons Unit (VPU) - Family Violence Initiative Fund (FVIF) | Section des personnes vulnérables - Fonds de l&#39;Initiative de lutte contre la violence familiale de la GRC |
| `2449` | Canadian Police Information Centre (CPIC) System including the Public Safety Portal (PSP) | Système du Centre d&#39;information de la police canadienne (CIPC) incluant le Portail de la Sécurité Publique (PSP) |
| `245` | Climate Change Funding Programs - Low Carbon Economy Leadership Fund | Le Fonds du leadership pour une économie à faibles émissions de carbone |
| `2450` | Service Feedback - Complaints | Rétroaction sur les services - plaintes, |
| `2451` | Coordination Agreement Discussions Tables | Tables de discussions sur l&#39;accord de coordination |
| `2452` | Notices and requests related to An Act respecting First Nations, Inuit and Métis children, youth and families | Avis et demandes liés à la Loi concernant les enfants, les jeunes et les familles des Premières Nations, des Inuits et des Métis |
| `2453` | Specialized Technical Investigative Services (STIS) | Les Services d’enquêtes spécialisées et techniques |
| `2454` | Information sharing service between INTERPOL/Europol and Canadian Law Enforcement | Service d’échange d’information entre INTERPOL/Europol |
| `2456` | Support to employees and veterans experiencing symptoms of or who have been diagnosed with an operational stress injury | Soutien aux employés et vétérans présentant des symptômes ou ayant reçu un diagnostic de traumatisme lié au stress opérationnel |
| `2457` | Canada Recovery Benefit (CRB) | Prestation canadienne de la relance économique (PCRE) |
| `2458` | Canada Recovery Caregiving Benefit (CRCB) | Prestation canadienne de la relance économique pour proches aidants (PCREPA) |
| `2459` | Canada Recovery Sickness Benefit (CRSB) | Prestation canadienne de maladie pour la relance économique (PCMRE) |
| `2460` | Canada Emergency Response Benefit (CERB) | Prestation canadienne d&#39;urgence (PCU) |
| `2461` | Canada Emergency Student Benefit (CESB) | Prestation canadienne d&#39;urgence pour les étudiants (PCUE) |
| `2462` | Canada Emergency Wage Subsidy (CEWS) | Subvention salariale d&#39;urgence du Canada (SSUC) |
| `2463` | Canada Emergency Rent Subsidy (CERS) | Subvention d&#39;urgence du Canada pour le loyer (SUCL) |
| `2464` | 10% Temporary Wage Subsidy for Employers | Subvention salariale temporaire de 10 % pour les employeurs (SST) |
| `2465` | Media Relations. | Relations avec les médias. |
| `2466` | International Real Property Services | Services en biens immobiliers internationaux |
| `2467` | Implementation of the Indian Residential Schools Settlement Agreement and Indian Residential Schools Documents Advisory Committee | Mise en œuvre de la Convention de règlement relative aux pensionnats indiens |
| `2468` | Indigenous Childhood Claims Litigation | Litiges relatifs aux réclamations pour les expériences vécues dans l&#39;enfance |
| `2469` | Canada Treaty Custodian | Gardien des traités du Canada |
| `247` | Climate Change Funding Programs - Low Carbon Economy Challenge: Champions Stream | Défi pour une économie à faibles émissions de carbone: volet des champions |
| `2477` | Support in accordance with the First Nations Fiscal Management Act, and its institutions | Support en lien avec la Loi sur la gestion financière des Premières Nations et ses institutions. |
| `2480` | Manage the Specific Claims Program | Gestion du programme des revendications particulières |
| `249` | Permits of equivalent levels of environmental safety | Permis de sécurité environnementale équivalente |
| `2495` | Impact Assessment Process | Processus d&#39;évaluation d&#39;impact |
| `25` | Access to the natural, historic and recreational site (no fee) | Accès au site naturel, historique et récréatif (sans frais) |
| `2505` | Permits under the Scott Islands Protected Marine Area Regulations | Permis en vertu du Règlement sur la zone marine protégée des îles Scott |
| `2515` | Northern Contaminated Sites Program | Programme des sites contaminés du Nord |
| `2517` | Canada Treaty Adoption Process | Processus canadien d&#39;adoption des traités |
| `2528` | Emergency Watch and Response | Surveillance et d&#39;interventions d&#39;urgence |
| `2531` | Orientation | Orientation |
| `2532` | Grants and Contributions in Aid of Academic Relations | Subventions et contributions en appui aux relations academiques |
| `2534` | Genealogy | Généalogie |
| `2536` | Loans to other institutions | Prêts à d&#39;autres institutions |
| `2537` | LAC User Card Registration Form | Formulaire d&#39;inscription pour la carte d&#39;usager de BAC |
| `2538` | Consultation of published and archival material | Consultation de matériel publié et archivistique |
| `2539` | Respond to requests for information from Parliamentarians. | Répondre aux demandes d&#39;information des parlementaires. |
| `254` | Environmental Funding - Aboriginal Fund for Species at Risk | Fonds autochtone pour les espèces en péril |
| `2540` | Loan request for exhibitions | Demande de prêts pour expositions |
| `2541` | «Listen, Hear Our Voices» Initiative | Initiative «Écoutez pour entendre nos voix» |
| `2542` | Access to records in support of the Federal Indian Day School Class Action Settl | Accès aux dossiers à l&#39;appui du règlement du recours collectif des externats indiens fédéraux |
| `2545` | Access to records of former Canadian Armed Forces members | Accès aux dossiers personnels des anciens membres des Forces armées canadiennes |
| `2549` | Cataloguing in Publication | Catalogage avant publication |
| `255` | Environmental Funding - Atlantic Ecosystems Initiatives | Initiatives des écosystèmes de l&#39;Atlantique |
| `2550` | Contributions Program of the Office of the Privacy Commissioner of Canada. | Programme des contributions du Commissariat à la protection de la vie privée du Canada. |
| `2551` | Surplus Canadian Publications | Publications canadiennes en surplus |
| `2552` | Privacy Impact Assessment (PIAs) Reviews. | Examens de Évaluations des facteurs relatifs à la vie privée (EFVP). |
| `2553` | Consultation services with federal institutions | Services-conseils au gouvernement |
| `2554` | Review and Investigate complaints under the Privacy Act. | Examiner et enquêter sur les plaintes en vertu de la Loi sur la protection des renseignements personnels. |
| `2555` | Receive and review Privacy Act breach reports. | Recevoir et examiner les rapports d&#39;atteintes à la vie privée en vertu de la Loi sur la protection des renseignements personnels. |
| `2556` | Review and investigate complaints under PIPEDA. | Examiner et enquêter les plaintes en vertu de la LPRPDE. |
| `2557` | On-Reserve Other Community Infrastructure Capacity Building | Renforcement des capacités pour les autres infrastructures communautaires pour les collectivités dans les réserves |
| `2558` | Receive and review breach reports under PIPEDA. | Recevoir et examiner les atteintes à la vie privée en vertu de la LPRPDE. |
| `2559` | Missing and Murdered Indigenous Women and Girls Secretariat | Le Secretariat pour les femmes et les filles autochtones disparues et assassinées |
| `2560` | Litigation Management Oversight Team | Direction de la surveillance de la gestion des litiges |
| `2561` | Strategic Policy, Cabinet and Parliamentary Affairs Branch | Direction générale des politiques stratégiques, des affaires du Cabinet et des affaires parlementaires |
| `2562` | Reconciliation Secretariat Branch | Direction générale du Secrétariat de la réconciliation |
| `2563` | Claims Assessment | Évaluation des revendications |
| `2564` | Contribution and Loan Funding to support Indigenous Communities Programs | Fonds de contribution et de prêt pour soutenir les programmes de négociations, de reconstruction des Nation et d’Espaces culturels dans les communautés autochtones. s |
| `2565` | Negotiations | Négociations |
| `2566` | BC Treaty Funding | Financement des traités CB |
| `2567` | Surplus Federal Real Property Initiative | Initiative sur les biens immobiliers excédentaires fédéraux |
| `2568` | Canadian Construction Materials Centre (CCMC) Product Assessments | Évaluation des produits du Centre canadien de matériaux de construction (CCMC) |
| `2569` | Indigenous Capacity Support Program | Programme de soutien des capacités autochtones |
| `2570` | Participant Funding Program | Programme d’aide financière aux participants |
| `2571` | Policy Dialogue Program | Programme de dialogue sur les politiques |
| `2572` | Projects subject to federal assessment under the IAA | Projets assujettis à l&#39;évaluation fédérale en vertu de la Loi sur l&#39;évaluation d’impact (LEI) |
| `2573` | Research Program | Programme de recherche |
| `2574` | Extractive Sector Transparency Measures Act | Loi sur les mesures de transparence dans le secteur extractif |
| `2576` | Pilimmaksaivik&#39;s Inuksugait Inventory | Inventaire des Inuksugait de Pilimmaksaivik |
| `2577` | Contribution in support of Climate Change Adaptation | Contribution à l&#39;appui de l&#39;adaptation au changement climatique |
| `2579` | Grants in support of Geo-Mapping for Energy and Minerals | Subventions à l&#39;appui du Programme Géocartographie de l?énergie et des minéraux |
| `2585` | Contributions in support of the ENERGY Innovation Program | Contributions à l&#39;appui des Programmes d&#39;innovation énergétique |
| `2586` | Electric Vehicle Infrastructure Demonstrations | Démonstrations d&#39;infrastructures pour véhicules électriques |
| `2587` | Smart Grid Infrastructure Demonstrations Program | Programme de démonstration de l&#39;infrastructure des réseaux électriques intelligents |
| `2588` | Clean Growth in the Natural Resources Sectors Innovation Program | Programme d&#39;innovation sur la croissance propre dans les secteurs des ressources naturelles |
| `2589` | Energy Efficient Buildings Program | Programme de bâtiments écoénergétiques |
| `2590` | Clean Energy for Rural and Remote Communities Program - Demonstration | Programme d&#39;énergie propre pour les collectivités rurales et éloignées |
| `2591` | Clean Technology Challenges - Impact Canada Initiative - Grants Portion | Défis de technologies propres - Initiative Impact Canada - subventions |
| `2592` | Clean Technology Challenges - Impact Canada Initiative | Défis de technologies propres - Initiative Impact Canada |
| `2593` | Emissions Reduction Fund Offshore Research, Development and Demonstration | Le programme de recherche, développement et démonstration extracôtière du Fonds de réduction des émissions |
| `2594` | Web content management services | Services de gestion du contenu web |
| `2595` | Contributions in support of Mountain Pine Beetle Management in Alberta | Contributions à l&#39;appui de la gestion du dendroctone du pin ponderosa en Alberta |
| `2596` | Contributions in support of Investments in the Forest Industry Transformation Program | Contribution à l&#39;appui du Programme d&#39;investissements dans la transformation de l&#39;industrie forestière |
| `2597` | Contributions in support of the Forest Innovation Program | Contributions à l&#39;appui du Programme de promotion de ld&#39;innovation forestière en foresterie |
| `2598` | Contribution program for Expanding Market Opportunities | Programme de développement des marchés |
| `2599` | Metallurgical Fuel Testing | Analyse des carburant métallurgique |
| `26` | Access to the Plains of Abraham Museum | Accès au Musée des plaines d&#39;Abraham |
| `2600` | Grants and Contributions in support of the Two Billion Tree Program | Subventions et contributions pour la croissance des forêts du Canada - 2 milliards d&#39;arbres |
| `2601` | Contribution to the Indigenous Forestry Initiative | Contribution à l&#39;Initiative de foresterie autochtone |
| `2602` | Grants and Contributions in support of Geoscience | Subventions et contributions en soutien aux géosciences |
| `2603` | BioHeat component of the Clean Energy for Rural and Remote Communities Program | Volet biothermie du programme Énergie propre pour les collectivités rurales et éloignées (EPCRE) |
| `2604` | CIM&#39;s Our Earth&#39;s Riches Mineral Literacy Installation | Installation Our Earth&#39;s Riches de l&#39;ICM pour mieux faire connaître le domaine minier aux jeunes Canadiens |
| `2605` | Spruce Budworm Early Intervention Strategy – Phase II Contribution Program | Stratégie d’intervention précoce contre la tordeuse des bourgeons de l’épinette – Phase II |
| `2606` | Mining Matters Educational Resources for Students | Ressources éducatives pour les étudiants &#39;Mining Matters&#39; |
| `2607` | Support for research on Woodland Caribou in support of conservation | Appuyer les recherches sur le caribou des bois à l&#39;appui de la conservation de cette espèce en péril |
| `2608` | Development and Delivery of Regional Mining Webinars | Développement et livraison de séminaire en ligne régionaux pour l&#39;exploitation minière |
| `2609` | National Youth Mining Career Awareness Strategy 2021-2026 | Stratégie nationale de sensibilisation aux carrières dans le secteur minier pour les jeunes 2021-2026 |
| `261` | Permit for disposal at sea | Permis pour l&#39;immersion en mer |
| `2610` | Green Construction through Wood (GCWood) Program | Programme de construction verte en bois (CVBois) |
| `2611` | Contributions in support of Indigenous Natural Resource Partnerships | Contributions en faveur des partenariats pour les ressources naturelles autochtones |
| `2612` | Contributions in support of Indigenous Advisory &amp; Monitoring Committees for EIPs (TMX &amp; L3) | Contributions pour appuyer les comités autochtones de consultation et de surveillance de projets d&#39;infrastructure énergétique - comités (TMX &amp; L3) |
| `2613` | Contributions in support of Indigenous Participation in Dialogues | Contributions à l&#39;appui du Fonds d&#39;aide financière aux participants pour les consultations auprès des Autochtones |
| `2614` | Contributions in support of Accommodation Measures for Trans Mountain Expansion | Contributions à l&#39;appui des mesures d&#39;accommodement du projet d&#39;agrandissement du réseau de Trans Mountain |
| `2616` | Funding for COVID-19 Safety Measures in Forest Sector Operations | Financement des mesures de sécurité COVID-19 dans les opérations du secteur forestier |
| `2617` | Industry Energy Management Programs | Programmes de gestion de l&#39;énergie industrielle |
| `2618` | Emissions Reduction Fund - Onshore Program | Fond de réduction des émissions - programme d&#39;installations terrestres |
| `2619` | Clean Energy for Rural and Remote Communities Program - Deployment | Programme d&#39;énergie propre pour les collectivités rurales et éloignées - Déploiement |
| `262` | Hazardous Waste Export and Import Permits | Permis d’exportation et d’importation de déchets dangereux |
| `2620` | Canadian Geospatial Data Infrastructure: Geospatial Web Services | Infrastructure canadienne de données géospatiales: Services web géospatiaux |
| `2621` | Impact Canada Initiative | Initiative Impact Canada |
| `2622` | Impact Canada Fellowship Program | Le programme de Fellowship d&#39;Impact Canada |
| `2623` | Governor-in-Council Appointments - Online account registration | Nominations par le gouverneur en conseil - Création de compte en ligne |
| `2624` | Senate Appointments | Nominations au Sénat |
| `2625` | Ministerial Correspondence | Correspondance ministérielle |
| `2626` | Public enquiries | Renseignements au public |
| `2627` | Horizontal Coordination of Government Communications | Coordination horizontale des communications gouvernementales |
| `2628` | Horizontal Coordination of Government advertising services | Coordination horizontale des services de publicité du gouvernement |
| `2629` | Horizontal Coordination of Government Public opinion research and analysis | Coordination horizontale de la recherche et analyse sur l’opinion publique |
| `263` | Environmental Funding - EcoAction Community Funding Program | Appel de propositions pour ÉcoAction |
| `2630` | Media monitoring and analysis, media relations | Surveillance et analyse médiatiques, relations avec les médias |
| `2631` | Fisheries Act - Aquatic Invasive Species Regulations Authorizations | la Loi sur les pêches - Autorisations en vertu du Règlement sur les especes aquatiques envahisantes |
| `2632` | Fisheries Act - Aquatic Invasive Species Regulations Fishing Licences | La Loi sur les pêches - permis de pêches du Règlement sur les especes aquatiques envahisantes |
| `2633` | Aquatic Invasive Species Program - Contribution Agreements | Programme sur les espèces aquatiques envahissantes - Ententes de contribution |
| `2634` | TMX Accommodation Measure Aquatic Habitat Restoration Program (AHRF) | Les mesures d&#39;accommodement TMX Fonds de restauration de l&#39;habitat aquatique (FRHA) |
| `2635` | TMX Accommodation Measure Terrestrial Cumulative Effects Initiative (TCEI) | Les mesures d&#39;accommodement TMX Initiative sur les effets cumulatifs en milieu terrestre (IECT) |
| `2636` | Contributions in support of the Salmonid and Salmon Enhancement Programming | Contributions à l&#39;appui du Programme de mise en valeur des salmonidés |
| `2637` | Indigenous Fisheries Management | Gestion des pêches autochtones |
| `2638` | Enforcement of Fisheries Legislation and Contaminated Shellfish Harvest Areas Closure Regulations | Application des lois sur les pêches et des règlements de fermeture de secteurs coquilliers contaminés |
| `2641` | CAMPUS - Individual subscription | CAMPUS - Abonnement individuel |
| `2642` | NFB.ca-Digital Store | ONF.ca-Boutique numérique |
| `265` | Environmental Funding - Lake Winnipeg Basin Program | Le programme du bassin du lac Winnipeg |
| `267` | Environmental Funding - Habitat Stewardship Program | Programme d&#39;intendance de l&#39;habitat pour les espèces en péril |
| `268` | Environmental Funding - Great Lakes Protection Initiative | Initiative de protection des Grands Lacs |
| `27` | Access to historic, thematic and educational activities | Accès à des activités historiques, thématiques et éducative |
| `278` | COSPAS-SARSAT Secretariat Contribution | Contribution du secrétariat COSPAS-SARSAT |
| `28` | Access to cultural activities | Accès à des activités culturelles |
| `280` | Heavy Urban Search and Rescue | Recherche et sauvetage en milieu urbain à l&#39;aide d&#39;équipement lourd |
| `282` | Search and Rescue New Initiatives Fund | Fonds des nouvelles initiatives de recherche et sauvetage |
| `283` | Search and Rescue Volunteer Association of Canada Contribution | Programme de contribution de l&#39;Association canadienne des volontaires en recherche et de sauvetage |
| `284` | Workers Compensation Program | Programme d&#39;indemnisation des travailleurs |
| `285` | Disaster Financial Assistance Arrangements | Accords d&#39;aide financière en cas de catastrophe |
| `288` | Youth Gang Prevention Fund | Fonds de lutte contre les activités des gangs de jeunes |
| `289` | Processing Applications under the National Energy Board Act, sections 52, 58 or | Traitement des demandes présentées aux termes de l’article 52, 58 ou 58.16 de la loi sur l&#39;Office national de l&#39;énergie. |
| `29` | Commemorative program (no fee) | Programme de commémoration (sans frais) |
| `290` | Processing Applications for Long-term Export License | Traitement des demandes présentées pour licence d&#39;exportation à long terme |
| `291` | Hearing Recommendations/Decisions | Demandes nécessitant une audience |
| `292` | Export Authorizations | Autorisations d&#39;exportation |
| `293` | Electricity Export Permits | Permis d&#39;exportation d&#39;électricité |
| `294` | Processing Non-hearing Applications under the Canadian Energy Regulator Act S214 | Traitement des demandes n&#39;exigeant pas d&#39;audience publique aux termes de l&#39;article 214 de la loi sur la Régie canadienne de l&#39;énergie. |
| `296` | Processing Landowner Complaints | Règlement des plaintes des propriétaires fonciers |
| `299` | Processing Canada Oil and Gas Operations Act Applications | Traitement des demandes aux termes de la Loi sur les opérations pétrolières au Canada |
| `3` | Export Food - Health/Sanitary Certificate | Exportations d&#39;aliments - Certificats de santé ou de salubrité |
| `30` | Access to information and the protection of personal information | Accès à l&#39;information et protection des renseignements personnels |
| `304` | Processing Canada Petroleum Resources Act Applications | Traitement des demandes aux termes de la Loi fédérale sur les hydrocarbures |
| `309` | Processing Participant Funding Requests | Traitement des demandes d&#39;aide financière aux participants |
| `31` | Refugee Protection | Protection des réfugiés |
| `314` | Responding to Library Requests | Demandes à la bibliothèque |
| `315` | Access to Information Requests | Accès à l&#39;information |
| `32` | Refugee Appeals | Appels des réfugiés |
| `324` | Receipt of requests to use the territory | Réception des demandes d&#39;utilisation du territoire |
| `33` | Toll-free Voice | Appels sans frais |
| `335` | Community Resilience Fund | Fonds pour la résilience communautaire |
| `337` | Crime Prevention Action Fund | Fonds d&#39;action en prévention du crime |
| `339` | International Association of Fire Fighters | Programme de contribution a l&#39;Association international des pompiers |
| `34` | Fixed Line Phones | Téléphones fixes (filaires) |
| `341` | Northern and Indigenous Crime Prevention Fund | Fonds de prévention du crime chez les collectivités Autochtones et du Nord |
| `344` | Communities at Risk: Security Infrastructure Program | Programme de financement des projets d&#39;infrastructure de sécurité pour les collectivités à risque |
| `35` | Bulk Print | Impression en bloc |
| `351` | Gun and Gang Violence Action Fund | Fonds de lutte contre la violence liée aux armes à feu et aux gangs |
| `352` | Funding for First Nation and Inuit Policing Facilities Program (FNIPF) | Programme de financement des installations pour les services de police des Premières Nations et des Inuits (PISPPNI) |
| `353` | Financial assistance agreement – Lac Mégantic | Accord d’aide financière - Lac Mégantic |
| `354` | Shock Trauma Air Rescue Ambulance Service | Shock Trauma Air Rescue Ambulance Service |
| `355` | Avalanche Canada | Avalanche Canada |
| `356` | Memorial Grant Program for First Responders | Programme de subvention commémoratif pour les premiers répondants |
| `357` | Funding Decisions for Institutional Capacity | Décisions sur le financement de la capacité institutionnelle |
| `3570` | Veteran Homelessness (VH) | Programme de lutte contre l&#39;itinérance chez les vétérans (PLIV) |
| `3572` | Events, exhibitions and tours | Événements, expositions et visites |
| `3573` | Copyright | Droits d&#39;auteur |
| `3574` | Information Management and Disposition of Government Records | Gestion de l’information et disposition des documents fédéraux |
| `3575` | International Standard Numbers | Numéros internationaux normalisés |
| `3576` | Loans | Prêts |
| `3577` | Research Support | Soutien à la recherche |
| `3578` | Digital Access to Collections | Accès numérique à la collection |
| `3581` | Funding Programs | Programmes de financement |
| `3584` | Compensation program due to extraordinary security measure during majors events | Programme d&#39;indemnisation dû aux mesures de sécurité extraordinaire durant des événements majeurs |
| `3585` | Business Information Services | Services d&#39;information aux entreprises |
| `3586` | Media Relations | Relations avec les médias |
| `3589` | Shared Human Resources Services | Services partagés en ressources humaines |
| `3590` | Procurement Options Analysis / Procurement Triage Tool/Ongoing Procurement Support and Advisory | Analyse des options d’approvisionnement / l’Outil de triage / Soutien à l’approvisionnement et services consultatifs en continu |
| `3591` | Real Property Disposals Sector | Secteur de l’aliénation des biens immobiliers |
| `3593` | Climate Change Funding Programs - Low Carbon Economy Challenge 2023 | Défi pour une économie à faibles émissions de carbone 2023 |
| `3594` | Community Development Wrap-Around Initiative | Initiative de soutien globale au développement communautaire |
| `3595` | ATSSC Law Library Services | Services de Bibliothèque du SCDATA |
| `3596` | ATSSC General Inquiries | Demandes générales SCDATA |
| `3597` | ATSSC Registry Services | Services de greffe |
| `3598` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `3599` | Global Innovation Clusters Program | grappes mondiales de l’innovation |
| `36` | Internal Credential Management | Gestion des justificatifs internes |
| `3600` | ElevateIP | ÉleverlaPI |
| `3601` | Portfolio Management | de gestion de portefeuille |
| `3602` | Canadian Dental Care Plan Eligibility Verification and Information | Vérification et renseignements sur l’admissibilité au Régime canadien de soins dentaires |
| `3603` | Grants and Contributions in Support of the Global Forest Leadership Program | Subventions et contributions à l&#39;appui du programme de leadership mondial sur les forêts |
| `3604` | Canadian Dental Care Plan eligibility verification and enrollment | Vérification de l&#39;admissibilité et inscription au Régime canadien de soins dentaires |
| `3606` | Multi-Partner Research Initiative | Initiative de recherche multipartenaire |
| `3607` | Public Court Records Access | Accès aux dossiers de cours public |
| `3608` | Litigant &amp; Public Support Services | Services de soutien aux parties et au public |
| `3609` | Courtroom and Hearing Operations | Coordinations des audiences et des salles |
| `3610` | Operational Support to the Judiciary | Soutien opérationnel à la magistrature |
| `3611` | Legal &amp; Judicial Support to the Judiciary | Soutien juridique et judiciaire à la magistrature |
| `3612` | Electricity Predevelopment Program | Programme de prédéveloppement en matière d&#39;électricité |
| `3613` | Enabling Small Modular Reactor Program | Programme facilitant les petits réacteurs modulaires |
| `3614` | National Bovine Spongiform Encephalopathy (BSE) Surveillance Reimbursement Program | Programme national de remboursement pour la surveillance de l&#39;encephalopathie spongiforme bovine (ESB) |
| `3615` | Veterinary Biologics Establishment Licence or Registration | Permis ou enregistrement d&#39;établissement de produits biologiques vétérinaires |
| `3616` | Nuclear Stock Seed Potato Program | Programme des pommes de terre de semence de Matériel nucléaire |
| `3617` | Box Tree Moth Program | Programme de la pyrale du buis |
| `3618` | Hemlock Wooly Adelgid Program | Programme du puceron lanigère de la pruche |
| `3619` | Blueberry Maggot Program | Programme de la mouche du bleuet |
| `3620` | Oak Wilt Program | Programme du flétrissement du chêne |
| `3621` | Prohibited Propagative Plant Material Program | Programme du matériel végétal de multiplication interdit |
| `3622` | Spotted Lanternfly Program | Programme du fulgore tacheté |
| `3623` | Apple (Fresh) Export Program | Programme d&#39;exportation de pommes (fraîches) |
| `3624` | Cherry (Fresh) Export Program | Programme d&#39;exportation de cerises (fraîches) |
| `3625` | Blueberry (Fresh) Export Program | Programme d&#39;exportation de bleuets (frais) |
| `3626` | Pepper (Fresh) Export Program | Programme d&#39;exportation de poivrons (frais) |
| `3628` | Grain Screening Pellets Export Program | Programme d&#39;exportation des agglomérats de criblures de grains |
| `3629` | Drug Submission Evaluations of Human Pharmaceuticals | Évaluation des présentations de médicaments pharmaceutiques à usage humain |
| `3630` | Drug Submission Evaluations of Biologic Products | Évaluation des présentations de médicaments biologiques |
| `3631` | Drug Submission Evaluations of Veterinary Pharmaceuticals and Veterinary Health Products | Évaluation des présentations de médicaments vétérinaires pharmaceutiques et des produits de santé animale |
| `3632` | Medical Device Submission Evaluations | Évaluation des demandes d&#39;instruments médicaux |
| `3633` | Special Access Programs: Human Drugs | Programmes d&#39;accès spéciale: médicaments à usage humain |
| `3634` | Special Access Programs: Medical Devices | Programmes d&#39;accès spéciale: instruments médicaux |
| `3635` | Natural Health Product Application Reviews | Évaluation des applications de produits de santé naturels |
| `3636` | Natural Health Product Site Licence Application Reviews | Évaluation des applications de licence des sites de produits de santé naturels |
| `3637` | Research Ethics Board | Comité d&#39;éthique de la recherche |
| `3638` | Stratospheric Balloon Flight Opportunities (STRATOS) | Opportunités de vols de ballons stratosphériques (STRATOS) |
| `3639` | CCOHS Inquiries Service | Le Service des demandes de renseignements du CCHST |
| `3640` | CCOHS Publications | Publications du CCHST |
| `3641` | CCOHS Legislation Service | Service législation du CCHST |
| `3642` | CCOHS Databases/Collections | Bases de données et collections du CCHST |
| `3643` | Cyber Centre Learning Hub - Learning Management System | Carrefour de l’apprentissage du Centre pour la cybersécurité – Système de gestion de l’apprentissage |
| `3644` | Cyber Centre Learning Hub - Curriculum Review | Carrefour de l’apprentissage du Centre pour la cybersécurité – Examen des programmes |
| `3645` | Advice and Guidance - Supply Chain Integrity | Avis et conseils en matière de cybersécurité – Architecture de sécurité du système |
| `3646` | Compliance Reviews / Certifications - Cryptographic Module Validation Program | Certifications/examens de conformité – Programme de validation des modules cryptographiques |
| `3647` | Compliance Reviews / Certifications - Common Criteria Recognition Arrangement (CCRA) | Certifications/examens de conformité – Arrangement de reconnaissance des Critères communs |
| `3648` | Cyber Centre Learning Hub - Custom Course Development | Carrefour de l’apprentissage du Centre pour la cybersécurité – Élaboration de cours sur mesure |
| `3649` | Digital Communications – Web Communications | Communications numériques – Communications Web |
| `3650` | Cyber Flipbook | Le livre d epoche cybernétique |
| `3651` | Canadian Anti-Fraud Centre-Online Fraud Reporting Systems | Centre Antifraude du Canada - système de signalement en ligne |
| `3652` | Indigenous Policing Services - National Directorate | Service de police autochtone – national |
| `3653` | Issuance of Discharge Books | Délivrance des livrets de service des marins |
| `3654` | Surface Transportation Merger and Acquisition Review and Assessment Process | Processus d&#39;examen et d&#39;évaluation des fusions et acquisitions dans le domaine des transports de surface |
| `3657` | Transportation Data and Information Hub | Carrefour de données et d&#39;information sur les transports |
| `3658` | Motor Vehicle Safety Call Centre | Centre d&#39;appels pour la sécurité des véhicules automobiles |
| `3659` | Assistance for a formal application for certification | Aide fournie en vue de la préparation d’une demande de services de certification |
| `3660` | Administrative changes to amend documents under Schedule V | Modification administrative apportée à un document pour lequel une redevance est exigible en vertu de la présente annexe |
| `3661` | Ministerial exemption to an airworthiness directive pursuant to 605.84(3) | Exemption ministérielle à une consigne de navigabilité en vertu du paragraphe 605.84(3) |
| `3662` | Marine Medical Examiner Designation | Désignation des médecins examinateurs de la marine |
| `3663` | Marine Pilotage Licence or Pilotage Certificate | Brevet de pilote ou certificat de pilotage maritime |
| `3664` | Marking and lighting of obstacles to air navigation | Balisage et éclairage des obstacles à la navigation aérienne |
| `3665` | Flight Tests Conducted by the Department of Transport | Tests en vol effectués par le ministère des Transports |
| `3666` | Outreach and Promotion - Human Rights | Sensibilisation et promotion - Droits de la personne |
| `3667` | Outreach and Education - Pay Equity | Sensibilisation et éducation - Équité salariale |
| `3668` | Outreach and Education - Accessibility | Sensibilisation et éducation - Accessibilité |
| `3669` | Complaint Management - Pay Equity | Gestion des plaintes - Équité salariale |
| `3670` | Complaint Management - Accessibility | Gestion des plaintes - Accessibilité |
| `3671` | Enforcement and Compliance - Pay Equity | Exécution et conformité - Équité salariale |
| `3672` | Enforcement and Compliance - Accessibilty | Exécution et conformité - Accessibilité |
| `3673` | System for Official Languages Obligations (SOLO) | Système pour les obligations en langues officielles (SOLO) |
| `3674` | Job Classification Data | Données sur la classification des emplois |
| `3675` | Finance Data Innovation Radar | Radar de l&#39;innovation en matière de finance |
| `3676` | Diversity and inclusion statistics | Statistiques sur la diversité et l&#39;inclusion |
| `3677` | Student Experience Survey | Sondage sur l&#39;experience etudiante (SEE) |
| `3678` | Human resources statistics | Statistiques concernant les ressources humaines |
| `3684` | Research Support Process | Processus de soutien à la recherche |
| `3685` | Grants and Contributions Programs | Programmes de subventions et contributions |
| `3686` | Indigenous Program Agreements | Accords sur les programmes autochtones |
| `3687` | MPA Activity Plan Application Process | Processus de demande d&#39;activités pour la ZPM - Anguniaqvia niqiqyuam |
| `3688` | Small Craft Harbours | Ports pour petits bateaux |
| `3689` | Small Craft Harbours Grant and Contribution Programs | Programmes de subventions et de contributions pour les ports pour petits bateaux |
| `3690` | Access to activities at the Plains of Abraham Museum | Accès aux activités du Musée des plaines d&#39;Abraham |
| `3691` | Access to social, cultural and heritage content online (no fee) | Accès à du contenu socio-culturel et patrimonial en ligne (sans frais) |
| `3692` | Access to a parking space | Accès à une place de stationnement |
| `3693` | Access to archives (no fee) | Accès aux archives (sans frais |
| `3694` | Receipt of requests from the media and public at large (no fee) | Réception des demandes des médias et du public (sans frais) |
| `3695` | Access to social, cultural, heritage and sports activities for the public at large (no fee) | Accès à des activités socio-culturelles, patrimoniales et sportives gratuites pour le grand public (sans frais) |
| `3698` | Payment of judges&#39; salaries | Paiement des salaires des juges |
| `3699` | Payment of judges&#39; allowance claims | Paiement des indemnités de juges |
| `37` | External Credential Management | Gestion des justificatifs externes |
| `3700` | Indigenous Partnership Fund | Le Fonds pour les partenariats avec les Autochtones |
| `3701` | Innovation for Defence Excellence and Security (IDEaS) Marketplace | Marché Innovation pour la défense, l&#39;excellence et la sécurité (IDEeS) |
| `3702` | Outreach | Rayonnement |
| `3703` | Peer Support Program | Programme de soutien par les pairs |
| `3704` | Independent Legal Assistance | L&#39;assistance juridique indépendante |
| `3705` | Import Admissibility | Admissibilité à l&#39;importation |
| `3707` | Media Relations | Relations avec les médias |
| `3708` | IDEaS Innovation Support Referals (IRS) Program | Programme de références pour le soutien à l’innovation (RSI) d’IDEeS |
| `3709` | Deferred Income and Savings Plans written enquiries | Régimes de revenu différé – Réponse aux demandes écrites |
| `3710` | Deferred Income and savings plans specimens reviews | Régimes de revenu différé et d’épargne (spécimens) |
| `3711` | Applications to register new pension plans and deferred profit sharing plans | Demandes d’agrément des régimes de pension et des régimes de participation différée aux bénéfices |
| `3713` | GST/HST rulings and interpretations - written enquiries | Décisions et interprétations en matière de TPS/TVH – Demandes écrites |
| `3714` | Applications for Charitable registration or re-registration | Demandes d&#39;enregistrement ou de réenregistrement d&#39;organismes de bienfaisance |
| `3716` | Actuarial Validation Report Reviews | Les rapports d’évaluation actuarielle |
| `3717` | Charities written enquiries | Demandes écrites des organismes de bienfaisance |
| `3718` | Problem Resolution | Solution de problèmes |
| `3719` | GST/HST rulings and interpretations - telephone enquiries | Décisions et interprétations en matière de TPS/TVH – Demandes de renseignements téléphoniques |
| `3720` | Charities telephone enquiries | Renseignements téléphoniques sur les organismes de bienfaisance (complexes) |
| `3721` | Clearance Certificate Requests | Demande de certificat de décharge |
| `3722` | One-time top-up to the Canada Housing Benefit (OTCHB)The last day to apply for the one-time top-up to the Canada Housing Benefit was March 31, 2023. | Supplément unique à l’Allocation canadienne pour le logement (SUACL) |
| `3723` | Luxury Tax Rebate Applications | Demande de remboursement de la taxe de luxe |
| `3724` | Luxury Tax Exemption Certificate | Certificat d&#39;exemption de la taxe de luxe |
| `3725` | Luxury Tax and Information Return Filing | Déclaration de la taxe de luxe et de renseignements |
| `3726` | Liaison Officer Service | Service d&#39;agents de liaison |
| `3727` | Canada Dental Benefit (CDB)To note: The interim Canada Dental Benefit ended on June 30, 2024. | Prestation dentaire canadienne (PDC) |
| `3728` | Canada Carbon Rebate (previously known as the Climate action incentive payment) | Remise canadienne sur le carbone (auparavant appelée paiement de l’incitatif à agir pour le climat) |
| `3729` | Community Volunteer Income Tax Program | Programme communautaire des bénévoles en matière d&#39;impôt |
| `3730` | Animal Health Movement Control Permit | Permis de contrôle des déplacements pour santé animale |
| `3731` | Special Outline for Veterinary Biologics | Protocole spécial pour produits biologiques vétérinaires |
| `3732` | Outline of Production - Veterinary Biologics | Protocole de production pour produits biologiques vétérinaires |
| `3733` | Adjudication of Immigration and Refugee cases | Décision des cas d’immigration et de statut de réfugié |
| `3734` | Ministerial Exemption for the Purpose of Selling a Test Market Food | Exemptions ministérielles pour vendre un aliment d&#39;essai |
| `3735` | Federal Policing Security Intelligence | Renseignement de sécurité de la Police Fédérale |
| `3736` | Air Carrier Support Centre (ACSC) | Centre de soutien aux transporteurs aériens (CSTA) |
| `3737` | Trade Compliance Verification | Vérifications de l&#39;observation commerciale |
| `3738` | TCS Website - Inquiries Page | SDC Site web - page de demandes |
| `3739` | Sanctions asset seizure and forfeiture implementation, including review of orders for the seizure of assets. | Mise en œuvre de la saisie et de la confiscation des biens en vertu des sanctions, y compris la révision des ordonnances de saisie des biens. |
| `3740` | Administration to the Canada Fund for Local Initiatives (CFLI) | Administration du Fond Canadien d&#39;Initiative Local |
| `3741` | Coordinate Canada&#39;s engagement in the G7 and G20 at the Leaders and Foreign Ministers levels, including time-sensitive meetings and rapid responses to emerging global events. | Coordonner la participation du Canada au G7 et au G20 au niveau des dirigeants et des ministres des Affaires étrangères, y compris les réunions urgentes et les réponses rapides aux événements mondiaux émergents. |
| `3757` | Short-Term Rental Enforcement Fund (STREF) | Fonds pour l&#39;application des restrictions sur la location de courte durée (FARLCD) |
| `38` | Secure Remote Access | Accès à distance protégé |
| `39` | Midrange | Ordinateurs de milieu de gamme |
| `4` | Food Recalls and safety alerts | Rappels d&#39;aliments et avis de sécurité |
| `40` | Mainframe | Ordinateur central |
| `4000` | School Food Infrastructure Fund | Fonds pour l&#39;infrastructure alimentaire scolaire |
| `4001` | Review of Complaints | L&#39;examen des plaintes |
| `4002` | Review of federal organization’s procurement practices | L’examen des pratiques d’approvisionnement des organisations fédérales |
| `4003` | Alternative Dispute Resolution | Règlement des différends |
| `4004` | Shared Ombuds services | Services d’ombuds partagés |
| `4005` | Enterprise Service Project Management | Gestion de projets de services d’entreprise |
| `4006` | Media Relations | Bureau des relations avec les médias |
| `4007` | Warehouse Assessment Services | Services d&#39;évaluation d&#39;entrepôt |
| `4008` | Events | Événements |
| `4009` | Tours | Visites guidées |
| `4010` | Exhibitions | Expositions |
| `4011` | LiquidFiles | FichersLiquides |
| `4012` | National Communications &amp; Public Affairs (NCPA) - Digital Communications | Communications nationales et Affaires publiques (CNAP) - Communications numériques |
| `4013` | Specialized Digital Systems | Systèmes numériques spécialisés |
| `4014` | Specialized Services | Services spécialisés |
| `4015` | General Consular Guidance | Assistance consulaire générale |
| `4016` | Personnel Security and Contracting | Sécurité du personnel et des marchés |
| `4017` | Domestic Physical Security | Sécurité matérielle nationale |
| `4018` | Registrations of Canadians Abroad (ROCA) | Inscription des Canadiens à l&#39;étranger |
| `4019` | Passport Services | Services de passeports |
| `4020` | Citizenship Services | Services de citoyenneté |
| `4021` | Access to Canadian Top Secret Network | Accès au Réseau canadien très secret |
| `4022` | Administration of Authorization Regime | Administration du régime d’autorisations |
| `4023` | Cyber Attributions | Connaissances des menaces cybernétiques |
| `4024` | Digital Platform for Grants and Contributions Management | Plateforme numérique pour la gestion des subventions et des contributions |
| `4025` | Engineering Service | Service d&#39;ingénierie |
| `4026` | Family Support Unit | Unité de soutien aux familles |
| `4027` | Government in Council (GIC) and Ministerial Appointments | Nominations par le gouverneur en conseil (GEC) et ministérielles |
| `4028` | Integrated support for international assistance programming (G&amp;Cs, RBM, Risk, APP, specialist support: gender, environment, sexual exploitation and abuse) | Ressources en matière de Gestion axée sur les résultats (GAR) |
| `4029` | Labour Relations Centre of Expertise - Corporate Services | Centre d&#39;expertise en relations de travail - Services ministériels |
| `4030` | LES Benefits management - End of service entitlements | Gestion des prestations ERP - indemnités de départ |
| `4031` | LES Benefits management - Financial Operations/Management and Oversight - Contract and invoice Management | Gestion des prestations ERP - opérations financières/gestion et surveillance - Gestion des contrats et des factures |
| `4032` | LES Benefits management - Financial Operations/Management and Oversight - Funds Management | Gestion des prestations ERP - opérations financières/gestion et surveillance - Gestion des fonds |
| `4033` | LES Benefits management - Insured Benefit Plans | Gestion des avantages sociaux des ERP - Régimes de prestations assurées |
| `4034` | LES HR Framework - LES Labour Relations and Terms and Conditions of Employment | Cadre des RH ERP - Relations de travail et termes et conditions d&#39;emploi des ERP |
| `4035` | LES HR Framework -Management of Program and Policy Design for Performance management | Cadre des RH ERP - Gestion de la conception des programmes et politiques pour la gestion du rendement |
| `4036` | LES HR Framework -Policy Stewardship - Management of Program and Policy Design for Staffing, Classification, Labour Relations and Terms and Conditions of Employment | Cadre des RH ERP - Gestion des politiques et direction de la conception des programmes et des politiques pour la dotation, la classification, les relations de travail et les conditions d&#39;emploi |
| `4037` | LES HR Framework- Salary scale determination &amp; administration | Cadre de RH ERP-Établissement et administration des échelles salariales |
| `4038` | LES HR learning Framework -Management of Program and Policy Design for Learning | Cadre des RH ERP - Gestion de la conception des programmes et des politiques pour l’apprentissage |
| `4039` | LES Leave Admin system tool (Avilar) Pilot | Projet pilote (Avilar) du système d&#39;administration des congés ERP |
| `4040` | LES Program co-lead for LES HR systems Software as a service contract requirements | Co-direction du programme ERP pour le contrat de service des logiciels des systèmes de RH ERP |
| `4041` | LES Social Security Participation management | Gestion de la participation des ERP aux régimes locaux de sécurité sociale |
| `4042` | Parliamentary briefing materials for Deputy Ministers and Ministers | Documents de breffage parlementaire à l&#39;intention des sous-ministres et des ministres |
| `4043` | Request for Particulars | Demande de renseignements |
| `4044` | Seasonal Influenza Immunization for Locally Engaged Staff | Vaccination contre la grippe saisonnière pour les employés recrutés sur place |
| `4045` | Electronic Procurement Solution (EPS) | Solutions d&#39;achats électroniques (SAE) |
| `4046` | CanadaBuys Service Desk (Level 1) | Bureau D&#39;aide Achats Canada (Niveau 1) |
| `4047` | Onboarding Services | Services d&#39;intégration |
| `4048` | Federal Policing Border Integrity | Intégrité frontalière de la police fédérale |
| `4049` | Information Requests | Demande d`informations |
| `4050` | Regional Security Operations Division | Direction des opérations de sécurité régionales |
| `4051` | Consular Case Management | Gestion de cas consulaire |
| `4052` | Advice to the Minister | Conseils au ministre |
| `4053` | Canadian Technology Accelerator | Accélérateurs technologiques canadiens |
| `4054` | Consular and emergency communications | Communications consulaires et d&#39;urgence |
| `4055` | Diplomatic Security Liasion Services | Services de liaison pour la protection des diplomates |
| `4056` | Economic modelling | Modélisation économique |
| `4057` | Export Permit Services (Softwood Lumber and Logs) | Service des licences d&#39;exportation (bois d&#39;œuvre résineux and billes de bois) |
| `4058` | Governance of LES-Missions&#39; Management Consultative Board processes | Gouvernance du processus de Consultations entre les Conseils de direction des missions et les ERP |
| `4059` | Provide leadership on Emergency Response and Preparedness for Health International Assistance portfolio. | Assurer la direction en matière de réponse et de préparation aux urgences pour le secteur d&#39;assistance internationale en santé. |
| `4060` | Provision of humanitarian assistance and operational response to natural disasters abroad in developing countries | Prestation d&#39;assistance humanitaire et réponse opérationnelle aux catastrophes naturelles à l&#39;étranger dans les pays en développement |
| `4061` | Rapid Response Mechanism (RRM) | Mécanisme de réponse rapide (MRR) |
| `4062` | Moodle | Moodle |
| `4063` | Reconciliation and Indigenous engagement advice and policy development | Activités de réconciliation et de mobilisation des Autochtones et élaboration de politiques |
| `4064` | Horizontal Policies (Greening) - strategic environmental and economic assessments, compliance management, public statements, and reporting mandatory for all departmental proposals to Cabinet (ie. Budget asks, TB subs, MCs, regulations) | Services d&#39;appoint en matière de politiques (recherche, analyse et conseils en matière de politiques). |
| `4065` | Workstation Software Provisioning | Approvisionnement en logiciels de poste de travail |
| `4066` | Wide Area Network (WAN) | Réseau étendu (RE) |
| `4067` | Intra-building Network | Réseau à l’intérieur des immeubles |
| `4068` | External Network Connectivity | Connectivité au réseau externe |
| `4069` | Parliamentary District Policing Program | Programme de services de police du district parlementaire |
| `4070` | Assault-Style Firearms Compensation Program | Programme d&#39;indemnisation pour les armes à feu de style arme d&#39;assaut (PIAFSAA) |
| `4071` | Preparation of the Federal Budget | Préparation du budget fédéral |
| `4072` | Lead Coordination of Financial Sector | Préparation du budget fédéral |
| `4073` | International Economic Leadership | Préparation du budget fédéral |
| `4074` | Research and Innovation Programs Benefits Administration | Administration des avantages des programmes de recherche et d’innovation |
| `4075` | Online Services | Services en ligne |
| `4076` | ATIP Requests Processing | Traitement des demandes d’AIPRP |
| `4077` | Paper Records Management | gestion des documents papier |
| `4078` | Canadian Grain Sampling Program Sample Inspection | Inspection d’échantillon du Programme canadien d’échantillonnage des grains |
| `4079` | Christmas Tree Export Program | Programme d&#39;exportation d&#39;arbres de Noël |
| `4080` | Disability Benefits Program Benefits Administration | Administration des avantages du Programme de prestations d’invalidité |
| `4081` | Financial Assistance and Income Replacement Programs Benefits Administration | Administration des avantages des programmes d’aide financière et de remplacement du revenu |
| `4082` | Commemorative Benefits and Services | Avantages et services commémoratifs |
| `4083` | Financial Support for Health Care Programs | Soutien financier pour les programmes de soins de santé |
| `4085` | Development of Official-Language Communities – Post-Secondary Sector and Scientific Knowledge in French Support Fund | Développement des communautés de langue officielle - Fonds d’appui au secteur postsecondaire et aux savoirs scientifiques en français |
| `4086` | Multiculturalism and Anti-Racism Initiatives - National Holocaust Remembrance Program | Multiculturalisme et la lutte contre le racisme - Programme national de commémoration de l’Holocauste |
| `4087` | Indigenous Business Navigator Service | Service de navigateur pour les entreprises autochtones |
| `4088` | Commemorating the National Day for Truth and Reconciliation | Commémoration de la Journée nationale de la vérité et de la réconciliation |
| `4089` | Trade Missions and Events | Missions et activités commerciales |
| `4090` | Greener Neighbourhoods Pilot Program | Programme pilote pour des quartiers plus verts |
| `4091` | Oil Spill Response Challenge | Défi d’intervention en cas de déversement d’hydrocarbures |
| `4092` | Clean Energy for Rural and Remote Communities - demonstration stream | Énergie propre pour les collectivités rurales et éloignées - volet démonstration |
| `4093` | Consumer Information Centre | Centre d&#39;information aux consommateurs |
| `4094` | Oral Health Access Funding (OHAF) applications&#39; review and transfer of funds to eligible recipients | Oral Health Access Funding (OHAF) applications&#39; review and transfer of funds to eligible recipients |
| `4095` | Oral health providers claims&#39; and estimates&#39; processing and payment as part of the Canadian Dental Care Plan | Traitement des réclamations et des demandes d&#39;autorisations préalables et paiement aux fournisseurs de soins buccodentaires dans le cadre du Régime canadien de soins dentaires |
| `4096` | Compliance response and enforcement escalation | Réponse en matière de conformité et escalade en matière d&#39;application |
| `4097` | Compliance response and enforcement action to a Type I mandatory recall (MO) | Réponse en matière de conformité et mesures coercitives à la suite d&#39;un rappel obligatoire (MO) de type I |
| `4098` | Regulatory and legislative advice and guidance | Conseils et orientations en matière de réglementation et de legislation |
| `4099` | Education and Outreach | Éducation et sensibilisation |
| `41` | Storage | Stockage |
| `4100` | International, Intergovernmental and Stakeholder Relations | Relations internationales, intergouvernementales et avec les parties prenantes |
| `4101` | Status Confirmation Service | Service de confirmation du statut |
| `4102` | Office of Controlled Substances Licensed Dealer | Bureau des substances contrôlées Distributeur agréé |
| `4103` | Emergency Treatment Fund | Fonds d&#39;urgence pour le traitement |
| `4104` | Medical Access Support | Assistance en matière d&#39;accès aux soins médicaux |
| `4105` | Tobacco Quit Lines | Lignes d&#39;aide pour arrêter de fumer |
| `4106` | Approval of retained controlled substances by law enforcement | Autorisation de conservation des substances contrôlées par les forces de l&#39;ordre |
| `4107` | Licensing and registration recommendation | Recommandation en matière de licences et d’enregistrements |
| `4108` | Regulatory exemption guidance | Orientation sur les exemptions réglementaires |
| `4109` | Canadian Coast Guard Marine Operations and Response Transfer Payment Program | Programme de paiements de transfert pour les opérations maritimes et les interventions de la Garde côtière canadienne |
| `4110` | Certification and Market Access Program for Seals Contribution Agreement (CMAPS) | Le Programme de certification et d&#39;accès aux marchés des produits du phoque (PCAMPP) |
| `4111` | Contribution Program for Pacific Salmon Foundation | Programme de contribution à la Fondation du saumon du Pacifique |
| `4112` | Contribution Program For Salmon Sub-Committee | Programme de contribution au sous-comité du Saumon |
| `4113` | Contribution Program for The T. Buck Suzuki Environmental Foundation | Programme de contribution avec la T. Buck Suzuki Environmental Foundation |
| `4114` | External Dissemination of Commercial Fisheries Statistics | Dissémination externe des statisques des pêches commerciales |
| `4115` | Global oceanographic in situational data from the Global Telecommunication System | Données océanographiques mondiales in situ provenant du Système mondial de télécommunication |
| `4116` | Lost Fishing Gear Reporting Support Service | Service de soutien à la déclaration des engins de pêche perdus |
| `4117` | Marine Spatial Planning Atlas | Atlas de planification spatiale marine |
| `4118` | Media Relations | Relations médias |
| `4119` | Multi-Partners Oil Spill Response Research Contribution Program | Programme de contribution à la recherche en matière d’intervention à partenaires multiples lors d’un déversement d’hydrocarbures |
| `4120` | Offline Licensing Services | Services d&#39;émission de permis hors ligne |
| `4121` | Pacific Salmon Commercial Transition Program | Programme de transition commerciale pour le saumon du Pacifique |
| `4122` | Pacific Salmon Conservation and Stewardship Partnerships Program | Programme de partenariats pour la conservation et la gestion du saumon du Pacifique |
| `4123` | Public Enquiries | Demande de renseignements du public |
| `4124` | Sustainable Fisheries Contribution Program - Shared Ocean Fund (Indo-Pacific Strategy) | Programme de contribution aux pêches durables - Fonds commun pour les océans (Stratégie indo-pacifique) |
| `4125` | Consular Enquiries | Renseignements consulaires |
| `4126` | Cannabis Product Recalls management (type I) | Gestion des rappels de produits à base de cannabis (type I) |
| `4127` | Stakeholder engagement and communications | Engagement des parties prenantes et communications |
| `4128` | Strategic policy and planning for stakeholder relations with various groups on the opioid overdose crisis and chronic pain | Politique stratégique et planification des relations avec les parties prenantes de divers groupes concernant la crise des surdoses d&#39;opioïdes et la douleur chronique |
| `4129` | Provide executive leadership, oversight and decision-making | Assurer la direction exécutive, la supervision et la prise de decisions |
| `4130` | Compliance monitoring and reporting | Surveillance et rapports de conformité |
| `4131` | Policy development and regulatory updates | Élaboration de politiques et mises à jour réglementaires |
| `4132` | Ship Security Alert System (SSAS) Testing | Système d’alerte de sécurité du navire |
| `4133` | CSC National Victim Services Program: Process victim registration request | Programme national de services aux victims du SCC : demande d&#39;inscription |
| `4134` | CSC National Victim Services Program: Process Victim Statement | Programme national de services aux victims du SCC : traiter les déclarations de la victime |
| `4135` | CSC National Victim Services Program: Notify of offender&#39;s conditional release | Programme national de services aux victims du SCC : aviser les victimes de la mise en liberté sous condition d&#39;un délinquant |
| `4136` | GC Workplace Accessibility Passport (My Accessible Workplace) | Passeport pour l’accessibilité en milieu de travail du GC (Mon milieu de travail accessible) |
| `4137` | Pleasure Craft Operator Cards (PCOC) issued | Cartes de conducteur d’embarcation de plaisance (CCEP) délivrée |
| `4138` | Request or extend a certificate of bareboat registry | Demander ou prolonger un certificat d’immatriculation d’un bâtiment en affrètement coque nue |
| `4139` | Ship radio equipment technical review | Examen technique de l’équipement radio maritime |
| `4140` | Determination of Closest Possible Compliance (Marine) | Détermination de la conformité la plus proche possible (maritime) |
| `4141` | Navigation Safety Assessment Process (NSAP) | Processus d’évaluation de la sécurité de la navigation (PESN) |
| `4142` | Automated Emergency Notification Fan-Out Service (AENFOS) | Service automatisé de notification d’urgence en cascade (SANUC) |
| `4143` | Issuance of a certificate or endorsement not requiring examination other than medical examination (marine) | Délivrance d’un brevet ou d’un visa n’exigeant pas d’examen autre qu’un examen médical (marine) |
| `4144` | Issuance of a record of qualifications and examinations | Délivrance d’un relevé de qualifications et d’examens |
| `4145` | Replacement of certificate or endorsement (except for certificate or endorsement lost owing to shipwreck) (marine) | Remplacement d’un brevet, d’un certificat de compétence ou d’un visa, à l’exception d’un brevet, d’un certificat de compétence ou du visa perdu en raison d’un naufrage (marine) |
| `4146` | Development of Official-Language Communities – Post-Secondary Sector and Scientific Knowledge in French Support Fund | Développement des communautés de langue officielle - Fonds d’appui au secteur postsecondaire et aux savoirs scientifiques en français |
| `4147` | Receive and review notification of Public Interest Disclosures under the Privacy Act. | Recevoir et examiner les notifications de communications dans l&#39;intérêt public par les institutions fédérales en vertu de la Loi sur la protection des renseignements personnels. |
| `4148` | CCOHS Business Safety Portal | Portail pour la sécurité en entreprise du CCHST |
| `4149` | Intake and Printing - Personal Registration applications | Réception et impression - Demandes d&#39;enregistrement personnel |
| `4150` | Access to Guided Tours of the Governor General&#39;s Official Residences (free) | Accès aux visites guidées des résidences officielles du gouverneur général (gratuit) |
| `4151` | Provisioning of Greetings and Messages from the Governor General | Envoi de messages et de vœux du gouverneur général |
| `4152` | Recognition of Canadian Excellence with the Canadian Honors and Awards Programs | Reconnaissance de l&#39;excellence canadienne grâce aux programmes d&#39;honneurs et de distinctions canadiens |
| `4153` | Earthquake Early Warning System | Système d&#39;alerte précoce en cas de tremblement de terre |
| `4154` | Conduct a Review | Effectuer un examen |
| `4155` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `4156` | Media and Public Inquiries | Médias et demandes de renseignements du public |
| `4157` | Quasi-judicial review of certain ministerial authorizations | Examen quasi judiciaire de certaines autorisations |
| `4158` | Customs Brokers Professional Examination | Examen de compétences professionnelles des courtiers en douane |
| `4159` | Customs Brokers Licensing | Agrément des courtiers en douane |
| `4160` | Incidents and Investigations | Incidents et investigations - Explosifs |
| `4161` | Outreach | Sensibilisation - Explosifs |
| `4162` | Comprehensive Nuclear-Test-Ban Treaty (CTBT) International Monitoring System (IMS) | Traité d&#39;interdiction complète des essais nucléaires (TICE) Système international de surveillance (SIS) |
| `4163` | Geomagnetic Monitoring and Space Weather Forecasting (GMSWF) | Surveillance géomagnétique et prévisions météorologiques spatiales |
| `4164` | Nuclear Emergency Response (NER) | Intervention en cas d&#39;urgence nucléaire |
| `4165` | Seismic Monitoring (SM) | Surveillance sismique |
| `4166` | Earthquake Early Warning System | Le système d’alerte sismique précoce canadien |
| `4167` | Canada Housing Infrastructure Fund (CHIF) | Fonds canadien pour les infrastructures liées au logement (FCIL) |
| `4168` | Canada Public Transit Fund (CPTF) | Fonds pour le transport en commun du Canada (FTCC) |
| `4169` | Funding for Research Training and Talent Development | Financement de la formation en recherche et du développement des talents |
| `4170` | Funding for Discovery Research | Financement de la recherche axée sur la découverte |
| `4171` | Funding for Research and Technology Partnerships | Financement des partenariats en recherche et en technologie |
| `4172` | EPS Operations | Opérations de la SAE |
| `4173` | AgriAssurance Program: Kosher and Halal Investment Component | Programme Agri-assurance : Volet Investissement casher et halal |
| `4174` | Agricultural Clean Technology Program: Research and Innovation Stream - Accelerator | Programme des technologies propres en agriculture : Volet Recherche et innovation - Accélérateur |
| `4175` | AgriMarketing Program: Kosher and Halal Investment Component | Programme Agri-marketing : Volet Investissement casher et halal |
| `4176` | AgriMarketing Program: Market Diversification - National Industry Association Component | Programme Agri-marketing : Volet Diversification des marchés pour les associations nationales de l’industrie |
| `4177` | AgriMarketing Program: Market Diversification - Small and Medium-sized Entreprise | Programme Agri-marketing : Diversification des marchés pour les petites et moyennes entreprises |
| `4178` | Kosher and Halal Investment Program | Programme d’investissement casher et halal |
| `4179` | Program Payment Services Unit | Unité des services de paiement des programmes |
| `4180` | Tax Payer Relief Provisions | Dispositions d’allègement pour les contribuables |
| `4181` | Canadian Beacon Registry (CBR) | Registre canadien des balises |
| `4182` | Military spouse employment initiative | Initiative d’emploi pour les conjoints de militaires |
| `4183` | National Claims &amp; Litigation Directorate | Direction nationale des réclamations et du contentieux |
| `4184` | Service-related injury or illness benefits administered by Veterans Affairs Canada | Programmes de soins de santé pour une blessure ou une maladie liée au service administrés par Anciens Combattants Canada |
| `4185` | National Communications &amp; Public Affairs (NCPA) - Intellectual Property Office | Communications nationales et Affaires publiques (CNAP) - Bureau de la propriété intellectuelle |
| `4186` | National Armourer Program (IPTMP) | Programme national d’armurerie (SPAPTM) |
| `4187` | Police Dog Service Training Centre (PDSTC) | Centre de dressage des chiens de police (CDCP) |
| `4188` | Physical Security Program - Lead Security Agency for Physical Security and Internal Services for Physical Security | Programme de sécurité matérielle – Le principal organisme responsable de la sécurité matérielle (POSM) et services internes de sécurité matérielle |
| `4189` | Receive and review codes of practice submitted in accordance with Proceeds of Crime (Money Laundering) and Terrorist Financing Regulations (PCMLTFR) | Recevoir et examiner les codes de pratique soumis conformément au Règlement sur le recyclage des produits de la criminalité et le financement des activités terroristes (RRPCFAT) |
| `4190` | Potato Wart Program | Programme de la galle verruqueuse de la pomme de terre |
| `4191` | Livestock Feeds Licence | Licence d&#39;aliments pour animaux de ferme |
| `4192` | Insight Research | Programme de recherche axée sur la connaissance |
| `4193` | Research Partnerships | Programme de partenariats de recherche |
| `4194` | Canada Biomedical Research Fund | Fonds de recherche biomédicale du Canada |
| `4195` | Research Support Fund | Fonds de soutien à la recherche |
| `423` | Conduct Complaints | Plaintes pour inconduites |
| `424` | Interference Complaints | Plaintes pour ingérence |
| `425` | Direct Funding Payments | Paiements d&#39;aide financière directs |
| `426` | Immigration Appeals | Appels en matière d&#39;immigration |
| `427` | Admissibility Hearings | Enquêtes |
| `428` | Detention Reviews | Contrôle des motifs de détention |
| `429` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `44` | Middleware | Intergiciel |
| `45` | Database | Base de données |
| `46` | Cloud Brokering | Courtage infonuagique |
| `47` | Classified Infrastructure | Infrastructure classifiée |
| `48` | Workplace Technology Devices Provisioning | Approvisionnements des appareils technologiques en milieu de travail |
| `49` | Web Conferencing | Cyberconférence |
| `5` | Regulatory Clarification | Clarification règlementaires |
| `50` | Audio Conferencing | Téléconférence |
| `51` | Satellite | Satellite |
| `52` | Internet | Internet |
| `53` | Review and Appeal hearings | Audiences de révision et d&#39;appel |
| `57` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `6` | Service Complaints | Plaintes de service |
| `655` | Grant, Scholarship and Fellowship Funding Transfers to Administering Institution | Transferts de subventions et de bourses d&#39;études et de perfectionnement à des établissements administrateurs |
| `656` | Grant, Scholarship, Fellowship and Award Administration | Administration des subventions, des bourses de perfectionnement et des bourses d&#39;études |
| `657` | CanNor Grants and Contributions | Subventions et contributions CanNor |
| `658` | Access to Information and Privacy (ATIP) | Accès à l&#39;information et protection des renseignements personnels (AIPRP) |
| `659` | Youth Justice Fund | Fonds du système de justice pour les jeunes |
| `660` | Victims Fund | Fonds d&#39;aide aux victimes |
| `661` | Justice Partnership and Innovation Program | Programme juridique de partenariats et d&#39;innovation |
| `662` | Indigenous Justice Program | Programme de justice autochtone |
| `663` | Access to Justice in Both Official Languages Support Fund | Fonds d’appui à l’accès à la justice dans les deux langues officielles |
| `664` | NEXUS Program Application | Traitement des demandes de participation au programme NEXUS |
| `665` | CANPASS Suite of Programs Application | Traitement des demandes de participation à la suite de programmes CANPASS |
| `666` | Remote Area Border Crossing (RABC) Permit Application | Permis de Passage à la frontière dans les régions éloignées (PFRE) |
| `667` | Free and Secure Trade Program (FAST) Driver Application | Traitement des demandes de participation au programme Expéditions rapides et sécuritaires (EXPRES) |
| `668` | Commercial Driver Registration Program (CDRP) Application | Traitement des demandes du Programme d&#39;inscription des chauffeurs du secteur commercial (PICSC) |
| `669` | Traveller Processing | Traitement primaire des voyageurs |
| `670` | Air Traveller Processing | Traitement primaire des voyageurs - mode aérien |
| `671` | Rail Traveller Processing | Traitement primaire des voyageurs - mode ferroviaire |
| `672` | Marine Traveller Processing | Traitement primaire des voyageurs - mode maritime |
| `673` | Immigration Secondary (Temporary Resident Program) Visitor | Immigration secondaire (Programme des résidents temporaires) Visiteur |
| `674` | Immigration Secondary - (Temporary Resident Program) Work Permit | Immigration secondaire (Programme des résidents temporaires) Permis de travail |
| `675` | Immigration Secondary (Temporary Resident Program) Study Permit | Immigration secondaire (Programme des résidents temporaires) Permis d&#39;études |
| `676` | Immigration Secondary - (Temporary Resident Program) Temporary Resident Permit | Immigration secondaire (Programme des résidents temporaires) Visa de résident temporaire |
| `677` | Immigration Secondary - Criminal Rehabilitation | Immigration secondaire - Réhabilitation criminelle |
| `678` | Refugee Claims | Demandes d&#39;asile |
| `679` | Border Information Service (BIS) | Service d&#39;information sur la frontière (SIF) |
| `680` | Customs Special Services | Services spéciaux des douanes |
| `687` | Hydrometric data and information service | Service de données et d&#39;informations hydrométriques |
| `688` | Health and air quality forecast services | Services de prévision relatifs à la santé et à la qualité de l&#39;air |
| `689` | Marine program weather services | Services du programme météorologique maritime |
| `690` | Direct Funding Payments | Versements faits directement aux boursiers |
| `691` | Funding Transfers to Administering Institutions | Transferts des fonds de subventions et de bourses aux établissements administrateurs |
| `694` | Services to Businesses and Business Organizations | Services aux entreprises et aux organismes commerciaux |
| `7` | Canada Pension Plan (CPP) Benefits | Prestations du Régime de pensions du Canada |
| `707` | Services to Communities | Services aux collectivités |
| `712` | Registry Services | Services de greffe |
| `716` | Business Information Services | Service d&#39;information aux entreprises de l&#39;APECA |
| `717` | Public Inquiries | Demandes de renseignements du publique |
| `718` | Provision of Information - Access to Information | Communication de renseignements - Accès à l&#39;information |
| `719` | Carrier Code Application | Code de transporteur - Demande de participation |
| `720` | Courier Low Value Shipments (CLVS) Program Application | Demande de programme des messageries d&#39;expéditions de faible valeur (EFV) |
| `721` | Partners in Protection Program Membership Application Processing | Traitement des demandes d&#39;adhésion au programme Partenaires en protection |
| `722` | Trusted Trader Application- Customs Self-Assessment (CSA) | Demande de négociant digne de confiance - Programme d&#39;autocotisation des douanes (PAD) |
| `723` | Cultural Property Export Permits | Biens culturels - Délivrance des licences d&#39;exportation |
| `724` | Request for Assistance Application for Intellectual Property Rights (IPR) | Demande d&#39;aide de droits de propriété intellectuelle |
| `725` | Employee Assistance Services | Services d’aide aux employés |
| `726` | Employee Assistance Services: Employee Assistance Program | Services d’aide aux employés : Programme d’aide aux employés |
| `728` | Commercial Processing (highway, air, rail, marine, postal and courier) | Traitement commercial (routier, aérien, ferroviaire, maritime, postaux et messageries) |
| `729` | Processing Vehicle Import Forms 1 and 3 | Traitment des formulaires d&#39;importation de véhicles 1 et 3 |
| `730` | Public Service Occupational Health Program: Occupational Health Evaluations | Programme de santé au travail de la fonction publique: Évaluations de la santé au travail |
| `731` | Customs Bonded Warehouse Licence Application | Agrément d&#39;entrepôt de stockage des douanes |
| `732` | Public Service Occupational Health Program: Communicable Disease Prevention and | Programme de santé au travail de la fonction publique: Conseils relatifs à la prévention des maladies transmissibles |
| `733` | Customs Sufferance Warehouse License Application | Agrément d&#39;entrepôt d&#39;attente des douanes |
| `734` | Customs Broker Professional Examination and Customs Broker Licencing | Examen de compétences professionnelles des courtiers en douane et Agrément des courtiers en douane |
| `735` | Public Service Occupational Health Program: Occupational Hygiene Advice and Cons | Programme de santé au travail de la fonction publique: Conseils et consultations en matière d&#39;hygiène du travail |
| `736` | Public Service Occupational Health Program: Fitness to Work Evaluations | Programme de santé au travail de la fonction publique: Évaluations de l&#39;aptitude au travail |
| `737` | Release Prior to Payment Privilege | Privilège de la mainlevée avant le paiement |
| `738` | Public Service Occupational Health Program: Reviews for Pension Purposes | Programme de santé au travail de la fonction publique: Examens aux fins de pension de retraite |
| `739` | Public Service Occupational Health Program: Overseas Services | Programme de santé au travail de la fonction publique: Services à l’étranger |
| `740` | Duties Relief Program Application | Exonération des droits |
| `741` | Duty Free Shop Licence Application | Demandes d&#39;agrément de boutique hors taxes |
| `742` | Coasting Trade License (CTL) Application | Demande de licence de cabotage |
| `743` | Casual Refunds | Remboursement pour les importations occasionnelles |
| `744` | B2 Commercial Adjustments | Rajustements du secteur commercial (B2) |
| `745` | Advance Rulings and National Customs Rulings | Décisions anticipées et décisions nationales des douanes |
| `746` | Drawback Claims | Demandes de drawback |
| `747` | Access to Information and Privacy | Accès à l&#39;information et la protection des renseignements personnels |
| `748` | Feedback Mechanism | Mécanisme de rétroaction |
| `749` | Enforcement and Appeals Litigation | Appels des mesures d&#39;exécution et litige |
| `750` | Trade Appeals and Litigation | Appels des échanges commerciaux et litige |
| `751` | Employee Assistance Services: Specialized Organizational Services | Services d’aide aux employés : Services organisationnels spécialisés |
| `752` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `753` | Employee Assistance Services: Trauma Services | Services d’aide aux employés : Services d’intervention post-traumatique |
| `754` | Employee Assistance Services: Informal Conflict Management Services | Services d’aide aux employés : Services d&#39;assistance aux employés: Services de gestion informelle des conflits |
| `755` | Electronic Data Interchange (EDI) - Application and Testing Process | Échange de données informatisé (EDI) – Processus de demande et d’essai |
| `756` | Employee Assistance Services: Occupational Critical Incident Stress Management ( | Services d&#39;aide aux employés : Gestion du stress professionel à la suite d&#39;un incident critique (GSPIC) |
| `757` | Funding Decisions for Grants to Researchers | Décisions sur le financement des subventions de recherche |
| `758` | Funding Decisions for Institutional Capacity | Décisions de financement relatives à la capacité institutionnelle |
| `759` | Grant, Scholarship, Fellowship and Award Administration | Administration des subventions, des bourses et des octrois |
| `761` | Claim for Exemption under the Hazardous Materials Information Review Act | Demande de dérogation en vertu de la Loi sur le contrôle des renseignements relatifs aux matières dangereuses |
| `762` | National Dose Registry | Fichier dosimétrique national |
| `763` | National Dosimetry Services | Services nationaux de la dosimétrie |
| `764` | Health Care Policy Contribution Program | Programme de contributions pour les politiques en matière de soins de santé |
| `765` | Official Languages Health Program | Programme pour les langues officielles en santé |
| `766` | Canadian Thalidomide Survivors Support Program | Programme canadien de soutien aux survivants de la thalidomide |
| `767` | Policy Development Contribution Program | Programme de contributions pour l&#39;élaboration de politiques |
| `768` | Health Canada General Enquiries | Renseignements généraux pour Santé Canada |
| `770` | Statement of Need Program | Programme de déclaration de besoin pour les médecins diplômés |
| `771` | Health Canada Publications | Publications de Santé Canada |
| `772` | Food and Drugs Act Liaison Office (FDALO) | Bureau de liaison pour la Loi sur les aliments et les drogues (BLLAD) |
| `775` | National Disaster Mitigation Program | Programme national d&#39;atténuation des catastrophes |
| `779` | Emergency Management Exercises | Exercices de gestion des urgences |
| `788` | Virtual Risk Analysis | Analyse virtuelle des risques |
| `789` | Critical Infrastructure Gateway | Portail des infrastructures essentielles |
| `790` | Industrial Control Systems Symposiums and Technical Workshops | Symposium et ateliers techniques pour la sécurité des systèmes de contrôle |
| `792` | Critical Infrastructure Exercises | Exercices des infrastructures essentielles |
| `795` | Cyber Security Cooperation Program | Programme de coopération en matière de cybersécurité |
| `798` | Passenger Protect Inquiries Office (PPIO) | Demandes de renseignement du Programme de protection des passagers (BRPPP) |
| `8` | Email | Courriel (Yes et Legacy) |
| `800` | Access to information and privacy | Accès à l’information et protection des renseignements personnels |
| `801` | Safeguarding Science Outreach | Sensibilisation de la science en sécurité |
| `803` | Listed Terrorist Entities | Entités terroristes inscrites |
| `805` | Ministerial Correspondence | Correspondance ministérielle |
| `806` | Canada Centre for Community Engagement and Prevention of Violence | Centre canadien d&#39;engagement communautaire et de prévention de la violence |
| `808` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnel |
| `809` | Public Awareness Campaigns | Campagnes de sensibilisation auprès de la population |
| `810` | Aboriginal Community Safety Development Contribution | Contribution à l&#39;amélioration de la sécurité des collectivités autochtones |
| `811` | Contribution to Combat Serious and Organized Crime | Programme de contribution pour combattre les crimes graves et le crime organisé |
| `813` | Major International Events Security Cost Framework | Cadre sur les coûts de sécurité des événements internationaux majeurs |
| `814` | Nation&#39;s Capital Extraordinary Policing Costs | Contribution pour les coûts extraordinaire des services de police de la capitale nationale |
| `815` | National Flagging System Class Grant | Global de subventions du système national de repérage |
| `816` | Grants and Contributions Program to National Voluntary Organizations | Programme de subventions et de contributions pour les organismes bénévoles nationaux |
| `817` | Biology Casework Analysis Contribution Program | Programme de contribution aux analyses biologiques |
| `818` | National Office for Victims | Bureau national pour les victimes d&#39;actes criminels |
| `822` | Crime Prevention Inventory | Répertoire en prévention du crime |
| `832` | Federal Leadership on Corrections and Criminal Justice Research | Leadership fédéral en recherche correctionnelle et en justice criminelle |
| `838` | NewsDesk | InfoMedia |
| `839` | Federal Emergency Communications Coordination | Coordination des communications fédérales d&#39;urgence |
| `840` | Coordination of Federal Emergency Management (Government Operations Centre) | Coordination de la gestion fédérale des situations d&#39;urgence (Centre des opérations du gouvernement) |
| `843` | GCdocs | Gcdocs |
| `844` | GCcase | GCcas |
| `845` | Regional Resilience Assessments | Évaluations de la résilience régionale |
| `846` | Grants for the Disposal of Surplus Lighthouses | Programme de subventions et de contributions pour l&#39;aliénation de phares excédentaires |
| `849` | Media Relations | Relations médias |
| `850` | Category A - Authorizations under the Pest Control Product Regulations | Catégorie A - L&#39;autorisation en vertu du Règlement sur les produits antiparasitaires |
| `851` | Grant and contribution programs | Programmes de subventions et contributions |
| `859` | Category B - Authorizations under the Pest Control Product Regulations | Catégorie B - L&#39;autorisation en vertu du Règlement sur les produits antiparasitaires |
| `860` | Category C - Authorizations under the Pest Control Product Regulations | Catégorie C - L&#39;autorisation en vertu du Règlement sur les produits antiparasitaires |
| `861` | Category D - Authorizations under the Pest Control Product Regulations | Catégorie D - L&#39;autorisation en vertu du Règlement sur les produits antiparasitaires |
| `862` | Category E - Authorizations under the Pest Control Product Regulations | Catégorie E - L&#39;autorisation en vertu du Règlement sur les produits antiparasitaires |
| `863` | Category F - Authorizations under the Pest Control Product Regulations | Catégorie F - L&#39;autorisation en vertu du Règlement sur les produits antiparasitaires |
| `864` | Category L - Authorizations under the Pest Control Product Regulations | Catégorie L - L&#39;autorisation en vertu du Règlement sur les produits antiparasitaires |
| `865` | Pest Management Information Service | Service de renseignements sur la lutte antiparasitaire |
| `866` | User Requested Minor Use Label Expansions (URMULE) | Profil d&#39;emploi pour les usages limités à la demande des utilisateurs (PEPUDU) |
| `867` | Application for the Inspection of Confidential Test Data | Demande d&#39;examen des données d&#39;essai confidentielles |
| `868` | Category P – Pre-submission Consultation | Catégorie P - Consultations préalables aux demandes d&#39;homologation |
| `869` | Access to information and privacy | Accès à l’information et protection des renseignements personnels |
| `870` | Translation | Traduction |
| `871` | Interpretation | Interprétation |
| `872` | Terminology Standardization | Normalisation terminologique |
| `873` | Executive Correspondence | Correspondance de la haute gestion |
| `874` | Certificate of Pharmaceutical Product (CPP) &amp; Good Manufacturing Practices (GMP) | Certificat de produit pharmaceutique (CPP) de Bonnes Pratiques de Fabrication (BPF) |
| `875` | Drug Establishment Licensing (DEL) | Les licences d&#39;établissement de produits pharmaceutiques (LEPP) |
| `876` | Manufacturer&#39;s Certificate to Export licenced medical devices from Canada (MCE) | Certificat du fabricant relatif à l&#39;exportation d&#39;instruments médicaux homologués au Canada (CFE) |
| `877` | Medical Device Establishment Licencing (MDEL) | Licence d&#39;établissement pour les instruments médicaux (LEIM) |
| `878` | Registration of a Cells, Tissues and Organs (CTO) Establishment | Inscription d&#39;un établissement des Cellules, des Tissus et des Organes (CTO) |
| `879` | Drug Analysis Service (DAS) - Forensic analysis services | Service d&#39;analyse des drogues (SAD) – Services d&#39;analyse judiciaire |
| `880` | Drug Analysis Service (DAS) - Support services | Service d&#39;analyse des drogues (SAD) – Services de soutien |
| `881` | Federal Leadership on Crime Prevention Research | Leadership fédérale en matière de recherche sur la prévention du crime |
| `882` | First Nations and Inuit Policing Program (FNIPP) | Programme des Services de Police des Premières Nations et des Inuits (PSPPNI) |
| `888` | Grants and Contributions Services | Services des subventions et contributions |
| `890` | National Emergency Strategic Stockpile: Request for Assistance (RFA) | Réserve nationale stratégique d&#39;urgence |
| `891` | Authorization to Conduct Controlled Activities with Pathogens and Toxins | Autorisation d’exercer des activités réglementées avec des agents pathogènes et des toxines |
| `892` | Human Pathogens and Toxins Act Security Clearance | Loi sur les agents pathogènes et les toxines (LAPHT) autorisation de sécurité |
| `895` | Yellow Fever Vaccination Centre Designation | Désignation d&#39;un centre de vaccination contre la fièvre jaune |
| `896` | Access to Information and Privacy (ATIP) | Accès à l&#39;information et la protection des renseignements personnels (AIPRP) |
| `898` | Public Enquiries | Demandes de renseignement |
| `899` | Public Health Agency of Canada Publications | Publications de l&#39;Agence de la santé publique du Canada |
| `900` | Pension Administration – Pension Payments and Services | Administration des pensions – Prestations et services de pension |
| `901` | Receiver General Services – Management of Government of Canada Deposits | Services du receveur général ‒ Gestion des dépôts du gouvernement du Canada |
| `902` | Receiver General Services – Issuing payments | Services du receveur général Émission de paiements |
| `903` | Common Departmental Financial System | Système financier ministériel commun |
| `904` | Document Imaging Services | Services d&#39;imagerie documentaire |
| `905` | Canadian General Standards Board | Office des normes générales du Canada |
| `906` | Seized Property Management Directorate | Direction de la gestion des biens saisis |
| `907` | Complaints Information and Enquiry | Renseignements général et plaintes |
| `908` | GCSurplus | GCSurplus |
| `909` | Advertising – Coordination, Advisory and Training Services | Publicité ‒ Services de coordination, services-conseils et de formation |
| `910` | Public Opinion Research – Coordination, Advisory and Knowledge Management Services | Recherche sur l&#39;opinion publique ‒ Services de coordination, services-conseils et services de gestion des connaissances |
| `911` | Canada Gazette – Publication of Official Notices, Laws and Regulations | Gazette du Canada ‒ Publication des avis officiels, de lois et de règlements |
| `912` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `913` | Centralized Electronic Access to Government of Canada Publications | Accès électronique centralisé aux publications du gouvernement du Canada |
| `914` | Reference Services for Government of Canada Publications | Services de référence pour les publications du gouvernement du Canada |
| `915` | Licence application for nuclear substances and radiation devices | Demandes de permis de substances nucléaires et d’appareils à rayonnement |
| `916` | Copyright Media Clearance Program | Programme d’autorisation pour les médias protégés par les droits d’auteur |
| `917` | Licence application for Class II nuclear facilities and prescribed equipment | Demandes de permis pour installations nucléaires et équipement réglementé de catégorie II |
| `918` | Import or export licence application | Demande de permis d’importation ou d’exportation |
| `919` | Application for certification of exposure device operators | Demande d’accréditation des opérateurs d’appareil d’exposition |
| `920` | Transport licence application | Demande de permis de transport |
| `921` | Participant Funding Program | Programme de financement des participants |
| `9223` | Climate Change Funding Programs - Implementation Readiness Fund | Programmes de financement pour le changement climatique - Fonds de préparation à la mise en œuvre |
| `924` | Professional and Technical Services | Services Professionnels et Techniques |
| `925` | Ministerial Correspondence | Correspondance ministérielle |
| `926` | Canadian Firearms Program (CFP) - Firearms Licensing for individuals | Programme canadien des armes à feu (PCAF) - Permis d&#39;armes à feu pour les particuliers |
| `927` | Canadian Firearms Program (CFP) - Firearms Licensing for businesses | Programme canadien des armes à feu (PCAF) - Permis d&#39;armes à feu pour les entreprises |
| `928` | National Forensic Laboratory Services (NFLS) | Services nationaux de laboratoire judiciaure (SNLJ) |
| `929` | Certified Criminal Record Checks | Attestation de vérification de casier judiciaire |
| `930` | Canadian Criminal Real Time Identification Services (CCRTIS) - Accreditation Services | Les Services canadiens d&#39;identification criminelle en temps réel (SCICTR) - Service d&#39;accréditation |
| `931` | Integrated Forensic Identification Services (IFIS)- Disaster Victim Identification (DVI) | Service intégré de l&#39;identité judiciaire (SIIJ) - d&#39;identification des victimes de catastrophes (IVC). |
| `932` | National DNA Data Bank (NDDB) Indices Comparison | Banque nationale de données génétiques - comparaison des indices (BNDG) |
| `934` | Canadian Police Information Centre (CPI Centre) | Centre d&#39;information de la police canadienne (Centre IPC) |
| `935` | Canadian Police College (CPC) | Collège canadian de police (CCP) |
| `936` | National Law Enforcement Training (NLET) | Groupe de la formation policière nationale (GFPN) |
| `937` | Access to Information and Privacy (ATIP) | Accès à l’information et de protection des renseignements personnels (AIPRP) |
| `938` | Contract Security (Company Registration, Personal Security Screening, Call Centre) | Sécurité des contrats (enregistrement d&#39;une entreprise, filtrage de la sécurité du personnel, centre d&#39;appels) |
| `939` | Integrity Verification Services | Services de vérification d&#39;intégrité |
| `940` | Controlled Goods (Company Registration, Security Assessments, Exemption Applications for Visitors, Temporary Workers and International Students) | Marchandises contrôlées (enregistrement des entreprises, évaluations de sécurité, demandes d&#39;exemption pour les visiteurs, les travailleurs temporaires et étudiants étrangers) |
| `941` | Fairness Monitoring Services | Services de surveillance de l&#39;équité |
| `942` | Business Dispute Management Services | Gestion des conflits d&#39;ordre commercial |
| `943` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `944` | Secure Air Travel Act Recourse | Recours en vertu de la Loi sur la sûretés des déplacement aériens |
| `946` | Federal Leadership on Law Enforcement and Policing Research | Leadership fédéral en recherche en matière d&#39;application de la loi et la police |
| `947` | Passport Cancellation Reconsideration | Réexamen de l&#39;annulation des passeports |
| `949` | Registry Services (Registrar) | Service du greffe (greffier) |
| `95` | Intra-building Network Services | Services de réseau à l’intérieur des immeubles |
| `950` | Library Services | Service de Bibliothèque |
| `951` | Visitor Services and Experiences | Services et expériences aux visiteurs |
| `952` | Accommodation services in Parks Canada&#39;s Places | Services d&#39;hébergement dans les endroits de Parcs Canada |
| `954` | Issuance of Leases and Licenses of Occupation | Émission de baux et de permis d&#39;occupation |
| `955` | Townsite Management | Gestion des lotissements urbains |
| `956` | Atlantic Fisheries Fund | Fonds des pêches de l&#39;Atlantique |
| `957` | Lockage Services | Service d&#39;éclusage |
| `960` | Shared Travel Services | Services de voyage partagés |
| `961` | Access to Information Service | Service d&#39;accès à l&#39;information |
| `962` | Output-Based Pricing System (OPBS) Registration System | Système de tarification fondé sur le rendement |
| `963` | National Environmental Emergencies Centre | Centre National des Urgences Environnementales |
| `965` | Antarctic Environmental Protection Act permitting | Délivrance de permis - Loi sur la protection de l’environnement en Antarctique |
| `966` | GC Accommodations space management system | Système de gestion de l&#39;espace de GC locaux |
| `967` | Property and Facility Management | Gestion des biens et des installations |
| `968` | Events and Conference Management | Gestion d&#39;événements et de conférences |
| `969` | Architecture and Engineering | Architecture et génie |
| `970` | Payments in Lieu of Taxes | Paiements en remplacement d&#39;impôts |
| `971` | Real Estate Services | Services des biens immobiliers |
| `972` | Property Portfolio and Asset Advisory Services | Services consultatifs en matière de gestion de portefeuilles de biens immobiliers et de biens |
| `973` | Environment, Health and Safety Services for Real Property | Services en matière d&#39;environnement, de santé et de sécurité pour les biens immobiliers |
| `974` | Geomatics Services | Services géomatique |
| `975` | Federal Identification Registry for Storage Tank Systems (FIRSTS) | Registre fédéral d&#39;identification des systèmes de stockage (RFISS) |
| `977` | Ecological Gifts Program | Programme des dons écologiques |
| `978` | Public and Media Inquiries | Demandes de renseignements du public et des médias |
| `979` | Climate Change Funding Programs - Low Carbon Economy Challenge: Partnerships | Défi pour une économie à faibles émissions de carbone: volet des partenariats |
| `980` | Climate Change Funding Programs - Climate Action Fund | Le Fonds d&#39;action pour le climat |
| `981` | Public Inquiries Centre | Centre de renseignements à la population |
| `982` | Ministerial Correspondence | Correspondance ministérielle |
| `983` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `984` | Shared Human Resources Services | Services partagés en ressources humaines |
| `985` | Import permits for species harmful to Canadian ecosystems | Permis d&#39;importation d&#39;espèces nuisibles aux écosystèmes du Canada |
| `986` | Permits for trade in protected species | Permis pour le commerce d&#39;espèces protégées |
| `987` | Migratory Birds: all other permits | Oiseaux migrateurs: autres permis |
| `988` | Permits under the Wildlife Area Regulations | Permis en vertu du Règlement sur les réserves d&#39;espèces sauvages |
| `989` | Complaint Investigation of Suspected Inaccurate Measurement | Enquête sur les plaintes concernant les mesures inexactes soupçonnées |
| `990` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `991` | Canada Pension Plan Disability Benefits | Prestations d’invalidité du Régime de pensions du Canada |
| `992` | Northern Scientific Training Program (NSTP) | Programme de formation scientifique dans le Nord (PFSN) |
| `993` | Transfer Payments to Support Research and Activities Relating to the Polar Region | Paiements de transfert pour soutenir la recherche et les activités qui ont trait aux régions polaires |
| `994` | Transfer Payments to Support the Advancement of Northern Science and Technology | Programme de paiements de transfert en appui aux progrès scientifiques et technologiques dans le Nord |
| `995` | Access to Information and Privacy | Accès à l&#39;Information et Protection des Renseignements Personnels |
| `996` | Aids to Navigation | Aides à la navigation |
| `997` | British Columbia Aquaculture Regulatory Program | Programme de réglementation de l&#39;aquaculture en Colombie-Britannique - Modifications administratives |
| `998` | British Columbia Aquaculture Regulatory Program - Minor Technical Amendments | Programme de réglementation de l&#39;aquaculture en Colombie-Britannique - Modifications techniques mineures |
| `999` | British Columbia Aquaculture Regulatory Program - Applications for new licenses | Programme de réglementation de l&#39;aquaculture en Colombie-Britannique - Nouveaux sites et modifications techniques majeures |
| `SRV02642` | Test Market Authorization | Autorisation d&#39;essai de mise en marché |
| `SRV02643` | Ministerial Exemptions for the Purpose of Alleviating a Shortage in Canada | Exemptions ministérielles pour atténuer une pénurie d&#39;approvisionnement au Canada |
| `SRV02646` | Ministerial Exemption - Authorization Request, Movement of Products under SFCR | Exemption Ministre - Demande d&#39;autorisation pour mouvement de produits en vertu du RSAC |
| `SRV02647` | Meat Work Shift Agreements | Les ententes relatives aux périodes de travail de viande |
| `SRV02648` | C-PIQ - Canadian Partners in Quality Participation Program | Programme des partenaires pour la qualité au Canada (PPQ-C) |
| `SRV02649` | Certificate of Free Sale | Certificat de vente libre |
| `SRV02650` | Permit to Operate an Animal Semen Production Centre | Permis pour opérer un centre de production de sperme animal |
| `SRV02651` | Licence to operate a hatchery | Licence pour exploiter un couvoir |
| `SRV02652` | Accredited Veterinarian Agreement | Entente d&#39;accréditation des vétérinaires |
| `SRV02653` | Veterinarian Certification Procedure to Export Embryos | Procédure pour des vétérinaires de certification des embryons destinés à l&#39;exportation |
| `SRV02654` | Accredited External Laboratories | Laboratoires d&#39;accrédité externes |
| `SRV02655` | Soil Handling Program | Programme de manipulation de la terre |
| `SRV02656` | Aquatic Animal Domestic Movements | Déplacements d&#39;animaux aquatiques en territoire canadien |
| `SRV02657` | Specified Risk Material (SRM) Permit | Permis pour les matières à risque spécifiées (MRS) |
| `SRV02658` | Time-Sensitive Specified Risk Material (SRM) Permit | Permis de transport rapide pour les matières à risque spécifiées (MRS) |
| `SRV02659` | Cervid Movement Permit | Permis de déplacement des cervidés |
| `SRV02660` | Livestock Feed Registration or Renewal | Enregistrement ou renouvellement des aliments pour animaux de ferme |
| `SRV02661` | Research Exemption with Safety - Research with Livestock Feeds | Dispense de recherche avec la sécurité - Recherche sur les aliments pour animaux de ferme |
| `SRV02662` | Research Exemption - Research with Livestock Feeds | Dispense de recherche - Recherche sur les aliments pour animaux de ferme |
| `SRV02663` | Research Authorization- Research with Livestock Feeds | Autorisation de recherche - Recherche sur les aliments pour animaux de ferme |
| `SRV02664` | Product Licensing Submissions for Veterinary Biologics | Demandes d&#39;homologation de nouveaux produits |
| `SRV02665` | Veterinary Biologics Serial Release | Mise en circulation des séries de produits biologiques vétérinaires |
| `SRV02666` | Label review for major and or minor Veterinary Biologics | Évaluation de l&#39;étiquette |
| `SRV02667` | Aquatic Animal Health Compartmentalization Program | Programme de compartimentation santé des animaux aquatiques |
| `SRV02668` | Equine Infectious Anemia Control Program | Programme de lutte contre l&#39;anémie infectieuse des équidés |
| `SRV02669` | Chronic Wasting Disease Herd Certification Programs | Programmes de certification des troupeaux pour la maladie débilitante chronique |
| `SRV02670` | Scrapie Flock Certification Program | Programme de certification des troupeaux à l&#39;égard de la tremblante |
| `SRV02671` | Canadian Ractopamine-Free Poultry Certification Program | Programme canadien de certification des volailles exemptes de ractopamine |
| `SRV02672` | Canadian Ractopamine-Free Pork Certification Program | Programme canadien de certification des porcs exempts de ractopamine |
| `SRV02673` | Canadian Beta Agonist-Free Beef Certification Program | Programme canadien de certification des bovins exempts de bêta-agonistes |
| `SRV02674` | Certifying Freedom from Growth Enhancing Products - Beef to the EU | Programme Canadien de certification de l&#39;absence de stimulants de croissance pour l&#39;exportation de viande bovine à l&#39;Union Européenne |
| `SRV02675` | Growth Enhancing Products-Free (GEPs-Free) Veal Certification Program | Programme de certification des veaux exempts de produits stimulants de croissance (PSC) |
| `SRV02676` | Permit to release mink coronavirus experimental vaccine for emergency use | Permis de dissémination du vaccin expérimental pour visons contre le coronavirus pour les besoins d&#39;urgence |
| `SRV02677` | Import Plant-based Feed Ingredients | Importation d&#39;ingrédients d&#39;origine végétale destinés aux aliments du bétail |
| `SRV02678` | Import Animal Products and By-Products | Importation des produits et sous-produits d&#39;animaux terrestres |
| `SRV02679` | Import Aquatic Animals | Importation d&#39;animaux aquatiques |
| `SRV02680` | Import Animal Pathogens | Importation des zoonoses pathogènes |
| `SRV02681` | Import Veterinary Biologics | Importation de produits biologiques vétérinaires |
| `SRV02682` | Veterinary Biologics Export Certificates | Certificats d&#39;exportation de produits biologiques vétérinaires |
| `SRV02683` | Export Certificates - live animal, animal products and by-products | Certificats de santé pour l&#39;exportation - des produits et sous-produits d&#39;animaux terrestres |
| `SRV02687` | Licence to Print Official Seed Tag | Licence pour imprimer des etiquettes officielles de semence |
| `SRV02688` | Multiplication Agreement for Varietal Certification of Seed Multiplied Abroad | Entente de multiplication pour la certification variétale des semences à l&#39;étranger |
| `SRV02689` | Recognition of Export Grain Analysis by Authorized Laboratories (REGAL) program | Le Programme de laboratoires autorisé pour l&#39;analyse des grains à l&#39;exportation (PLAAGE) |
| `SRV02690` | Seed Import Conformity Assessor | Évaluateur de la conformité des semences importee |
| `SRV02691` | Research Authorization under the Fertilizers Act and Regulations | Autorisation d&#39; recherches en vertu de la Loi sur les engrais |
| `SRV02692` | Unconfined Environmental Release Authorization | Autorisation de la dissémination en milieu ouvert |
| `SRV02693` | Confined Research Field Trial Authorization (PBO) | Autorisation de la conduite d&#39;essais de recherche au champ en conditions confinées |
| `SRV02694` | Authorized Exporter Program | Programme d&#39;exportateur autorisé |
| `SRV02695` | Evaluation and Recognition of Third Party Auditors | l&#39;évaluation et à la reconnaissance des tiers auditeurs |
| `SRV02696` | Hay Export Program | Programme d&#39;exportation de foin |
| `SRV02697` | Canadian Nursery Certification Program | Programme canadien de certification des pépinières |
| `SRV02698` | Niger Seed Export Program | Programme d&#39;exportation de graines de niger |
| `SRV02699` | Seed Potato Tuber Quality Management Program | Programme de gestion de la qualité des tubercules de pommes de terre de semence |
| `SRV02700` | Canadian Debarking Grub Hole Control Program for Export of Cedar Forest Products | Programme canadien d&#39;écorçage du bois et de contrôle des trous de vers (PCEBCTV) pour l&#39;exportation de produits forestiers de thuya vers l&#39;Union européenne |
| `SRV02701` | Forage (Heated) Export Program | Programme d&#39;exportation des fourrages séchés à la chaleur |
| `SRV02702` | Pre-Shipment Approval Program for the Export of Grain from Canada | Programme d&#39;approbation pré-expédition s&#39;appliquant au grain exporté par le Canada |
| `SRV02703` | Fruit Tree Export Program | Programme d&#39;exportation d&#39;arbres fruitiers |
| `SRV02704` | Grain, Seed, Screening Program | Programme des grains, semences, criblures |
| `SRV02705` | Canadian Heat Treated Wood Products Certification Program | Programme canadien de certification des produits de bois traités à la chaleur |
| `SRV02706` | Canary Seed Export Program | Programme d&#39;exportation de l&#39;alpiste des Canaries |
| `SRV02707` | Hardwood Export Program | Programme d&#39;exportation de bois de feuillus |
| `SRV02708` | Wild Rice Export Program | Programme d&#39;exportation de riz sauvage |
| `SRV02709` | Canadian Sawn Wood Certification Program | Programme canadien de certification du bois scié |
| `SRV02710` | United States – Canada Greenhouse-Grown Plant Certification Program | Programme États-Unis - Canada de certification des végétaux cultivés en serre |
| `SRV02711` | Canadian Growing Media Program, Approval Process and Import Requirements | Programme canadien des milieux de culture, processus d&#39;approbation préalable et exigences en matière d&#39;importation de végétaux enracinés dans des milieux de culture approuvés |
| `SRV02712` | Grapevine Export Program | Programme d&#39;exportation de la vigne |
| `SRV02713` | Systems Approach Based Oriental Fruit Moth Certification Program | Programme de certification visant la tordeuse orientale du pêcher fondé sur une approche systémique |
| `SRV02714` | Plant Pest Containment Program | Programme de confinement pour phytoravageurs |
| `SRV02715` | Canadian Phytosanitary Certification Program for Seed (CPCPS) | Programme canadien de certification phytosanitaire des semences (PCCPS) |
| `SRV02716` | SMSRC Response and Support Coordination program | CSRIS Programme de coordination de l’intervention et du soutien |
| `SRV02717` | Sexual Misconduct Support and Resource Centre 24/7 Support Line | Centre de soutien et de ressources sur l&#39;inconduite sexuelle (CSRIS) Ligne de Soutien 24/7 |
| `SRV02718` | SMRC Contribution Program | Programme de contributions du CIIS |
| `SRV02719` | Restorative Engagement | Démarches Réparatrices |
| `SRV02720` | Licence to Use Seed Potato Certification Tags | Permis pour utiliser des Étiquettes de certification des pommes de terre de semence |
| `SRV02721` | Emerald Ash Borer Program | Programme de l&#39;agrile du frêne |
| `SRV02722` | Japanese Beetle Program | Programme du scarabée japonais |
| `SRV02723` | Apple Maggot Program | Programme de la mouche de la pomme |
| `SRV02724` | Woolly Cup Grass | prévenir la propagation d&#39;Eriochloa villosa (ériochloé velue) |
| `SRV02725` | Canadian Grain Sampling Program | Programme canadien d&#39;échantillonnage des grains |
| `SRV02726` | Barberry Propagation Program | Programme de multiplication de l&#39;épine-vinette |
| `SRV02727` | Blueberry Certification Program | Programme de certification des bleuets |
| `SRV02728` | Crop Variety Registration (VRO) | Enregistrement des variétés |
| `SRV02729` | Fertilizer or Supplement Registration | Enregistrement d&#39;engrais ou de supplément |
| `SRV02730` | Plant Breeders&#39; Rights (PBR Certificate) | Protection des obtentions végétales |
| `SRV02731` | Phytosanitary Certificate for Export | Certificat phytosanitaire pour l&#39;exportation |
| `SRV02732` | Seed Analysis Certificate for Export Purposes (CFIA 1113) | Certificat d&#39;analyse de semences aux fins d&#39;exportation |
| `SRV02733` | Certificate of Origin (Plant Pests / LDD) | Certificat d&#39;origine (spongieuse nord-américaine, Lymantria dispar) |
| `SRV02734` | Re-export Phytosanitary Certificate | certificats phytosanitaires de réexportation |
| `SRV02735` | Request for Opinion or Data Review for Livestock Feeds | Demande d&#39;avis ou d&#39;examen de données pour les aliments du bétail |
| `SRV02736` | Regulatory Opinion PNT/VRO | Avis réglementaire (VCN/BEV) |
| `SRV02737` | Ask CFIA | Demandez à l&#39;ACIA |
| `SRV02738` | General Enquiries | Demande de renseignements |
| `SRV02739` | Plant Health Investigation - Incident Response | Enquête sur la salubrité des végétaux - intervention en cas d’incident |
| `SRV02740` | Non-propagative Potato Program | Programme de pommes de terre non destinées à la multiplication |
| `SRV02741` | Notice of Import Conformity | Ll&#39;avis de libération |
| `SRV02742` | Destination Inspection Service (DIS) | Service d&#39;inspection à destination (SID) |
| `SRV02743` | Licenced Seed Crop Inspector | Inspecteur de cultures de semences agréés |
| `SRV02744` | Authorized Seed Crop Inspection Service | Service d&#39;inspection de cultures de semences autorisés |
| `SRV02745` | Agriculture Climate Solutions | Solutions Agricoles Pour le Climat |
| `SRV02746` | Market Development Program for Turkey and Chicken | Programme de développement des marchés du dindon et du poulet |
| `SRV02747` | The Poultry and Egg-On Farm Investment Program | Le Programme d&#39;investissement à la ferme pour la volaille et les œufs |
| `SRV02748` | Supply Management Processing Investment Fund | Le Fonds d&#39;investissement pour la transformation des produits sous la gestion de l&#39;offre |
| `SRV02750` | Disposal at sea emergency permits | Permis d’immersion en mer d’urgence |
| `SRV02751` | Environmental emergencies | Urgences environnementales |
| `SRV02752` | Accreditation of Seed Graders | Accréditation de classificateurs de semences |
| `SRV02753` | Brown Spruce Longhorned Beetle Program | Programme du longicorne brun de l&#39;épinette |
| `SRV02754` | Growers Crop Certificate - &#34;Seed Potato Certification Program&#34; | Certificat de culture des producteurs - « Programme de certification des pommes de terre de semence » |
| `SRV02755` | Fertilizer Export Certificates | Certificats d&#39;exportation pour l&#39;engrais |
| `SRV02762` | Permit to Import - Plants and Plant Products | Permis d&#39;importation - les végétaux et les produits végétaux |
| `SRV02763` | Notice to Industry | Avis à l&#39;industrie |
| `SRV02764` | Preventative Control Inspection | l&#39;inspection de contrôle préventif |
| `SRV02765` | Supporting a Humanitarian Workforce to Respond to COVID-19 and Other Large-Scale Emergencies | Appuyer une main-d&#39;œuvre humanitaire pour répondre à la COVID-19 et à d&#39;autres urgence de grande envergure |
| `SRV02766` | Building Safer Communities Fund | Fonds pour bâtir des communautés sécuritaires |
| `SRV02767` | Written Authorization to Conduct Activities on Plant Pests | Autorisation écrite de mener des Activités sur des phytoravageurs |
| `SRV02768` | Regional Air Transportation Initiative (RATI) | L’Initiative régionale de transport aérien (ITAR) |
| `SRV02769` | Care and Custody | Prise en charge et garde |
| `SRV02770` | Plant Movement Certificate | Certificat de circulation de végétaux |
| `SRV02771` | Canada Community Revitalization Fund (CCRF) | Le Fonds canadien de revitalisation des communautés (FCRC) |
| `SRV02772` | Tourism Relief Fund (TRF) | Le Fonds d’aide au tourisme |
| `SRV02773` | Jobs and Growth Fund (JGF) | Le Fonds pour l’emploi et la croissance |
| `SRV02774` | Aerospace Regional Recovery Initiative (ARRI) | L’Initiative de relance régionale de l’aérospatiale (IRRA) |
| `SRV02775` | Data Centre Facilities | Installations des centres de données |
| `SRV02776` | Public Awareness Contribution Program (PACP) | Programme de contribution à la sensibilisation du publique (PCEP) |
| `SRV02779` | Real Property Contract Oversight Services | Services de surveillance des contrats immobiliers |
| `SRV02780` | Project Management | Gestion de projet |
| `SRV02783` | Correctional Interventions | Interventions correctionnelles |
| `SRV02784` | Community Supervision | Surveillance dans la collectivité |
| `SRV02785` | Indigenous Reconciliation Transfer Payment Program - RAP - Contributions | Programme de paiements de transfert de la réconciliation avec les Autochtones - contributions |
| `SRV02786` | Treaty Related Measures Contribution Agreement (TRM) | Entente de contribution sur les mesures liées aux traités (ETR) |
| `SRV02787` | Network Services | Services de réseau |
| `SRV02789` | Application for Cannabis Record Suspension | Demande de suspension du casier liée au cannabis |
| `SRV02790` | Intellectual Property Centre of Expertise (IP CoE) | Centre d&#39;expertise en Propriété intellectuelle (CE PI) |
| `SRV02791` | Canada Digital Adoption Program - Boost Your Business Technology | Programme canadien d’adoption du numérique - Améliorez les technologies de votre entreprise |
| `SRV02792` | Weather Information Services to Public Authorities | Services d&#39;informations météorologiques aux autorités publiques |
| `SRV02793` | Meteorological Support for Environmental Emergency Response | Soutien météorologique pour les urgences environnementales |
| `SRV02795` | Temporary exemption for emergency circumstances under the Reduction of Carbon | Exemption temporaire pour situations d&#39;urgence en vertu du Règlement sur la réduction des émissions de dioxyde de carbone |
| `SRV02798` | Temporary waivers to fuel regulations | Exemptions temporaires en vertu des règlements sur les carburants |
| `SRV02800` | Antarctic Environmental Protection Act permitting | Protection de l&#39;environnement en Antarctique |
| `SRV02811` | Enhanced Nature Legacy - Indigenous-led Area Based Conservation | Conservation par zone menée par les Autochtones - Capacité et formation |
| `SRV02812` | Enhanced Nature Legacy - Indigenous-led Area Based Conservation - Establishment | Conservation par zone menée par les Autochtones - Établissement |
| `SRV02813` | Nature Smart Climate Solutions Fund | Fonds des solutions climatiques axées sur la nature |
| `SRV02814` | Avalanche Control | Contrôle des avalanches |
| `SRV02815` | GCXchange | GCéchange |
| `SRV02816` | Taxation Statistical Analyses and Data Processing | Analyse statistique et traitement de données de l’impôt |
| `SRV02817` | Debt Management Call Centre | Centre d’appels de la gestion des créances |
| `SRV02818` | Financial audits of the Public Accounts of Canada | Audit des états financiers des Comptes publics du Canada |
| `SRV02820` | Internal Audit | Audit Interne |
| `SRV02821` | Scientific Research and Experimental Development (SR&amp;ED) Tax Credits, Canadian film or video production tax credit (CPTC), and film or video production services tax credit (PSTC) – Claims not selected for a review or an audit | Crédit d’impôt pour la recherche scientifique et le développement expérimental (RS&amp;DE), crédit d’impôt pour production cinématographique ou magnétoscopique canadienne (CIPC) et crédit d’impôt pour services de production cinématographique ou magnétoscopique (CISP) Demandes non sélectionnées pour un examen ou une vérification |
| `SRV02822` | Scientific Research and Experimental Development (SR&amp;ED) Tax Credits – Refundable claims selected for a review | Crédit d’impôt pour la recherche scientifique et le développement expérimentale (RS&amp;DE) – demandes remboursables sélectionnées pour un examen |
| `SRV02823` | Event Management Service | Service de gestion d&#39;évenements |
| `SRV02824` | Canadian film or video production tax credit (CPTC) and film or video production services tax credit (PSTC) – Claims selected for an audit | Crédit d’impôt pour production cinématographique ou magnétoscopique canadienne (CIPC) et crédit d&#39;impôt pour services de production cinématographique ou magnétoscopique (CISP) – Demandes sélectionnées pour une vérification |
| `SRV02825` | Canada Worker Lockdown Benefit (CWLB) | Prestation canadienne pour les travailleurs en cas de confinement (PCTCC) |
| `SRV02826` | Hardest-Hit Business Recovery Program (HHBRP) | Programme de relance pour les entreprises les plus durement touchées (PREPDT) |
| `SRV02827` | Financial audit of Export Development Canada’s consolidated financial statements | Audit d’états financiers consolidés d’Exportation et développement Canada |
| `SRV02828` | Tourism and Hospitality Recovery Program (THRP) | Programme de relance pour le tourisme et l&#39;accueil (PRTA) |
| `SRV02829` | Financial audits of territorial organizations | Audits financiers des organisations territoriales |
| `SRV02830` | Canada Recovery Hiring Program (CRHP) | Programme d&#39;embauche pour la relance économique du Canada (PEREC) |
| `SRV02831` | Local Lockdown Program (LLP) | Programme de soutien en cas de confinement local |
| `SRV02832` | Internal Communications | Communications internes |
| `SRV02834` | Graphic Design Services | Services de conception graphique |
| `SRV02836` | Editing Services | Services de révision |
| `SRV02838` | Public Enquiries Services | Services de renseignements au public |
| `SRV02840` | Web services | Services web |
| `SRV02841` | Social Media Services | Services des médias sociaux |
| `SRV02842` | Strategic Communications | Communication Stratégiques |
| `SRV02843` | Digital Communications and Design Support | Communications numériques et aide à la conception |
| `SRV02844` | Consular Outreach and Stakeholder Engagement | Service de sensibilisation du Public |
| `SRV02845` | Media Relations | Relations avec les médias |
| `SRV02846` | Media monitoring and analysis | Surveillance et analyse des médias |
| `SRV02848` | Public Opinion Research and Consultations | Recherche en opinion publique et consultations |
| `SRV02849` | Financial audits of international organizations | Audits financiers des organisations internationales |
| `SRV02850` | Performance audits of territorial Organizations | Audit de performance d’organisations territoriales |
| `SRV02851` | International Relations Correspondence | Correspondance pour les relations internationales |
| `SRV02852` | Environmental petitions correspondence | Correspondance pour les pétitions environnementales |
| `SRV02853` | Environmental Petitions | Pétitions environnementales |
| `SRV02854` | Health Policy Branch Transfer Payment Programs | Programmes de paiements de transfert de la Direction générale des politiques de santé |
| `SRV02855` | Public inquiries | Demandes de renseignements du public |
| `SRV02856` | Media relations | Relations avec les médias |
| `SRV02857` | Technical accounting and audit advisory services | Services-conseils spécialisés en comptabilité et en audit |
| `SRV02859` | Grants and Contributions in Aid of Academic Relation | Subventions et contributions en appui aux relations academiques |
| `SRV02860` | Trade commissioner service | Services des délégués commerciaux |
| `SRV02862` | Foreign Direct Investment | Investissement direct étranger |
| `SRV02863` | Requests for designation, regional assessment, and strategic assessment | Des demandes de désignation, d&#39;évaluation régionale et d&#39;évaluation stratégique |
| `SRV02864` | Employee Assistance Services | Services d’aide aux employés |
| `SRV02865` | Public Service Occupational Health Program | Programme de santé au travail de la fonction publique |
| `SRV02866` | Hazardous Waste Export and Import Permits | Permis d’exportation et d’importation de déchets dangereux |
| `SRV02867` | Permit for disposal at sea | Permis pour l&#39;immersion en mer |
| `SRV02868` | Rapid Test Kit Provision (Federal) | Fourniture de kit de test rapide (fédéral) |
| `SRV02869` | International Accommodation Services | Services d&#39;hébergement internationaux |
| `SRV02870` | Client Relations | Relations avec les clients |
| `SRV02871` | Engineering Services | Service d&#39;ingénierie |
| `SRV02872` | Material Management Service | Service de gestion du matériel |
| `SRV02873` | Transfer and diffusion of space technology | Diffusion et transfert de technologies spatiales |
| `SRV02874` | Security Program Management Service | Service de gestion de programme de sécurité |
| `SRV02875` | Atmospheric data on carbon monoxide concentration (MOPITT on Terra) | Données atmosphériques sur la concentration de monoxyde de carbone (MOPITT sur Terra) |
| `SRV02876` | Criminal Code Designations | Désignations du Code criminel |
| `SRV02877` | Atmospheric data on ozone, aerosol &amp; nitrogen dioxide concentration (OSIRIS-Odin) | Données atmosphériques sur la concentration d’ozone, d’aérosols et de dioxyde d’azote (OSIRIS-Odin) |
| `SRV02878` | Atmospheric gas monitoring data (SCISAT) | Données de surveillance des gaz atmosphériques (SCISAT) |
| `SRV02879` | Space imagery data for Space Astronomy (NEOSSAT) | Données d’imagerie spatiale pour l&#39;astronomie (NEOSSAT) |
| `SRV02880` | Space imagery data for Space Surveillance (NEOSSAT) | Données d’imagerie spatiale pour la surveillance de l’espace (NEOSSAT) |
| `SRV02881` | National Information Services | Services national d&#39;information (SNI) |
| `SRV02882` | Earth Observation Data (RCM) | Données d&#39;observation de la Terre (MCR) |
| `SRV02883` | Earth Observation Data (R2) | Données d’observation de la Terre (R2) |
| `SRV02884` | Historical Earth observation data (R1) | Données historiques d&#39;observation de la Terre (R1) |
| `SRV02885` | Guidelines on risk-based monitoring of grants and contributions | Lignes directrices sur le suivi axé sur les risques des subventions et de contributions |
| `SRV02886` | Access to Places Administered by Parks Canada | Accès aux Lieux Administrés par Parcs Canada |
| `SRV02887` | Emergency Dispatch | Envoi d&#39;urgence |
| `SRV02888` | User support for SAR data (Service Desk) | Support aux utilisateurs des données SAR (Service Desk) |
| `SRV02889` | Support for SCISAT data users | Support aux utilisateurs des données SCISAT |
| `SRV02890` | Weights and Measures Calibration | L&#39;étalonnage des appareils de pesage et de mesure |
| `SRV02891` | Connecting Canadians to Canada’s Natural and Cultural Heritage | Connecter les Canadiens au Patrimoine Naturel et Culturel du Canada |
| `SRV02896` | Issuance of Research and Collections Permits | Délivrance de permis de recherche et de collections |
| `SRV02898` | Promotion and Disease Prevention: Communicable Disease Control and Management - Direct Service Delivery | Promotion et prévention des maladies : Contrôle et gestion des maladies transmissibles - Prestation directe de services |
| `SRV02899` | Pathways to Safe Indigenous Communities | Voies vers des communautés autochtones sûres |
| `SRV02900` | National Compensation Services (NCS) | Services nationaux de rémunération (SNR) |
| `SRV02901` | Substance Use and Addictions Program | Programme sur l’usage et des dépendances aux substances |
| `SRV02902` | Respond to requests for information and complaints of Cannabis promotion prohibitions | Répondre aux demandes d&#39;information et aux plaintes relatives aux interdictions de promotion du cannabis |
| `SRV02903` | Screening and Triage-Personal Registration | Examen et triage – Demandes d’inscription personnelle |
| `SRV02904` | Media Enquiries | Demandes des médias |
| `SRV02907` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `SRV02908` | Correspondence Referrals to other Departments (dep&#39;t email, contact us page) | Correspondance Renvois vers d&#39;autres départements (courriel du département, page Contactez-nous) |
| `SRV02909` | Departmental Correspondence (not including referrals) | Correspondance ministérielle (à l&#39;exclusion des renvois) |
| `SRV02910` | Public Enquiries (not referrals) | Demandes de renseignements du public (pas de renvois) |
| `SRV02911` | Ministerial Correspondence (SPB) | Correspondance ministérielle (DGPS) |
| `SRV02912` | Canadian Hazards Information Service (Untargeted) | Service canadien d&#39;information sur les risques (non ciblé) |
| `SRV02913` | GeoConnections Program | Programme GéoConnexions |
| `SRV02914` | Canada Greener Homes Initiative | Initiative canadienne pour des maisons plus vertes |
| `SRV02915` | Youth Employment and Skills Strategy - S &amp; T Internship Program - Green Jobs | Stratégie emploi et compétences jeunesse - le Programme de stages en sciences et technologie - emplois verts |
| `SRV02916` | Departmental Security Management System (DSMS) - Service name updated to :Security Screening Management System (SSMS) | Systeme de gestion du filtrage de sécurité (SGFS) |
| `SRV02917` | Open Science and Data Platform | Plateforme de science et de données ouvertes |
| `SRV02918` | Emissions Reduction Fund Offshore Deployment Program | Programme de déploiement extracôtier du fonds de réduction des émissions |
| `SRV02919` | Smart Grid Deployment Program | Programme de déploiement de réseaux intelligents |
| `SRV02920` | Emerging Renewable Power Program | Programme des énergies renouvelables émergentes |
| `SRV02921` | Smart Renewables and Electrification Pathways Program - Deployment | Programme des énergies renouvelables intelligentes et de trajectoires d’électrification - Déploiement |
| `SRV02922` | Strategic Interties Predevelopment Program | Programme de prédéveloppement des interconnexions stratégiques |
| `SRV02923` | Smart Renewables and Electrification Pathways Program - Capacity Building and Indigenous Engagement Grants | Programme des énergies renouvelables intelligentes et de trajectoires d’électrification - Renforcement des capacités et Subventions pour l’engagement des Autochtones |
| `SRV02924` | Nature Conservation | Conservation de la nature |
| `SRV02925` | Wildfire Emergency Response | Intervention d&#39;urgence en cas d&#39;incendie de forêt |
| `SRV02926` | Large Value Transfer Payment | Paiement de transfert de grande valeur |
| `SRV02927` | Results of the Survey of Private Sector Economic Forecasters | Résultats de l&#39;enquête auprès des prévisionnistes économiques du secteur privé |
| `SRV02928` | Law Enforcement | Forces de l&#39;ordre |
| `SRV02930` | Publication of key economic documents | Publication de documents économiques clés |
| `SRV02932` | CCOHS E-Learning | Apprentissage en ligne du CCHST |
| `SRV02933` | Value-Added Services Provided at Places Administered by Parks Canada | Services à valeur ajoutée offerts dans les lieux administrés par Parcs Canada |
| `SRV02934` | Visitor Safety and Search and Rescue | Sécurité des visiteurs et recherche et sauvetage |
| `SRV02935` | Water and Wastewater Treatment | Traitement de l’eau et des eaux usées |
| `SRV02936` | Clean Growth Hub | Carrefour de la croissance propre |
| `SRV02937` | Emergency geomatics and satellite mapping service | Service de géomatique d&#39;urgence et de cartographie par satellite |
| `SRV02938` | Satellite Ground Stations | Stations-relais pour satellites |
| `SRV02939` | Canada Map Office | Bureau des cartes du Canada |
| `SRV02940` | Clean Energy for Rural and Remote Communities Program - Capacity Building | Programme d&#39;énergie propre pour les collectivités rurales et éloignées - Renforcement des capacités |
| `SRV02941` | Radiological Risk Assessments | Évaluation des risques radiologiques |
| `SRV02942` | Human Monitoring and Assessment | Surveillance et évaluation humaines |
| `SRV02943` | National Calibration Reference Centre Performance Testing Program | Centre national de référenceProgramme de test de performance |
| `SRV02944` | National Radon Program | Programme national sur le radon |
| `SRV02945` | Provide Confidential Business Information Access in Emergencies | Fournir un accès confidentiel aux informations commerciales en cas d&#39;urgence |
| `SRV02946` | Chemical Emergency Response | Intervention d&#39;urgence chimique |
| `SRV02947` | Health Surveillance and Monitoring: Incident Reporting | Surveillance et contrôle de la santé: rapports d&#39;incidents |
| `SRV02948` | Nuclear Emergency Response | Réponse aux urgences nucléaires |
| `SRV02949` | Compliance and Enforcement: Risk Management of Urgent and Serious Events | La conformité et de l’application de la loi: La gestion des risques urgente et serieux |
| `SRV02950` | Congratulatory certificates from the Prime Minister | Certificats de félicitations du premier ministre |
| `SRV02951` | Requests for certified copies of Orders in Council | Demandes de copies certifiées de décrets |
| `SRV02952` | Emergency Air Quality Guidance | Conseils sur la qualité de l&#39;air en cas d&#39;urgence |
| `SRV02953` | Emergency Drinking Water Guidance | Conseils sur l&#39;eau potable en cas d&#39;urgence |
| `SRV02954` | OSFI External Website | Site web du BSIF |
| `SRV02955` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `SRV02956` | Major Rehabilitation Works on Victoria Bridge | Travaux de réhabilitation du pont Victoria |
| `SRV02957` | Contributions to Ensure Air Services to Remote Communities | Contributions visant à assurer le service de transport aérien aux collectivités éloignées |
| `SRV02958` | Airport Critical Infrastructure Program | Programme des infrastructures essentielles des aéroports |
| `SRV02959` | Airport Relief Fund | Fonds de soutien aux aéroports |
| `SRV02960` | Commissioners Office | Bureau du commissaire |
| `SRV02967` | Communication Services | Services de communication |
| `SRV02968` | Executive Services and Ministerial Liaison | Services exécutifs et liaison ministérielle |
| `SRV02969` | RCMP- Criminal Intelligence Service Canada (CISC) | (GRC) Service canadien de renseignements criminels (SCRC) |
| `SRV02970` | Real Property Management | Gestion des biens immobiliers |
| `SRV02972` | Operational Readiness and Response | Préparation et réponse opérationnelles |
| `SRV02973` | National Criminal Operations (NCROPS) | Opérations criminelles nationales (SNPC) |
| `SRV02974` | Operational Communication Centers (OCC) | Stations de transmissions opérationnelles (STO) |
| `SRV02975` | Strategic Policing Agreements and Service | Accords de services de police stratégiques et Service |
| `SRV02976` | Operational Systems Service Centre (OSSC) : | Centre de service des systèmes de la police opérationnels (CSSPO) |
| `SRV02977` | RCMP- National Crime Prevention and Indigenous Policing Services | (GRC) Services nationaux de prévention du crime et de police autochtone |
| `SRV02978` | Federal Policing Criminal Operations (FPCO) | Opérations Criminelles de la Police Fédérale (OCPF) |
| `SRV02979` | National Security | Sécurité nationale |
| `SRV02980` | RCMP- National Critical Infrastructure Team | (GRC) Équipe nationale des infrastructures essentielles |
| `SRV02981` | Canadian Air Carrier Protective Program | Programme de protection des transporteurs aériens canadiens |
| `SRV02982` | Protective Policing | Police de protection |
| `SRV02983` | RCMP- Witness Protection | (GRC) Protection des témoins |
| `SRV02984` | Project Seahorse | Projet Seahorse |
| `SRV02985` | National Intelligence | Renseignement national |
| `SRV02987` | Interpol/Europol | Interpol/Europol |
| `SRV02988` | Passport Selection | Sélection de passeports |
| `SRV02990` | Operational Information Management | Gestion de l&#39;information opérationnelle |
| `SRV02991` | International Operations and, Policing Development | Opérations internationales et développement des services de police |
| `SRV02992` | International Liaison and Coordination Centre | Centre de coordination et de liaison internationale |
| `SRV02993` | International Deployment Services | Services de déploiement international |
| `SRV02994` | International Health, Protection and Wellness | Santé, protection et bien-être international |
| `SRV02997` | RCMP- Canadian Police Information Center | (GRC) Centre d&#39;information de la police canadienne |
| `SRV02998` | RCMP- Canadian Criminal Real Time Identification Services | (GRC) Services canadiens d&#39;identification criminelle en temps réel |
| `SRV02999` | RCMP- Science and Strategic Partnerships | (GRC) Partenariats scientifiques et stratégiques |
| `SRV03000` | Air Services | Services aériens |
| `SRV03001` | Specialized Technical Investigative Services | Services d&#39;enquêtes techniques spécialisées |
| `SRV03002` | Protective Technical Services | Services techniques de protection |
| `SRV03003` | Chemical, Biological, Radiological, Nuclear and Explosives | Chimique, biologique, radiologique, nucléaire et explosifs |
| `SRV03004` | Behavioural Sciences Investigative Services (BSIS) | Services d&#39;enquêtes en sciences du comportement (SESC) |
| `SRV03005` | National Centre for Missing Persons and Unidentified Remains (NCMPUR) | Centre national pour les personnes disparues et les restes non identifiés (CNPDRN) |
| `SRV03006` | National Child Exploitation Crime Centre (NCECC) | Centre national contre l&#39;exploitation des enfants (CNCEE) |
| `SRV03007` | Truth Verification Section (TVS) | Section des contrôles de sincérité (SCS) |
| `SRV03008` | National Radio Services (NRS) | Programme de services radio nationaux (SRN) |
| `SRV03009` | Operations and Platform Support | Soutien des opérations et des plateformes |
| `SRV03010` | Digital Systems and Solutions Delivery | Soutien aux forces de l&#39;ordre des systèmes, applications et services critiques |
| `SRV03012` | Corporate Staffing - Member | Dotation ministérielle - Membre |
| `SRV03014` | Cadet Training Services | Services de formation des cadets |
| `SRV03015` | Legal Services | Services juridiques |
| `SRV03016` | Liaison with national and international enforcement partners | Liaison avec les partenaires nationaux et internationaux chargés de l&#39;application de la loi |
| `SRV03017` | Exemptions from the Controlled Drugs and Substances Act in reponse to emergencies (CSCB) | Exemptions pour l&#39;utilisation de substances contrôlées en réponse à des urgences (DGSCC) |
| `SRV03018` | Issuance of No Objection Letters for imports | Délivrance de lettres de non-objection pour les importations |
| `SRV03019` | Issuance of Designated Device Registrations under the Controlled Drugs and Substances Act | Délivrance de l&#39;enregistrement d&#39;un instruments désignés |
| `SRV03044` | Federal Economic Immigration- Permanent Residence | Immigration économique fédérale- Résidence permanente |
| `SRV03045` | Regional Economic Immigration- Permanent Residence | Immigration économique régionale- Résidence permanente |
| `SRV03046` | Family Reunification- Permanent Residence | Regroupement familial- Résidence permanente |
| `SRV03047` | Humanitarian/Compassionate and Discretionary Immigration- Permanent Residence | Immigration pour considérations d’ordre humanitaire et discrétionnaire- Résidence permanente |
| `SRV03048` | Grant of Citizenship | Attribution de citoyenneté |
| `SRV03049` | Passports &amp; Travel Documents | Délivrance de passeports et de titres de voyage |
| `SRV03050` | Passport Administrative Services | Services administratifs des passeports |
| `SRV03051` | Work Permit | Permis de travail |
| `SRV03054` | African Swine Fever Industry Preparedness Program: Prevention and Preparedness Stream | Programme de préparation de l’industrie à la peste porcine africaine : Volet Prévention et préparation |
| `SRV03055` | African Swine Fever Industry Preparedness Program: Welfare Slaughter and Disposal Stream | Programme de préparation de l’industrie à la peste porcine africaine : Volet Abattage par compassion et élimination |
| `SRV03056` | AgriCommunication | Programme Agri-communication |
| `SRV03057` | Agricultural Clean Technology:Research and Innovation Stream | Programme des technologies propres en agriculture : Volet Recherche et innovation |
| `SRV03058` | Wine Sector Support Program | Programme d&#39;aide au secteur du vin |
| `SRV03060` | The Victim Liaison Officer | L&#39;agent de liaison de la victime |
| `SRV03061` | Sexual Misconduct Support and Resource Center&#39;s Community Support for Sexual Misconduct Survivors Grant Program | Le programme de subventions pour le soutien communitaire pour les personnes surviantes d&#39;inconduite sexuelle du Centre de soutien et de resources sur l&#39;inconduite sexuelle |
| `SRV03062` | Veterans Ombud Intervention Services | Services d’intervention de l’ombud des vétérans |
| `SRV03063` | Clothing Allowance | Allocation vestimentaire |
| `SRV03064` | eServiceCanada | eServiceCanada |
| `SRV03065` | Outreach Support Centre | Centre d’appui des services mobiles |
| `SRV03066` | Dispute resolution on Canadian business operations abroad | Résolution des litiges concernant les activités des entreprises canadiennes à l&#39;étranger |
| `SRV03069` | Canada Community Building Fund (CCBF) | Le Fonds pour le développement des collectivités du Canada (FDCC) |
| `SRV03070` | Accreditation of foreign representatives services | Services d&#39;accréditation des représentants étrangers |
| `SRV03072` | Advice to Canadian garment, mining and oil &amp; gas companies operating outside Canada | Conseils aux entreprises canadiennes du secteur de l&#39;habillement, de l&#39;exploitation minière et du pétrole et du gaz opérant à l&#39;étran |
| `SRV03084` | Digital Marketing Platform for EduCanada (DMPE) | Plateform de Marketing Digital pour EduCanada |
| `SRV03085` | Diplomatic Security Liaison Services | Services de liaison pour la protection des diplomates |
| `SRV03089` | Enabling the coordination of activities related Trade mission/events/initiatives | Permettre la coordination des activités liées aux missions/événements/initiatives commerciales |
| `SRV03091` | Enterprise Systems Support | Soutien des système d&#39;entreprise |
| `SRV03093` | Foreign Heads of Mission Agrément and Ceremonies | Services d’agrément et des cérémonies pour les chefs de mission étrangers |
| `SRV03094` | Foreign military attachés and honorary consuls approvals services | Services d&#39;approbation des attachés militaires et des consuls honoraires |
| `SRV03095` | Geographic Reporting | Rapports géographiques |
| `SRV03097` | Grants and Contributions - CanExport Associations | Subventions et contributions - CanExport Associations |
| `SRV03098` | Grants and Contributions - CanExport Innovation | Subventions et contributions - CanExport Innovation |
| `SRV03099` | Grants and Contributions - CanExport SMEs | Subventions et contributions - CanExport PME |
| `SRV03100` | Heads of Mission Outreach Services | Services de rayonnement pour les chefs de mission |
| `SRV03111` | IRCC Liaison Services | Services de liaision d&#39;IRCC |
| `SRV03126` | Mission Readiness &amp; Security Operations | Préparation des Missions et Opérations de Sécurité |
| `SRV03133` | Privileges and Immunities services | Services des privilèges et immunités |
| `SRV03143` | Trade Commissioner Service | Service des délégués commerciaux |
| `SRV03144` | Strategic communications | Communications stratégiques |
| `SRV03145` | Canada&#39;s Toll-Free Number for Poison Centre Service (1-844-POISON-X) | Numéro sans frais du Canada pour le service des centres antipoison (1-844-POISON-X) |
| `SRV03146` | Cannabis Laboratory (CL) - Forensic analysis services | Laboratoire Cannabis (LC) - Services d&#39;analyse judiciaire |
| `SRV03147` | Retransformation Authorization | Autorisation de retransformation |
| `SRV03148` | Vitis hot water treatment Program | Programme de traitement à l&#39;eau chaude pour Vitis |
| `SRV03149` | Spongy Moth Program | Programme de la spongieuse nord-américaine |
| `SRV03151` | Advice on Women Peace and Security | Conseils sur les femmes, la paix et la sécurité |
| `SRV03153` | LDD Forest Products - Receiving Regulated Product | Produits forestiers LDD - Réception de produits réglementés |
| `SRV03154` | License for Removal of Animals or Things Under the authority of The Health of Animals Act | Permis pour l&#39;enlèvement d&#39;animaux ou de choses en vertu de la Loi sur la santé des animaux |
| `SRV03155` | Anti-Crime and Counter-Terrorism Capacity Building Programs (AC/CTCBP) | Programme d’aide au renforcement des capacités en matière de lute contre la criminalité et le terrorism |
| `SRV03156` | Application for a certificate - Mistaken identity | Demande d&#39;attestation - erreur d&#39;identité |
| `SRV03157` | Application for Review of Seizure Order | Demande d&#39;examination de décret concernant la saisie de biens situés au Canada |
| `SRV03158` | Application to no longer be a designated person | Demande de radiation |
| `SRV03159` | Shipborne Dunnage Program | Programme du bois de calage transporté par les navires |
| `SRV03160` | Avian Influenza Movement - General Permit | Mouvement de la grippe aviaire – Permis général |
| `SRV03161` | Peat Export Program | Programme d&#39;exportation de tourbe |
| `SRV03162` | Compliance Letter (Animal Pathogen Laboratories) | Lettre de conformité (Laboratoires d&#39;agents pathogènes animaux) |
| `SRV03164` | Baseline Threat Assessments (BTAs) | L’évaluation de base des menaces(EBM) |
| `SRV03168` | Cancellation and revocation of passports and refusal of passport services | Annulation et révocation de passeports et refus de services de passeport |
| `SRV03170` | Research Security Centre | Centre de la sécurité de la recherche |
| `SRV03171` | Canada Arts Presentation Fund - Presenter Support Organizations | Fonds du Canada pour la présentation des arts - Organismes d&#39;appui à la diffusion |
| `SRV03172` | Canada Arts Presentation Fund - Development | Fonds du Canada pour la présentation des arts - Soutien au développement |
| `SRV03173` | Bilateral agreements and joint working groups | Ententes bilatérales et groupes de travail |
| `SRV03175` | Canada Book Fund - Support for Publishers- Publishing Support | Fonds du livre du Canada - Soutien aux éditeurs - Soutien à l’édition |
| `SRV03176` | Canadian International Innovation Program (CIIP) | Le programme canadien de l&#39; innovation à l&#39;internationale (PCII) |
| `SRV03177` | Development of Emergency Economic Stimulus Packages | Élaboration de plans de relance économique d’urgence |
| `SRV03178` | Canadian Police Arrangement and Civilian Deployment Platform | l’Arrangement sur la police civile canadienne (APCC)/la Plateforme de déploiements de ressources civiles |
| `SRV03179` | Canada Book Fund - Support for Organizations | Fonds du livre du Canada - Soutien aux organismes |
| `SRV03181` | Cyber Defence Services | Services de cyberdéfense |
| `SRV03182` | Certificates under the United Nations Act | Certification en vertu de la Loi sur les Nations Unies |
| `SRV03183` | Canada Book Fund - Support for Booksellers | Fonds du livre du Canada - Soutien aux librairies |
| `SRV03184` | Canada Cultural Investment Fund - Endowment Incentives | Fonds du Canada pour l&#39;investissement en culture - Incitatifs aux fonds de dotation |
| `SRV03185` | Canada Cultural Investment Fund - Limited Support to Endangered Arts Organizations | Fonds du Canada pour l&#39;investissement en culture - Appui limité aux organismes artistiques en situation précaire |
| `SRV03186` | Federal Cyber Incident Response Plan (FCIRP) | Plan fédéral de réponse aux cyberincidents (PFRC) |
| `SRV03187` | Digital Citizen Contribution Program - Digital Citizen Initiative | Programme de contributions en matière de citoyenneté numérique - Initiative de citoyenneté |
| `SRV03188` | ATSSC Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `SRV03189` | Canada Periodical Fund - Aid to publishers- Digital Periodical | Fonds du Canada pour les périodiques - Aide aux éditeurs - Périodique numérique |
| `SRV03190` | Canada Periodical Fund - Aid to publishers - Community Newspaper | Fonds du Canada pour les périodiques - Aide aux éditeurs - Journal communautaire |
| `SRV03191` | Canada Periodical Fund- Business Innovation - Magazines | Fonds du Canada pour les périodiques - Innovation commerciale - Magazines |
| `SRV03192` | Canada Periodical Fund - Business Innovation - Community Newspapers | Fonds du Canada pour les périodiques - Innovation commerciale - Journaux communautaires |
| `SRV03193` | Administration of the Explosives Act and Explosives Regulations, 2013 | Administration de la loi sur les explosifs et du règlement sur les explosifs de 2013 |
| `SRV03194` | Canada Periodical Fund - Collective Initiatives | Fonds du Canada pour les périodiques - Initiatives collectives |
| `SRV03195` | GC Accommodation Booking system | Système de réservation de GC locaux |
| `SRV03196` | Weapons Threat Reduction Program (WTRP) | Programme de réduction de la menace liée aux armes |
| `SRV03197` | Vetting | Vérification |
| `SRV03199` | Venture Capital Attraction | Attraction du capital de risque |
| `SRV03200` | Chemical Weapons Convention Implementation Act (CWCIA) administration | Gestion de la loi sur la mise en oeuvre de la Convention sur les armes chimiques |
| `SRV03203` | FSD Claim and entitlement administration | Administration des réclamations et des droits liés aux DSE |
| `SRV03204` | Training: Governance, Access, Technical Security and Espionage (GATE) | Formation : Gouvernance, accès, sécurité technique et espionnage (GATE) |
| `SRV03207` | Canada Periodical Fund - Special Measures for Journalism | Fonds du Canada pour les périodiques - Mesures spéciales pour appuyer le journalisme |
| `SRV03209` | Celebration and Commemoration - Commemorate Canada | Célébrations et commémorations - Commémoration Canada |
| `SRV03212` | Support for Hosting - International Multisport Games for Aboriginal Peoples and Persons with a Disability | Soutien pour l&#39;acceuil - Jeux internationaux multisports pour les Autochtones et les personnes ayant un handicap |
| `SRV03214` | Support for Hosting - International Single Sport Events | Soutien pour l&#39;acceuil - Manifestations internationales unisport |
| `SRV03215` | Zero Emission Vehicles Infrastructure Program (ZEVIP) | Programme d’infrastructure pour les véhicules à émission zéro (PIVEZ) |
| `SRV03216` | International Major Multisport Games | Grands Jeux internationaux multisports |
| `SRV03219` | Support the TCS clients (external) and the TCS Network (internal) with the Canadian Technology Accelerator applications (external) and assessments (internal) | Accélérateurs technologiques canadiens - support aux clients du SDC (externe) et au réseau interne |
| `SRV03220` | Zero Emission Vehicle Awareness Initiative (ZEVAI) | Initiative de sensibilisation aux véhicules à émission zéro (ISVEZ) |
| `SRV03221` | Fuel Consumption Guide (FCG) | Guide de consommation de carburant |
| `SRV03222` | Green Freight Program (GFP) | Programme de transport écoénergétique de marchandises |
| `SRV03223` | Electric Charging and Alternative Fuel Station Locator | Localisateur de stations de recharge et de stations de ravitaillement en carburants de remplacement |
| `SRV03224` | Critical Infrastructure and Manufacturing Plan (CIMP): Reporting on manufacturing sector impacts from critical infrastructure disruptions | Plan relatif aux infrastructures critiques et à l&#39;industrie manufacturière (ICIM) : Rapport sur l&#39;impact des perturbations des infrastructures critiques dans le secteur manufacturier |
| `SRV03225` | Spectrum Auction | Enchères du spectre |
| `SRV03226` | Satellite Operations | Opérations par satellite |
| `SRV03227` | International Radio Frequency Coordination | Coordination internationale des radiofréquences |
| `SRV03228` | Information and Communications Technology Critical Infrastructure Resilience – Cyber Security | Résilience des infrastructures essentielles des technologies de l’information et des communications – Cybersécurité |
| `SRV03229` | EcoDriving | Cours d’écoConduite en ligne gratuit |
| `SRV03230` | Emergency Telecommunications | Télécommunications d’urgence |
| `SRV03231` | EnerGuide for Vehicles | ÉnerGuide pour les véhicules |
| `SRV03232` | Remediation of Terrestrial Interference | Réparation du brouillage des stations terrestres |
| `SRV03233` | Auto$mart driver training | Programme de formation des conducteurs Le bon $ens au volant |
| `SRV03235` | Affixing the Great Seal of Canada on formal documents | Apposition du Grand Sceau du Canada sur les documents officiels |
| `SRV03236` | Fuel-efficient driving techniques | Techniques de conduite écoénergétique |
| `SRV03237` | Strategic direction/support/training relating to FDI | Orientation stratégique/contribution/formation aux activités d’attraction et d’IDE |
| `SRV03238` | Weights and Measures Inspection | Services d&#39;inspection poids et mesures |
| `SRV03239` | Sport Support - National Multisport Services Organization | Soutien au sport - Organismes nationaux de services multisports |
| `SRV03240` | Speechwriting | Rédaction de discours |
| `SRV03242` | SmartDriver | Conducteur averti |
| `SRV03243` | Weights and Measures Approvals | L&#39;approbation des appareils de pesage et de mesure |
| `SRV03244` | Sport Support - Canadian Sport Centre | Soutien au sport - Centre canadien multisport |
| `SRV03246` | Sport Support - Sport for Social Development in Indigenous Communities | Soutien au sport - Sport au service du développement social dans les communautés autochtones |
| `SRV03248` | Electricity and Natural Gas Meter Inspection | Inspections de compteurs d&#39;électricité et de gaz naturel |
| `SRV03250` | Research Security | Sécurité de la recherche |
| `SRV03251` | Clean Fuels Fund (CFF) | Fonds pour les combustibles propres |
| `SRV03253` | Remote Sensing Space Systems Act (RSSSA) administration, including licensing and regulatory activities | Administration de la Loi sur les systèmes de télédétection spatiaux (LSTS), y compris les activités de licence et de réglementation |
| `SRV03254` | Regulatory Affairs and Litigation Support | Affaires réglementaires et d&#39;appui au litige |
| `SRV03255` | Building Communities through Arts and Heritage - Community Anniversaries | Développement des communautés par le biais des arts et du patrimoine - Commémorations communautaires |
| `SRV03256` | Providing statistical analysis and reports (CFO-Stats) | Fournir de l&#39;analyse et des rapports statistiques (DPF-Stats) |
| `SRV03257` | Building Communities through Arts and Heritage - Legacy Fund | Développement des communautés par le biais des arts et du patrimoine - Fonds des legs |
| `SRV03258` | Grants and Contribution Programs | Programmes de subentions et contributions |
| `SRV03259` | Public Enquiries | Enquêtes publiques |
| `SRV03261` | Authorized Service Provider Recognized Technician Training | Formation des fournisseur services autorisés techniciens reconnus |
| `SRV03263` | Promoting and Protecting Democracy Fund (Pro-Dem) and the Inclusion, Diversity and Human Rights Fund (IDHR) | Fonds pour la promotion et la protection de la démocratie (Pro-Dem) et Fonds pour l&#39;inclusion, la diversité et les droits de la personne (IDHR) |
| `SRV03264` | Electricity and Natural Gas Approvals | Approbation de compteurs d&#39;électricité et de gaz naturel |
| `SRV03267` | Electricity and Natural Gas Measuring Apparatus Accuracy | Précision des appareils de mesure de l&#39;électricité et de gaz naturel |
| `SRV03268` | Coordination of international STI Canadian priorities with SBDA&#39;s | Coordination des priorités internationales en STI avec les ministères et agences fédéraux à vocation scientifique |
| `SRV03270` | FSD Policy compliance and guidance | Conformité et orientation en matière de politique des DSE |
| `SRV03272` | Corporate Governance | Gouvernance |
| `SRV03276` | Permits under the Special Economic Measures Act and the Justice for Victims of Corrupt Foreign Officials Act | Permis en vertu de la Loi sur les mesures économiques spéciales et de la Loi sur la justice pour les victimes de dirigeants étrangers corrompus |
| `SRV03278` | Corporate Performance and Reporting | Rendement et rapports de l&#39;entreprise |
| `SRV03279` | Peace and Stabilization Operations Program | Programme pour la stabilisation et les opérations de paix |
| `SRV03284` | Economic Analysis and Evaluation | Analyse et évaluation économiques |
| `SRV03286` | EduCanada Extranet | Extranet EduCanada |
| `SRV03289` | Indigenous Languages and Cultures - Northern Aboriginal Broadcasting | Langues et cultures autochtones - Radiodiffusion autochtone dans le Nord |
| `SRV03291` | Multiculturalism and Anti-Racism Initiatives - Projects | Multiculturalisme et la lutte contre le racisme - Projets |
| `SRV03296` | Multiculturalism and Anti-Racism Initiatives - Organizational Capacity Building | Multiculturalisme et la lutte contre le racisme - Renforcement des capacités organisationnelles |
| `SRV03297` | Networks support for International STI | Appui aux Réseaux en STI international |
| `SRV03298` | Museums Assistance - Exhibition Circulation Fund | Aide aux musées - Fonds des expositions itinérantes |
| `SRV03301` | Museums Assistance - Indigenous Heritage | Aide aux musées - Patrimoine autochtone |
| `SRV03303` | Ministerial Liaison | Liaison ministerielle |
| `SRV03304` | Museums Assistance - Collections Management | Aide aux musées - Gestion des collections |
| `SRV03305` | Military and Scientific Overflight Clearance request management | Gestion des demandes d&#39;autorisation de survol militaire et scientifique |
| `SRV03306` | Museums Assistance - Canada-France Agreement | Aide aux musées - Accord Canada-France |
| `SRV03307` | Canada Travelling Exhibitions Indemnification | Indemnisation pour les expositions itinérantes au Canada |
| `SRV03308` | Cultural Property Export and Import Act - Movable Cultural Property Grants | Loi sur l’exportation et l’importation de biens culturels - Subventions de biens culturels mobiliers |
| `SRV03309` | Cultural Property Export and Import Act - Designation of institutions and public authorities | Loi sur l’exportation et l’importation de biens culturels - Désignation d’établissements et d’administrations publiques |
| `SRV03311` | Marine Scientific Research (MSR) request management | Gestion des demandes de recherche scientifique marine |
| `SRV03316` | Management of FDI events | Gestion des évènements IDE |
| `SRV03322` | Canadian Conservation Institute and Canadian Heritage Information Network - Scientific Services | Institut canadien de conservation et Réseau canadien d&#39;information sur le patrimoine - Services scientifiques |
| `SRV03323` | Canadian Conservation Institute and Canadian Heritage Information Network - General Information Requests | Institut canadien de conservation et Réseau canadien d&#39;information sur le patrimoine - Demandes d&#39;informations générales |
| `SRV03325` | Canadian Conservation Institute and Canadian Heritage Information Network- In-person and Online Workshops and Webinars | Institut canadien de conservation et Réseau canadien d&#39;information sur le patrimoine - Ateliers et webinaires en personne et en ligne |
| `SRV03327` | Canadian Conservation Institute and Canadian Heritage Information Network - Advanced Professional Development Workshops | Institut canadien de conservation et Réseau canadien d&#39;information sur le patrimoine - Ateliers de développement professionnel avancé |
| `SRV03330` | Development of Official-Language Communities –Community Cultural Action Fund | Développement des communautés de langue officielle - Fonds d’action culturelle communautaire |
| `SRV03332` | Development of Official-Language Communities - Teacher Recruitment and Retention Strategy in Minority French Language Schools | Développement des communautés de langue officielle - Stratégie de recrutement et de rétention d’enseignants pour les écoles de langue française en situation minoritaire |
| `SRV03333` | International Relations and Border Policy | Les relations internationales et la politique frontalière |
| `SRV03334` | Development of Official-Language Communities - Cooperation with the Non-Governmental Sector | Développement des communautés de langue officielle - Collaboration avec le secteur non gouvernemental |
| `SRV03335` | Enabling the coordination of Matchmaking/B2B | Jumelages/B2B |
| `SRV03336` | Enterprise Architecture | Architecture d&#39;Entreprise |
| `SRV03339` | Evaluation Publications | Publications d&#39;évaluation |
| `SRV03343` | Ghost Gear Fund | Fonds pour les engins fantômes |
| `SRV03345` | Development of Official-Language Communities – Community Spaces Fund | Développement des communautés de langue officielle - Fonds pour les espaces communautaires |
| `SRV03349` | International bilateral STI agreements and arrangements | Accords et arrangements bilatéraux de cooperation internationale bilatéraux en STI |
| `SRV03350` | Enhancement of Official Languages - Teacher Recruitment and Retention Strategy in French Immersion and French Second-Language Programs | Mise en valeur des langues officielles - Stratégie de recrutement et de rétention d’enseignants dans les programmes d’immersion et de français langue seconde |
| `SRV03351` | Enhancement of Official Language - Promotion of Bilingual Services | Mise en valeur des langues officielles - Promotion de l’offre de services bilingues |
| `SRV03353` | Enhancement of Official Language - Support for Interpretation and Translation | Mise en valeur des langues officielles - Appui à l’interprétation et à la traduction |
| `SRV03355` | Enhancement of Official Language - Appreciation and Rapprochement | Mise en valeur des langues officielles - Appréciation et rapprochement |
| `SRV03359` | Executive Briefing | La division du breffage de la haute direction |
| `SRV03360` | Federal-Provincial Consultative Committee on Education-related International Activities (FPCCERIA) | Comité consultatif fédéral-provincial sur les activités internationales liées à l&#39;éducation (CCFPAIE) |
| `SRV03365` | Foreign military ship visit request management | Visite de navires militaires étrangers |
| `SRV03368` | Geographic Advice | Conseil géographique |
| `SRV03370` | Global Security Reporting Program (GSRP) | Programme des rapports sur la securité mondiale (PRSM) |
| `SRV03371` | Grants and Contributions - CanExport Community Investments | Subventions et contributions - CanExport investissements des communautés |
| `SRV03374` | Monitoring and Compliance | Surveillance et conformité |
| `SRV03375` | Fighting and Managing Wildfires in a Changing Climate | Combattre et gérer les feux de forêt dans un climat en changement |
| `SRV03376` | Aquatic Invasive Species Prevention Fund | Fonds de prévention des espèces aquatiques envahissantes |
| `SRV03377` | Training And Exercising Participation Contribution Program | Programme de contribution pour la participation aux activités de formation et d&#39;exercice |
| `SRV03378` | Wildland Fire Resilience | Contribution à l&#39;appui de Programme Résilience des feux de forêt |
| `SRV03379` | Residential Schools Legacy | Séquelles des pensionnats |
| `SRV03380` | Aboriginal Entrepreneurship Program - Access to Business Opportunities stream | Programme d&#39;entrepreneuriat autochtone - Accès à des possibilités d&#39;affaires |
| `SRV03381` | Jordan&#39;s Principle: Funding | Principe de Jordan: financement |
| `SRV03382` | Inuit Child First Initiative: Direct Service Delivery | L&#39;Initiative : Les enfants inuits d&#39;abord : Prestation directe de services |
| `SRV03383` | Inuit Child First Initiative: Funding | L&#39;Initiative : Les enfants inuits d&#39;abord : financement |
| `SRV03384` | Contribution Agreement Funding related to Article 24 of the Nunavut Agreement | Financement de l&#39;accord de contribution lié à l&#39;article 24 de l&#39;Accord du Nunavut |
| `SRV03385` | New Frontiers in Research Fund | Fonds Nouvelles frontières en recherche |
| `SRV03386` | Coastal Environmental Baseline Contribution Program | Programme de contribution environnementale côtière de référence |
| `SRV03387` | Indigenous Community-Boat Volunteer Contribution Program | Programme de contribution des bénévoles des communautés autochtones sur les bateaux |
| `SRV03388` | Certification for Canadian exporters of aquatic products under the Convention on International Trade in Endangered Species of Wild Fauna and Flora (CITES) | Certification pour les exportateurs canadiens d&#39;espèces aquatiques assujettis à la Convention sur le commerce international des espèces de faune et de flore sauvages menacées d&#39;extinction (CITES) |
| `SRV03389` | National Emergency Management Governance | Gouvernance de la gestion des urgences nationales |
| `SRV03390` | Alerts and Advisories | Alertes et Avis |
| `SRV03391` | Immigration Detentions | Détention d&#39;immigrants |
| `SRV03392` | Critical Construction Project Assurance | Assurance des Projets de Construction Critiques |
| `SRV03393` | Immigration Hearings Representation | Représentation aux audiences d&#39;immigration |
| `SRV03394` | Removal | Renvois |
| `SRV03395` | Immigration Investigations | Enquêtes d&#39;immigration |
| `SRV03396` | Immigration National Security Screening | Filtrage de sécurité nationale de l&#39;immigration |
| `SRV03399` | Criminal Investigations | Enquêtes criminelles |
| `SRV03400` | Waste Diversion of Office Supplies | Réacheminement des déchets de fournitures de bureau |
| `SRV03401` | Community Participation And Co-Development Contribution Program | Fonds de subventions et de contributions pour la participation communautaire et le codéveloppement |
| `SRV03402` | Canadian Coast Guard Auxiliary Contribution Fund | Fonds de contribution de la Garde côtière auxiliaire canadienne |
| `SRV03403` | Collaboration with Priority Critical Infrastructure Owners and Operators | Collaboration avec des propriétaires et exploitants d’infrastructures essentielles prioritaires |
| `SRV03404` | Incident Handling and Support | Intervention et soutien en cas d’incident |
| `SRV03408` | Service Coordination | Coordination des services |
| `SRV03410` | Cyber Threat Surface Analysis | Analyse de l’exposition aux cybermenaces |
| `SRV03411` | Cybersecurity Advice &amp; Guidance - System Security Architecture | Avis et conseils en matière de cybersécurité – Architecture de sécurité du système |
| `SRV03413` | Access to Information and Privacy - Privacy Act | Accès à l’information et protection des renseignements personnels - Loi sur la protection des renseignements personnels |
| `SRV03414` | Access to Information and Privacy - Access to Information Act | Accès à l’information et protection des renseignements personnels - Loi sur l&#39;accès à l&#39;information |
| `SRV03415` | Work Point Booking Tool | Outil de réservation pour postes de travail |
| `SRV03416` | Whale Protection And Recovery Initiative Contribution Program | Programme de contribution de l’Initiative de protection et de rétablissement des baleines |
| `SRV03417` | Commonwealth Blue Charter Champion Contribution Program | Programme de contribution des champions de la Charte bleue du Commonwealth |
| `SRV03418` | Sustainable Fisheries Science Fund Contribution Program (SFSRSP) | Programme de contributions du Fonds des sciences halieutiques durables |
| `SRV03419` | Marine Environmental Quality Regulatory / Non Regulatory Measures Contribution Program | Qualité du milieu marin réglementaire / non réglementaire |
| `SRV03420` | Pacific Integrated Commercial Fisheries Initiative (PICFI) | Initiative des pêches commerciales intégrées du Pacifique (IPCIP) |
| `SRV03421` | Human-Wildlife Coexistence- Incident Response and Safety Management | Coexistence entre l&#39;homme et la faune - Réponse aux incidents et gestion de la sécurité |
| `SRV03422` | Library Services | Services de bibliothèque |
| `SRV03423` | Reducing The Threat Of Vessel Traffic On Marine Mammals Contribution Program | Programme de contribution pour réduire la menace du trafic maritime sur les mammifères marins |
| `SRV03424` | Media and Promotion of Canada&#39;s Natural and Cultural Heritage | Médias et promotion du patrimoine naturel et culturel du Canada |
| `SRV03425` | Environmental Protection Services | Services de protection de l’environnement |
| `SRV03426` | Ocean And Climate Change Science Contribution Program | Programme de contributions pour les sciences des océans et des changements climatiques |
| `SRV03427` | National Contaminants Advisory Group Contribution Program | Programme de contributions du Groupe consultatif national sur les contaminants |
| `SRV03428` | Marine Spatial Planning Contribution Program | Programme de contributions pour la planification spatiale marine |
| `SRV03429` | Core geospatial observation sites in remote locations of Canada (GO Canada) | Sites de base d&#39;observation géospatiale en régions éloignées du Canada (GO Canada) |
| `SRV03430` | Freshwater Habitat Science Contribution Program | Programme de contributions pour les sciences des océans et des eaux douces |
| `SRV03431` | Ontario Waterways and Water Management | Voies navigables et gestion de l&#39;eau en Ontario |
| `SRV03432` | Freshwater Research Contribution Program | Programme de contributions pour la recherche sur l’eau douce |
| `SRV03433` | Ocean And Freshwater Science Contribution Program | Programme de contributions pour la science de l’habitat d’eau douce |
| `SRV03434` | Ground support for space science (THEMIS) | Soutien au sol des sciences spatiales (THEMIS) |
| `SRV03435` | Wildfire Prevention and Risk Mitigation | Prévention des incendies de forêt et atténuation des risques |
| `SRV03436` | National Infrastructure Component (NIC) | Volet Infrastructures nationales (VIN) |
| `SRV03437` | Clean Water and Wastewater Fund (CWWF) | Le Fonds pour l&#39;eau potable et le traitement des eaux usées (FEPTEU) |
| `SRV03438` | Disaster Mitigation and Adaptation Fund | Fonds d&#39;atténuation et d&#39;adaptation en matière de catastrophes |
| `SRV03440` | Investing in Canada Infrastructure Program (ICIP) | Programme d&#39;infrastructure Investir dans le Canada (PIIC) |
| `SRV03441` | Active Transportation Fund (ATF) | Le Fonds pour le transport actif (FTA) |
| `SRV03442` | National and Regional Projects (NRP) | Projets nationaux et régionaux (PNR) |
| `SRV03443` | Public Transit Infrastructure Fund (PTIF) | Le Fonds pour l&#39;infrastructure de transport en commun (FITC) |
| `SRV03444` | Rural Transit Solutions Fund (RTSF) | Fonds pour les solutions de transport en commun en milieu rural (FSTCMR) |
| `SRV03445` | Small Communities Fund (SCF) | Fonds des petites collectivités (FPC) |
| `SRV03446` | Zero Emissions Transit Fund (ZETF) | Fonds pour le transport en commun à zéro émission (FTCZE) |
| `SRV03447` | Copyright Services | Services des droits d&#39;auteur |
| `SRV03448` | Frontline Avalanche Safety and Control Service | Service de sécurité et de contrôle des avalanches en première ligne |
| `SRV03449` | Backcountry Avalanche Monitoring and Reporting | Surveillance et Rapport sur les Avalanches en Arrière-Pays |
| `SRV03450` | Canadian Heritage accessibility feedback process | Processus de rétroaction sur l&#39;accessibilité de Patrimoine canadien |
| `SRV03451` | Access to Information and Privacy (ATIP) | Demande d&#39;accès à l&#39;information et de protection des renseignements personnels (AIPRP) |
| `SRV03452` | Reaching Home (RH) | Directives de Vers un chez-soi (DVC) |
| `SRV03453` | Public Service Employee Survey (PSES) | Sondage auprès des fonctionnaires fédéraux (SAFF) |
| `SRV03454` | Cyber Maturity Self-Assessment (CMSA) | Autoévaluation de la cybermaturité (AECM) |
| `SRV03455` | GC Digital Talent | Talents numériques du GC |
| `SRV03456` | Tracker | Suivi |
| `SRV03457` | Grants and Contribution Programs | Programmes de subventions et de contributions |
| `SRV03458` | Web Inquiries | Demandes de renseignements sur le Web |
| `SRV03459` | Policy, Advocacy, and Coordination | Politique, représentation et coordination |
| `SRV03461` | Ministerial exemption under subsection 5.9(2) of the Aeronautics Act | Exemption ministérielle en vertu du paragraphe 5.9(2) de la Loi sur l&#39;aéronautique |
| `SRV03462` | Statement of aerobatic competency | Énoncé de compétence en voltige aérienne |
| `SRV03463` | Aviation Exams | Examens aéronautiques |
| `SRV03464` | Ministerial authorization under Part VII, other than under section 701.10 | Autorisation ministérielle en vertu de la partie VII, autre qu&#39;en vertu de l&#39;article 701.10 |
| `SRV03465` | Aircraft Parking | Stationnement des aéronefs |
| `SRV03466` | Vehicle Parking | Stationnement des véhicules |
| `SRV03467` | General Terminal: Domestic and International | Accès à l&#39;aérogare : Vols intérieurs et internationaux |
| `SRV03468` | Aircraft Landing and Flying Training | Formation à l&#39;atterrissage et au vol d&#39;avions |
| `SRV03469` | Emergency Response Services | Services d&#39;intervention d&#39;urgence |
| `SRV03470` | Annual Mobile Equipment Registration | L&#39;enregistrement annuelle d&#39;équipement mobile |
| `SRV03471` | Coasting Trade inspections : Letters of Compliance Issued | Inspections des métiers du cabotage : Lettres de conformité émises |
| `SRV03472` | Air cargo screening equipment certification | Certification des équipements de contrôle du fret aérien |
| `SRV03473` | Inspection on a domestic vessel | Inspection à bord d’un bâtiment canadien |
| `SRV03475` | Ministerial and Deputy Correspondence | Correspondance ministérielle et du sous-ministre |
| `SRV03476` | Education and awareness on rail and intermodal transportation security | Éducation et sensibilisation à la sûreté du transport ferroviaire et intermodal |
| `SRV03477` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `SRV03478` | Safe Manning Document Review | Examen du Document d&#39;effectifs de sécurité |
| `SRV03479` | Vessel Plan Document Review | Examen des documents du plan du bâtiment |
| `SRV03480` | Licensing for aviation personnel | Licences pour le personnel en aviation |
| `SRV03481` | Seafarer examination and/or assessment of qualification | Examen et/ou évaluation des qualifications des gens de mer |
| `SRV03482` | Certification for a seafarer | Certification des gens de mer |
| `SRV03483` | Search for Sea Service | Recherche de service en mer |
| `SRV03484` | Identity document for a seafarer | Document d&#39;identité pour un marin |
| `SRV03485` | Register a vessel | Immatriculer un bâtiment |
| `SRV03486` | Transfer of Vessel Ownership | Transfert de propriété d&#39;un navire |
| `SRV03487` | Register a mortgage for a vessel | Enregistrer une hypothèque sur un bâtiment |
| `SRV03488` | Vessel History | Historique du bâtiment |
| `SRV03489` | Replacement of a Canadian aviation document | Remplacement d&#39;un document d&#39;aviation canadien |
| `SRV03490` | Access Public Ports Facilities | Accès aux Installations des Ports Publics |
| `SRV03491` | Issuance, in response to a request by industry, of an evaluation or authorization of industry training products. | Délivrance, à la suite d’une demande de l’industrie, d’une évaluation ou d’une autorisation concernant des produits de formation de l’industrie. |
| `SRV03492` | Marine Insurance Certificate for a Vessel | Certificat d&#39;assurance maritime pour un bâtiment |
| `SRV03493` | Vessel Operations Restriction Regulation (VORR) Permit | Règlement sur les restrictions visant l’utilisation des bâtiments (RRVUB) permis |
| `SRV03494` | Cargo Inspection | Inspection des cargaisons |
| `SRV03495` | Dangerous Goods inspection | Inspection des marchandises dangereuses |
| `SRV03496` | Canadian Flagged Vessels (SOLAS &amp; Domestic Ferries) Security Certification | Certification de sûreté pour les bâtiments battant Pavillon canadien (SOLAS et traversiers intérieurs) |
| `SRV03497` | Verification of outstanding deficiencies for foreign vessels | Vérification des déficiences en suspens pour les navires étrangers |
| `SRV03498` | Type certificate for an aeronautical product | Certificat de type pour un produit aéronautique |
| `SRV03499` | Supplemental type certificate for an aeronautical product | Certificat de type supplémentaire pour un produit aéronautique |
| `SRV03500` | Canadian Technical Standard Order (CAN-TSO) for an appliance or part | Ordonnance sur les normes techniques canadiennes (CAN-TSO) pour un appareil ou une pièce |
| `SRV03501` | Repair design approval for an aeronautical product | Approbation de conception de réparation pour un produit aéronautique |
| `SRV03502` | Licensing for air traffic controllers | Licence pour les contrôleurs aériens |
| `SRV03503` | Part design approval for an aeronautical product | Approbation de conception de pièce pour un produit aéronautique |
| `SRV03504` | Access Importation and Manufacturing protocols and guidance | Accéder aux protocoles et aux conseils d’importation et de fabrication |
| `SRV03505` | Access Connected and Automated Vehicles information | Accéder aux informations sur les véhicules connectés et automatisés |
| `SRV03506` | Air carrier joint venture review and authorization process | Processus d&#39;examen et d&#39;autorisation des coentreprises de transporteurs aériens |
| `SRV03507` | Certificate of registration for a means of containment facility | Certificat d&#39;enregistrement pour une installation de confinement |
| `SRV03508` | Exemption by Order under subsection 24(1) of the Canadian Navigable Waters Act | Exemption par décret en vertu du paragraphe 24(1) de la Loi sur les eaux navigables canadiennes |
| `SRV03509` | Pleasure Craft Licence | Délivrance des permis d&#39;embarcations de plaisance |
| `SRV03510` | Railway Operating Certificate | Certificat d&#39;exploitation ferroviaire |
| `SRV03511` | Transportation Security Clearance | Autorisation de sécurité des transports |
| `SRV03512` | Licensing for aircraft maintenance engineers | Licences pour les ingénieurs en maintenance d&#39;aéronefs |
| `SRV03513` | Canadian Airline Designations and Airline Capacity Allocation | Désignations des compagnies aériennes canadiennes |
| `SRV03514` | Education and Awareness | Éducation et sensibilisation |
| `SRV03515` | Equivalency and Temporary Certificates | Certificats d’équivalence et certificats temporaires |
| `SRV03516` | General Inquiries related to the TDG Program, including means of containment, regulations and legislation | Demandes de renseignements généraux concernant le programme du TMD, y compris les contenants, les règlements et les lois. |
| `SRV03517` | Reservation of an aircraft registration mark | Réservation d&#39;une marque d&#39;immatriculation d&#39;aéronef |
| `SRV03518` | Approval of Emergency Response Assistance Plans (ERAP) | Approbation des plans d’intervention d’urgence (PIU) |
| `SRV03519` | Canadian Transport Emergency Centre (CANUTEC) | Centre canadien d’urgence transport |
| `SRV03520` | Canadian Transport Emergency Centre (CANUTEC) - Publication of the Emergency Response Guidebook (ERG) | Centre canadien d&#39;urgence transport (CANUTEC) - Publication du Guide des interventions d&#39;urgence (ERG) |
| `SRV03521` | CANUTEC Registration system | Service à l&#39;inscription de CANUTEC |
| `SRV03522` | Approval for a marine training program or course provided by a marine training institution | Approbation d&#39;un programme ou d&#39;un cours de formation maritime dispensé par un établissement d&#39;enseignement maritime reconnu |
| `SRV03523` | Maritime Labour Convention Certificates | Certificat de travail maritime. |
| `SRV03524` | Seafarer Recruitment and Placement Service (SRPS) provider licensing | Licence de service de recrutement et de placement des gens de mer (SRPGM) |
| `SRV03525` | TC Situation Centre (SitCen) | Centre d’intervention de Transports Canada (SitCen) |
| `SRV03526` | Marine Medical Certificate | Certificat médical de la marine |
| `SRV03527` | Access National Collision Database (NCDB) | Accéder à la base de données nationale sur les collisions (BNDC) |
| `SRV03528` | Air transportation merger and acquisition review and authorization process | Processus d&#39;examen et d&#39;autorisation des fusions et acquisitions de transport aérien |
| `SRV03529` | Approved training organization certificate | Certificat pour organismes de formation agréés |
| `SRV03530` | Alternative means of compliance (AMOC) with an airworthiness directive | Moyens alternatifs de conformité (AMOC) à une consigne de navigabilité |
| `SRV03531` | Administration of the Marine War Risk Act and the agreement with the Canadian Shipowners Mutual Assurance Association | Administration de la Loi sur les risques de guerre en matière d&#39;assurance maritime et de l&#39;accord avec l&#39;Association pour assurance mutuelle d&#39;armateurs canadiens |
| `SRV03532` | Approval of Air Cargo Security Program Participants | Approbation des participants au Programme de sûreté du fret aérien |
| `SRV03533` | Small Vessel Compliance Program (SVCP) | Programme de conformité des petits bâtiments (PCPB) |
| `SRV03534` | Medical certificates for aviation personnel | Certificats médicaux pour le personnel en aviation |
| `SRV03535` | Marine Security Operations Centres : Pre-Arrival Information Report Screening | Centres des opérations de la sûreté maritime : Contrôle des rapports d&#39;information préalables à l&#39;arrivée |
| `SRV03536` | Ports &amp; Marine Facilities Security Certification | Certification de sûreté des ports et des installations maritimes |
| `SRV03537` | Grants and Contributions | Subventions et contributions |
| `SRV03538` | Access defect and recall information | Accéder aux informations sur les défauts et les rappels |
| `SRV03539` | Access Road Safety standards information | Accéder aux informations sur les normes de sécurité routière |
| `SRV03540` | Access Motor Vehicle Safety Best practices information | Accéder aux informations sur les meilleures pratiques en matière de sécurité des véhicules automobiles |
| `SRV03541` | Approval of ‘works’ under the Canadian Navigable Waters Act | Approbation des « ouvrages » en vertu de la Loi sur les eaux navigables canadiennes |
| `SRV03542` | Dispensation for a seafarer | Dispense pour un gens de mer |
| `SRV03543` | Manufacturer Identification Codes (MIC) | Codes d&#39;identification du fabricant (MIC) |
| `SRV03544` | Declarations of Conformity (DOC) | Déclarations de conformité (DOC) |
| `SRV03545` | Continuous Synopsis Records | Fiche synoptique continue |
| `SRV03546` | Delegated Statutory Inspection Program (DSIP) exemption request applications received | Demandes de dérogation au Programme de Délégation des Inspections Obligatoires (PDIO) reçues |
| `SRV03547` | Marine Technical Review Board Decision | Décision du Comité d&#39;examen technique maritime |
| `SRV03548` | Explosives Detection Dog and Handler Teams (EDDHT) Certification | Certification d&#39;équipe maître et chien entraînée à la détection d’explosifs (EMCEDE) |
| `SRV03549` | Access Driver Assistance Technologies information | Accéder aux informations sur les technologies d&#39;aide à la conduite |
| `SRV03550` | Access School bus safety information | Accès aux informations sur la sécurité des autobus scolaires |
| `SRV03551` | Aircraft registration | Immatriculation d&#39;aéronef |
| `SRV03552` | Flight authority | Autorité de vol |
| `SRV03553` | Certificate of approval for a maintenance or manufacturing organization | Certificat d&#39;approbation pour une organisation de maintenance ou de fabrication |
| `SRV03554` | Approval of an aircraft maintenance schedule | Approbation des calendriers de maintenance d&#39;aéronefs |
| `SRV03555` | Restricted certification authority for an individual | Autorité de certification restreinte pour un particulier |
| `SRV03556` | Inspection of an amateur-built aircraft | Inspection d&#39;un avion de construction amateur |
| `SRV03557` | Prewash Endorsement | Approbation du prélavage |
| `SRV03558` | Verification of Shipper&#39;s procedures | Vérification des procédures de l&#39;Expéditeur |
| `SRV03559` | Rescinding detention of a foreign vessel | Annuler une ordonnance de détention pour un bâtiment étranger |
| `SRV03560` | Report a safety defect | Signaler un défaut de sécurité |
| `SRV03561` | Request a Motor Vehicle Transport Act Exemption | Demander une exemption prévue par la Loi sur les transports routiers |
| `SRV03562` | Authorization to take possession under the Wrecked, Abandoned or Hazardous Vessels Act | Autorisation de prendre possession en vertu de la Loi sur les bâtiments naufragés, abandonnés ou dangereux |
| `SRV03563` | Media enquiries | Demandes médiatiques |
| `SRV03564` | Certification of a flight training unit | Certification d&#39;une unité de formation au pilotage |
| `SRV03565` | Letter of acceptance for foreign maintenance organizations | Lettre d&#39;acceptation pour les organismes de maintenance étrangères |
| `SRV03566` | Aircraft leasing | Location d&#39;aéronefs |
| `SRV03567` | Special flight operations certificate | Certificat d’opérations aériennes spécialisées |
| `SRV03568` | Air operator certificate | Certificat d&#39;exploitant aérien |
| `SRV03569` | Adjudication of Immigration and Refugee cases | Décision des cas d’immigration et de statut de réfugié |




---

#### `service_name_en` – Service Name (English) / Nom du service (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field has a maximum length of 350 characters.
 / Ce champ ne doit pas être vide.
Ce champ a une longueur maximale de 350 caractères.
  


**Description:**  
EN: Identifies the official name of the service.  
FR: Indique le nom officiel du service.


---

#### `service_name_fr` – Service Name (French) / Nom du service (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field has a maximum length of 350 characters.
 / Ce champ ne doit pas être vide.
Ce champ a une longueur maximale de 350 caractères.
  


**Description:**  
EN: Identifies the official name of the service.  
FR: Indique le nom officiel du service.


---

#### `service_description_en` – Service Description (English) / Description du service (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field has a maximum length of 1800 characters.
 / Ce champ ne doit pas être vide.
Ce champ a une longueur maximale de 1800 caractères.
  


**Description:**  
EN: Provides a brief description of the service, in plain language.  
FR: Offre une brève description du service, en langage simple.


---

#### `service_description_fr` – Service Description (French) / Description du service (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field has a maximum length of 1800 characters.
 / Ce champ ne doit pas être vide.
Ce champ a une longueur maximale de 1800 caractères.
  


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
| `CLIENT` | Targeted, Client-based service | Service ciblé axé sur les clients |
| `SOCIETY` | Untargeted, Societal-based service | Service non-ciblé axé sur la société |




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
**Choice Set:** program_id (1231 values)  


**Description:**  
EN: Identifies the unique program code associated with program elements for all strategic outcomes, programs, sub-programs, and sub-sub-programs. The Program codes in the government-wide Chart of Accounts can be used.
Corporate planners in the department/agency who are responsible for the Policy on Results can assist in identifying this, if needed. Multiple values must be separated by a comma (,).
  
FR: Indique le code de programme unique associé aux éléments de programme pour tous les résultats stratégiques, les programmes, les sous-programmes et les sous-sous-programmes. Les codes de programme du Plan comptable à l'échelle de l'administration fédérale peuvent être utilisés.
Les planificateurs ministériels du ministère ou de l'organisme responsables de la Politique sur les résultats peuvent aider à déterminer le code d'identification du programme, au besoin. Séparez les entrées par une virgule (,) s’il y en a plusieurs qui s’appliquent.



##### Allowed Values (program_id)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `AYO00` | Police Operations | Opérations policières |
| `AYR00` | Canadian Law Enforcement Services | Services canadiens d&#39;application de la loi |
| `AYX00` | Civilian review of Royal Canadian Mounted Police members&#39; conduct in the performance of their duties | Examen civil de la conduite des membres de la Gendarmerie royale du Canada dans l&#39;exercice de leurs fonctions |
| `BAA00` | Nuclear laboratories | Laboratoires nucléaires |
| `BAB00` | Nuclear decommissioning and radioactive waste management | Déclassement nucléaire et gestion des déchets radioactifs |
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
| `BEG05` | Judicial Support and Registry Services | Services de soutien judiciaire et services du greffe |
| `BEN00` | Appeal case reviews | Examen d&#39;appels |
| `BEO00` | Canadian Air Transport Security Authority | Administration canadienne de la sûreté du transport aérien |
| `BEZ01` | Copyright Tariff Setting and Issuance of Licences | Établissement de tarifs et délivrance de licences pour l&#39;utilisation des droits d&#39;auteur |
| `BFD00` | Canadian Broadcasting Corporation | Société Radio-Canada |
| `BFJ00` | Canada Council for the Arts | Conseil des Arts du Canada |
| `BFO01` | Maintenance of infrastructure and security | Entretien des infrastructures et sécurité |
| `BFY01` | Educational, cultural and heritage activities | Activités pédagogiques, culturelles et patrimoniales |
| `BFZ01` | Occupational health and safety information and services | Services et renseignements sur la santé et la sécurité au travail |
| `BGA00` | Canadian Dairy Commission | Commission canadienne du lait |
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
| `BGJ00` | Assistance for housing needs | Aide pour combler les besoins en matière de logement |
| `BGK00` | Financing for housing | Financement de l&#39;habitation |
| `BGL00` | Housing expertise and capacity development | Savoir-faire en matière de logement et développement du potentiel |
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
| `BGN04` | Personal Support Worker Retirement Savings Innovation Program | Programme d&#39;innovation pour l&#39;épargne-retraite des préposés aux services de soutien à la personne |
| `BGN05` | Canada Disability Benefit | Prestation canadienne pour les personnes handicapées |
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
| `BGO27` | Community Workforce Development Program/ Canada Retraining and Opportunities Initiative | Programme de développement de la main-d&#39;œuvre des communautés / Initiative canadienne pour le perfectionnement professionnel et les possibilités d&#39;emploi |
| `BGO28` | Canada Worker Lockdown Benefit | Prestation canadienne pour les travailleurs en cas de confinement |
| `BGO29` | Canadian Apprenticeship Strategy | Stratégie canadienne de formation en apprentissage |
| `BGO30` | Pandemic-Related Benefits | Prestations liées à la pandémie |
| `BGO31` | Canadian Benefit for Parents of Young Victims of Crime | Allocation canadienne aux parents de jeunes victimes de crimes |
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
| `BGR04` | Clean Growth and Climate Change Mitigation | Croissance propre et atténuation des changements climatiques |
| `BGR05` | International Environment and Climate Change Engagement | Engagement international sur l&#39;environnement et les changements climatiques |
| `BGR06` | Climate Change Adaptation | Adaptation aux changements climatiques |
| `BGS01` | Air Quality | Qualité de l&#39;air |
| `BGS02` | Water Quality and Ecosystems Partnerships | Qualité de l&#39;eau et partenariat sur les ecosystèmes |
| `BGS03` | Community and Sustainability | Communauté et durabilité |
| `BGS04` | Aquatic Ecosystems Health, Substances and Waste Management | Santé des écosystèmes aquatiques et gestion des substances et des déchets |
| `BGS05` | Compliance Promotion and Enforcement - Pollution | Promotion de la conformité et application de la loi - Pollution |
| `BGS06` | Canada Water Agency Program | Programme de l&#39;Agence canadienne de l&#39;eau |
| `BGS07` | Environmental Pollution Management | Gestion de la pollution environnementale |
| `BGS08` | Pollution Enforcement | Application de la loi en matière de pollution |
| `BGT01` | Species at Risk | Espèces en péril |
| `BGT02` | Migratory Birds and Other Wildlife | Oiseaux migrateurs et autres espèces sauvages |
| `BGT03` | Habitat Conservation and Protection | Conservation et protection des habitats |
| `BGT04` | Biodiversity Policy and Partnerships | Politiques et partenariats sur la biodiversité |
| `BGT05` | Environmental Assessment | Évaluation environnementale |
| `BGT06` | Compliance Promotion and Enforcement - Wildlife | Promotion de la conformité et application de la loi - Faune |
| `BGT07` | Conservation and Species | Conservation et espèces |
| `BGT08` | Conservation and Species Enforcement | Application de la loi en matière de conservation et d&#39;espèces |
| `BGU01` | Weather and Environmental Observations, Forecasts and Warnings | Observations, prévisions et avertissements météorologiques et environnementaux |
| `BGU02` | Hydrological Services | Services hydrologiques |
| `BGU03` | Meteorological Services | Services météorologiques |
| `BGU04` | Hydrological Service | Service hydrologique |
| `BGV01` | Impact Assessment Policy Development | Élaboration de politiques en matière d&#39;évaluation d&#39;impact |
| `BGV02` | Assessment Delivery | Réalisation des évaluations |
| `BGV03` | Assessment Administration, Conduct, and Monitoring | Administration, réalisation et surveillance de l&#39;évaluation |
| `BGV04` | Indigenous Relations and Engagement | Relations avec les Autochtones et participation des Autochtones |
| `BGW01` | Heritage Places Establishment | Création de lieux patrimoniaux |
| `BGW02` | Heritage Places Conservation | Conservation des lieux patrimoniaux |
| `BGW03` | Heritage Places Promotion and Public Support | Promotion des lieux patrimoniaux et soutien du public |
| `BGW04` | Visitor Experience | Expérience du visiteur |
| `BGW05` | Heritage Canals, Highways and Townsites Management | Gestion des canaux patrimoniaux, des routes et des lotissements urbains |
| `BGW06` | Access Routes, Infrastructure, and Community Services | Routes d&#39;accès, infrastructure et services aux communautés |
| `BGW07` | Cultural Heritage | Patrimoine culturel |
| `BGW08` | Emergency and Wildland Fire Management | Gestion des urgences et des feux de végétation |
| `BGW09` | Nature Conservation | Conservation de la nature |
| `BGW10` | Operations Management | Gestion des opérations |
| `BGW11` | Protected Areas Establishment | Établissement des aires protégées |
| `BGW12` | Public Understanding and Appreciation | Compréhension et appréciation du public |
| `BGW13` | Visitor Experience and Services (National, Marine, and Urban Parks) | Services et expériences aux visiteurs (Parcs nationaux, marins et urbains) |
| `BGW14` | Visitor Experience and Services (National Historic Sites and Canals) | Services et expériences aux visiteurs (Lieux historiques nationaux et canaux) |
| `BGX01` | Legislative Audit | Audit législatif |
| `BGY00` | Shared water resources management | Gestion des ressources communes en eau |
| `BGZ00` | Great Lakes water quality management | Gestion de la qualité de l&#39;eau des Grands Lacs |
| `BKX00` | International Development Research Centre | Centre de recherches pour le développement international |
| `BKY00` | Governor General Support | Soutien du gouverneur général |
| `BKZ00` | Canadian Tourism Commission | Commission canadienne du tourisme |
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
| `BNL05` | Pilimmaksaivik | Pilimmaksaivik |
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
| `BNP01` | Business Innovation | Innovation en entreprise |
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
| `BNQ05` | Clean Energy Innovation | Innovations dans les énergies propres |
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
| `BNR03` | Research and Technology Partnerships | Partenariats en recherche et en technologie |
| `BNS00` | Standards Council of Canada | Conseil canadien des normes |
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
| `BNZ02` | Office of the Commissioner for Federal Judicial Affairs | Commissariat à la magistrature fédérale |
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
| `BRG02` | Protection | Protection |
| `BRH01` | Court administration | Administration de la Cour |
| `BRH02` | Administration of the Judges Act for the Judges of the Supreme Court of Canada | Administration de la Loi sur les juges pour les juges de la Cour suprême du Canada |
| `BRI00` | Canadian Museum of History | Musée canadien de l&#39;histoire |
| `BRL00` | Canadian Museum for Human Rights | Musée canadien des droits de la personne |
| `BRN00` | Canadian Museum of Immigration at Pier 21 | Musée canadien de l&#39;immigration du Quai 21 |
| `BRQ00` | Canadian Museum of Nature | Musée canadien de la nature |
| `BRT01` | Support for Canadian and Indigenous Content Creation | Soutien pour la création de contenu canadien et de contenu autochtone |
| `BRT02` | Access to the Communications System | Accès au système de communication |
| `BRT03` | Protection Within the Communications System | Protection au sein du système de communication |
| `BRU00` | National Museum of Science and Technology | Musée national des sciences et de la technologie |
| `BRY00` | National Gallery of Canada | Musée des beaux-arts du Canada |
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
| `BSJ01` | Access and Services | Accès et services |
| `BSJ02` | Outreach and support to communities | Sensibilisation et soutien aux collectivités |
| `BSJ03` | Access to information and privacy | Accès à l&#39;information et protection des renseignements personnels |
| `BSK00` | National Arts Centre Corporation | Société du Centre national des Arts |
| `BSM01` | Audiovisual programming and production | Programmation et production audiovisuelles |
| `BSN00` | National Capital Commission | Commission de la capitale nationale |
| `BSP01` | Distribution of works and audience engagement | Distribution des œuvres et interaction avec les auditoires |
| `BSP02` | Promotion of works and National Film Board outreach | Promotion des œuvres et rayonnement de l&#39;Office national du film |
| `BSP03` | Preservation, conservation and digitization of works | Préservation, conservation et numérisation des œuvres |
| `BSQ00` | Funding the production of Canadian content | Financement à la production de contenus canadiens |
| `BSR00` | Promoting Canadian talent and content | Promotion des talents et des contenus canadiens |
| `BSS00` | Administration and Interpretation of the Conflict of Interest Act and the Conflict of Interest Code for Members of the House of Commons | Application et interprétation de la Loi sur les conflits d&#39;intérêts et du Code régissant les conflits d&#39;intérêts des députés |
| `BST00` | Members and House Officers | Députés et agents supérieurs de la Chambre |
| `BSU00` | House Administration | Administration de la Chambre |
| `BSV00` | Information Support for Parliament | Services d&#39;information aux parlementaires |
| `BSW00` | Physical security | Sécurité physique |
| `BSX00` | Senators, House Officers, and their Offices | Sénateurs, hauts fonctionnaires, et bureaux des sénateurs |
| `BSY00` | Administrative Support | Soutien administratif |
| `BSZ00` | Chamber, Committees and Associations | Chambre, comités et associations |
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
| `BTE00` | Administration and Interpretation of the Ethics and Conflict of Interest Code for Senators | Administration et interprétation du Code régissant l&#39;éthique et les conflits d&#39;intérêts |
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
| `BTG08` | Hydrographic Services, Data and Science | Services hydrographiques, données et sciences |
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
| `BTM05` | Innovative Forestry Solutions | Solutions forestières novatrices |
| `BTM06` | Integrated Landscape Dynamics | Dynamique intégrée des paysages |
| `BTM07` | Cumulative Effects | Effets cumulatifs |
| `BTM08` | Lower Carbon Transportation | Transport faible en carbone |
| `BTM09` | Electricity Resources | Ressources en électricité |
| `BTM10` | Energy Efficiency | Efficacité énergétique |
| `BTM11` | Energy and Climate Change Policy | Politique en matière d&#39;énergie et de changements climatiques |
| `BTM12` | Innovative Geospatial Solutions | Solutions géospatiales novatrices |
| `BTM13` | Energy Innovation and Clean Technology (EICT) | Innovation énergétique et technologies propres (IETP) |
| `BTN00` | The Jacques-Cartier and Champlain Bridges Inc. | Les Ponts Jacques-Cartier et Champlain Inc. |
| `BTO01` | Forest Sector Competitiveness | Compétitivité du secteur forestier |
| `BTO02` | Provision of Federal Leadership in the Minerals and Metals Sector | Prestation d&#39;un leadership fédéral dans le secteur des minéraux et des métaux |
| `BTO03` | Clean and Conventional Fuels | Combustibles propres et conventionnels |
| `BTO04` | International Energy Engagement | Mobilisation au titre de l&#39;énergie à l&#39;échelle internationale |
| `BTO05` | Statutory Offshore Payments | Paiements législatifs pour les hydrocarbures extracôtiers |
| `BTO06` | Indigenous Partnerships Office | Bureau des partenariats avec les Autochtones |
| `BTO07` | Nòkwewashk | Nòkwewashk |
| `BTO08` | Youth Employment and Skills Strategy - Science and Technology Internship Program (Green Jobs) | La Stratégie emploi et compétences jeunesse - Programme de stages en sciences et technologie (Emplois verts) |
| `BTO09` | Indigenous Reconciliation and Regulatory Coordination | Réconciliation avec les peuples autochtones et coordination réglementaire |
| `BTQ00` | Windsor-Detroit Bridge Authority | Autorité du pont Windsor-Détroit |
| `BTR01` | Learning | Apprentissage |
| `BTS01` | Disclosure and Reprisal Management | Gestion des divulgations et des représailles |
| `BTT01` | Analysis and Outreach | Analyse et liaison |
| `BTT02` | Dispute Resolution | Règlement des différends |
| `BTT03` | Determinations and Compliance | Déterminations et conformité |
| `BTU00` | Manage International Bridges | Gestion de ponts internationaux |
| `BTV00` | Marine Atlantic Inc. | Marine Atlantique S.C.C. |
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
| `BTW19` | Rail Security Program | Programme de la sûreté ferroviaire |
| `BTW20` | Transportation of Dangerous Goods Regulatory Framework | Cadre réglementaire pour le transport des marchandises dangereuses |
| `BTW21` | Transportation of Dangerous Goods Oversight | Surveillance du transport des marchandises dangereuses |
| `BTW22` | Transportation of Dangerous Goods Technical Support | Soutien technique du transport des marchandises dangereuses |
| `BTW23` | Multimodal Safety &amp; Security Services | Services de la sécurité et la sûreté multimodales |
| `BTW24` | Security Clearances | Habilitations de sécurité |
| `BTW25` | Emergency Management | Gestion des urgences |
| `BTW26` | National Enforcement Program | Programme national d&#39;application de la loi |
| `BTW27` | National Security and Intelligence Program | Programmes de sécurité nationale et de renseignement |
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
| `BTZ00` | VIA Rail Canada Inc. | VIA Rail Canada Inc. |
| `BUA01` | Conditional Release Decisions | Décisions relatives à la mise en liberté sous condition |
| `BUB01` | Conditional Release Openness and Accountability | Application transparente et responsable du processus de mise en liberté sous condition |
| `BUC01` | Record Suspension/Pardon and Expungement Decisions/Clemency Recommendations | Décisions relatives à la suspension du casier/au pardon et à la radiation et recommandations concernant la clémence |
| `BUD00` | Canada Post Corporation | Société canadienne des postes |
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
| `BUF12` | Science and Engineering | Sciences et génie |
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
| `BUJ03` | Contraband Interdiction and Management | Interception et gestion des objets interdits |
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
| `BUK10` | Social Programs | Programmes sociaux |
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
| `BUO06` | Ready Cyber and Joint Communication and Information Systems (JCIS) | Cyberforces et systèmes de communication et d&#39;information interarmées (SCII ) prêts au combat |
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
| `BUU00` | Financial Literacy | Littératie financière |
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
| `BUW01` | Supervision Program | Programme de surveillance |
| `BUW02` | Strategic Policy and Reviews | Politique stratégique et examens |
| `BUX01` | Financial Intelligence Program | Programme du renseignement financier |
| `BUX02` | Strategic Intelligence, Research and Analytics | Renseignements stratégiques, recherche et analyse |
| `BUY00` | Security and Intelligence | Sécurité et renseignement |
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
| `BVB13` | Human Development: Health &amp; Education | Développement de la personne: Santé et éducation |
| `BVB14` | Growth that works for everyone | Une croissance au service de tous |
| `BVB15` | Environment and Climate Action | Environnement et l&#39;action pour le climat |
| `BVB16` | Human Rights, Governance, Democracy &amp; Inclusion | Droits de la personne, gouvernance, démocratie et inclusion |
| `BVB17` | Peace and Security Policy | Politique liée à la Paix et sécurité |
| `BVB18` | Inclusive Governance | Gouvernance inclusive |
| `BVB19` | International Security Policy and Diplomacy | Politique de sécurité internationale et diplomatie |
| `BVB20` | International Assistance Policy | Politique d&#39;aide internationale |
| `BVB21` | International Strategy and Engagement | Stratégie et engagement internationaux |
| `BVB22` | International Security | Sécurité internationale |
| `BVC01` | Trade Policy, Agreements, Negotiations and Disputes | Politiques et négociations commerciales, accords et différends |
| `BVC02` | Trade Controls | Réglementation commerciale |
| `BVC03` | International Business Development | Développement du commerce international |
| `BVC04` | International Innovation and Investment | Innovation et investissement international |
| `BVC05` | Europe, Arctic, Middle East and Maghreb Trade | Commerce en Europe, dans l&#39;Arctique, au Moyen-Orient et au Maghreb |
| `BVC06` | Americas Trade | Commerce dans les Amériques |
| `BVC07` | Asia Pacific Trade | Commerce en Asie-Pacifique |
| `BVC08` | Sub-Saharan Africa Trade | Commerce en Afrique subsaharienne |
| `BVC10` | Trade Policy and Negotiations | Politique et négociations commerciales |
| `BVC11` | International Business Development, Investment Attraction and Innovation Support | Développement du commerce international, attraction des investissements et soutien à l&#39;innovation |
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
| `BVD15` | Development, Humanitarian, and Peace and Security Programming | Programme de développement, d&#39;aide humanitaire, de paix et de sécurité |
| `BVE01` | Consular Assistance and Services for Canadians Abroad | Aide consulaire et les services aux Canadiens à l&#39;étranger |
| `BVE02` | Emergency Preparedness and Response | Préparation et intervention en cas d&#39;urgence |
| `BVE03` | Emergency Management, Consular assistance and services to Canadians abroad | Gestion des urgences, aide consulaire et services aux Canadiens à l&#39;étranger |
| `BVF01` | Platform Corporate Services | Services ministériels au niveau de la plateforme |
| `BVF02` | Foreign Service Directives | Directives sur le service extérieur |
| `BVF03` | Client Relations and Mission Operations | Relations avec les clients et opérations des missions |
| `BVF04` | Locally Engaged Staff Services | Services aux employés recrutés sur place |
| `BVF05` | Real Property Planning and Stewardship | Planification et intendance des biens immobiliers |
| `BVF06` | Real Property Project Delivery, Professional and Technical Services | Services professionnels et techniques pour l&#39;exécution des projets de biens immobiliers |
| `BVF07` | Mission Readiness and Security | Préparation et sécurité de la mission |
| `BVF08` | Mission Network IM/IT | Gestion de l&#39;information et technologie de l&#39;information du réseau des missions |
| `BVF09` | International Platform | Plateforme internationale |
| `BVF10` | People at Missions | Personnel dans les missions |
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
| `BVG24` | Oral Health | Santé buccodentaire |
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
| `BVP02` | Chronic Diseases and Conditions | Maladies et affections chroniques |
| `BVP03` | Evidence for Health Promotion, and Chronic Disease and Injury Prevention | Données probantes liées à la promotion de la santé et à la prévention des maladies chroniques et des blessures |
| `BVP04` | Mental Health, Suicide, Substance Use, and Safe Relationships | Santé mentale, suicide, toxicomanie et relations sécuritaires |
| `BVQ01` | Laboratory Science Leadership and Services | Services et leadership en matière de science en laboratoire |
| `BVQ02` | Communicable Disease and Infection Control | Contrôle des maladies transmissibles et des infections |
| `BVQ03` | Vaccination | Vaccination |
| `BVQ04` | Foodborne, Waterborne and Zoonotic Diseases | Maladies zoonotiques, d&#39;origine hydrique et d&#39;origine alimentaire |
| `BVQ05` | Emerging and Respiratory, Vaccine Preventable Infectious Disease, Preparedness and Response | Maladies infectieuses émergentes et respiratoires, maladies infectieuses évitables par la vaccination, préparation et intervention |
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
| `BVX02` | Real Property and Infrastructure Services | Services immobiliers et d&#39;infrastructure |
| `BVX03` | Parliament Hill and Surroundings | Colline du Parlement et ses environs |
| `BVX04` | Cape Breton Operations (CBO) – Portfolio Management | Opérations du Cap-Breton (OCB) – Gestion du portefeuille |
| `BVY01` | Linguistic services | Services linguistiques |
| `BVY02` | Communication Services | Services de communication |
| `BVY03` | Government-Wide Digital Solutions and Services | Solutions et services numériques pangouvernementaux |
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
| `BWB04` | Staffing | Dotation |
| `BWB05` | Legislation, regulation, and oversight | Législation, réglementation, et surveillance |
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
| `BWD05` | High Performance Computing Solution | Solution informatique de haute performance |
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
| `BWI07` | Transition Support | Soutient à la transition |
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
| `BWI19` | Income Replacement Benefit | Prestation de remplacement du revenu |
| `BWI20` | Canadian Forces Income Support | Soutien du revenu des Forces canadiennes |
| `BWJ01` | Canada Remembers Program | Programme Le Canada se souvient |
| `BWJ02` | Funeral and Burial Program | Programme de funérailles et d&#39;inhumation |
| `BWK01` | Veterans Ombudsperson | Ombudsman des vétérans |
| `BWL01` | Review and Appeal | Révision et appel |
| `BWM01` | Statutory, Legislative and Policy Support to First Nations Governance | Soutien statutaire, législatif et politique à la gouvernance autochtone |
| `BWM02` | Negotiation of Treaties, Self-Government Agreements and Other Constructive Arrangements | Négociation des traités, des ententes sur l&#39;autonomie gouvernementale et d&#39;autres ententes constructives |
| `BWM03` | Specific Claims | Revendications particulières |
| `BWM04` | Management of Treaties and Agreements | Gestion des traités et des ententes |
| `BWM05` | Guidance and Advice on Duty to Consult | Orientation et conseils sur l&#39;obligation de consulter |
| `BWM06` | Consultation and Policy Development | Consultation et élaboration de politiques |
| `BWM07` | Federal Interlocutor&#39;s Contribution Program | Programme de contribution de l&#39;Interlocuteur fédéral |
| `BWM08` | Basic Organizational Capacity | Capacité organisationnelle de base |
| `BWM09` | Other Claims | Autres revendications |
| `BWM10` | Indigenous Institutional Development and Land Management | Développement institutionnel autochtone et gestion des terres |
| `BWM11` | Northern and Arctic Governance and Partnerships | Gouvernance et partenariats dans le Nord et l&#39;Arctique |
| `BWM12` | Individual Affairs | Affaires individuelles |
| `BWM13` | Indian Residential Schools Settlement Agreement | Convention de règlement relative aux pensionnats indiens |
| `BWM14` | Residential Schools Legacy | Séquelles des pensionnats |
| `BWM15` | Support for Indigenous Engagement and Capacity | Soutien à la mobilisation et au renforcement des capacités des Autochtones |
| `BWM16` | Support for Indigenous-led Services and Programming | Soutien aux services et aux programmes dirigés par les Autochtones |
| `BWM17` | Management of Litigation and Claims | Gestion des litiges et des revendications |
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
| `BWP15` | Canadian Agricultural Strategic Priorities Program | Programme canadien des priorités stratégiques de l&#39;agriculture |
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
| `BWR12` | Northern Sustainable Management | Gestion durable dans le Nord |
| `BWR13` | Northern Strategic Policy and Governance | Politiques stratégiques et gouvernance du Nord |
| `BWR14` | Northern Science Leadership | Leadership scientifique dans le Nord |
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
| `BWV01` | Conference Services | Services de conférences |
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
| `BWX03` | Canadian High Arctic Research Station (CHARS) Operations and Logistics | Opérations et logistique de la Station de recherche de l&#39;Extrême-Arctique canadien |
| `BWY01` | Review of Canadian Security Intelligence Service operations | Examen des opérations du Service canadien du renseignement de sécurité |
| `BWY02` | Investigation of complaints against the Canadian Security Intelligence Service | Enquêtes sur les plaintes contre le Service canadien du renseignement de sécurité |
| `BWZ00` | Economic and fiscal analysis | Analyse financière et économique |
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
| `BXG02` | Federal Policing Intelligence | Renseignement de la Police fédérale |
| `BXG03` | Protective Operations | Opérations de protection |
| `BXG04` | Federal Policing Prevention and Engagement | Prévention et engagement de la Police fédérale |
| `BXG05` | International Operations | Opérations internationales |
| `BXG06` | Federal Operations Support | Soutien aux opérations fédérales |
| `BXG07` | Federal Policing National Governance | Gouvernance nationale de la Police fédérale |
| `BXH01` | Canadian Firearms Investigative and Enforcement Services | Services d&#39;enquête et d&#39;application de la loi en matière d&#39;armes à feu |
| `BXH02` | Criminal Intelligence Service Canada | Service canadien de renseignements criminels |
| `BXH03` | Forensic Science and Identification Services | Services des sciences judiciaires et de l&#39;identité |
| `BXH04` | Canadian Police College | Collège canadien de police |
| `BXH05` | Sensitive and Specialized Investigative Services | Services d&#39;enquêtes spécialisées et de nature délicate |
| `BXH06` | Specialized Technical Investigative Services | Services spécialisés d&#39;enquêtes techniques |
| `BXH07` | RCMP Departmental Security | Sécurité ministérielle de la GRC |
| `BXH08` | RCMP Operational IM/IT Services | Services opérationnels de la GI-TI de la GRC |
| `BXH09` | Canadian Firearms Licensing and Registration | Délivrance de permis et enregistrement des armes à feu au Canada |
| `BXH10` | National Cybercrime Coordination Centre | Centre National de coordination contre la cybercriminalite |
| `BXI01` | Provincial/Territorial Policing | Services de police provinciaux et territoriaux |
| `BXI02` | Municipal Policing | Services de police municipaux |
| `BXI03` | Indigenous Policing | Services de police autochtones |
| `BXI04` | Operational Policing Support | Soutien policier opérationnel |
| `BXI05` | Force Generation | Mise sur pied de la force |
| `BXI06` | Excellence in Operations | Excellence des opérations |
| `BXI07` | Community Safety Policing Support | Soutien à la police de sécurité communautaire |
| `BXI08` | Provincial/Territorial/Municipal Policing | Services de police provinciaux, territoriaux et municipaux |
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
| `BXR03` | Advancing Equality for Women | Promotion de l&#39;égalité des femmes |
| `BXR04` | Preventing and Addressing Gender-Based Violence | Prévenir et contrer la violence fondée sur le sexe |
| `BXR05` | Advancing Equality for Sexual Orientation, Gender Identity or Expression and Sex Characteristics | Programme de promotion de l&#39;égalité des sexes, de l&#39;orientation sexuelle, de l&#39;identité et de l&#39;expression de genre |
| `BXR06` | Gender-Based Analysis Plus | Analyse comparative entre les sexes Plus |
| `BXS01` | Quasi-judicial Review Program | Programme d&#39;examen quasi judiciaire |
| `BXT01` | Company Performance | Rendement des sociétés |
| `BXT02` | Industry Performance | Système de rendement du secteur |
| `BXT03` | Emergency Management | Gestion des situations d&#39;urgence |
| `BXT04` | Regulatory Framework | Cadre de réglementation |
| `BXU01` | Energy and Pipeline Information | Information sur l&#39;énergie et les pipelines |
| `BXU02` | Pipeline Information | Information sur les pipelines |
| `BXV01` | Stakeholder Engagement | Mobilisation des parties prenantes |
| `BXV02` | Indigenous Engagement | Mobilisation des Autochtones |
| `BXW01` | National security and intelligence activity reviews and complaints investigations | Surveillance des activités en matière de sécurité nationale et de renseignement et enquêtes sur les plaintes |
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
| `BYE05` | Connectivity | Connectivité |
| `BYE06` | Security | Sécurité |
| `BYE07` | Enterprise Services Design and Delivery | Conception et prestation des services d&#39;entreprise |
| `BYE08` | Hosting Services | Services d&#39;hébergement |
| `BYF00` | Canadian Race Relations Foundation | Fondation canadienne des relations raciales |
| `BYG01` | Electoral Boundaries Readjustment Administration | Révision des limites des circonscriptions électorales |
| `BYH00` | Canadian Commercial Corporation | Corporation commerciale Canadienne |
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
| `BYQ00` | VIA HFR – VIA TGF Inc | VIA HFR – VIA TGF Inc |
| `BYR01` | Freshwater Management | Gestion de l&#39;eau douce |
| `BYR02` | Freshwater Policy and Engagement | Politique et mobilisation de l&#39;eau douce |
| `BYS01` | Housing Policy and Programming | Politiques et programmes de logement |
| `BYS02` | Homelessness Policy and Programming | Politiques et programmes sur l&#39;itinérance |
| `BYT01` | Public Transit and Active Transportation | Transport en commun et transport actif |
| `BYT02` | Water, Wastewater and Solid Waste | Eau, eaux usées et déchets solides |
| `BYT03` | Resilient Infrastructure | Infrastructures résilientes |
| `BYT04` | Community Building | Développement des collectivités |
| `BYT05` | Major Bridges and Projects | Grands ponts et projets |
| `BYT06` | Alternative Financing | Autres modes de financement |
| `BYU01` | Pharmaceutical Trends Program | Le programme sur les tendances relatives aux produits pharmaceutiques |
| `BYU02` | Patented Medicine Price Monitoring Program | Programme de surveillance du prix des médicaments brevetés |
| `BYX01` | Icebreaking Services | Services de déglaçage |
| `BYX02` | Aids to Navigation | Aides à la navigation |
| `BYX03` | Waterways Management | Gestion des voies navigables |
| `BYX04` | Marine Communications and Traffic Services | Services de communications et de trafic maritimes |
| `BYX05` | Shore-based Asset Readiness | État de préparation des actifs terrestres |
| `BYY01` | Search and Rescue | Recherche et sauvetage |
| `BYY02` | Marine Environmental and Hazards Response | Intervention environnementale |
| `BYY03` | Maritime Security | Sécurité maritime |
| `BYY04` | Fleet Operational Capability | Capacité opérationnelle de la flotte |
| `BYY05` | Fleet Maintenance | Entretien de la flotte |
| `BYY06` | Fleet Procurement | Acquisitions de la flotte |
| `BYY07` | Canadian Coast Guard College | Collège de la Garde côtière canadienne |
| `BYZ01` | Production | Production |
| `BYZ02` | Public Engagement | Engagement des auditoires |
| `BYZ03` | Education | Éducation |
| `BYZ04` | Preservation | Préservation |
| `BZA01` | Trade Policy and Negotiations | Politique et négociations commerciales |
| `BZA02` | International Business Development, Investment Attraction and Innovation Support | Développement du commerce international, attraction des investissements et soutien à l&#39;innovation |
| `BZA03` | Development, Humanitarian, and Peace and Security Programming | Programme de développement, d&#39;aide humanitaire, de paix et de sécurité |
| `BZA04` | International Strategy and Engagement | Stratégie et engagement internationaux |
| `BZA05` | International Security and Political Affairs | Sécurité internationale et affaires politiques |
| `BZB01` | Emergency Management, Consular assistance and services to Canadians abroad | Gestion des urgences, aide consulaire et services aux Canadiens à l&#39;étranger |
| `BZB02` | International Platform | Plateforme internationale |
| `BZB03` | People at Missions | Personnel dans les missions |
| `HGD00` | International Policing Operations | Opérations policières internationales |
| `HGE00` | Canadian Police Culture and Heritage | Culture et patrimoine de la police canadienne |
| `HGF00` | Transfer Payments | Paiements de transfert |
| `ISS00` | Internal services | Services internes |
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
| `ISS10` | Internal services – Office of the Privacy Commissioner | Services internes – Commissariat à la protection de la vie privée |
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
| `ISS20` | Internal services | Services internes |
| `ISS30` | Internal services | Services internes |
| `ISS40` | Internal services | Services internes |
| `ISS50` | Internal services | Services internes |
| `ISSA0` | Internal services | Services internes |
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
For the scope of this question, please answer yes if the service uses an automated decision systems to make or assist officers in making administrative decisions, those that affect legal rights, privileges or interests of clients, whether internal or external. When a system is an automated decision system that makes or assists an officer in making, the requirements of the Directive must be met, and an Algorithmic Impact Assessment published. Refer to the Guide on the Scope of the Directive on Automated Decision-Making to learn more about whether the system is in scope of the Directive on Automated Decision-Making. You can also reach out to your department’s Chief Information and Chief Data Offices to learn more about whether the system falls in scope of the Directive.
  
FR: Un système décisionnel automatisé est défini dans la Directive sur la prise de décisions automatisée et désigne toute technologie qui assiste ou remplace le jugement des décideurs humains, comme ceux qui proviennent de domaines tels que les statistiques, la linguistique et les sciences informatiques, et utilisent des techniques telles que les systèmes basés sur des règles, la régression, l’analytique prédictive, l’apprentissage automatique, l’apprentissage en profondeur et les réseaux neuronaux.
Pour la portée de cette question, veuillez répondre "oui" si le service utilise des systèmes décisionnel automatisé pour prendre ou aider les agents à prendre des décisions administratives, celles qui affectent les droits juridiques, les privilèges ou les intérêts des clients, qu'ils soient internes ou externes. Lorsqu'un système est un système décisionnel automatisé qui prend ou aide un agent à prendre des décisions, les exigences de la Directive doivent être respectées, et une Évaluation de l'incidence algorithmique doit être publiée. Référez-vous au Guide sur la portée de la Directive sur la prise de décisions automatisée pour en savoir plus sur la portée de la Directive sur la prise de décision automatisée. Vous pouvez également contacter les bureaux du Dirigeant principal de l'information et du Dirigeant principal des données de votre ministère pour en savoir plus sur la portée de la Directive.



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
Ce champ a une longueur maximale de 1800 caractères.
  


**Description:**  
EN: Describe what the system does. Include: the name or title of the system, the role of the system in the decision, whether it is full or partial automation, and how officers use the system to make or inform the decision. Include whether or not an Algorithmic Impact Assessment is published, and if not indicate the reason for not publishing one.
  
FR: Décrivez ce que fait le système. Inclure : le nom ou titre du système, le rôle du système dans la prise de décision, s'il s'agit d'une automatisation complète ou partielle, et comment les agents utilisent le système pour prendre ou informer la décision. Indiquer si une Évaluation de l'incidence algorithmique est publiée ou non, et si ce n'est pas le cas, indiquez la raison pour laquelle elle n'est pas publiée.



---

#### `automated_decision_system_description_fr` – Automated Decision System Description (French) / Description du système décisionnel automatisé (français)

**Type:** `text`  
**Required:** No  
**Validation:** This field is required due to a response in a different field.
This field has a maximum length of 1800 characters.
 / Ce champ est requis en raison d'une réponse présente dans un autre champ.
Ce champ a une longueur maximale de 1800 caractères.
  


**Description:**  
EN: Describe what the system does. Include: the name or title of the system, the role of the system in the decision, whether it is full or partial automation, and how officers use the system to make or inform the decision. Include whether or not an Algorithmic Impact Assessment is published, and if not indicate the reason for not publishing one.
  
FR: Décrivez ce que fait le système. Inclure : le nom ou titre du système, le rôle du système dans la prise de décision, s'il s'agit d'une automatisation complète ou partielle, et comment les agents utilisent le système pour prendre ou informer la décision. Indiquer si une Évaluation de l'incidence algorithmique est publiée ou non, et si ce n'est pas le cas, indiquez la raison pour laquelle elle n'est pas publiée.



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
FR: Indique si un client peut demander une résolution à ses problèmes avec le service ou fournir de la rétroaction en ligne.


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
Ce champ a une longueur maximale de 1000 caractères.
  


**Description:**  
EN: Comments related to online services - client Interaction points (English). For any interaction points reported as "Not Applicable", comments have to be provided.
  
FR: Commentaires en anglais en lien avec les services en ligne - points d'interaction avec les clients. Pour tout point d'interaction signalés comme « sans objet », des commentaires doivent être fournis.



---

#### `os_comments_client_interaction_fr` – Comments on Online Services - Client Interaction Points (French) / Commentaires sur les services électroniques - points d'interaction avec les clients (français)

**Type:** `text`  
**Required:** No  
**Validation:** This field is required due to a response in a different field.
This field has a maximum length of 1000 characters.
 / Ce champ est requis en raison d'une réponse présente dans un autre champ.
Ce champ a une longueur maximale de 1000 caractères.
  


**Description:**  
EN: Comments related to online services - client Interaction points (French). For any interaction points reported as "Not Applicable", comments have to be provided.
  
FR: Commentaires en français en lien avec les services en ligne - points d'interaction avec les clients (français). Pour tout point d'interaction signalés comme « sans objet », des commentaires doivent être fournis.



---

#### `last_service_review` – Year of last service review / Année du dernier examen de service

**Type:** `text`  
**Required:** No  
**Choice Set:** last_service_review (25 values)  


**Description:**  
EN: Identifies the fiscal year when the most recent service review was completed.  
FR: Identifie l’exercice financier lors duquel le plus récent examen de service a été mené.


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
EN: Identifies the most recent year in which this service was improved based on client feedback.  
FR: Identifie l'exercice financier la plus récente au cours de laquelle ce service a été amélioré en fonction des commentaires des clients.


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
EN: Identifies whether the Canada Revenue Agency's Business Number is used in the delivery of the service as the standard identifier in accordance with the Data reference standard on the business number.
  
FR: Indique si le numéro d’entreprise de l’Agence du revenu du Canada est utilisé dans la prestation des services en tant qu’identificateur standard, conformément à la Norme référentielle relative aux données sur le numéro d’entreprise.



##### Allowed Values (cra_bn_identifier_usage)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `N` | No | Non |
| `NA` | N/A (not a service to businesses) | S.O. (N&#39;est pas un service aux entreprises) |
| `Y` | Yes | Oui |




---

#### `num_phone_enquiries` – Number of Telephone Enquiries Received / Nombre de demandes de renseignements reçues par telephone

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field must be either a number, "NA", or "ND"
This value must not be negative.
 / Ce champ ne doit pas être vide.
Ce champ doit contenir soit un chiffre, soit « NA », soit « ND ».
Cette valeur ne doit pas être négative.
  


**Description:**  
EN: Identifies the number of enquiries about the service received in this fiscal year. Note: This field represents only requests for information about the service. Report service requests or applications submitted by telephone in the "telephone applications" field. A value of 0 means no calls were received; ND means no data was collected; and NA means it is not possible to submit telephone enquiries.
Note: This field is not included in 'Total Applications'.
  
FR: Indique le nombre de demandes d'information reçues par téléphone au cours d'un exercice financier. Remarque: Ce champ indique seulement le nombre de demandes d'information au sujet d'un service. Servez-vous du champ « Nombre de demandes soumises par téléphone » pour les demandes de prestation de service reçues par téléphone. La valeur 0 signifie qu'aucun appel n'a été reçu, ND signifie qu'aucune donnée n'est disponible, et NA signifie qu'il n'est pas possible de présenter des demandes d’information par téléphone.
Remarque : Ce champ n'est pas inclus dans « Nombre total de demandes ».



---

#### `num_applications_by_phone` – Number of Applications Submitted by Telephone / Nombre de demandes soumises par téléphone

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field must be either a number, "NA", or "ND"
This value must not be negative.
 / Ce champ ne doit pas être vide.
Ce champ doit contenir soit un chiffre, soit « NA », soit « ND ».
Cette valeur ne doit pas être négative.
  


**Description:**  
EN: Identifies the number of applications submitted in a fiscal year for the telephone channel. A value of 0 means no applications were received for this channel; ND means there is no data collected for this channel; and NA means no applications can be submitted through this channel.
  
FR: Indique le nombre de demandes de prestation de service reçues par téléphone au cours d'un exercice. La valeur 0 signifie qu'aucune demande n'a été reçue via ce mode de prestation, aucune donnée (ND) signifie qu'aucune donnée n’est disponible, et sans objet (NA) signifie que le service n’est pas offert au moyen de ce mode de prestation.



---

#### `num_website_visits` – Number of Website Visits / Nombre de visites sur le site Web

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field must be either a number, "NA", or "ND"
This value must not be negative.
 / Ce champ ne doit pas être vide.
Ce champ doit contenir soit un chiffre, soit « NA », soit « ND ».
Cette valeur ne doit pas être négative.
  


**Description:**  
EN: Identifies the number of visits to the service's website in a fiscal year. A value of 0 means there were no visits; ND means there is no data collected website visits; and NA means there is no associated public website.
Note: This field is not included in 'Total Applications'.
  
FR: Indique le nombre de de visites au site Web du service lors d'un exercice financier. La valeur 0 signifie qu'aucune visite au site Web n’a été enregistrée, aucune donnée (ND) signifie que le nombre de visites n’est pas mesuré, et sans objet (NA) signifie qu’il n’y a aucune site web à visiter.
Remarque : Ce champ n'est pas inclus dans « Nombre total de demandes ».



---

#### `num_applications_online` – Number of Applications Submitted Online / Nombre de demandes soumises en ligne

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field must be either a number, "NA", or "ND"
This value must not be negative.
 / Ce champ ne doit pas être vide.
Ce champ doit contenir soit un chiffre, soit « NA », soit « ND ».
Cette valeur ne doit pas être négative.
  


**Description:**  
EN: Identifies the number of applications submitted in a fiscal year for the online channel. A value of 0 means no applications were received for this channel; ND means there is no data collected for this channel; and NA means no applications can be submitted through this channel. Examples include applications received via a website/online portal, via web forms (e.g., MyPayEnquiry) and digitally administered audits and evaluations.
  
FR: Indique le nombre de demandes de prestation de service reçues en ligne au cours d'un exercice. La valeur 0 signifie qu'aucune demande n'a été reçue via ce mode de prestation, aucune donnée (ND) signifie qu'aucune donnée n’est disponible, et sans objet (NA) signifie que le service n’est pas offert au moyen de ce mode de prestation. Il s'agit par exemple des demandes reçues sur un site Web ou un portail en ligne, sur des formulaires Web (p. ex., Ma demande de paye) et des vérifications et évaluations administrés numériquement.



---

#### `num_applications_in_person` – Number of Applications Submitted In-Person / Nombre de demandes soumises en personne

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field must be either a number, "NA", or "ND"
This value must not be negative.
 / Ce champ ne doit pas être vide.
Ce champ doit contenir soit un chiffre, soit « NA », soit « ND ».
Cette valeur ne doit pas être négative.
  


**Description:**  
EN: Identifies number of applications received in-person in a fiscal year for the service. A value of 0 means no applications were received for this channel; ND means there is no data collected for this channel; and NA means no applications can be submitted through this channel. Examples include in-person applications, volume of inspections, audits, evaluations, etc.
  
FR: Indique le nombre de demandes de prestation de service reçues en personne au cours d'un exercice. La valeur 0 signifie qu'aucune demande n'a été reçue via ce mode de prestation, aucune donnée (ND) signifie qu'aucune donnée n’est disponible, et sans objet (NA) signifie que le service n’est pas offert au moyen de ce mode de prestation. Il s’agit par exemple des demandes en personne, du volume d'inspections, d'audits, d'évaluations, etc.



---

#### `num_applications_by_mail` – Number of Applications Submitted via Postal Mail / Nombre de demandes soumises par la poste

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field must be either a number, "NA", or "ND"
This value must not be negative.
 / Ce champ ne doit pas être vide.
Ce champ doit contenir soit un chiffre, soit « NA », soit « ND ».
Cette valeur ne doit pas être négative.
  


**Description:**  
EN: Identifies the number of applications received through postal mail in a fiscal year. A value of 0 means no applications were received for this channel; ND means there is no data collected for this channel; and NA means no applications can be submitted through this channel.
  
FR: Indique le nombre de demandes de prestation de service reçues par la poste au cours d'un exercice. La valeur 0 signifie qu'aucune demande n'a été reçue via ce mode de prestation, aucune donnée (ND) signifie qu'aucune donnée n’est disponible, et sans objet (NA) signifie que le service n’est pas offert au moyen de ce mode de prestation.



---

#### `num_applications_by_email` – Number of Applications Submitted by Email / Nombre de demandes soumises par courriel

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field must be either a number, "NA", or "ND"
This value must not be negative.
 / Ce champ ne doit pas être vide.
Ce champ doit contenir soit un chiffre, soit « NA », soit « ND ».
Cette valeur ne doit pas être négative.
  


**Description:**  
EN: Identifies the number of applications received through email in a fiscal year for the service. A value of 0 means no applications were received for this channel; ND means there is no data collected for this channel; and NA means no applications can be submitted through this channel.
Examples include applications received by email and audits, reviews and evaluations by email.
  
FR: Indique le nombre de demandes de prestation de service reçues par courriel au cours d'un exercice. La valeur 0 signifie qu'aucune demande n'a été reçue via ce mode de prestation, aucune donnée (ND) signifie qu'aucune donnée n’est disponible, et sans objet (NA) signifie que le service n’est pas offert au moyen de ce mode de prestation.
Il s'agit par exemple des demandes reçues par courriel et des audits, examens et évaluations par courriel.



---

#### `num_applications_by_fax` – Number of Applications Submitted by Fax / Nombre de demandes soumises par fax

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field must be either a number, "NA", or "ND"
This value must not be negative.
 / Ce champ ne doit pas être vide.
Ce champ doit contenir soit un chiffre, soit « NA », soit « ND ».
Cette valeur ne doit pas être négative.
  


**Description:**  
EN: Identifies the number of applications received through fax in a fiscal year for the service. A value of 0 means no applications were received for this channel; ND means there is no data collected for this channel; and NA means no applications can be submitted through this channel.
  
FR: Indique le nombre de demandes de prestation de service reçues par télécopieur au cours d'un exercice. La valeur 0 signifie qu'aucune demande n'a été reçue via ce mode de prestation, aucune donnée (ND) signifie qu'aucune donnée n’est disponible, et sans objet (NA) signifie que le service n’est pas offert au moyen de ce mode de prestation.



---

#### `num_applications_by_other` – Number of Applications Submitted via other channels / Nombre de demandes soumises par les autre modes de prestations

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field must be either a number, "NA", or "ND"
This value must not be negative.
 / Ce champ ne doit pas être vide.
Ce champ doit contenir soit un chiffre, soit « NA », soit « ND ».
Cette valeur ne doit pas être négative.
  


**Description:**  
EN: Identifies the number of applications received through other channels not listed in a fiscal year for the service. A value of 0 means no applications were received for this channel; ND means there is no data collected for this channel; and NA means no applications can be submitted through this channel.
If service volumes are not tracked by channel, please include service volumes in this field. As well, please include in this field volumes for funding allocations without applications or other services that do not require applications (e.g. medical screening at intake, investigations, hearings, advice) or which do not disaggregate service demand by delivery channel.
Note: Volumes reported in each channel should be mutually exclusive. Do not report the same application or interaction in more than one channel.
  
FR: Indique le nombre de demandes de prestation de service reçues par des modes de prestations qui ne sont pas énumérés dans ce gabarit au cours d'un exercice. La valeur 0 signifie qu'aucune demande n'a été reçue via ce mode de prestation, aucune donnée (ND) signifie qu'aucune donnée n’est disponible, et sans objet (NA) signifie que le service n’est pas offert au moyen de ce mode de prestation.
Si les volumes de service ne sont pas suivis par canal, veuillez inclure les volumes de service dans ce champ. De même, veuillez inclure dans ce champ les volumes d'allocations de fonds sans demandes ou d'autres services qui ne nécessitent pas de demandes (p. ex., examen médical à l'admission, enquêtes, audiences, conseils) ou qui ne ventilent pas la demande de service par canal de prestation.
Remarque : les volumes déclarés dans chaque canal doivent s'exclure mutuellement. Ne déclarez pas la même demande ou interaction dans plus d'un canal.



---

#### `special_remarks_en` – Special Remarks (English) / Remarques spéciales (anglais)

**Type:** `text`  
**Required:** No  
**Validation:** This field has a maximum length of 2000 characters. / Ce champ a une longueur maximale de 2000 caractères.  


**Description:**  
EN: Provides additional space for comments related to volumetrics information. Please refer to associated Field ID, where applicable. For comments related to other fields, departments can create and publish an explanatory note on their website with a link to the GC Service Inventory dataset. This field is mandatory if there is an amount reported under “Number of applications submitted via other channels”
  
FR: Fournit de l'espace supplémentaire pour les commentaires relatifs aux renseignements sur les volumes. Veuillez vous reporter au code d'identification du champ, s'il y a lieu. Pour les commentaires relatifs à d'autres champs, les ministères peuvent publier une note explicative sur leur site Web suivi d'un lien vers l'ensemble de données du Répertoire des services du GC. Ce champ est requis s’il y a un montant rapporté sous le champ « Nombre de demandes soumises par les autres modes de prestation »



---

#### `special_remarks_fr` – Special Remarks (French) / Remarques spéciales (français)

**Type:** `text`  
**Required:** No  
**Validation:** This field has a maximum length of 2000 characters. / Ce champ a une longueur maximale de 2000 caractères.  


**Description:**  
EN: Provides additional space for comments related to volumetrics information. Please refer to associated Field ID, where applicable. For comments related to other fields, departments can create and publish an explanatory note on their website with a link to the GC Service Inventory dataset. This field is mandatory if there is an amount reported under “Number of applications submitted via other channels”
  
FR: Fournit de l'espace supplémentaire pour les commentaires relatifs aux renseignements sur les volumes. Veuillez vous reporter au code d'identification du champ, s'il y a lieu. Pour les commentaires relatifs à d'autres champs, les ministères peuvent publier une note explicative sur leur site Web suivi d'un lien vers l'ensemble de données du Répertoire des services du GC. Ce champ est requis s’il y a un montant rapporté sous le champ « Nombre de demandes soumises par les autres modes de prestation »



---

#### `service_uri_en` – URL to Service (English) / URL du service (anglais)

**Type:** `text`  
**Required:** No  
**Validation:** This field has a maximum length of 1500 characters. / Ce champ a une longueur maximale de 1500 caractères.  


**Description:**  
EN: Identifies the departmental webpage where the service is described and/or accessed.  
FR: Indique la page Web du ministère où le service est décrit ou peut être lancé.


---

#### `service_uri_fr` – URL to Service (French) / URL du service (français)

**Type:** `text`  
**Required:** No  
**Validation:** This field has a maximum length of 1500 characters. / Ce champ a une longueur maximale de 1500 caractères.  


**Description:**  
EN: Identifies the departmental webpage where the service is described and/or accessed.  
FR: Indique la page Web du ministère où le service est décrit ou peut être lancé.


---



## Service Standards & Performance Results / Normes de service et résultats de rendement 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `fiscal_yr` | Fiscal Year / Exercice financier | `text` | Yes |  | fiscal_yr | Identifies the fiscal year (April 1 to March 31) during which service activitie… |
| `service_id` | Service ID Number / Numéro d&#39;identification du service | `text` | Yes |  | service_id | The unique number assigned to a service in the inventory to make it easier to r… |
| `service_name_en` | Service Name (English) / Nom du service (anglais) | `text` | Yes |  |  | Identifies the official name of the service. |
| `service_name_fr` | Service Name (French) / Nom du service (français) | `text` | Yes |  |  | Identifies the official name of the service. |
| `service_standard_id` | Service Standard ID / Numéro d&#39;identification de la norme relative aux services | `text` | Yes |  |  | Identifies the unique number assigned to each service standard for that service… |
| `service_standard_en` | Service Standard (English) / Norme relative aux services (anglais) | `text` | Yes |  |  | Identifies the service standard related to a particular service. See Guideline … |
| `service_standard_fr` | Service Standard (French) / Norme relative aux services (français) | `text` | Yes |  |  | Identifies the service standard related to a particular service. See Guideline … |
| `type` | Service Standard Type / Type de norme relative aux services | `text` | Yes |  | type | Identifies the type of service standard as defined in the Guideline on Service … |
| `channel` | Service Standard Channel / Mode de prestation de la norme de service | `text` | Yes |  | channel | Identifies the service channel to which the service standard applies |
| `channel_comments_en` | Comments on the service standard channel (English) / Commentaires sur le mode de prestation de la norme de service (anglais) | `text` | No |  |  | Comments related to the service standard channel and provides explanation of "O… |
| `channel_comments_fr` | Comments on the service standard channel (French) / Commentaires sur le mode de prestation de la norme de service (Francais) | `text` | No |  |  | Comments related to the service standard channel and provides explanation of "O… |
| `target` | Service Standard Target / Cible de la norme relative aux services | `numeric` | No |  |  | The frequency that the organization expects to meet service standard (reported … |
| `volume_meeting_target` | Business Volume That Met Service Standard Target / Volume d&#39;activités qui respectent la norme de service | `bigint` | No |  |  | Identifies the number of final outputs issued appropriate to the service (eg. p… |
| `total_volume` | Total Volume / Volumes totaux | `bigint` | No |  |  | Identifies the total number of final outputs issued appropriate to the service … |
| `comments_en` | Comments on the service standard in general (English) / Commentaires sur la norme de service en général (anglais) | `text` | No |  |  | Comments related to the service standard in general. |
| `comments_fr` | Comments on the service standard in general (French) / Commentaires sur la norme de service en général (français) | `text` | No |  |  | Comments related to the service standard in general. |
| `standards_targets_uri_en` | URL to Service Standards and Targets (English) / URL vers les normes de service et les cibles (anglais) | `text` | Yes |  |  | Identifies the departmental webpage (Canada.ca) where the service standards and… |
| `standards_targets_uri_fr` | URL to Service Standards and Targets (French) / URL vers les normes de service et les cibles (français) | `text` | Yes |  |  | Identifies the departmental webpage (Canada.ca) where the service standards and… |
| `performance_results_uri_en` | URL to Real-Time Performance Results (English) / URL aux résultats de rendement en temps réel (anglais) | `text` | No |  |  | Identifies the departmental webpage where the real-time performance results for… |
| `performance_results_uri_fr` | URL to Real-Time Performance Results (French) / URL aux résultats de rendement en temps réel (français) | `text` | No |  |  | Identifies the departmental webpage where the real-time performance results for… |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `fiscal_yr` – Fiscal Year / Exercice financier

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** fiscal_yr (13 values)  


**Description:**  
EN: Identifies the fiscal year (April 1 to March 31) during which service activities took place. For example, records for fiscal year 2023-2024 should include applications received from April 1, 2023, to March 31, 2024.
  
FR: Indique l'exercice financier (1 avril au 31 mars) durant lequel les activités du service ont eu lieu. Par exemple, les données pour l’exercice financier 2023-2024 devraient inclure les demandes de service qui ont été reçues entre le 1er avril 2023 et le 31 mars 2024.



##### Allowed Values (fiscal_yr)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
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




---

#### `service_id` – Service ID Number / Numéro d'identification du service

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field cannot contain commas.
 / Ce champ ne doit pas être vide.
Ce champ ne peut pas contenir de virgules.
  
**Choice Set:** service_id (2673 values)  


**Description:**  
EN: The unique number assigned to a service in the inventory to make it easier to refer to specific services.  
FR: Le numéro unique attribué à un service dans le répertoire afin de faciliter le référencement à des services précis.


##### Allowed Values (service_id)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `1` | Permit to Operate a Rendering Plant | Permis d&#39;exploitation d&#39;une usine de traitement |
| `10` | Procurement | Approvisionnement |
| `1000` | Reconciliation | Réconciliation |
| `1001` | Old Age Security (OAS) Benefits | Prestations de la Sécurité de la vieillesse |
| `1002` | Research Data Centres (RDC) | Centres de données de recherche (CDR) |
| `1003` | Employment Insurance (EI) Benefits | Prestations d’assurance-emploi |
| `1004` | Canada Nature Fund for Aquatic Species at Risk | Le Fonds de la nature du Canada pour les espèces aquatiques en péril |
| `1005` | Canadian Benefit for Parents of Young Victims of Crime | Allocation canadienne aux parents de jeunes victimes de crimes |
| `1006` | Catch Certification Program | Programme de certification des captures |
| `1007` | Canada Apprenticeship Grants | Subventions aux apprentis du Canada |
| `1008` | Aquatic Ecosystems Restoration Fund (AERF) | Fonds de restauration des écosystèmes aquatiques (FREA) |
| `1009` | Fisheries Act Authorizations | Autorisations en vertu de la Loi sur les pêches |
| `1010` | Fisheries and Aquaculture Clean Technology Adoption Program (FACTAP) | Programme d&#39;adoption des technologies propres pour les pêches et l&#39;aquaculture (PTPPA) |
| `1011` | Habitat Stewardship Program for Aquatic Species at Risk | Programme d&#39;intendance de l&#39;habitat pour les espèces aquatiques en péril |
| `1012` | Intergovernmental and International Relations | Relations intergouvernementales et internationales |
| `1013` | Introduction and Transfer Licensing Application Review | Processus d&#39;évaluation de permis d&#39;introduction et de transfert |
| `1014` | National Indigenous Representative Organizations | Organisations autochtones représentatives nationale |
| `1015` | MPA Activity Plan Application Process - Anguniaqvia niqiqyuam MPA | Processus de demande d&#39;activités pour la ZPM - Anguniaqvia niqiqyuam |
| `1016` | MPA Activity Plan Application Process - SGaan Kinghlas-Bowie Seamount MPA | Processus de demande d&#39;activités pour la ZPM - Mont sous-marin SGaan Kinghlas-Bowie |
| `1017` | MPA Activity Plan Application Process - Eastport MPA | Processus de demande d&#39;activités pour la ZPM - Eastport |
| `1018` | MPA Activity Plan Application Process - Endeavour Hydrothermal Vents | Processus de demande d&#39;activités pour la ZPM - Champ hydrothermal Endeavour |
| `1019` | Métis Housing | Logement des Métis |
| `1020` | MPA Activity Plan Application Process - Gilbert Bay MPA | Processus de demande d&#39;activités pour la ZPM - Baie Gilbert |
| `1021` | MPA Activity Plan Application Process - Gully MPA | Processus de demande d&#39;activités pour la ZPM - Gully |
| `1022` | MPA Activity Plan Application Process - Hecate Strait/Queen Charlotte Sound Glas | Processus de demande d&#39;activités pour la ZPM - Détroit d&#39;Hécate |
| `1023` | Inuit Housing | Logement des Inuit |
| `1024` | MPA Activity Plan Application Process - Musquash Estuary MPA | Processus de demande d&#39;activités pour la ZPM - Estuaire de la Musquash |
| `1025` | MPA Activity Plan Application Process - St. Anns Bank MPA | Processus de demande d&#39;activités pour la ZPM - Banc de Sainte-Anne |
| `1026` | National Online License System (NOLS) | Système national d&#39;émission de permis en ligne (SNEPL) |
| `1027` | National Recreational Licensing System (NRLS) (Pacific Only) | Système national d&#39;émission de permis de pêche récréative (SNDPP) |
| `1028` | Observer Designation Application and Renewal Processing | demandes de désignation d&#39;observateur et des demandes de renouvellement |
| `1029` | Oceans Management Contribution Program in support of oceans conservation and management | Programme de contributions pour la gestion des océans pour appuyer l&#39;élaboration et la mise en œuvre d&#39;activités de conservation et de gestion des océans |
| `1030` | Oceans Management Program - Grants in support Indigenous Groups in the Development and Implementation of Oceans Conservation and Management Activities | Programme de gestion des océans - Subventions à l’appui des groupes autochtones dans l’élaboration et la mise en œuvre d’activités de conservation et de gestion des océans |
| `1031` | Recreational Fisheries Conservation Partnerships Program Contribution Agreements | Programme de partenariats relatifs à la conservation des pêches récréatives |
| `1032` | Salmon Conservation Stamp | Timbre de protection du saumon |
| `1033` | Small Craft Harbours Class Contribution Program | Programme de contribution du MPO aux ports pour petits bateaux |
| `1034` | Small Craft Harbours Divestiture Class Grant Program | Programme de dessaisissement des ports pour petits bateaux |
| `1035` | Species at Risk Act Permits | Les permis de la Loi sur les espèces en péril |
| `1036` | Marine Environmental and Hazards Response | Intervention en cas de dangers et d’incidents environnementaux maritimes |
| `1037` | Icebreaking | Déglaçage |
| `1038` | Provision of Distress and Safety Communications | Prestation de services de communication de détresse et de sécurité |
| `1039` | Provision of Marine Information | Diffusion de renseignements maritimes |
| `1040` | Provision of Radio Communications and Public Correspondence Service | Prestation de services de correspondance publique et de communications radio |
| `1041` | Search and Rescue Coordination | Recherche et sauvetage Coordination |
| `1042` | Orientation sessions for persons with a priority entitlement. | Droit de priorité: Séances d&#39;orientation pour les bénéficiares d&#39;un droit de priorité |
| `1043` | Search and Rescue Response | Recherche et sauvetage |
| `1044` | Vessel Screening and Regulation of Vessel Traffic Movements | Contrôle des navires et réglementation des mouvements du trafic maritime |
| `1045` | Waterways Management | Gestion des voies navigables |
| `1046` | Release of Statistical Data on International Trade | Diffusion de données statistiques sur le commerce international |
| `1047` | Release of Statistical Data on Balance of Payment | Diffusion de données statistiques sur la balance de paiement |
| `1048` | Ministerial Designations for Protective Services by the RCMP | Désignations ministérielles pour les Services de la protection par la GRC |
| `1050` | Cadet Online Registration | Inscription en ligne pour les cadets |
| `1051` | Military History and Heritage | Histoire et patrimoine militaires |
| `1052` | Access to Information and Privacy | Accès à l&#39;information et de la protection des renseignements personnels |
| `1053` | Assistance connecting with foreign markets | Aide pour accéder aux marchés étrangers |
| `1054` | Acquiring Surplus Equipment | Acquisition De Biens Excédentaires |
| `1055` | Drugs and Medical Devices: Permission to Market | Médicaments et instruments médicaux : Autorisation de mise en marché |
| `1056` | Executrek Program | Programme ExécuTrek |
| `1057` | Legacy Sites Unexploded Explosive Ordnance (UXO) Program | Programme des munitions explosives non explosées (UXO) sur le anciens sites |
| `1058` | Compensation for Employers of Reservists Program (CERP) | Programme de Dédommagement des Employeurs de Réservistes |
| `1059` | Natural Health Products: Permission to Market | Produits de santé naturels : Autorisation de mise en marché |
| `1060` | Natural Health Products: Permission to Operate | Produits de santé naturels : Autorisation d&#39;exploitation |
| `1062` | Drugs and Medical Devices: Right to Sell Domestically | Médicaments et instruments médicaux : Droit de vendre à l&#39;échelle nationale |
| `1064` | Innovation for Defence Excellence and Security (IDEaS) | Innovation pour la défense, l’excellence et la sécurité (IDEeS) |
| `1065` | Mobilizing Insights in Defence and Security (MINDS) | Mobilisation des idées nouvelles en matière de défense et de sécurité (MINDS) |
| `1066` | Ministerial Correspondence Unit | Unité de la correspondance ministérielle |
| `1088` | Special Access Programs | Programmes d&#39;accès spéciale |
| `1089` | Food Market Authorization and Standards | Autorisation et normes du marché alimentaire |
| `1090` | Wage Earner Protection Program | Programme de protection des salariés |
| `1091` | Analytical testing services | Services d’analyse |
| `1092` | Science Horizons Youth Internship Program | Programme de stages Horizons Sciences pour les jeunes |
| `1093` | General Enquiry and Referral Telephone Service (1-800 O Canada) | Demande de renseignements généraux et service d’aiguillage par téléphone (1-800 O Canada) |
| `1094` | People Information Management Automated Request Tracker - Information/Data Request Service | Renseignements de gestion des personnes et données sur les demandes de service |
| `1095` | National Print Services | Service d&#39;impression national |
| `1096` | Occupational Health and Safety Tribunal Canada | Tribunal de santé et sécurité au travail Canada |
| `1097` | Individual Income Tax Returns | Déclaration d&#39;impôt sur le revenus des particuliers |
| `1098` | Authorize a Representative | Autoriser un Représentant |
| `1099` | GST/HST Returns | Production d&#39;une déclaration de la TPS/TVH |
| `1100` | GST/HST Rulings | Décisions en matière de TPS/TVH |
| `1101` | T2 Corporation Income Tax Returns | Déclaration de revenus des sociétés T2 |
| `1102` | Excise Duty, Excise Tax, Air Travellers Security Charge, and Fuel Charge returns | Droits d&#39;accise, taxes d&#39;accise, droit pour la sécurité des passagers du transport aérien, et déclaration de la redevance sur les combustibles |
| `1103` | IT Interoperability - GC Interop | Interopérabilité TI - GC Interop |
| `1104` | Income Tax Rulings | Décisions en Impôt |
| `1105` | Charity Information Return Filing | Déclaration de renseignements des organismes de bienfaisance |
| `1106` | Partnership Information Returns | Déclaration de Renseignements des Sociétés de Personnes |
| `1107` | Canada child benefit (CCB) applications | Les demandes d&#39;Allocation canadienne pour enfants (ACE) |
| `1108` | Tax Credit Application | Demande de crédit d&#39;impôt |
| `1109` | Children&#39;s Special Allowances (CSA) applications | Les demandes d&#39;Allocations Spéciales pour Enfants (ASE) |
| `1110` | Advanced Canada workers benefit (ACWB) | Avance de l’allocation canadienne pour les travailleurs (AACT) |
| `1111` | Provincial and territorial tax credit payments | Les versements de crédits d&#39;impôt provinciaux et territoriaux |
| `1112` | Provincial and territorial child benefit program payments | Les versements provinciaux et territoriaux pour les programmes de prestations pour enfants |
| `1113` | Formal Review Request (Objections) | Demande de vérification officielle (Oppositions) |
| `1114` | Public Enquiries | Demandes de renseignement |
| `1115` | Trust Income Tax Returns | Dépôt des déclarations de revenus des fiducies |
| `1116` | Business Number (BN) Registration | Inscription d&#39;un Numéro d&#39;Entreprise (NE) |
| `1117` | Access to Information and Privacy | Accès à l&#39;information et à la protection des renseignements personnels |
| `1118` | Prime Minister&#39;s Email | Courriel du premier ministre |
| `1119` | Copyright Tariff Setting | Établissement de tarifs liés au droit d’auteur |
| `1120` | Issuance of licences for the use of copyright works when the owner is unlocatable | Délivrance de licences pour les oeuvres protégées par un droit d&#39;auteur lorsque le titulaire est introuvable |
| `1121` | Public Notices of funding opportunities | Avis publics concernant les possibilités de financement |
| `1122` | Public enquiries | Demandes de renseignements du publique |
| `1123` | Public Notices of Successful Funding Applications | Avis publics concernant les demandes de financement retenues |
| `1126` | Funding transfers to administering institutions | Transfert des fonds aux établissements administrateurs |
| `1127` | Direct funding payments | Versement direct des fonds |
| `1128` | Grants and Awards Management | Gestion des subventions et bourses |
| `1129` | Access to Information and Privacy | Loi sur l’accès à l’information et Loi sur la protection des renseignements personnels |
| `1130` | GCshare | GCpartage |
| `1131` | Funding Services | Services de financement |
| `1132` | Diagnostic Testing and Reference Services | Tests de diagnostic et Services de référence |
| `1133` | Training and Guidance on the Duty to Consult | Formation et conseils sur l&#39;obligation de consulter |
| `1134` | Aboriginal and Treaty Rights Information System (ATRIS) and Training on using the system. | Système d&#39;information sur les droits ancestraux et issus de traités (SIDAIT) et formation sur l&#39;utilisation du système. |
| `1135` | Modern Treaty Management Environment (MTME) | Environnement de gestion des traités modernes (EGTM) |
| `1136` | Consultation Protocols and Resource Centres | Protocoles de consultation et centres de ressources |
| `1137` | Executive Correspondence | Correspondance de haute gestion |
| `1138` | Training &amp; Education on Modern treaties &amp; Self-Government Agreements | Formation et éducation sur les traités modernes et les ententes sur l’autonomie gouvernementale |
| `1139` | Individual Tax Enquiries (Contact Centre) | Demandes de renseignements sur l&#39;impôt des particuliers (Centre de contact) |
| `1140` | The First Nations Fiscal Management Act and its institutions. | La Loi sur la gestion financière des Premières Nations et ses institutions. |
| `1141` | Business Enquiries (Contact Centre) | Demandes de renseignements des entreprises (Centre de contact) |
| `1142` | Microbiological Emergency Response Team | Équipe d&#39;intervention d&#39;urgence |
| `1143` | Benefit Enquiries (Contact Centre) | Demandes de renseignements sur les prestations (Centre de contact) |
| `1144` | Pay and Benefits | Rémunération et avantages sociaux |
| `1145` | Maintain and update the Indian Register | Tenir le Registre des Indiens et le mettre à jour |
| `1146` | Disability Tax Credit | Crédit d&#39;impôt pour personnes handicapées |
| `1147` | My Government of Canada Human Resources (MyGCHR) | Mes ressources humaines du gouvernement du Canada (MesRHGC) |
| `1148` | Secure Certificate of Indian Status | Certificat sécurisé de statut d&#39;Indien |
| `1149` | Canada.ca | Canada.ca |
| `1150` | Treaty Payments Events | Paiement événements dans les traités |
| `1151` | Treaty Annuity Payments | Paiement des annuités prévues dans les traités |
| `1153` | Complaint Management - Human Rights | Gestion des plaintes - Droits de la personne |
| `1154` | Registration of persons with a priority entitlement | Inscription des personnes bénéficiant d&#39;un droit de priorité |
| `1155` | Identification of persons with a priority entitlement to vacant positions | Identification des personnes ayant le droit de priorité aux postes vacants |
| `1156` | Process permission requests from public servants seeking to be a candidate in an election | Traiter les demandes de permission des fonctionnaires souhaitant se porter candidats à une élection |
| `1157` | Targeted Contribution Funding to Support Climate Change Projects | Fonds de contribution ciblés pour soutenir les projets liés aux changements climatiques |
| `1158` | Official Language proficiency: Exclusions on medical grounds | Compétence en matière de langues officielles : Exemptions pour des raisons d&#39;ordre médical |
| `1159` | Provide minerals prospecting permits | Délivrer des permis de prospection |
| `1160` | Provide mineral claims | Délivrer des claims miniers |
| `1161` | Provide mining leases | Délivrer des baux miniers |
| `1162` | Provide licenses to prospect for minerals | Délivrer des licences de prospection des minéraux |
| `1163` | Provide coal exploration licenses, location permits and leases | Délivrer des permis de recherche de gisement de houille, des permis et des concessions d&#39;un emplacement |
| `1164` | Provide Crown land use permits | Fournir des permis d&#39;utilisation des terres de la Couronne |
| `1165` | Provide Crown land surface leases | Fournir des baux de surface pour les terres de la Couronne. |
| `1166` | Northern Participant Funding Program | Programme d&#39;aide financière aux participants du Nord |
| `1167` | Provide funding and advice to support Indigenous entrepreneurship and business d | Fournir du financement et des conseils pour soutenir l’entrepreneuriat autochtone et le développement des entreprises. |
| `1172` | FSWEP; Ongoing student recruitment inventory for hiring managers | Programme fédéral d&#39;expérience de travail étudiant: Répertoire d&#39;étudiants pour les gestionnaires |
| `1173` | Compliance - Employment Equity | Conformité - Équité en matière d&#39;emploi |
| `1176` | Post-secondary Co-op / Internship Program (CO-OP); Recruitment options for managers | Programme postsecondaire d&#39;enseignement coopératif / de stages: Options de recrutement pour les gestionnaires |
| `1178` | Provide funding and advice to support First Nation Economic Development Capacity | Fournir des conseils et du financement afin d’appuyer la capacité et la préparation du développement économique des Premières Nations. |
| `1179` | Research Affiliate Program (RAP); Recruitment options for managers | Programme des adjoints de recherche: Options de recrutement pour les gestionnaires |
| `1180` | Post-Secondary Recruitment Program (PSR); Recruitment options for managers | Programme de recrutement postsecondaire: Options de recrutement pour les gestionnaires |
| `1182` | Indian Land Registry | Registre des terres indiennes |
| `1183` | Recruitment of Policy leaders (RPL); Recruitment options for managers | Recrutement de leaders en politiques: Options de recrutement pour les gestionnaires |
| `1187` | Access to Information and Privacy Request Services | Service de demandes d&#39;accès à l&#39;information et protection des renseignements personnels |
| `1188` | With First Nation consent, administer and process additions to reserve applicati | Avec le consentement des Premières Nations, administrer et traiter les demandes d’ajout aux réserves afin de soutenir le développement communautaire et économique durable des Premières Nations. |
| `1190` | Additions to Reserve | Ajouts aux réserves |
| `1193` | Regulatory Development under the First Nations Commercial and Industrial Develop | Développement de règlements en vertu de la Loi sur le développement commercial et industriel des Premières Nations |
| `1195` | Public Service Resourcing System (PSRS); PSRS Help desk | Système de ressourcement de la fonction publique (SRFP): Service de dépannage du SRFP |
| `1196` | Procurement Strategy for Aboriginal Business and the Indigenous Business Directo | Stratégie d&#39;approvisionnement auprès des entreprises autochtones et Le répertoire des entreprises autochtones |
| `1197` | Indigenous Business Directory | Annuaire des entreprises autochtone |
| `1198` | Meeting Statutory/ Regulatory Obligations with Respect to Elections and Lawmakin | Respect des obligations statutaires ou réglementaires en matière d’élections et de législation |
| `1199` | Access to Capital | Accès au capital |
| `12` | Procurement Training Services | Services de formation sur l&#39;approvisionnement |
| `1200` | Prime Minister&#39;s Website | Site Web du premier ministre |
| `1202` | Personnel Psychology Centre; Assessment accommodation | Centre de psychologie du personnel: Mesures d&#39;adaptation en matière d&#39;évaluation |
| `1204` | Personnel Psychology Centre; Test Services | Centre de psychologie du personnel: Services d&#39;évaluation |
| `1208` | Environmental Funding - Community Interaction Program | Programme Interactions communautaires |
| `1210` | Personnel Psychology Centre;Consultation Services | Centre de psychologie du personnel: Services de consultation |
| `1211` | Measuring Device Prototype Approvals (new approvals) | Approbation des prototypes d&#39;appareils de mesure (nouvelles approbations) |
| `1212` | First Nation Land Management | Gestion des terres des Premières Nations |
| `1213` | Reserve Land and Environment Management Program | Programme de gestion de l&#39;environnement et des terres de réserves |
| `1214` | Matrimonial Real Property | Biens Immobiliers Matrimoniaux |
| `1215` | Land Use Planning | Planification de l&#39;utilisation des terres |
| `1216` | First Nations Solid Waste Management Initiative | Initiative de gestion des matières résiduelles des Premières Nations |
| `1217` | Environmental Review Process | Processus d&#39;évaluation environnementale |
| `1218` | Authorized Service Provider Accreditation, Registration and Renewal | Renouvellement d&#39;un fournisseur de services autorisé |
| `1219` | Contaminated Sites On Reserve Program | Programme des sites contaminés dans les réserves |
| `1220` | Approvals | Approbations |
| `1221` | Bankruptcy and Insolvency Records Search | Recherche de dossiers de faillite et d&#39;insolvabilité |
| `1222` | Licensed Insolvency Trustee (LIT) Licence Renewal | Renouvellement de Licence de syndics autorisés en insolvabilité (SAI) |
| `1223` | Heritage Designations | Désignation patrimoniales |
| `1225` | Federal Heritage Buildings Review Office | Bureau d&#39;examen des édifices fédéraux du patrimoine |
| `1228` | Rulings / Interpretations | Décisions / interprétations |
| `1229` | Amend, upon ministerial approval, Schedule I of The First Nation Oil And Gas And | Modifier, avec l’approbation ministérielle, l’annexe 1 de la Loi sur la gestion du pétrole et du gaz des fonds des Premières Nations pour y inclure les Premières Nations ayant tenu avec succès un vote visant à permettre l’exercice de la gouvernance a |
| `1230` | With First Nation consent, issue leases, permits or licenses to industry stakeho | Avec le consentement des Premières Nations, délivrer des baux, des permis ou des licences aux intervenants de l’industrie pour faciliter la prospection pétrolière et gazière et la mise en valeur des ressources sur les terres des Premières Nations. As |
| `1231` | Information and Transaction Services | Le service d&#39;information et de transaction |
| `1232` | Media Relations | Relations avec les médias |
| `1233` | Funding for Essential Community-Based Services: First Nations Child and Family Services | Financement des services essentiels communautaires: Services à l’enfance et à la famille des Premières Nations |
| `1234` | Licensed Insolvency Trustee (LIT) License Issuance Decisions | Décisions sur l&#39;octroi d&#39;une licence de syndic autorisé en insolvabilité (SAI) |
| `1235` | Incorporations | Incorporations |
| `1236` | Funding for Essential Community-Based Services: Assisted Living | Financement des services essentiels communautaires : aide à la vie autonome |
| `1237` | Nuans - Provide Corporate Name Search Report | Nuans-Générer un rapport de dénomination |
| `1238` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnel |
| `1239` | Funding for Essential Community-Based Services: Income Assistance | Financement des services essentiels communautaires : aide au revenu |
| `1240` | Futurpreneur Canada | Futurpreneur Canada |
| `1241` | Funding Essential Community-Based Services: Family Violence Prevention Shelter Program | Financement des services essentiels communautaires : Programme pour la prévention de la violence familiale |
| `1242` | Canadian Passport | Passeport canadien |
| `1243` | Canada Small Business Financing Program (CSBFP) | Programme de financement des petites entreprises du Canada (PFPEC) |
| `1244` | Merger Review - Competition Law Enforcement | Examen des fusions – Application du droit de la concurrence |
| `1245` | Funding for Essential Community-Based Services: Family Violence Prevention Shelt | Financement des services essentiels communautaires : Financement aux refuges pour la prévention de la violence familiale |
| `1246` | Information Centre - Law Enforcement | Centre d&#39;information - Application de la loi |
| `1247` | Funding for Essential Community-Based Services: Urban Programming for Indigenous Peoples | Financement des services essentiels communautaires : Programmes urbains pour les peuples autochtones |
| `1248` | CA Identification Number Application &amp; Updates | Numéro d&#39;identification CA Demande et mises à jour |
| `1249` | Copies of Corporate Documents and Certificates | Copies de documents constitutifs et certificats |
| `125` | Domestic Statistics and Market Information Web | Statistiques canadiennes et site Web d&#39;information sur les marchés |
| `1250` | Written Opinions | Avis écrits |
| `1251` | Capital Confirmations | Confirmations de la qualité des fonds propres |
| `1252` | In-Person Service | Service en personne |
| `1253` | Register Industrial Designs | Enregistrement de dessins industriels |
| `1254` | Office for Client Satisfaction | Bureau de la satisfaction des clients |
| `1255` | Register Copyrights | Enregistrement de droits d&#39;auteur |
| `1256` | Labour Market Impact Assessment | Études d’impact sur le marché du travail |
| `1257` | Disability Pension and Pain and Suffering Compensation | Pension d&#39;invalidité et indemnité pour douleur et souffrance |
| `1258` | Register Trademarks | Enregistrement de marques de commerce |
| `1260` | Canada Lands Survey System | Système d&#39;arpentage des terres du Canada |
| `1261` | Career Impact Allowance | Allocation pour incidence sur la carrière |
| `1262` | Exceptional Incapacity Allowance | Allocation d&#39;incapacité exceptionnelle |
| `1263` | Treatment Allowance | Allocation de traitement |
| `1264` | Attendance Allowance | Allocation pour soins |
| `1265` | IP Advisory Services | Service de conseils en PI |
| `1266` | Management of Grants and Contributions (Gs&amp;Cs) for Employment and Social Development Programs | Administration des subventions et contributions (S et C) pour les programmes d’Emploi et Développement social |
| `1267` | Grant Patents | Délivrance de brevets |
| `1268` | Connect to Innovate (CTI) | Brancher pour innover |
| `1269` | Financial Support for Long Term Care | Aide financière pour soins de longue durée |
| `127` | Canadian Soil Information Services (CanSIS) | Système d’information sur les sols du Canada (SISCan) |
| `1270` | Healthcare Costs and Supports | Coûts de soins de santé et soutien |
| `1271` | Veterans Independence Grants &amp; Reimbursements | Programme pour l&#39;autonomie des anciens combattants – Subventions et remboursements |
| `1272` | Educational Assistance for Children | Aide à l&#39;éducation pour les enfants |
| `1273` | War Veterans Allowance | Allocation aux anciens combattants |
| `1274` | Accessible Technology Development Program (ATP) | Programme de développement de la technologie accessible |
| `1275` | IRAP Grants and Contributions | Subventions et contributions du PARI |
| `1276` | Connecting Families Initiative (CFi), formerly Affordable Access Initiative | L&#39;initiative Familles branchées, anciennement l&#39;Initiative d&#39;accès abordable |
| `1277` | Care and Maintenance of Veterans&#39; Graves | Programme d&#39;entretien des stèles funéraires |
| `1278` | Earnings Loss Benefit | Allocation pour perte de revenus |
| `1279` | Public Recognition and Awareness | Reconnaissance et sensibilisation du public |
| `1280` | Commemorative Partnerships | Programme de partenariat pour la commémoration |
| `1281` | Funeral and Burial | Aide pour les funérailles et l&#39;inhumation |
| `1282` | Computers for School Plus (CFS+) | Ordinateurs pour les écoles et Plus (OPE+) |
| `1283` | Career Transition Services | Services de réorientation professionnelle |
| `1284` | Emergency Financial Support for Veterans | Aide financière d&#39;urgence pour les vétérans |
| `1286` | Veteran and Family Well-being Fund | Fonds pour le bien-être des vêtêrans et de leur famille |
| `1287` | Digital Literacy Exchange Program (DLEP) | Programme d&#39;échange en matière de littératie numérique |
| `1288` | Retirement Income Security Benefit | Allocation de sécurité du revenu de retraite |
| `1289` | Digital Skills for Youth (DS4Y) | Programme de compétences numériques pour les jeunes (CNJ) |
| `129` | Geospatial | Produits géospatiaux |
| `1290` | Work-Sharing | Travail partagé |
| `1291` | Contributions Program for Non-Profit Consumer and Voluntary Organizations | Programme de contributions pour les organisations sans but lucratif de consommateurs et de bénévoles |
| `1292` | Provision of a Social Insurance Number | Émission d’un numéro d’assurance sociale |
| `1293` | Job Bank - Find a Job | Guichet-Emplois– Trouver un emploi |
| `1294` | Job Bank for Employers | Guichet-Emplois pour les employeurs |
| `1295` | Labour Market Information | Information sur le marché du travail |
| `1296` | Canada Student Grants and Canada Student Loans | Bourses canadiennes pour étudiants et Prêts canadiens aux étudiants |
| `1297` | ATIP Online request platform | Plateforme de demande d’AIPRP en ligne |
| `1298` | Canada Apprentice Loans | Prêt canadien aux apprentis |
| `1299` | Contact Us- General Information to Data Users and Technical Support to Survey Respondents | Contactez-nous - Information générale aux utilisateurs des données et support technique aux répondants |
| `13` | Information and Education Services to Businesses | Services d&#39;information et de formation aux entreprises |
| `130` | Drought Watch | Guetter la sécheresse |
| `1300` | Funding Essential Community-Based Services: Elementary and Secondary Education | Financement des services essentiels communautaires : financement de l’éducation primaire et secondaire |
| `1301` | Clean Growth Hub | Carrefour de la croissance propre |
| `1302` | First Nations and Inuit Skills Link Program | Programme Connexion compétences à l’intention des Premières Nations et des Inuits |
| `1303` | Certification, Coordination, and Technical Analysis for Broadcast Radio and TV | Certification, coordination et analyse technique pour la radiodiffusion et la télévision |
| `1304` | Issuing Radio Operator Certificates | Délivrance de certificats d&#39;opérateur radio |
| `1305` | First Nations and Inuit Summer Work Experience Program | Programme Expérience d&#39;emploi d’été pour les étudiants inuits et des Premières Nations |
| `1306` | Issuing Radio/Spectrum Licences | Délivrance de licences radio et de spectre |
| `1307` | Strategic Innovation Fund (SIF) Online Application | Demande en ligne du Fonds stratégique pour l&#39;innovation (FSI) |
| `1308` | Grants and Contributions | Subventions et contributions |
| `1309` | My StatCan | Mon StatCan |
| `131` | Office of Intellectual Property and Commercialization | Bureau de la propriété intellectuelle et de la commercialisation (BPIC) |
| `1310` | First Nations and Inuit Cultural Education Centres Program Funding | Financement du Programme des centres éducatifs et culturels des Premières Nations et des Inuits |
| `1311` | Issuance of permits | Émission des permis |
| `1312` | Indspire | Indspire |
| `1313` | First Nations, Métis Nation and Inuit Post-Secondary Education Strategies | Stratégies d’éducation postsecondaire des Premières Nations, de la Nation métisse et des Inuits |
| `1314` | Métis Nation Post-Secondary Education Strategy | Stratégie d’éducation postsecondaire de la Nation métisse |
| `1315` | Radio and Terminal Equipment Certification | Homologation de l&#39;équipement radio et du matériel terminal |
| `1316` | Inuit Post-Secondary Strategy | Stratégie d’éducation postsecondaire des Inuits |
| `1317` | Release of Statistical Data on the Monthly Gross Domestic Product (GDP) by Industry | Diffusion de données statistiques sur le produit intérieur brut mensuel (PIB) par industrie |
| `1318` | Release of Statistical Data on the Quarterly Gross Domestic Product (GDP) | Diffusion de données statistiques sur le produit intérieur brut trimestriel (PIB) |
| `1319` | Release of Statistical Data on Manufacturing Sector | Diffusion de données statistiques sur le secteur de la fabrication |
| `132` | Saint-Hyacinthe Research and Development Centre&#39;s Industrial Program | Programme industriel du Centre de recherche et de développement de Saint-Hyacinthe |
| `1320` | Release of Statistical Data on Retail Trade | Diffusion de données statistiques sur le commerce de détail |
| `1321` | Release of Statistical Data on Enterprise Finances | Diffusion de données statistiques sur les finances des entreprises |
| `1322` | Canada Education Savings Grant and Canada Learning Bond | Subvention canadienne pour l’épargne-études et Bon d’études canadien |
| `1323` | CanCode | CodeCan |
| `1325` | Critical Injury Benefit | Indemnité pour blessure grave |
| `1326` | Capital Model Approvals | Approbation des modèles de fonds propres |
| `1327` | Release of Statistical Data on Wholesale Trade | Diffusion de données statistiques sur le commerce de gros |
| `1328` | Access to Information and Privacy | Accès à l&#39;information et de protection des renseignements personnels |
| `1329` | Actuarial Services | Services actuariels |
| `133` | AgriInvest | Agri-investissement |
| `1330` | Consumer Price Index (CPI) | l&#39;Indice des prix à la consommation (IPC) |
| `1331` | Canada Disability Savings Grant and Canada Disability Savings Bond | Subvention canadienne pour l’épargne-invalidité et Bon canadien pour l’épargne-invalidité |
| `1332` | ISED Citizen Services Centre | Centre de services aux citoyens d&#39;ISDE |
| `1333` | BizPal | PerLe |
| `1334` | Canadian Occupational Projection System | Système sur la projection des professions du Canada |
| `1335` | Business Benefits Finder | Outil de recherche d&#39;aide aux entreprise |
| `1336` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `1337` | Occupational Health and Safety Compliance and Enforcement (OHSCE) | Conformité et application de la Santé et sécurité au travail (CASST) |
| `1338` | Northern Ontario Development Program (NODP) | Programme de développement du Nord de l&#39;Ontario (PDNO) |
| `1339` | Client Service Centre (CSC) | Centre de services à la clientèle |
| `134` | AgriStability | Agri-stabilité |
| `1340` | Regional Economic Growth through Innovation (REGI) | Croissance économique régionale par l&#39;innovation (CERI) |
| `1341` | Merchant Seamen Compensation Act (MServCanA) | Loi sur l’indemnisation des marins marchands |
| `1342` | Women Entrepreneurship Strategy (WES) Ecosystem Fund | Fonds pour l&#39;écosystème de la SFE |
| `1343` | Release of Statistical Data on Industrial Product Index (IPPI) | Diffusion de données statistiques sur l&#39;Indice des prix des produits industriels (IPPI) |
| `1344` | Community Futures Program | Programme de développement des collectivités (PDC) |
| `1345` | Economic Development Initiative (EDI) | Initiative de développement économique (IDE) |
| `1346` | Innovation Superclusters Initiative | Initiative des supergrappes d&#39;innovation |
| `1347` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `1348` | Treasury Board of Canada Secretariat’s Claims Office | Bureau des réclamations du Secrétariat du Conseil du Trésor du Canada |
| `1349` | Open Government Portal - Access to data and information | Portail gouvernement ouvert – accès à l’information ouverte et données ouvertes. |
| `135` | Farm Debt Mediation Service | Service de médiation en matière d&#39;endettement agricole |
| `1350` | Classification Program | Programme de classification |
| `1351` | Release of Statistical Data on Census of Population | Diffusion de données statistiques sur le Recensement de la population |
| `1352` | Labour Force Survey | Enquête sur la population active |
| `1353` | Release of Statistical Data on Employment, Payroll and Hours | Diffusion de données statistiques sur l&#39;emploi, la rémunération et les heures de travail |
| `1354` | Client Services- Custom Products | Services au Client - Produits personnalisés |
| `1355` | Statistical Capacity Building – Workshops, Training and Conferences | Renforcement des capacités statistiques - Ateliers, formations et conférences |
| `1356` | National Allegations and Complaints | Plaintes et allégations nationales |
| `1357` | Assessment and Investigations | Services d&#39;examen et d&#39;enquêtes |
| `1358` | Fraud Awareness | Sensibilisation à la fraude |
| `1359` | National Allegations and Complaints | Plaintes et allégations nationales |
| `136` | AgriAssurance: National Industry Association Component | Programme Agri-assurance : Volet Associations nationales de l&#39;industrie |
| `1360` | Forensic Investigations | Enquêtes juricomptable |
| `1361` | Fraud Awareness Training | Formation de sensibilisation a la fraude |
| `1364` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels (AIPRP) |
| `1365` | Executive correspondence services | Services de la correspondance de la haute direction |
| `1366` | Departmental Library | Bibliothèque ministérielle |
| `1367` | Public Enquiries | Renseignements au public |
| `1368` | Canadian Forces Income Support Benefit | Allocation de soutien du revenu des Forces canadiennes |
| `1369` | Administration of Grants &amp; Contributions (Gs&amp;Cs) Service for the Labour Program | Administration des subventions et contributions (S et C) pour le Programme du travail |
| `137` | AgriMarketing Program: National Industry Association | Programme Agri-marketing : Volet Associations nationales de l&#39;industrie |
| `1370` | Labour Management Collaboration Program (also known as Workplace Harassment and | Programme de collaboration syndicale-patronale (aussi connu sous le nom de Fonds de prévention du harcèlement et de la violence en milieu de travail) |
| `1371` | Federal Workers&#39; Compensation | Service fédéral d’indemnisation des accidentés du travail |
| `1372` | Priority Entitlement; Support of medically released veterans with a priority entitlement | Droit de priorité: Soutien aux anciens combattants possédant un droit de priorité |
| `1373` | Federal Mediation and Conciliation Service (FMCS) | Service fédéral de médiation et de conciliation (SFMC) |
| `1374` | Labour Standards Compliance and Enforcement (LSCE) | Conformité et application des normes du travail (CANT) |
| `1375` | Legislated Employment Equity Program (LEEP) | Programme légiféré d&#39;équité en matière d&#39;emploi |
| `1376` | Federal Contractors Program (FCP) | Programme de contrats fédéraux |
| `1377` | Workplace Information Services | Services d’information sur les milieux de travail |
| `138` | AgriScience Program: Projects | Programme Agri-science - projets |
| `1380` | Supplementary Retirement Benefit | Prestation de retraite supplémentaire |
| `1383` | Administration of the Corrections and Conditional Release Regulations | Application du Règlement sur le système correctionnel et la mise en liberté sous condition |
| `1387` | Media enquiries | Demandes de renseignements des médias |
| `1388` | Public enquiries | Renseignements au public |
| `1389` | Orders in Council (OIC) | Décrets |
| `139` | AgriInnovate Program | Programme Agri-innover |
| `1391` | View our Reference Resources | Consultez nos ressources de références |
| `1393` | Read our Analysis | Lisez nos analyses |
| `1397` | Investigations; Conduct investigations on staffing irregularities and improper political activities. | Enquêtes: Mener des enquêtes sur les irrégularités en dotation et les activités politiques irrégulières |
| `14` | GC WAN | Réseau étendu du RGC |
| `140` | AgriRisk: Administrative Capacity Stream | Initiatives Agri-risques: Volet de renforcement des capacités administratives |
| `1403` | Monitoring Services: Surveys and analytical databases | Activités de surveillance: Sondages et bases de données analytiques |
| `1407` | Personal Information Requests Services | Services de demande d’accès à des renseignements personnels |
| `1410` | Grants and contributions | Subventions et contributions |
| `1411` | Leaders&#39; Debates Commission | La Commission aux débats des chefs |
| `1412` | Security Intelligence Review Committee (SIRC) | Le Comité de surveillance des activités de renseignement de sécurité (CSARS) |
| `1413` | National Security and Intelligence Committee of Parliamentarians (NSICOP) | Le Comité des parlementaires sur la sécurité nationale et le renseignement (CPSNR) |
| `1414` | Information about Surveys and for Survey Participants | Renseignements au sujet des enquêtes et pour les participants aux enquêtes |
| `1415` | Access our Statistical Data | Accédez à nos données statistiques |
| `1419` | Rehabilitation Services and Vocational Assistance | Services de réadaptation et d&#39;assistance professionnelle |
| `1420` | Temporary Foreign Workers - Application for Work Permit | Travailleurs étrangers temporaires - Demande de permis de travail |
| `1421` | International Mobility Program: Opinion and Enquires to Employers | Programme de mobilité internationale : Opinion et demandes de renseignements aux employeurs |
| `1422` | Electronic Travel Authorization | Autorisation de voyage électronique |
| `1423` | Temporary Resident Visa | Visa de résident temporaire |
| `1424` | Visitor Record (In-Canada) | Fiche du visiteur (au Canada) |
| `1425` | Restoration of status (In-Canada) | Rétablissement du statut (au Canada) |
| `1426` | Temporary Resident Permit | Permis de résident temporaire |
| `1427` | Temporary Resident Permit for Victims of Trafficking in Persons | Permis de résident temporaire pour les victimes de trafic de personnes |
| `1428` | Study Permit | Permis d&#39;études |
| `1429` | International Experience Canada - Application for Work Permit | Expérience internationale Canada - Demande d&#39;un permis de travail |
| `1430` | Federal Skilled Worker - Application for Permanent Residence | Travailleurs qualifiés (fédéral) - Demande de résidence permanente |
| `1431` | Federal Skilled Trades - Application for Permanent Residence | Travailleurs de métiers spécialisés (fédéral) - Demande de résidence permanente |
| `1432` | Provides a retail subsidy and a Harvesters Support Grant and Community Food Programs Fund to eligible communities | Fournit une subvention au commerce de détail et une subvention de soutien aux récoltants aux communautés éligibles. |
| `1433` | Canadian Experience Class - Application for Permanent Residence | Catégorie de l&#39;expérience canadienne - Demande de résidence permanente |
| `1434` | Start-up Visa - Application for Permanent Residence | Visa pour démarrage d&#39;entreprise - Demande de résidence permanente |
| `1435` | Immigrant Investor Venture Capital (IIVC) | Capital de risque pour les immigrants investisseurs (CRII) |
| `1436` | Federal Self employed - Application for Permanent Residence | Travailleurs autonomes (fédéral) - Demande de résidence permanente |
| `1437` | Live In Caregivers - Application for Permanent Residence | Aides familiaux résidants - Demande de résidence permanente |
| `1438` | Caring for Children or for People with High Medical Needs - Application for Perm | Garde d&#39;enfants ou soins aux personnes ayant des besoins médicaux élevés - Demande de résidence permanente |
| `1439` | Quebec Skilled Workers/Trades - Application for Permanent Residence | Travailleurs qualifiés – Québec - Demande de résidence permanente |
| `144` | AgriCompetitiveness | Programme Agri-compétitivité |
| `1440` | Quebec Business (Entrepreneur, Investor, Self-employed) - Application for Perma | Gens d&#39;affaires au Québec (entrepreneurs, investisseurs, travailleurs autonomes) - Demande de résidence permanente |
| `1441` | Provincial Nominees - Application for Permanent Residence | Candidats des provinces - Demande de résidence permanente |
| `1442` | Family Class Priority - Application for Permanent Residence | Demandes prioritaires de la catégorie du regroupement familial - Demande de résidence permanente |
| `1443` | Parents and Grandparents - Application for Permanent Residence | Parents et grands-parents - Demande de résidence permanente |
| `1444` | Other Relatives - Sponsorship for Permanent Residence | Autres membres de la famille - Parrainage pour la résidence permanente |
| `1445` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `1446` | Spouse or common-law partner in Canada - Application for Permanent Residence | Époux ou conjoints de fait au Canada - Demande de résidence permanente |
| `1447` | Temporary Resident Permit Holder - Application for Permanent Residence | Titulaire d&#39;un Permis de séjour temporaire - Demande de résidence permanente |
| `1449` | Humanitarian &amp; Compassionate - Application for Permanent Residence | Motifs d&#39;ordre humanitaire - Demande de résidence permanente |
| `145` | Youth Employment and Skills Program | Programme d’emploi et de compétences des jeunes |
| `1450` | Resettled Refugees - Permanent Residence | Réfugiés réinstallés - Résidence Permanente |
| `1451` | Humanitarian Public Policy - Application for resettlement to Canada | Politique d&#39;intérêt public humanitaire -Demande de réinstallation au Canada |
| `1452` | Fire Management | Gestion du Feu |
| `1453` | Immigration Loan | Prêts aux immigrants |
| `1454` | One-year window - Application for Permanent Residence of eligible dependants | Délai prescrit d&#39;un an - demande de résidence permanente de personnes à charge admissibles |
| `1455` | Protected Person &amp; Dependants - Permanent Residence | Personne protégée et personnes à charge - Résidence Permanente |
| `1456` | Search and Rescue | recherche et sauvetage |
| `1457` | In-Canada Asylum Claim | Octroi de l&#39;asile au Canada |
| `1458` | Access to information and privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1459` | The Issuance of a Danger Opinion | Émission d&#39;un avis de danger |
| `146` | Canadian Agricultural Strategic Priorities Program | Programme canadien des priorités stratégiques de l’agriculture |
| `1460` | Settlement Transfer Payments | Paiements de transfert, Programme d’établissement |
| `1461` | Federal Internship for Newcomers Program | Programme fédéral de stage pour les nouveaux arrivants |
| `1462` | Larkin Kerwin Library | Bibliothèque Larkin-Kerwin |
| `1463` | Pre-removal Risk Assessment | Examen des risques avant renvoi |
| `1464` | Permanent Resident Card Renewals &amp; Replacements | Renouvellement et remplacement de carte de résident permanent |
| `1465` | Issuance of a Permanent Resident Travel Document | Délivrance d&#39;un titre de voyage de résident permanent |
| `1466` | Resettlement Assistance Program Transfer Payments: Contributions to Service Provider Organisations | Paiements de transfert du Programme d&#39;aide à la réinstallation: Contributions aux fournisseurs de services |
| `1467` | Earth Observation Satellite Data services | Services des données satellitaires en observation de la terre |
| `1468` | The International Charter: Space and Major Disasters | Charte Internationale: espace et catastrophes majeures |
| `1469` | Space situational awareness (SSA) analysis reports (CRAMS) | Rapports d&#39;analyses de surveillance de l&#39;espace (CRAMS) |
| `147` | Agricultural Greenhouse Gas Program | Programme de lutte contre les gaz à effet de serre en agriculture |
| `1470` | Resettlement Assistance Program Transfer Payments: Income Support to Refugees in Canada | Paiements de transfert du Programme d&#39;aide à la réinstallation: Soutien du revenu aux réfugiés au Canada |
| `1471` | Interim Federal Health: Reimbursements to Health Care Professionals | Remboursement dans le cadre du programme fédéral de santé intérimaire |
| `1472` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1473` | Space Astronomy &amp; Space Situational Awareness Imagery | Imagerie spatiale pour la surveillance de l&#39;espace et l&#39;astronomie spatiale |
| `1474` | Satellite-based Automated Identification of Ships (S-AIS) Data Services | Services de données du système d&#39;identification automatique spatioporté (AIS) |
| `1475` | Climate Research Data | Données pour la recherche sur le climat |
| `148` | Canada Pavilion Program | Programme du pavillon du Canada |
| `1480` | Provision of Interim Federal Health Program coverage to eligible beneficiaries | Couverture pour les bénéficiaires admissibles au Programme fédéral de santé intérimaire |
| `1481` | Medical Surveillance Notification | Notification de la surveillance médicale |
| `1482` | Citizenship Grant- Application for Citizenship under Sections 5(1), 5(2), of the | Attribution de citoyenneté - Demande de citoyenneté au titre des articles 5 (1) et 5(2) de la Loi sur la citoyenneté |
| `1483` | Provide crown land quarry permits/leases | Fournir des permis ou des baux d&#39;exploitation de carrière sur des terres de la Couronne |
| `1484` | Application for Grant of Citizenship - Stateless Individual with a Canadian pare | Demande d&#39;attribution de citoyenneté aux personnes apatrides avec un parent canadien |
| `1485` | Application for Grant of Citizenship - Adopted Individual | Demande d&#39;attribution de citoyenneté à une personne adoptée |
| `1486` | Resumption of Citizenship | Réintégration de la citoyenneté |
| `1487` | Renunciation of Citizenship | Répudiation de la citoyenneté |
| `1488` | Proof of Citizenship | Preuve de citoyenneté |
| `1489` | Search of Citizenship Records | Recherche de documents de citoyenneté |
| `149` | Market Intelligence and Information Service | Services de renseignements sur les marchés |
| `1490` | Citizenship Education &amp; Outreach | Éducation et sensibilisation à la citoyenneté |
| `1491` | Issuance of a Regular Passport | Délivrance d&#39;un Passeport régulier |
| `1492` | Issuance of a Diplomatic Passport | Délivrance d&#39;un Passeport diplomatique |
| `1493` | Issuance of Special Passports | Délivrance de Passeport spécial |
| `1494` | Certificate of Identity | Certificat d&#39;identité |
| `1495` | Refugee Travel Document | Titre de voyage pour réfugiés |
| `1496` | Issuance of an Emergency Travel Document | Délivrance d&#39;un Titre de voyage d&#39;urgence |
| `1497` | Visa facilitation for Official Travel | Facilitation de l&#39;octroi des visas pour les voyages officiels |
| `1498` | Addition of a special stamp in a passport or other travel document | Ajout d&#39;une estampille spéciale sur le passeport ou un autre titre de voyage |
| `1499` | Addition of an observation in a passport or other travel document | Ajout d’une observation sur un passeport ou un autre titre de voyage |
| `15` | Mobile Devices | Gestion des appareils mobiles d’entreprise |
| `150` | Market Access Single Window | Guichet unique pour l&#39;accès aux marchés |
| `1500` | Certifying true copies of part of a passport or another travel document | Certifier les copies conformes d&#39;une partie d&#39;un passeport ou d&#39;un autre titre de voyage |
| `1501` | Verification of Status / Replacement of Immigration Document | Vérification du statut ou remplacement d&#39;un document d&#39;immigration |
| `1502` | Personnel Security | Service de sécurité aux employés |
| `1503` | Amendments to historical records or valid Temporary Resident documents | Modifications apportées à des dossiers historiques ou à des documents de résident temporaire valides |
| `1504` | Physical Security: Access Control | Sécurité physique: contrôle des accès |
| `1505` | Access to Information Request Services | Services d&#39;accès à l&#39;information |
| `1506` | NFB Archives | ONF Archives |
| `1507` | ATIP Consultative Services | Services consultatifs de l&#39;AIPRP |
| `1508` | Determination of Rehabilitation for criminality or serious criminality | Décision sur la réadaptation dans les cas de criminalité ou de grande criminalité |
| `1509` | ATIP Compliance Services | Services de conformité de l&#39;AIPRP |
| `1510` | Renunciation of Permanent Residency | Renonciation au statut de résident permanent |
| `1511` | Authorization to return to Canada | Autorisation de revenir au Canada |
| `1512` | IRCC Web Validation Portal | Portail de validation Web de l&#39;Immigration, réfugiés et Cittoyeneté Canada |
| `1513` | Global Assistance to Irregular Migrants | Aide mondiale aux migrants irréguliers |
| `1514` | Access to Information | Accès à l’information |
| `1515` | Ice Assistance Emergency Program | Programme d&#39;urgence d&#39;aide liée aux conditions des glaces |
| `1516` | Privacy | Protection des renseignements personnels |
| `1517` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1518` | Responses to queries from Authorized Representatives | Réponses aux questions des représentants |
| `1519` | Earth Observation Data Service | Service de données d&#39;observation de la Terre |
| `152` | Canada Brand | Guichet unique pour l&#39;accès aux marchés - Marque Canada |
| `1520` | Global Skills Strategy - Work Permit Application | Stratégie en matière de compétences mondiales - Demande de Permis de travail |
| `1521` | Canadian Hazards Information Service (Targeted) | Service canadien d&#39;information sur les risques (ciblé) |
| `1522` | Canadian Spatial Reference System | Système canadien de référence spatiale |
| `1523` | Atlantic Immigration Pilot - Application for Permanent Residence | Programme pilote d&#39;immigration au Canada atlantique - Demande de résidence permanente |
| `1524` | Canadian Wildland Fire Information System | Système canadien d&#39;information sur les feux de végétation |
| `1525` | Flight Operations | Operations Aériennes |
| `1526` | Public Screenings | Projections publiques |
| `1527` | Case Management | Gestion de cas |
| `1528` | Media Enquiries | Demandes des médias |
| `1529` | Media Enquiries | Demandes des médias |
| `153` | Access to Information and Privacy | L&#39;accès à l&#39;information et de la protection des renseignements personnels |
| `1530` | Industry Advisory Service / Northern Projects Management Office (NPMO) | Soutien de l&#39;industrie / Le Bureau de gestion des projets nordiques (BGPN) |
| `1531` | Social media responses to public enquiries | Réponses aux demandes de renseignements publiques dans les médias sociaux |
| `1532` | Funds to Support Education and Training for Veterans | Fonds pour appuyer les études et la formation des vétérans |
| `1533` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `1534` | Social Media Responses to Public Enquiries | Réponses aux demandes de renseignements publiques dans les médias sociaux |
| `1535` | Contribution Program for the Centre of Excellence for the Marine Transportation | Programme de contribution au Centre d’excellence pour le transport maritime des hydrocarbures et de gaz naturel liquéfié (GNL) |
| `1536` | Community Participation Funding Program | Programme de financement de la participation communautaire |
| `1537` | Program to Protect Canada&#39;s Coastlines and Waterways | Programme de protection du littoral et des voies navigables du Canada |
| `1538` | Building Canada Fund (Infrastructure Canada Program - TC manages agreements on b | Fonds Chantiers Canada (programme d&#39;Infrastructure Canada - TC gère des ententes pour le compte d&#39;Infrastructure Canada) |
| `1539` | Canada Strategic Infrastructure Fund (Infrastructure Canada Program - TC manages | Fonds canadien sur l&#39;infrastructure stratégique (programme d&#39;Infrastructure Canada - TC gère des ententes pour le compte d&#39;Infrastructure Canada) |
| `154` | Dairy Processing Investment Fund | Fonds d&#39;investissement dans la transformation des produits laitiers |
| `1540` | Border Infrastructure Fund (Infrastructure Canada Program - TC manages agreement | Fonds sur l&#39;infrastructure frontalière (programme d&#39;Infrastructure Canada - TC gère des ententes pour le compte d&#39;Infrastructure Canada) |
| `1541` | Gateways and Border Crossings Fund | Fonds pour les portes d&#39;entrée et les passages frontaliers |
| `1542` | Asia-Pacific Gateway and Corridor Transportation Infrastructure Fund | Fonds d&#39;infrastructure de transport de l&#39;Initiative de la Porte et du Corridor de l&#39;Asie-Pacifique |
| `1543` | National Trade Corridors Fund | Fonds national des corridors commerciaux |
| `1544` | Enforcement of Private Buoy Regulations for privately owned floating information | Règlement sur les bouées privées pour les balises d&#39;information flottantes appartenant à des particuliers en vertu de la Loi de 2001 sur la marine marchande du Canada. |
| `1545` | Receiver of Wreck Program under the Canada Shipping Act 2001 | Programme des receveur d&#39;épaves en vertu de la Loi de 2001 sur la marine marchande du Canada |
| `1546` | Management of exemptions of prohibited activities on navigable waterways | Gestion des exemption en lien avec des activités interdites sur les eaux navigables |
| `1547` | National Science Library | Bibliothèque scientifique nationale |
| `1548` | International Events and Convention Services Program (IECSP) | Programme des services aux événements internationaux et aux congrès (PSEIC) |
| `1549` | Federal Science Libraries Network (FSLN) | Réseau des bibliothèques scientifiques fédérales (RBSF) |
| `155` | CSC National Victim Services Program | Programme national de services aux victims du SCC |
| `1550` | Access to Information and Privacy Acts | Lois sur l&#39;accès à l&#39;information et la protection des renseignements personnels |
| `1551` | Technical Services | Services techniques |
| `1552` | Research Services | Services de recherches |
| `1553` | Codes Canada | Codes Canada |
| `1554` | Canada&#39;s official time | Heure officielle du Canada |
| `1555` | Instrument Calibration Services | Services d&#39;étalonnage d&#39;instruments |
| `1556` | Calibration laboratory assessment service | Service d&#39;évaluation des laboratoires d&#39;étalonnage |
| `1557` | Certified Reference Materials | Matériaux de référence certifiés |
| `1558` | IRAP Advisory Services to Firms | Services consultatifs du PARI aux entreprises |
| `156` | Dairy Farm Investment Program Producers | Programme d&#39;investissement pour fermes laitières |
| `1560` | IRAP Advisory Services through Contributions to Organizations | Services-conseils du PARI - contributions aux organismes |
| `1561` | Legal Advice, Counsel, and Representation for Veterans | Avis, conseils et représentation juridiques destinés aux vétérans |
| `1562` | Operating a federal railway | Exploitation d&#39;un chemin de fer fédéral |
| `1563` | Conduct outreach and training sessions for other government departments and Indi | Organiser des séances de sensibilisation et de formation pour les autres ministères et les entreprises autochtones. |
| `1564` | Rail Safety Improvement Program (RSIP) | Programme d&#39;amélioration de la sécurité ferroviaire (PASF) |
| `1565` | Rail security | Sûreté du transport ferroviaire |
| `1566` | Child car seat safety | Sécurité des sièges d&#39;auto pour enfants |
| `1567` | Defects and recalls of vehicles, tires and child car seats | Défauts et rappels de véhicules, de pneus et de sièges d&#39;auto pour enfants |
| `1568` | Driver Assistance Technologies | Technologies d&#39;aide à la conduite |
| `1569` | Safety standards for vehicles, tires and child car seats | Normes de sécurité pour véhicules, pneus et sièges d&#39;auto pour enfants |
| `157` | Access to Information and Privacy | Accès à l’information et de protection des renseignements personnels |
| `1570` | Stay safe when driving | Conduire en toute sécurité |
| `1571` | School bus safety activities | Activités de sécurité des autobus scolaires |
| `1572` | Vehicle Importation to and Manufacturing in Canada | Importation et fabrication de véhicules au Canada |
| `1573` | Innovative technologies | Technologies novatrices |
| `1574` | Motor Carriers, Commercial Vehicles and Drivers | Exigences pour véhicules utilitaires, transporteurs routiers et les conducteurs |
| `1575` | Research and testing on vehicles and child car seats | Sièges d&#39;auto pour enfant et véhicules : Recherche et mise à l&#39;essai |
| `1576` | Media Enquiries | Demandes des médias |
| `1577` | Road security | Sûreté routière |
| `1578` | Public Enquiries | Renseignements au public |
| `1579` | Road Safety Transfer Payment Program | Programme de paiement de transfert de sécurité routière |
| `158` | AgriAssurance: Small and Medium-sized Enterprise | Programme Agri-assurance : Volet Petites et moyennes entreprises |
| `1580` | Transportation of Dangerous Goods Program | Le programme du Transport des marchandises dangereuses |
| `1581` | Approval of Emergency Response Assistance Plans (ERAP) | l&#39;agrément des plans d&#39;intervention d&#39;urgence (PIU) |
| `1582` | CANUTEC - Canadian Transport Emergency Centre | CANUTEC - Centre canadien d&#39;urgence transport |
| `1583` | Major Project Management Office Tracker | Suivi des projets du Bureau de gestion des grands projets |
| `1584` | Airport Capital Assistance Program (ACAP) | Programme d&#39;aide aux immobilisations aéroportuaires |
| `1585` | Airport Operations and Maintenance Subsidy Program | Programme de subvention à l&#39;exploitation et à l&#39;entretien des aéroports |
| `1586` | Allowances to former employees of Newfoundland Railways, Steamships and Telecomm | Allocations aux anciens employés des services des chemins de fer, des navires à vapeur et des télécommunications de Terre-Neuve mutés aux Chemins de fer nationaux du Canada |
| `1587` | Ferry Services Contribution Program | Programme de contribution pour les services de traversier |
| `1588` | Issuance of Kimberley Process certificates for the export of rough diamonds | Délivrance des certificats du Processus de Kimberley pour l&#39;exportation des diamants bruts |
| `1589` | Grant to the Province of British Columbia in respect of the provision of ferry a | Subvention à la province de la Colombie-Britannique à l&#39;égard de la prestation de services de traversier et de cabotage pour marchandises et voyageurs |
| `1590` | Labrador Coastal Airstrips Restoration Program | Programme de réfection des bandes d&#39;atterrissage de la côte du Labrador |
| `1591` | Northumberland Strait Crossing subsidy payment under the Northumberland Strait C | Paiement de subvention pour l&#39;ouvrage de franchissement du détroit de Northumberland selon la Loi sur l&#39;ouvrage de franchissement du détroit de Northumberland (législatif). |
| `1592` | Outaouais Road Development Agreement | Entente d&#39;aménagement des routes de l&#39;Outaouais |
| `1593` | Payments to the Canadian National Railway Company in respect of the termination | Versements à la Compagnie des chemins de fer nationaux du Canada (CN) à la suite de l’abolition des péages sur le pont Victoria à Montréal et pour la réfection de la voie de circulation du pont (législatif) |
| `1594` | Ports Asset Transfer Program | Programme de transfert des installations portuaires |
| `1595` | Transportation Association of Canada | Association des transports du Canada |
| `1596` | Remote Passenger Rail Program | Programme de contributions pour les services ferroviaires voyageurs |
| `1597` | Media Enquiries | Demandes des médias |
| `1598` | Aircraft Parking | Stationnement des aéronefs |
| `1599` | Farm Products Council of Canada Reports and Publications | Rapports et publications du Conseil des produits agricoles du Canada |
| `16` | Videoconferencing | Vidéoconférence |
| `160` | Information Services | Services d&#39;information |
| `1600` | Vehicle Parking | Stationnement des véhicules |
| `1601` | Creation and distribution of Farm Products Council of Canada&#39;s Focus newsletter | Création et distribution du bulletin Focus du Conseil des produits agricoles du Canada |
| `1602` | General Terminal: Domestic and International | Accès à l&#39;aérogare : Vols intérieurs et internationaux |
| `1603` | Aircraft Landing – Domestic, International and Flying Training | Atterrissage d&#39;avions – Vols intérieurs, internationaux et instruction de vol |
| `1604` | Emergency Response Services Outside Normal Operating hours | Services d&#39;intervention d&#39;urgence en dehors des heures normales de service |
| `1605` | Annual Mobile Equipment Registration | L&#39;enregistrement annuelle d&#39;équipement mobile |
| `1606` | Management of obstructions to navigation | Gestion des obstacles à la navigation |
| `1607` | Harbour Dues | Service de port |
| `1608` | Approval of ‘works&#39; on Canada&#39;s navigable waterways under the Canadian Navigable | Approbation d&#39;ouvrages sur les voies navigables du Canada en vertu de la Loi sur la protection de la navigation. |
| `1609` | Marine security | Sûreté maritime |
| `161` | AgriDiversity | Programme Agri-diversité |
| `1610` | Marine accidents and investigations | Accidents maritimes et enquêtes |
| `1611` | Marine pollution and environmental response | Pollution marine et intervention environnementale |
| `1612` | Vessel design, construction and maintenance | Conception, construction et entretien des bâtiments |
| `1613` | Public Ports - Berthage | Service d&#39;amarrage |
| `1614` | Vessel licensing and registration | Permis et immatriculation des bateaux |
| `1615` | Public Ports - Storage | Service d&#39;entreposage |
| `1616` | Boating Safety Contribution Program | Programme de contributions pour la sécurité nautique |
| `1617` | Incident Management &amp; Response (Coast Guard reports, Duty Officer, PNR Arctic mo | Urgences maritimes |
| `1618` | Public Ports - Utilities and Other Services | Services publics et autres services |
| `1619` | Public Ports - Wharfage &amp; Transfer | Service de quayage et de transfert |
| `162` | Indigenous Agriculture and Food Systems Initiative | Initiative sur les systèmes agricoles et alimentaires autochtones |
| `1620` | Vessel inspection and certification | Inspection et certification des bâtiments |
| `1621` | Program to Advance Transportation Innovation: Program to Advance Connectivity an | Programme de promotion de l&#39;innovation en matière de transport : Programme de promotion de la connectivité et l&#39;automatisation du système de transports |
| `1622` | Marine training and certification of individuals | Formation et certification maritime |
| `1623` | Innovative Solutions Canada | Solutions Innovatrices Canada |
| `1624` | Program to Advance Indigenous Reconciliation | Programme visant à favoriser la réconciliation avec les peuples autochtones |
| `1625` | Transport Canada Situation Centre | Centre d&#39;intervention de Transports Canada |
| `1626` | Enforce the Coasting Trade Act - Penalties and Periods of Sanction | Application de la loi sur le cabotage - Sanctions et périodes de sanction |
| `1627` | Respond to designation requests by Canadian airlines | Répondre aux demandes de désignation des lignes aériennes canadiennes |
| `1628` | Financial Recognition for Veterans&#39; Caregivers | Reconnaissance financière pour les aidants de vétérans |
| `1629` | Ministerial and Deputy Correspondance | Correspondance ministérielle et du sous-ministre |
| `163` | Living Laboratories Initiative: Collaborative Program | Initiative des laboratoires vivants : Programme de collaboration |
| `1631` | Grants and Contributions to support the Northern Transportation Adaptation Initi | Subventions et contributions pour soutenir l&#39;initiative d&#39;adaptation du transport dans le nord |
| `1632` | Grants and Contributions to support the Transportation Assets Risk Assessment In | Subventions et contributions pour soutenir l&#39;initiative d&#39;évaluation des risques liés aux actifs de transport |
| `1633` | Veteran Family Program | Programme pour les familles des vétérans |
| `1634` | Grants and Contributions to Support Clean Transportation Initiatives | Subventions et contributions pour soutenir des initiatives de transport propre |
| `1635` | Grant to the International Civil Aviation Organization (ICAO) for Cooperative De | Subvention au Programme de développement coopératif de la sécurité opérationnelle et de maintien de la navigabilité de l&#39;Organisation de l&#39;aviation civile internationale (OACI) |
| `1636` | Payments to other governments or international agencies for the operation and ma | Versements aux autres gouvernements ou organismes internationaux pour l&#39;exploitation et l&#39;entretien des aéroports, des installations de navigation aérienne et des voies aériennes |
| `1637` | Commercial air services | Services aériens commerciaux |
| `1638` | Aircraft airworthiness | Navigabilité des aéronefs |
| `1639` | Provide Environmental Assessment Related Technical Advice | Fournir des conseils techniques connexes à l&#39;évaluation environnementale |
| `164` | AgriMarketing Program: Small and Medium-sized Enterprisers | Programme Agri-marketing : Volet Petites et moyennes entreprises |
| `1640` | Licences for the manufacture, storage and sale of explosives | Licences pour la fabrication, l&#39;entreposage et la vente des explosifs |
| `1641` | Authorization of explosives | Autorisation des explosifs |
| `1642` | Analysis and Certification of Explosives | Analyse et certification des explosifs |
| `1643` | National Fireworks Certification Program | Programme national de certification des artificiers |
| `1644` | Control of Explosives Precursor Chemicals (Restricted Components) | Contrôle des précurseurs chimique d’explosifs (composants d’explosif limités) |
| `1645` | Importing, Exporting and Transporting-in-Transit Permits | Permis d&#39;Importation, exportation et transport en transit |
| `1646` | Processing, by an employee of the Department of Transport, of a medical certific | Traitement par un employé du ministère des Transports d&#39;un certificat médical relativement à une licence de pilote ou à un permis de pilote, sauf un permis d&#39;élève-pilote |
| `1647` | Security Screening | Contrôle de sécurité |
| `1648` | Licensing for pilots and personnel | Délivrance de licences pour les pilotes et le personnel |
| `1649` | Registering and leasing aircraft | Immatriculation et location des aéronefs |
| `165` | Dispute Resolution | Règlement des Différends |
| `1650` | Air navigation services | Services de navigation aérienne |
| `1651` | Aviation accidents and investigations | Accidents d&#39;aviation et enquêtes |
| `1652` | Pipeline Arbitration Secretariat | Secrétariat d&#39;arbitrage des pipelines |
| `1653` | ENERGY STAR® Portfolio Manager Energy Benchmarking Tool | Outil d&#39;analyse comparative ENERGY STAR® Portfolio Manager |
| `1654` | Greening Government Services, and Federal Buildings Initiative | Services pour un gouvernement vert et l&#39;Initiative des bâtiments fédéraux |
| `1655` | General operating and flight rules | Règles générales d&#39;utilisation et de vol des aéronefs |
| `1656` | NRCan searchable product list for regulated and ENERGY STAR certified products | List de produts interrogeables de RNCan permettant de rechercher des produits réglementés et certifiés ENERGY STAR |
| `1657` | SmartWay Transportation Partnership | Partenariat de transport SmartWay |
| `1658` | Public enquiries | Demandes du public |
| `1659` | Training of pilots and aviation personnel | Instructeurs de vol et personnel de l&#39;aviation |
| `166` | Rule-Making | Prise de Règlements |
| `1660` | Licensing for aircraft maintenance engineers (AME) | Licences de technicien d&#39;entretien d&#39;aéronefs (TEA) |
| `1661` | Operating airports and aerodromes | Exploitation d&#39;aéroports et d&#39;aérodromes |
| `1662` | Aviation security | Sûreté aérienne |
| `1663` | Drone safety | Sécurité des drones |
| `1664` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1665` | Hangar and Ground Handling | Hangars et services au sol |
| `1666` | Aircraft Services Logistics | Logistique entourant le services des aéronefs |
| `1668` | Aircraft Engineering | Service de génie en aéronautique |
| `1669` | Aircraft Maintenance | Entretien des aéronefs |
| `167` | Determinations and Compliance | Déterminations et Conformité |
| `1670` | NDTCB: General Standards Board certification for non-destructive testing | Organisme de certification nationale en essais non destructifs de Ressources naturelles Canada : certification par l&#39;Office des normes générales du Canada en essais non destructifs |
| `1671` | Canadian Space Agency Class Grants and Contributions Program | Programme global des subventions et contributions de l&#39;Agence spatiale canadienne |
| `1672` | NDTCB: Portable tube-based X-ray fluorescence analyzer operator certification | Organisme de certification nationale en essais non destructifs de Ressources naturelles Canada : certification des opérateurs d&#39;analyseur à fluorescence rayons X à tube à rayons X portatif |
| `1673` | NDTCB: Written examination for the CNSC’s exposure device operator certification | Organisme de certification nationale en essais non destructifs de Ressources naturelles Canada : examen écrit de certification des opérateurs d&#39;appareils d&#39;exposition de la Commission canadienne de sûreté nucléaire |
| `1674` | Canadian Certified Reference Materials Project | Projet canadien des matériaux de référence certifiés |
| `1675` | Transportation Fuels website | Site Web Info-Carburant |
| `1676` | Diesel testing and certification | Essai et certification des moteurs diesel |
| `1677` | The Canadian Astronomy Data Centre (CADC) | Le Centre canadien de données astronomiques (CCDA) |
| `1678` | Grants and Contributions | Subventions et Contributions |
| `1679` | Canadian Impact Assessment Registry | Registre canadien d’évaluation d’impact |
| `168` | Information, Advice and Expertise | Information, Conseils et Expertise |
| `1680` | Physical Security Abroad – Security, Maintenance and Service Line Delivery | Sécurité Physique à l&#39;étranger - Sécurité, Entretien et Service d&#39;Exécution des Projets de ligne |
| `1681` | Engineering Services | Services d&#39;ingénierie |
| `1682` | Capital Project Delivery Services | Services de Réalisation de Projets immobiliers |
| `1683` | Missions Operations | Opérations des missions |
| `1684` | Real Property Transactions Services | Services de transactions immobilières |
| `1685` | International Project Delivery Services | Services internationaux de réalisation de projets |
| `1686` | Professional and Technical Services (e.g. architectural, engineering and interio | Services professionnels et techniques (services d’architecture, d’ingénierie et de design d’intérieur, par exemple) |
| `1688` | International Procurement and Contracting Services | Services internationaux d&#39;approvisionnement et de contrats |
| `1689` | Global Logistics Services | Services logistiques mondiaux |
| `169` | Funding Decisions for Scholarships and Fellowships | Décisions sur le financement des bourses |
| `1690` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `1691` | Grants and Contributions for International Assistance | Subventions et contributions pour l&#39;aide internationale |
| `1693` | Results-based management (RBM) and risk management information sessions provided | Appui fourni aux partenaires potentiels et existants en matière de gestion axée sur les résultats (GAR) et gestion du risque |
| `1694` | Results Based Management (RBM) resources (center of excellence) | Ressources en matière de Gestion axée sur les résultats (GAR) |
| `1695` | Canadian sanctions | Sanctions canadiennes |
| `1696` | Export Import Control Systems Support | Prise en charge des Systèmes des contrôles à l&#39;exportation et à l&#39;importation |
| `1697` | Jules Léger Library | Bibliothèque Jules-Léger |
| `1698` | Export and Import Permit Service | Service des licences d&#39;exportation et d&#39;importation |
| `1699` | Authentication of documents | Authentification des documents |
| `17` | Contact Centre | Centre de contact |
| `170` | Receiving Financial Transaction Reports | Réception de déclaration d&#39;opérations financières |
| `1700` | Intelligence Surveillance Reconnaissance | Renseignement, surveillance et reconnaissance |
| `1701` | Aircraft Operations and Maintenance Training | Formation sur les opérations et l&#39;entretien des aéronefs |
| `1702` | Parliamentary Affairs | Relations avec le Parlement |
| `1703` | Ministerial non-GIC appointments and GIC non-diplomatic appointments | Nominations ministérielles non effectuées par le gouverneur en conseil et nominations non diplomatiques effectuées par le gouverneur en conseil |
| `1704` | Strategic Governance, Ministerial Correspondence | Gouvernance stratégique, Correspondance ministérielle |
| `1705` | Corporate and common service management and delivery for DM and MIN offices | Services corporatif et services communs livré aux bureaux des ministres et des sous-ministres |
| `1706` | Access to Information and Privacy (ATIP) | Accès à l&#39;information et la protection des renseignements personnels |
| `1707` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1708` | Geo.ca | Geo.ca |
| `1709` | National Air Photo Library | Photothèque nationale de l&#39;air |
| `171` | Disclosures of Financial Intelligence | Communications de renseignements financiers |
| `1710` | Environmental Assessment done by Review Panels | Évaluation environnementale par une commission d&#39;examen |
| `1711` | Open Science &amp; Technology Repository (OSTR) | Dépôt ouvert des sciences &amp; technologies (DOST) |
| `1712` | Natural Resources Canada Library | Bibliothèque de Ressources naturelles Canada |
| `1713` | David Florida Laboratory: Spacecraft assembly, integration and testing centre | Laboratoire David-Florida : Centre d&#39;intégration, d&#39;assemblage et d&#39;essai d&#39;engins spatiaux |
| `1714` | Environmental Assessment done by the Agency | Évaluations environnementales réalisées par l&#39;Agence |
| `1715` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `1716` | ecoENERGY for Housing - Enquiries | écoÉNERGIE pour l&#39;habitation – Demandes de renseignements |
| `1717` | Access to Information and Privacy | Accès à l&#39;information et la protection des renseignements personnels |
| `1718` | Environmental Assessment done by Substitution | Évaluation environnementale par substitution |
| `1719` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `172` | Enquiries for Reporting Entities | Demandes de renseignements d&#39;entités déclarantes |
| `1720` | Request for assistance for outbreak or Federal public health surge support(s) | Demande d&#39;assistance pour de l&#39;aide en cas d&#39;éclosion ou la poussée fédérale de la santé soutient |
| `1721` | Respond to Correspondence Addressed to the Minister | Répondre aux correspondances adressées au ministre |
| `1722` | Respond to Correspondence Addressed to the President | Répondre aux correspondances adressées au président |
| `1724` | Jacob Finkelman Library | Bibliothèque Jacob Finkelman |
| `1725` | Social Security Tribunal Secretariat Call Centre | Centre d&#39;appels du secrétariat du Tribunal de la sécurité sociale |
| `1726` | Financial Literacy | Littératie financière |
| `1728` | Access to information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1729` | Federal On-Reserve School Operations and Funding | Financement et fonctionnement des écoles fédérales dans les réserves |
| `173` | Funding Decisions for Scholarships and Fellowships | Décisions sur le financement des bourses |
| `1731` | Enterprise Information and Records Management | Gestion des archives et de l&#39;information de l&#39;entreprise |
| `1732` | Personnel Security | Service de sécurité aux employés |
| `1733` | Physical Security: Access Control | Sécurité physique: contrôle des accès |
| `1734` | Departmental Library | Bibliothèque ministérielle |
| `1735` | Enterprise Information and Records Management (EIRM) | Gestion des archives et de l&#39;information de l&#39;entreprise (GAIE) |
| `1736` | Public Enquiries | Renseignements au public |
| `1737` | Aboriginal Aquatic Resource &amp; Ocean Management Contribution Agreements | Ententes de contribution du Programme autochtone de gestion des ressources aquatiques et océaniques |
| `1738` | Aboriginal Fisheries Strategy Food, Social and Ceremonial (FSC) Contribution Agr | Accords de contribution relatifs aux pêches autochtones à des fins alimentaires, sociales et rituelles (ASR) dans le cadre de la Stratégie relative aux pêches autochtones |
| `1739` | Aboriginal Fund for Species at Risk Contribution Agreements | Ententes de contribution des Fonds autochtones pour les espèces en péril (FAEP) |
| `1740` | Atlantic Integrated Fisheries Initiative Contribution Agreements | Ententes de contribution de l&#39;Initiative des pêches commerciales intégrées de l&#39;Atlantique (IPCIA) |
| `1741` | Access to information | Accès à l&#39;information |
| `1742` | Global oceanographic in situational data from the Global Telecommunication Syste | Données océanographiques dans situational mondiales du Système mondial de télécommunications |
| `1744` | Lake Ontario and St. Lawrence River water levels | Niveaux d&#39;eau du Lac Ontario et du fleuve Saint-Laurent |
| `1745` | Marine Environmental Data Section (MEDS) | Section des données sur le milieu marin |
| `1746` | Ministerial Correspondence | Correspondence ministerielle |
| `1747` | Nautical Charts and Publications | Cartes marines et services |
| `1748` | Northern Integrated Fisheries Initiative Contribution Agreements | Ententes de contribution de l&#39;InitiativeInitiative des pêches commerciales intégrées du Nord (IPCIN) |
| `1749` | Pacific Integrated Commercial Fisheries Initiative Contribution Agreements | Ententes de contribution de l’Initiative de pêche commerciale intégrée du Pacifique (IPCIP) |
| `1750` | Tides, Currents and Water Levels (CHS) | Marées, courants et niveaux d&#39;eau (SHC) |
| `1751` | Provide funding to First Nations for transfers of band moneys | Fournir des fonds aux Premières nations pour les transferts d&#39;argent de la bande |
| `1752` | Indian Moneys Expenditure Requests | Demandes de dépenses d&#39;argent des Indiens |
| `1753` | Living Estates: Individual trust account payout requests | Biens des personnes vivantes: Demandes de paiement d&#39;un compte individuel en fiducie |
| `1754` | Estates Management | Gestion des successions |
| `1755` | Band Support Funding | Financement du soutien des bandes |
| `1756` | Tribal Council Funding | Financement des conseils tribaux |
| `1757` | Employee Benefits | Avantages sociaux des employés |
| `1758` | Professional and Institutional Development | Dévelopement professionnel et institutionnel |
| `1759` | Emergency Management, Crisis &amp; Strategic Communications: First Nations Emergency Management Funding | Gestion des urgences, communications de crise et stratégiques : Financement de la gestion des urgences des Premières Nations |
| `1760` | On-Reserve Education Facilities Funding | Fonds d&#39;installations d&#39;enseignement pour les collectivités dans les réserves |
| `1761` | On-Reserve Education Facilities Policy and Technical Support | Politique et soutien technique en matière d&#39;installations d&#39;enseignement pour les collectivités dans les réserves |
| `1763` | On-Reserve Education Facilities Capacity Building | Renforcement des capacités pour les installations d&#39;enseignement pour les collectivités dans les réserves |
| `1764` | On-Reserve Water and Wastewater | L&#39;eau et les eaux usées dans les réserves |
| `1765` | On-Reserve Other Community Infrastructure Policy and Technical Support | Politique et soutien technique en matière d&#39;autres infrastructures communautaires pour les collectivités dans les réserves |
| `1766` | On-Reserve Water and Wastewater Infrastructure Capacity Building | Renforcement des capacités pour les Infrastructure d&#39;approvisionemet en eau et des eaux usées dans les réserves. |
| `1767` | On-Reserve Housing: Funding, Policy and Technical Support, and Capacity Building | Fonds d&#39;infrastructure du logement dans: le financement, soutien politique et technique, et renforcement des capacités |
| `1768` | On-Reserve Housing Policy and Technical Support | Politique de logement dans les réserves et soutien technique |
| `1769` | On-Reserve Housing Capacity Building | Renforcement des capacités en matière de logement dans les réserves |
| `1770` | On-Reserve Other Community Infrastructure Funding | Fonds d&#39;autres infrastructures communautaires pour les collectivités dans les réserves |
| `1771` | On-Reserve Water and Wastewater Infrastructure Policy and Technical Support | Politique et soutien technique en Matière d&#39;infrastructure d&#39;approvisionnement en eau et d&#39;assainissement des réserves |
| `1772` | Gas Tax Fund (GTF) | Fonds de la taxe sur l&#39;essence (FTE) |
| `1773` | New Building Canada Fund – Provincial-Territorial Infrastructure Component – Nat | Nouveau Fonds Chantiers Canada – volet Infrastructures provinciales-territoriales – Projets nationaux et régionaux (VIPT-PNR) |
| `1774` | New Building Canada Fund – Provincial-Territorial Infrastructure Component – Sma | Nouveau Fonds Chantiers Canada – volet Infrastructures provinciales-territoriales – Fonds des petites collectivités (VIPT-FPC) |
| `1775` | Public Transit Infrastructure Fund (PTIF) | Fonds pour l&#39;infrastructure de transport en commun (FITC) |
| `1776` | Clean Water and Wastewater Fund (CWWF) | Fonds pour l&#39;eau potable et le traitement des eaux usées (FEPTEU) |
| `1777` | Investing in Canada Infrastructure Program (ICIP) | Programme d&#39;infrastructure investir dans le Canada (PIIC) |
| `1778` | Supplementary Health Benefits - Direct Service Delivery | Prestations de santé supplémentaires – Prestation directe de services. |
| `1779` | Disaster Mitigation and Adaption Fund (DMAF) | Fonds d&#39;atténuation et d&#39;adaptation en matière de catastrophes (FAAC) |
| `178` | Funding Decisions for Grants to Researchers | Décisions sur le financement des subventions de recherche |
| `1780` | Municipal Asset Management Program (MAMP) | Programme de gestion des actifs municipaux (PGAM) |
| `1781` | Municipalities for Climate Innovation Program (MCIP) | Programme Municipalités pour l&#39;innovation climatique (PMIC) |
| `1782` | Smart Cities Challenge (SCC) | Défi des villes intelligentes |
| `1783` | Supplementary Health Benefits- Funding | Prestations de santé supplémentaires – Prestation directe de services. |
| `1784` | Ministerial and Deputy Correspondance | Correspondance ministérielle et du sous-ministre |
| `1785` | Access to Information and Privacy (ATIP) | Accès à l&#39;information et protection des renseignements personnels (AIPRP) |
| `1786` | Primary Health Care: Clinical and Client Care - Direct Service Delivery | Soins de santé primaires : soins cliniques et soins aux clients – prestation de services directe |
| `1789` | Media Enquiries | Relations des médias |
| `1790` | Public Enquiries | Requêtes du public |
| `1791` | Primary Health Care: Clinical and Client Care - Funding | Soins de santé primaires : soins cliniques et soins aux clients – Financement |
| `1792` | FSWEP; Inventory of student employment opportunities in Public Service | Programme fédéral d&#39;expérience de travail étudiant: Répertoire des possibilités d&#39;emploi pour étudiants dans la fonction publique |
| `1793` | Research Affiliate Program (RAP); Job opportunities for post-secondary students | Programme des adjoints de recherche: Offres d&#39;emploi pour les étudiants de niveau postsecondaire |
| `1794` | PSR; Job opportunities for college and university graduates | Programme de recrutement postsecondaire: Possibilités d&#39;emploi pour les diplômés des collèges et des universités |
| `1795` | Home and Long-Term Care: Home &amp; Community Care - Direct Service Delivery | Soins à domicile et de longue durée : Soins à domicile et en milieu communautaire – Prestation directe de services |
| `1796` | Recruitment of Policy Leaders (RPL); Job opportunities for professionals, academics and scientist | Recrutement de leaders en politiques: Opportunités d&#39;emplois pour les professionnels, diplômés universitaires et les scientifiques |
| `1797` | Home and Long-Term Care: Home and Community Care - Funding | Soins à domicile et de longue durée : Soins à domicile et en milieu communautaire – – Financement |
| `1798` | Primary Health Care: Community Oral Health Services - Direct Service Delivery | Soins de santé primaires : Services communautaires de santé bucco-dentaire – Prestation directe de services |
| `1799` | Primary Health Care: Community Oral Health Services - Funding | Soins de santé primaires : Services communautaires de santé bucco-dentaire – Financement |
| `18` | Learning Services ; access to the School&#39;s learning products | Services d&#39;apprentissage; accès aux produits d&#39;apprentissage de l&#39;école |
| `1800` | Public Health Promotion and Disease Prevention Direct Service Delivery | Prestation directe de services de promotion de la santé publique et de prévention des maladies |
| `1801` | Public Health Promotion and Disease Prevention Services Funding | Financement des services de promotion de la santé publique et de prévention des maladies |
| `1802` | Public Health Protection and Disease Prevention: Environmental Public Health - Direct Service Delivery | Protection de la santé publique et prévention des maladies : Hygiène du milieu - Prestation directe de services |
| `1803` | Public Health Protection and Disease Prevention: Environmental Public Health - Funding | Protection de la santé publique et prévention des maladies : Hygiène du milieu -Financement |
| `1804` | Jordan&#39;s Principle: Direct Service Delivery | Principe de Jordan: Prestation directe de services |
| `1805` | Jordan&#39;s Principle: Funds for Coordination under Canadian Human Rights Tribunal (CHRT 41) | Principe de Jordan :Fonds de coordination pour le Tribunal canadien des droits de la personne (TCDP 41) |
| `1806` | Public Health Promotion and Disease Prevention: Mental Wellness - Funding | Promotion de la santé publique et prévention des maladies: Bien-être mental – Financement |
| `1807` | Public Health Promotion and Disease Prevention: Healthy Child Development - Funding | Promotion de la santé publique et prévention des maladies : développement sain des enfants - Financement |
| `1808` | Public Health Promotion and Disease Prevention: Healthy Living - Funding | Promotion de la santé publique et prévention des maladies: Modes de vie sains - financement |
| `1809` | Public Health Promotion and Disease Prevention: Communicable Disease Control and Management - Funding | Promotion et prévention des maladies : Contrôle et gestion des maladies transmissibles - Financement |
| `1810` | Health Systems Support: Health Human Resources - Funding | Soutien aux systèmes de santé : Ressources humaines en santé – Financement |
| `1811` | Community Infrastructure: Health Facilities-Funding | Financement-Infrastructure communautaire : Établissements de santé |
| `1812` | Primary Health Care : eHealth Infostructure - Funding | Soins de santé primaires : Infostructure de cybersanté - Financement |
| `1813` | Health Systems Support: Health Planning, Quality Management and Systems Integration - Funding | Soutien aux systèmes de santé : planification des soins de santé, gestion de la qualité et intégration des systèmes - Financement |
| `1814` | Health Systems Support: British Columbia Tripartite and Health Systems Transformations - Funding | Soutien aux systèmes de santé : transformations tripartites et des systèmes de santé de la Colombie-Britannique – Financement |
| `1817` | Logistical services for FPT Conferences | Service de Logistique pour conférences FPT |
| `1818` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1821` | Access to information and privacy requests | Accès à l&#39;information et protection des renseignements personnels |
| `1822` | Public and media enquiries | Demandes de renseignements du public et des médias |
| `1823` | Investigate Federal Offender Concerns | Enquêter sur les préoccupations des délinquants fédéraux |
| `1824` | Access to Information and Privacy | Demande de d&#39;accès à l&#39;information et aux renseignements personnels |
| `1825` | Public and Media Enquiries | Demandes du publique et des médias |
| `1827` | Building Canada Fund - Major Infrastructure Component (BCF-MIC) | Fonds Chantiers Canada - Volet Grandes Infrastructures (FCC-VGI) |
| `1828` | New Building Canada Fund (NBCF) - National Infrastructure Component (NIC) | Nouveau Fonds Chantiers Canada (NFCC) - Volet Infrastructures Nationales (VIN) |
| `1829` | Green Infrastructure Fund (GIF) | Fonds d&#39;infrastructure verte (FIV) |
| `1830` | Toronto Waterfront Revitalization Initiative (TWRI) | Infrastructure Canada et l&#39;Initiative de revitalisation du secteur riverain de Toronto |
| `1831` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1832` | SECURITAS | SECURITAS |
| `1833` | Independent safety investigations | Enquêtes indépendantes de sécurité |
| `1834` | Smart Cities Community Support Program | Programme de soutien aux collectivités sur les villes intelligentes |
| `1835` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1836` | Evaluation Services and Learning Division | Direction des services à l’évaluation et de l’apprentissage |
| `1837` | Canada Periodical Fund - Aid to Publishers - Magazines | Fonds du Canada pour les périodiques - Aide aux éditeurs - magazines |
| `1839` | Evaluation Division | Division de l&#39;évaluation |
| `1840` | Canadian economic sanctions | Sanctions économiques canadiennes |
| `1844` | Public Opinion Research Report (PORR) | Rapports de recherches sur l&#39;opinion publique (RROP) |
| `1845` | Disposition Authorizations | Autorisations de disposition |
| `1848` | International Standard Book Number - ISBN | Numéro international normalisé du livre - ISBN |
| `1849` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1850` | International Standard Music Number - ISMN | Numéro international normalisé de la musique - ISMN |
| `1851` | International Standard Serial Number - ISSN | Numéro international normalisé des publications en série - ISSN |
| `1854` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `1855` | Travel Information Program | Programme de renseignements aux voyageurs |
| `1856` | Consular Assistance and Services for Canadians Abroad | Assistance consulaire et services pour les Canadiens à l&#39;étranger |
| `1857` | International trade and investment | Commerce international et investissements |
| `1858` | Importing into Canada | Importation au Canada |
| `1859` | International innovation | Innovation de portée internationale |
| `1860` | Trade Commissioner Service | Service des délégués commerciaux |
| `1861` | Canadian Technology Accelerators | Accélérateurs technologiques canadiens |
| `1862` | Public Enquiries | Demande d&#39;informations parvenant du public |
| `1863` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `1866` | Law Enforcement Records Checks | Vérification des dossiers policiers |
| `1867` | Copy Services | Services de copies |
| `1868` | Documentary Heritage Communities Program - DHCP | Programme pour les collectivités du patrimoine documentaire - PCPD |
| `1869` | Reference | Référence |
| `1870` | Ship Sanitation Inspections | Inspections sanitaires de navire |
| `1871` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `1872` | Canadian Firearms Program (CFP) - Support to Law Enforcement | Programme canadien des armes à feu (PCAF) - Aide aux forces de l&#39;ordre |
| `1873` | Canadian Firearms Program (CFP) - Firearms Registration | Programme canadien des armes à feu (PCAF) - Enregistrement des armes à feu |
| `1874` | ATIP | AIPRP |
| `1875` | Canada&#39;s National Do Not Call List | Liste nationale de numéros de télécommunication exclus du Canada |
| `1876` | Voter Contact Registry | Registre de communication avec les élécteurs |
| `1877` | Payment of judges&#39; salaries and allowance claims | Paiement des salaires et indemnités des juges |
| `1879` | Administration of the federal judicial appointment process | Administration du processus de nomination des juges fédérale |
| `1880` | Judges&#39; Language Training | Formation linguistique des juges |
| `1881` | Federal Courts Reports | Recueil des décisions des Cours fédérales |
| `1882` | Review judges&#39; conduct complaints | Examiner les plaintes relatives à la conduite des juges |
| `1884` | Accreditation services for events | Services d&#39;accreditation pour les événements |
| `1885` | Event logistical services for media | Services logistiques pour les média lors d&#39;événements |
| `1886` | Ex gratia compensation program for events | Programme d&#39;indemnisation à titre gracieux lors d&#39;événements |
| `1887` | Client Services | Services à la clientèle |
| `1888` | Women Entrepreneurship Fund | Fonds pour les femmes en entrepreneuriat |
| `1889` | Administration of JUDICOM | Administration de JUDICOM |
| `1892` | Application for Record Suspension | Demande de suspension du casier |
| `1893` | Application for Clemency | Demande de clémence |
| `1894` | Decision Registry Requests | Demande d&#39;accès au Registre des décisions |
| `1895` | Request to Attend a Hearing | Demande pour assister à une audience |
| `1896` | Access to Information Requests | Demande d&#39;accès à l&#39;information |
| `1897` | Services for Victims: Providing information and registration services to victims | Services aux victimes : Prestation de services d’information et d’inscription aux victimes |
| `1898` | Services for Victims: Providing Audio Recordings to Registered Victims | Services aux victimes : Accès aux enregistrements sonores par les victimes inscrites |
| `1899` | Victims Complaints Mechanism | Mécanisme de plainte des victimes |
| `19` | Enterprise Requested Delivery | Demandes de livraison en organisation |
| `1900` | Application for Expungement | Demande de radiation |
| `1901` | Canada Book Fund - Support for Publishers- Business Development | Fonds du livre du Canada - Soutien aux éditeurs - développement des entreprises |
| `1902` | Creative Export Canada | Exporation créative Canada |
| `1903` | Canada Music Fund | Fonds de la musique du Canada |
| `1904` | Canadian Film or Video Production Tax Credit | Crédit d&#39;impôt pour production cinématographique ou magnétoscopique canadienne |
| `1905` | Film or Video Production Services Tax Credit | Crédit d&#39;impôt pour services de production cinématographique ou magnétoscopique |
| `1906` | Canada Arts Training Fund | Fonds du Canada pour la formation dans le secteur des arts |
| `1907` | Canada Cultural Investment Fund - Strategic Initiatives | Fonds du Canada pour l&#39;investissement en culture - Initiatives stratégiques |
| `1908` | Canada Arts Presentation Fund - Professional Arts Festivals and Performing Arts Series Presenters | Fonds du Canada pour la présentation des arts - Festivals artistiques et diffuseurs de saisons de spectacles professionnels |
| `1909` | Canada Cultural Spaces Fund | Fonds du Canada pour les espaces culturels |
| `1910` | Celebration and Commemoration - Celebrate Canada | Célébrations et commémorations - Le Canada en fête |
| `1911` | Museums Assistance - Access to Heritage | Aide aux musées - Accès au patrimoine |
| `1912` | Building Communities through Arts and Heritage - Local Festivals | Développement des communautés par le biais des arts et du patrimoine - Festivals locaux |
| `1913` | Canada History Fund | Fonds pour l’histoire du Canada |
| `1915` | Canadian Conservation Institute and Canadian Heritage Information Network - Conservation Services | Institut canadien de conservation et Réseau canadien d&#39;information sur le patrimoine - Services de conservation |
| `1916` | Canadian Conservation Institute and Canadian Heritage Information Network | Institut canadien de conservation et Réseau canadien d&#39;information sur le patrimoine |
| `1917` | Privacy Act Requests | Demandes en vertu de la Loi sur la protection des renseignements personnels. |
| `1919` | Support and assistance to athletes | Soutien et aide aux athlètes |
| `192` | RCMP- Contract &amp; Indigenous Policing (C &amp; IP) | (GRC) Services de police contractuels et autochtones (SPCA) |
| `1920` | Support for Hosting - Canada Games | Soutien pour l&#39;acceuil - Jeux du Canada |
| `1921` | Sport Support - National Sport Organization | Soutien au sport - Organismes nationaux de sport |
| `1922` | Indigenous Languages and Cultures - Indigenous Languages | Langues et cultures autochtones - Langues autochtones |
| `1923` | Multiculturalism and Anti-Racism Initiatives - Events | Multiculturalisme et la lutte contre le racisme - Événements |
| `1924` | Development of Official-Language Communities – Cooperation with the Community Sector | Développement des communautés de langue officielle - Collaboration avec le secteur communautaire |
| `1925` | Enhancement of Official Languages – Cooperation with the Non-Governmental Sector | Mise en valeur des langues officielles - Collaboration avec le secteur non gouvernemental |
| `1928` | Access to Information requests | Accès à l&#39;information et protection des renseignements personnels |
| `1929` | Privacy Requests | Demandes de protection des renseignements personnels |
| `1931` | Decision Registry: Research Requests | Registre des décisions: Demandes de recherche |
| `1932` | Status Confirmation Service (controlled substances) | Service de confirmation du statut (substances désignées) |
| `1933` | Importation of designated devices | Importation d&#39;instruments désignés |
| `1934` | Pharmacy Referrals to Provincial Regulatory Authorities for situations of non-co | Renvois aux autorités réglementaires provinciales pour les pharmacies en situations de non-conformité |
| `1935` | Referrals to Law Enforcement | Renvois aux organismes d&#39;application de la loi |
| `1936` | Approval of retained controlled substances by law enforcement | Approbation des substances désignées retenues par les organismes d&#39;application de la loi |
| `1937` | Responding to enquiries from law enforcement | Répondre aux demandes des organismes d&#39;application de la loi (Demandes d&#39;état et ordres de production) |
| `1938` | Responding to enquiries from external stakeholders | Répondre aux demandes des parties prenantes externes |
| `1939` | Responding to enquiries from internal stakeholders | Répondre aux demandes des parties prenantes internes |
| `1940` | Pre-Licence Inspection Packages | Trousses d&#39;inspection pré-licence |
| `1941` | Notices of Restriction for Pharmacists and Practitioners | Avis de restriction pour les pharmaciens et practiciens |
| `1942` | Substance Use and Addictions Program | Programme sur l&#39;usage et les dépendances aux substances |
| `1943` | Import-Export Permits | Permis d’importation-exportation |
| `1944` | Issuance of Industrial Hemp Import and Export Permits under the Cannabis Act and | Délivrance des permis d’importation et d’exportation de chanvre industriel en vertu de la Loi sur le cannabis et de ses règlements |
| `1945` | Issuance of licence for Analytical Testing under the Cannabis Act and its Regula | Délivrance de licences d&#39;essais analytiques en vertu de la Loi sur le cannabis et de ses règlements |
| `1946` | Issuance of Cannabis Drug Licences under the Cannabis Act and its Regulations | Délivrance de licences de drogues contenant du cannabis en vertu de la Loi sur le cannabis et de ses règlements |
| `1947` | Industrial Hemp Licences | Licences liée au chanvre industriel |
| `1948` | Issuance of licence for Research under the Cannabis Act and its Regulations | Délivrance de licences de recherche en vertu de la Loi sur le cannabis et de ses règlements |
| `1949` | Exemptions under the Cannabis Act | Exemptions en vertu de la Loi sur le cannabis |
| `195` | Money Services Businesses (MSBs) Registry - Registration | Registre des entreprises de services monétaires (ESM) – Inscription |
| `1950` | Tobacco Control Program - Enquiries and Complaints | Programme de lutte au tabagisme - Demandes et plaintes |
| `1951` | Compliance Promotion Activities | Activité de promotion de la conformité |
| `1952` | Review, assess and action compliance issues related to cannabis and hemp | Examiner, évaluer et traiter les questions de conformité liées au cannabis et au chanvre |
| `1953` | Cannabis Product Recalls | Rappels de produits du cannabis |
| `1954` | Initial Licensing | Octroi de licences initiales |
| `1955` | Renewals and Amendments | Renouvellements et modifications |
| `1956` | Security | Sécurité |
| `1957` | Personal Registration Certificates | Certificats d’inscription personnelle |
| `1958` | Client Services - Call Centre, Cannabis, Correspondence | Services à la clientèle — Centre d’appels, cannabis, correspondance |
| `1959` | Email: cannabis@canada.ca | Le courriel: cannabis@canada.ca |
| `1960` | Cannabis Police Services | Services à la clientèle - Services policiers relatifs au cannabis |
| `1961` | Issuance of Licences for controlled substances and precursor chemicals under the Controlled Drugs and Substances Act and its Regulations (New, Renewal, Amendment) (CSCB) | Délivrance de licences pour des substances réglementées et des précurseurs chimiques en vertu de la loi sur les drogues et les substances réglementées et de ses règlements (nouvelles licences, renouvellements, modifications) (DGSCC) |
| `1962` | Issuance of Import and Export Permits for Controlled Substances and Chemical Precursors under the Controlled Drugs and Substances Act and its Regulations (CSCB) | Délivrance de licences d&#39;importation et d&#39;exportation de substances réglementées et de précurseurs chimiques en vertu de la loi réglementant certaines drogues et autres substances et de son règlement d&#39;application (DGSCC) |
| `1963` | Issuance of Registrations for Class B Precursors | Inscriptions de précurseurs chimiques de catégorie B |
| `1964` | Issuance of Authorization Certificates for Preparations or Mixtures of Class A or Class B Precursors under the Controlled Drugs and Substances Act and its Regulations (CSCB) | Délivrance de certificats d&#39;autorisation pour les préparations ou mélanges de précurseurs de classe A ou B en vertu de la loi réglementant certaines drogues et autres substances et de son règlement d&#39;application (DGSCC) |
| `1965` | Exemptions to conduct research with controlled substances including clinical trials | Exemptions relatives a la recherche incluant les essais cliniques |
| `1966` | Exemptions to operate a supervised consumption site | Exemptions relatives aux sites de consommation supervisée |
| `1967` | Issuance of Test Kit Registrations under the Controlled Drugs and Substances Act and its Regulations | Octroi d&#39;enregistrements de nécessaires d&#39;essai pour les substances désignées |
| `1968` | Investor Services - Government Liaison | To be provided |
| `1969` | Investor Services - Proposals and Information Gathering | To be provided |
| `1970` | Investors Services - Advice and Support | To be provided |
| `1971` | Marketing - Outreach | To be provided |
| `1972` | Communications - Public &amp; Media Inquiries | To be provided |
| `1973` | Honours and Awards | Décorations et citations |
| `1975` | Canadian Centre for Climate Services | Centre canadien des services climatiques |
| `1976` | Process Verification | Vérification des processus |
| `1977` | Licences | Délivrance de licences |
| `1978` | Safe Food for Canadians Licence | Licence relatives à la salubrité des aliments au Canada |
| `1979` | Access to Information Request | Demande d&#39;accès à l&#39;information |
| `1980` | AgriRisk: Microgrants | Initiatives Agri-risques: Microsubventions |
| `1981` | AgriRisk: Research and Development Contribution Funding Stream | Initiatives Agri-risques: Volet de financement par contribution de recherche et développement |
| `1982` | Laboratory Testing | L&#39;analyse de laboratoire |
| `1984` | Agricultural Clean Technology Program: Adoption Stream | Programme des technologies propres en agriculture |
| `1985` | Local Food Infrastructure Fund | Fonds des infrastructures alimentaires locales |
| `1986` | Dairy Direct Payment Program | Programme de paiements directs pour les producteurs laitiers |
| `1987` | Solutions Integration Service | Service d&#39;intégration des solutions |
| `1988` | Responses to Access to Information and Privacy | Réponses aux demandes en vertu de la Loi sur l’accès à l’information ou de la Loi sur la protection des renseignements personnels |
| `1989` | Conferencing Services | Services de conférence |
| `1990` | Statistical, Research and Technical Publications | Publications statistiques, scientifiques et techniques |
| `1991` | Harvest Sample Crop Quality Results (Unofficial Results) | Programme d&#39;échantillons de récolte (résultats non officiels) |
| `1992` | Climate Change Funding Programs - Energy Savings Rebate program | Programme de remises écoénergétiques |
| `1993` | Climate Change Funding Programs - Climate Action Incentive Fund - SME | Fonds d’incitation à l’action pour le climat - PME |
| `1994` | Climate Change Funding Programs - Climate Action Incentive Fund - MUSH | Fonds d’incitation à l’action pour le climat - MUEH |
| `1995` | Public Weather | Météo publique |
| `1996` | Income Replacement Benefit | Prestation de remplacement du revenu |
| `1997` | Authorized Service Providers | Fournisseur de services autorisé |
| `1998` | Provision of Calibration Sets | Ensembles d&#39;étalonnage |
| `1999` | Documentation for Optional Inspection, Quality Assurance or Analytical Testing | Documents visant l&#39;inspection facultative, l&#39;assurance de la qualité ou les services d&#39;analyse |
| `2` | Import Live Animal, Hatching Eggs and Germplasm (Semen and Embryos) | Importation d&#39;animaux vivants, d&#39;oeufs d&#39;incubation et de germoplasme d&#39;animaux |
| `20` | High-performance Computing | Calcul de haute performance |
| `2000` | Certificate Final for Grain | Certificat final de grain |
| `2001` | Official CGC Sealed Sample with Certificate | Échantillon officiel scellé et certificat de la CCG |
| `2002` | Final Quality Determination for Grain Producers | Détermination définitive de la qualité pour les producteurs de grain |
| `2003` | Allocation of Producer Cars | Attribution des wagons de producteurs |
| `2004` | Payment Protection for Grain Producers | Protection du paiement à l&#39;intention des producteurs de grain |
| `2005` | Additional Pain and Suffering Compensation | Indemnité supplémentaire pour douleur et souffrance |
| `2006` | Responses to Public and Media Inquiries | Réponses aux demandes de renseignements du public et des médias |
| `2007` | Ice Warnings, Forecasts and Information | Avertissements, prévisions et informations sur les glaces |
| `2008` | State funeral | Funérailles d&#39;État |
| `2009` | Atmospheric Data and Information Service | Service de données et d&#39;informations atmosphériques |
| `2010` | New Fiscal Relationship (10 Year) Grant | Subvention nouvelle relation financière (de 10 ans) |
| `2013` | Canada Energy Regulator Management System Audits of Regulated Companies | Vérifications des systèmes de gestion des sociétés réglementées par la Régie de l&#39;énergie du Canada. |
| `2014` | Canada Energy Regulator Financial Audit of Regulated Companies. | Vérification des états financiers des sociétés réglementées par la Régie de l&#39;énergie du Canada. |
| `2015` | Client Service Centre | Centre de services à la clientèle |
| `2016` | Interchange Canada | Échanges Canada |
| `2017` | Management Accountability Framework | Cadre de responsabilisation de gestion |
| `2018` | General Inquiries | Demandes générales |
| `2019` | Directory of Federal Real Property (DFRP) | Répertoire des biens immobiliers fédéraux (RBIF) |
| `2020` | Federal Contaminated Sites Inventory (FCSI) | Inventaire des sites contaminés fédéraux (ISCF) |
| `2021` | IP Data | Données sur la PI |
| `2022` | Performance Management for Employees | Gestion du rendement pour les employés |
| `2023` | Processing Applications under the Canadian Energy Regulator Act, sections 183, 2 | Traitement des demandes aux termes de l&#39;article 183, 214, 262 ou 298 de la loi sur la Régie canadienne de l&#39;énergie. |
| `2024` | Treasury Board Submission Centre | Centre des présentations du Conseil du Trésor |
| `2025` | Provision of Grants and Contributions | Octroi de subventions et de contributions |
| `2028` | New Substances Notification | Déclaration de substances nouvelles |
| `2029` | Accessibility and Inclusivity in the Built Environment | Accessiblité et inclusivité dans l&#39;environnement bâti |
| `2030` | Green and Sustainable Government for Real Property | Gouvernement vert et durable pour les biens immobiliers |
| `2031` | Canadian Shellfish Sanitation Program (Emergency (bi-valve) shellfish area closu | Programme canadien de contrôle de la salubrité des mollusques (Recommandations pour la fermeture d&#39;urgence de la zone des mollusques) |
| `2032` | Athlete Assistance | Aide aux athlètes |
| `2033` | Appraisal and Valuation Services | Services d&#39;évaluation |
| `2034` | GC Talent Cloud | Nuage de talents du GC |
| `2035` | GCcollab | GCcollab |
| `2036` | Application Portfolio Management (APM) submission | Soumission du Plan de TI et gestion du portefeuille d&#39;applications (GPA) |
| `2038` | Permits for Migratory Bird Sanctuary Regulations | Permis en vertu du Règlement sur les refuges d&#39;oiseaux migrateurs |
| `204` | Money Services Businesses - Registry Search | Entreprises de services monétaires – Recherche d&#39;entités inscrites |
| `2041` | Treaty Annuity Payments | Paiements de rente conventionnelle |
| `2042` | Transfers of Band Moneys | Transferts d&#39;argent de bande |
| `2043` | Treaty Payments Events | Événements de paiement de traités |
| `2044` | Indian Moneys Expenditure Requests | Demandes de versement des fonds indiens |
| `2045` | Individual Trust Account Payout Requests | Demandes de paiement de compte en fiducie individuel |
| `2046` | Estates Management | Gestion des successions |
| `2047` | Indian Registry | Registre indien |
| `2048` | Issuance of the Secure Certificate of Indian Status | Délivrance du certificat sécurisé de statut d&#39;Indien |
| `2049` | Community-Based Services: First Nations Economic Development Capacity &amp; Readiness Funding | Services communautaires : financement de la capacité et de l’état de préparation en matière de développement économique des Premières Nations |
| `2050` | First Nations Commercial and Industrial Development Act | Loi sur le développement commercial et industriel des Premières nations |
| `2051` | Food Safety Investigation - Incident Response | Enquête sur la salubrité alimentaire - intervention en cas d’incident |
| `2052` | Amendments to Schedule I of The First Nation Oil And Gas And Moneys Management Act | Modifications à l’annexe 1 de la Loi sur la gestion du pétrole et du gaz et des fonds des Premières Nations |
| `2053` | Funding for Essential Community-Based Services: First Nation Land Management | Financement des services essentiels communautaires : gestion des terres des Premières Nations |
| `2054` | Interdepartmental Procurement Strategy for Aboriginal Businesses | Stratégie interministérielle d’approvisionnement auprès des entreprises autochtones |
| `2055` | Incentives for Zero-Emission Vehicles Program | Le programme incitatifs pour l&#39;achat de véhicules zéro émission |
| `2056` | Aboriginal Entrepreneurship Program - Access to Capital | Programme d&#39;entrepreneuriat autochtone - L’accès au capital |
| `2057` | Operation and Maintenance of First Nations and Inuit Health Facilities | Fonctionnement et l’entretien des établissements de santé des Premières Nations et des Inuits |
| `2058` | Procurement Strategy for Indigenous Business and the Indigenous Business Directory | Stratégie d’approvisionnement auprès des entreprises autochtones et Répertoire des entreprises autochtones |
| `2059` | Community Based On-Reserve Oil and Gas Management | Gestion communautaire du pétrole et du gaz sur les terres de réserve |
| `2060` | Indian Land Registry | Registre des terres indiennes |
| `2061` | Funding Community-Based Services: Reserve Land and Environment Management Program | Financement des services communautaires : Programme de gestion de l’environnement et des terres de réserve |
| `2062` | Contaminated Sites On-Reserve Program | Programme des sites contaminés dans les réserves |
| `2063` | Land Use Planning | Planification de l&#39;utilisation des terres |
| `2064` | First Nations Waste Management Initiative | Initiative des gestion des matières résiduelles des Premières Nations |
| `2065` | Environmental Review Process | Processus d&#39;examen environnemental |
| `2066` | Additions to Reserve | Ajouts aux réserves |
| `2067` | Sustainable On-Reserve First Nation Community and Economic Development | Développement économique et communautaire durable des Premières Nations dans les réserves |
| `2068` | Band Governance Management System | Système d&#39;information sur l&#39;administration des bandes |
| `2069` | Matrimonial Real Property | Biens immobiliers matrimoniaux dans les réserves |
| `2070` | Program to Address Disturbances from Vessel Traffic: Vessel slowdown | Programme de lutte contre les perturbations causées par le trafic maritime : Ralentissement du navire |
| `2071` | Animal Health Investigation - Incident Response | Enquête sur la salubrité des animaux - intervention en cas d’incident |
| `2072` | Quebec Fisheries Fund (QFF) | Fonds des pêches du Québec (FPQ) |
| `2073` | Program to Address Disturbances from Vessel Traffic: WhaleReport Alert System | Programme de lutte contre les perturbations causées par le trafic maritime : Système d&#39;alerte de rapport de baleine WhaleAlert |
| `2074` | Program to Protect Canada&#39;s Coastlines and Waterways: Abandoned Boats Program | Programme de protection du littoral et des voies navigables du Canada : Programme de bateaux abandonnés |
| `2075` | Program to Protect Canada&#39;s Coastlines and Waterways: Indigenous and Local Commu | Programme de protection du littoral et des voies navigables du Canada : Programme de partenariat et de mobilisation des collectivités autochtones et locales |
| `2076` | Program to Protect Canada&#39;s Coastlines and Waterways: Marine Training Program | Programme de protection du littoral et des voies navigables du Canada : Programme de formation dans le domaine maritime |
| `2077` | MPA Activity Plan Application Process - Laurentian Channel MPA | Processus de demande d&#39;activités pour la ZPM - Laurentian Channel |
| `2078` | MPA Activity Plan Application Process - Basin Head MPA | Processus de demande d&#39;activités pour la ZPM - Basin Head |
| `2079` | MPA Activity Plan Application Process - Banc-des-Americains MPA | Processus de demande d&#39;activités pour la ZPM - Banc-des-Americains |
| `208` | Management and Oversight | Gestion et Surveillance |
| `2080` | Canadian Industry Statistics | Statistiques relatives à l&#39;industrie canadienne |
| `2082` | Canadian Importers Database | Base de données sur les importateurs canadiens |
| `2083` | Trade Data Online | Données sur le commerce en direct. |
| `2084` | Financial Performance Data | Données sur la performance financière |
| `2085` | Program to Protect Canada&#39;s Coastlines and Waterways: Program to Enhance Maritim | Programme de protection du littoral et des voies navigables du Canada : Programme de sensibilisation accrue aux activités maritimes |
| `2086` | National Collision Database (NCDB) | Base nationale de données sur les collisions (BNDC) |
| `2087` | Indigenous Habitat Participation Program | Programme pour la participation autochtone sur les habitats |
| `2091` | BC Salmon Restoration and Innovation Fund (BCSRIF) | Fonds de restauration et d&#39;innovation pour le saumon de la Colombie-Britannique (FRISB) |
| `2092` | Marine Mammal Response Program | Programme d&#39;intervention auprès des mammifères marins |
| `2093` | TMX Accommodation Measure Salish Sea Initiative (SSI) | Initiative de la mer Salish (IMS) |
| `2094` | Enhanced Nature Legacy - Canada Target 1 Challenge Top-up | Complément du Défi de l’objectif 1 du Patrimoine naturel bonifié du Canada |
| `2095` | Canada Nature Fund - Community-nominated priority places for species at risk | Les lieux prioritaires désignés par les collectivités pour les espèces en péril du Fonds de la nature du Canada |
| `2096` | International Assistance Group | Service d&#39;entraide internationale |
| `2098` | Legal Services - Advisory | Services juridiques - Conseils |
| `2099` | Legal Services - Litigation | Services juridiques - Contentieux |
| `21` | Grants and Contribution Programs | Programmes de subventions et de contributions |
| `2100` | Legal Services - Legislative and Regulatory | Services juridiques – Législation et réglementation |
| `2101` | Investment Support | Soutien en matière d&#39;investissement |
| `2102` | Introductions | Présentations |
| `2103` | Roadmap | Feuille de route |
| `2104` | Women&#39;s Program | Programme de promotion de la femme |
| `2105` | Gender-Based Violence Program | Programme de financement de la lutte contre la violence fondée sur le sexe |
| `2106` | Equality for Sex, Sexual Orientation, Gender Identity and Expression Program | Programme de promotion de l&#39;égalité des sexes, de l&#39;orientation sexuelle, de l&#39;identité et de l&#39;expression de genre |
| `2107` | Client initiated request to transfer the file between offices in Canada | Demande initiée par le client pour transférer le dossier entre des bureaux au Canada |
| `2108` | Temporary Passport | Délivrance d&#39;un passeport provisoire |
| `2109` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `2110` | Family Orders and Agreement Enforcement Assistance | Aide à l&#39;exécution des ordonnances et des ententes familiales |
| `2112` | Ecosystems and Oceans Science Contribution Framework | Cadre de contribution de Sciences des écosystèmes et des océans |
| `2114` | Issuance of Authority – Air Licence, International Charter Permits and Wet Lease | Délivrance de l&#39;autorisation - Licence aérienne, permis d&#39;affrètement international et bail avec équipage |
| `2115` | introduction to and Advanced Training on the IAA | Introduction et formation avancée à la LEI |
| `2116` | Emergency Management Services | Services de gestion des urgences |
| `2117` | Impact Assessment done by Review Panels | Évaluation d&#39;impact par une commission d&#39;examen |
| `2118` | Impact Assessment done by Substitution | Évaluation d&#39;impact par substitution |
| `2119` | Monitoring and addressing events in the financial sector, response to liquidity | Surveillance et traitement des événements dans le secteur financier, réponse à la crise des liquidités |
| `2121` | Impact Assessment done by the Agency | Évaluation d&#39;impact réalisée par l&#39;Agence |
| `2122` | Northern Contaminants Program | Programme de lutte contre les contaminants dans le Nord |
| `2123` | Basic Organizational Capacity | Capacité organisationnelle de base |
| `2124` | Federal Interlocutor&#39;s Contribution Program(FICP) (Projects Stream) | Programme de contribution de l&#39;Interlocuteur fédéral |
| `2125` | Consultation and Policy Development | Consultations et de l&#39;élaboration des politiques |
| `2126` | Support in accordance with the Addition of Lands to Reserve and Reserve Creation Act, the First Nations Fiscal Management Act and the Framework Agreement on First Nation Land Management Act and the related institutions | Appui portant sur la Loi sur l’ajout de terres aux réserves et la création de réserves, la Loi sur la gestion financière des premières nations et la Loi sur l’Accord-cadre relatif à la gestion des terres de premières nations. |
| `2127` | List of First Nations managing their lands under the First Nations Land Management Act | Liste des Premières Nations qui gèrent leur terres sous la Loi sur la gestion des terres des Premières Nations |
| `2128` | Ministerial Correspondence | Correspondence ministérielle |
| `2129` | Indigenous Arts Centre | Centre d&#39;art autochtone |
| `2130` | Access to Information | Accès à l&#39;information |
| `2131` | Coordinate COVID-19 Funding Opportunities | Coordination des possibilités de financement liées à la COVID?19 |
| `2132` | Settlement Program Transfer Payments | Paiements de transfert du Programme d&#39;établissement |
| `2133` | Privacy | Protection des renseignements personnels |
| `2134` | Canada Energy Regulator (CER)&#39;s Emergency Response Procedures | Procedures d&#39;intervention d&#39;urgence de la Régie de l&#39;énergie du Canada |
| `2136` | Canadian Criminal Real Time Identification Services (CCRTIS) - Biometric Business Solutions (BBS) Certification Services. | Les Services canadiens d&#39;identification criminelle en temps réel (SCICTR) - Services de certification- Solutions biométriques d&#39;entreprise (SBE) |
| `2137` | Sensitive and Specialized Investigative Services (SSIS) | Services d&#39;enquêtes spécialisées et de nature délicate (SESND) |
| `2138` | Criminal Intelligence Service Canada (CISC) | Service canadian de renseignements criminels (SCRC) |
| `2139` | Departmental Correspondence Unit | Unité de la correspondance ministérielle |
| `2140` | Media Relations | Relations avec les médias |
| `2141` | Conservation management | Gestion de la conservation |
| `2142` | Highway Operations | Opérations de voirie |
| `2143` | Waterways Safety and Reporting | Services de sécurité et d&#39;information sur les voies navigables |
| `2144` | Alerts and advisories | Alertes et avis |
| `2145` | Government Resiliency and Continuity Management (Centre for Resiliency and Continuity Management) | Gestion de la continuité et de la résilience du gouvernement (Centre de gestion de la continuité et de la résilience) |
| `2146` | Accelerated Growth Service | Service de croissance accélérée |
| `2148` | Media relations | Relations avec les médias |
| `2149` | Stakeholder Relations | Stakeholder Relations |
| `2150` | Make a Complaint | Dépôt d&#39;une plainte |
| `2151` | Request a Review | Demande d&#39;examen |
| `2152` | Public Education and Outreach | Sensibilisation du public et liaison avec les collectivités |
| `2153` | Conduct a Review | Effectuer un examen |
| `2154` | Investigate a Complaint | Enquêter sur une plainte |
| `2155` | Funding Programs for Health Research and Training | Programmes de financement de la recherche et de la formation en santé |
| `2158` | Funding Programs | Programmes de financement |
| `2159` | Small Business Services and Public Enquiries | Services aux petites entreprises et demandes de renseignements pour le public |
| `22` | Web Inquiries | Demandes de renseignements sur le Web |
| `2201` | Mandatory Isolation Supports for Temporary Foreign Workers Program | Programme d&#39;aide pour l&#39;isolement obligatoire des travailleurs étrangers temporaires |
| `2213` | Emergency On-Farm Support Fund | Fonds d’urgence pour les mesures de soutien à la ferme |
| `2214` | Emergency Processing Fund | Le Fonds d&#39;urgence pour la transformation |
| `2215` | Surplus Food Rescue Program | Programme de récupération d’aliments excédentaires |
| `2216` | IP Education, tools, and resources | Éducation, outils et ressources en matière de PI |
| `2217` | Register Integrated Circuit Topography | Enregistrement de topographies de circuits intégrés |
| `2218` | Black Entrepreneurship Program | Programme pour l&#39;entrepreneuriat des communautés noires |
| `2219` | Women Entrepreneurship Knowledge Hub | Portal de connaissances pour les femmes en entrepreneuriat |
| `2220` | Rapid test kit provision | Fourniture de kit de test rapide |
| `2221` | COVID Alert | Alerte COVID |
| `2222` | Canada Digital Adoption Program - Grow Your Business Online | Programme canadien d’adoption du numérique - Développer vos activités commerciales en ligne |
| `2223` | Food Waste Reduction Challenge | Défi de réduction du gaspillage alimentaire |
| `2224` | AAFC Contact Centre | Centre d’appels de la Direction des programmes du revenu agricole (DPRA) |
| `2225` | Innovative Solutions Canada Program | Solutions innovatrices Canada (SIC) |
| `2226` | Safeguarding Your Research Portal | Portail Protégez Votre Recherche |
| `2227` | Strategic Science Fund (SSF) | Fonds stratégique des sciences (FSS) |
| `2228` | CRC-Intellectual Property Licensing | Licences de propriété intellectuelle |
| `2229` | Universal Broadband Fund (STS-CCB) | Fonds pour la large bande universelle |
| `2230` | COVID-19 Tracking System (CTS) | Système de suivi pour la COVID-19 (SSC) |
| `2233` | TBS IRIS (SAP) Corporate Financial Systems for the Central Agency Cluster Shared Systems (CAC-SS) | SCT IRIS (SAP) Systèmes financiers ministériels des Systèmes partagés du Regroupement des organismes centraux (SP-ROC) |
| `2234` | IC Contact Us: AGS Call Centre Service | Contactez-nous IC: Service de centre d&#39;appel |
| `2235` | Accelerated Growth Service | Service croissance accélérée |
| `2236` | The Accelerated Growth Service (AGS) | Le service de croissance accélérée |
| `2237` | ExploreIP | ExplorerPI |
| `2238` | Client Support Centre | Centre de soutien à la clientèle |
| `2239` | Expenditure Management Component | Le système de gestion des dépenses |
| `2240` | Issuance of Certificates of Qualification under the Floating Plant Clause (Coasting Trade Act) | Délivrance de certificats de qualification en vertu de la clause d&#39;outillage flottant (Loi sur le cabotage) |
| `2241` | Public Service Employee Survey (PSES) | Sondage auprès des fonctionnaires fédéraux (SAFF) |
| `2242` | Executive Talent Management | Gestion des talents des cadres supérieurs |
| `2243` | Canadian Experiences Fund | Fonds pour les expériences canadiennes |
| `2244` | Women Entrepreneurship Fund | Le Fonds pour les femmes en entrepreneuriat |
| `2245` | Women Entrepreneurship Strategy Ecosystem Fund | Le Fonds pour l&#39;écosystème de la Stratégie pour les femmes en entrepreneuriat |
| `2246` | Regional Relief and Recovery Fund | Fonds d&#39;aide et de relance régionale |
| `2247` | Large Employer Emergency Financing Facility (LEEFF) | Crédit d’urgence pour les grands employeurs (CUGE) |
| `2248` | Patent Collective Pilot Program (Gs&amp;Cs) | Programme pilote sur le Collectif de brevets |
| `2250` | Indigenous Intellectual Property Program Grant (Gs&amp;Cs) | Subvention du programme sur la propriété intellectuelle autochtone |
| `2251` | Intellectual Property Clinics Program (Gs&amp;Cs) | Programme de cliniques sur la propriété intellectuelle |
| `2253` | GC Integrated Planning submission | Soumission du Plan Intégrée GC |
| `2254` | COVID Vaccines Inventory Management | Gestion des inventaires vaccins COVID |
| `2255` | New Substances Program | Programme des substances nouvelles |
| `2256` | New Substances Notifications (Food and Drugs Act use) | Déclaration de substances nouvelles (usage en vertu de la Loi sur les aliments et drogues) |
| `2257` | Treasury Board Policy Suite Website | Site Web des politiques du Conseil du Trésor |
| `2259` | Early Retirement Incentive Program- A Unique Program (not associated with Receiver General Functions). Maintain pension services for employees of coal mines. | Programme d’encouragement à la retraite anticipée – Un programme unique (indépendant des fonctions du receveur général). Assurer les services de pensions pour les employés des mines de charbon. |
| `2260` | Investment Canada Act (ICA) Net Benefit Review, National Security Review | Loi sur Investissement Canda examen de l&#39;avantage net, examen relatif à la sécurité nationale |
| `2261` | Repository of Federal Public Sector (Core Public Administration) Collective Agreements | Répertoire des conventions collectives du secteur public fédéral (administration publique centrale) |
| `2262` | Project Risk and Complexity Assessment (Callipers) | L’Évaluation de la complexité et des risques des projets (Calibrage) |
| `2263` | Public Service Occupational Health Program COVID Response Division | Programme de santé au travail de la fonction publique - Division de l&#39;intervention liée à la COVID |
| `2264` | COVID-19 Mental Health Response | COVID-19: Intervention en santé mentale |
| `2265` | Travel Health Advice | Conseils de santé aux voyageurs |
| `2266` | GC-Wide Application Support Services | Services de soutien des applications à l&#39;échelle du GC |
| `2267` | Designated Quarantine Facilities | Installations de quarantaine désignées |
| `2268` | Central Notification System | Système de notification central |
| `2269` | Listeriosis Reference Service for Canada | Service de référence sur la listériose au Canada |
| `2270` | Measuring device approval services (non new approvals / revisions) | Services d&#39;approbation des dispositifs de mesure (non nouvelles approbations / révisions) |
| `2271` | Recruitment | Recrutement |
| `2274` | Prosecutorial Legal Advice | Conseils juridiques en matière de poursuites |
| `2275` | Respond to inquiries. | Répondre aux demandes de renseignements. |
| `2276` | Water/sewage treatment | Eau/traitement des eaux usées |
| `2277` | Emergency Support Function #10 | Fonction de soutien d&#39;urgence no. 10 |
| `2278` | National Fine Recovery Program (NFRP) | Programme national de recouvrement des amendes (PNRA) |
| `2280` | Class A Precursor Licences (New, Renewals, Amendments, Closures) | Octroi de licences de précurseurs chimiques de catégorie A (Nouvelles, renouvellements, modifications et fermetures) |
| `2281` | Cannabis Status Confirmation Service | Service de confirmation du statut en matiere du cannabis |
| `2283` | Amend Industrial Hemp Licences | Modifier les licences de chanvre en vertu de la Loi sur le cannabis et de ses règlements |
| `2284` | Fish Harvester Benefit and Grants program | Programme de Prestation et Subvention aux Pêcheurs |
| `2285` | One-Time Payment to Persons with Disabilities | Paiement Unique aux Personnes en Situation de Handicap |
| `2286` | Enquiries | Demande de renseignements |
| `2287` | Canadian Family Justice Fund | Fonds canadien de justice familiale |
| `2288` | Public Legal Education and Information | Éducation et information juridiques publiques |
| `2289` | Professional Training | Formation professionnelle |
| `2290` | Garnishment Registry of the National Capital Region (GAPDA) | Greffe de la saisie-arrêt de la région de la capitale nationale (LSADP) |
| `2291` | Central Registry of Divorce Proceedings (CRDP) | Bureau d&#39;enregistrement des actions en divorce (BEAD) |
| `2292` | Health Care Policy and Strategies Program | Programme des politiques et des stratégies en matière de soins de santé |
| `2293` | COVID-19 Public Enquiries | Demandes de renseignement sur la COVID-19 |
| `2294` | ArriveCAN Public Enquiries | Demandes de renseignement sur ArriveCAN |
| `2295` | COVID-19 Authorized Accommodations Toll-Free line | Ligne sans frais des hébergements autorisés COVID-19 |
| `2296` | Official Languages Health Program | Programme pour les langues officielles en santé |
| `2297` | Supporting the Canadian Red Cross&#39; Urgent Relief Efforts Related to COVID-19, Floods and Wildfires | Appuyer les efforts urgents de secours de la Croix-Rouge canadienne liés è la COVID-19, aux inondations et aux feux de forêt |
| `2298` | Botulism Reference Service for Canada | Service de référence pour le botulisme au Canada |
| `23` | Policy, Advocacy, and Coordination | Politique, représentation et coordination |
| `2300` | Canadian Travel Number (CTN) | Numéro canadien de voyages (NCV) |
| `2330` | Business Advisory Services. | Services-conseils à l&#39;entreprise. |
| `2358` | Youth Take Charge | Les jeunes s&#39;engagent |
| `2359` | Exchanges Canada - Youth Forums Canada | Échanges Canada - Forums Jeunesse Canada |
| `2360` | CNSC Emergency Management Duty Officer | Agente de service chargé de la gestion des urgences de la CCSN |
| `2361` | Radiological and Nuclear Expertise | Expertise nucléaire et radiologique |
| `2362` | Transportation Security Clearance | Habilitation de sécurité en matière de transport |
| `2363` | Program to Advance Transportation Innovation: Canadian Transportation Research F | Programme de promotion de l&#39;innovation en matière de transport : Groupe de recherches sur les transports au Canada |
| `2364` | Drone safety | Sécurité des drones |
| `2365` | Operating a federal railway | Exploitation d&#39;un chemin de fer fédéral |
| `2366` | Aviation Security - Issuing Exemptions | Sûreté aérienne - délivrance d&#39;exemptions |
| `2367` | Program to Address Disturbances from Vessel Traffic: Quiet Vessel Initiative | Programme de lutte contre les perturbations causées par le trafic maritime : Initiative pour des navires silencieux |
| `2368` | Issuance of AMOC/Exemption to the requirements of an Airworthiness Directive | Délivrance d&#39;un AMOC/Exemption aux exigences d&#39;une directive de navigabilité |
| `2369` | Contribution Program to Support Essential Air Services for Remote Communities | programme de contribution pour le programme de soutien aux services aériens essentiels aux collectivités éloignées |
| `2370` | Administration of the Marine War Risk Act and the agreement with the Canadian Sh | Administration de la Loi sur les risques de guerre en matière d&#39;assurance maritime et de l&#39;accord avec l&#39;Association pour assurance mutuelle d&#39;armateurs canadiens. |
| `2371` | Program to Protect Canada&#39;s Coastlines and Waterways: Safety Equipment and Basic | Programme de protection du littoral et des voies navigables du Canada : Initiative sur l&#39;équipement de sécurité et l&#39;infrastructure maritime de base dans les collectivités nordiques |
| `2372` | Program to Advance Indigenous Reconciliation: Program to Enhance Maritime Situat | Programme visant à favoriser la réconciliation avec les peuples autochtones : Programme de sensibilisation accrue aux activités maritimes |
| `2373` | Program to Advance Indigenous Reconciliation: Marine Safety Equipment and Traini | Programme visant à favoriser la réconciliation avec les peuples autochtones : Programme de formation et d&#39;équipement de sécurité maritime |
| `2374` | Inspecting a Railway | Inspection d&#39;un chemin de fer |
| `2375` | National Contact Centre Network (NCCN) | Réseau national des centres de contact (RNCC) |
| `2376` | Natural Infrastructure Fund (NIF) | Fonds pour les infrastructures naturelles (FIN) |
| `2377` | Green and Inclusive Community Buildings (GICB) | Bâtiments communautaires verts et inclusifs (BCVI) |
| `2378` | General Enquiry Services | Services de renseignements généraux (SRG) |
| `2379` | Cyber Security Assessments | Évaluations de la cybersécurité |
| `2380` | Canada Business App | l&#39;application Enterprises Canada |
| `243` | Species at Risk Act Permit System | Système de permis de la Loi sur les espèces en péril |
| `244` | Migratory Game Bird Hunting Permits | Permis de chasse aux oiseaux migrateurs considérés comme gibier |
| `2440` | Operational Communications Centre National Support Services (OCCNSS) | Services nationaux du soutien aux stations de transmissions opérationnelles (SNSSTO) |
| `2442` | RCMP Operations Coordination Centre (ROCC) | Centre de coordination des opérations de la GRC (CCOG) |
| `2443` | RCMP-Indigenous Relations Services (RIRS) | GRC services de relations avec les autochtones (GRC-SRA) |
| `2444` | Youth Officer Training (YOT) (online and in-person) | Formation des policiers éducateurs (FPE) (en ligne et en personne) |
| `2445` | RCMPTalks | Discussions GRC |
| `2446` | Youth Leadership Workshop (YLW) | Atelier de perfectionnement en leadership (APL) |
| `2447` | Indian Act Land Administration | Gestion des terres sous la Loi sur les Indiens |
| `2448` | Vulnerable Persons Unit (VPU) - Family Violence Initiative Fund (FVIF) | Section des personnes vulnérables - Fonds de l&#39;Initiative de lutte contre la violence familiale de la GRC |
| `2449` | Canadian Police Information Centre (CPIC) System including the Public Safety Portal (PSP) | Système du Centre d&#39;information de la police canadienne (CIPC) incluant le Portail de la Sécurité Publique (PSP) |
| `245` | Climate Change Funding Programs - Low Carbon Economy Leadership Fund | Le Fonds du leadership pour une économie à faibles émissions de carbone |
| `2450` | Service Feedback - Complaints | Rétroaction sur les services - plaintes, |
| `2451` | Coordination Agreement Discussions Tables | Tables de discussions sur l&#39;accord de coordination |
| `2452` | Notices and requests related to An Act respecting First Nations, Inuit and Métis children, youth and families | Avis et demandes liés à la Loi concernant les enfants, les jeunes et les familles des Premières Nations, des Inuits et des Métis |
| `2453` | Specialized Technical Investigative Services (STIS) | Les Services d’enquêtes spécialisées et techniques |
| `2454` | Information sharing service between INTERPOL/Europol and Canadian Law Enforcement | Service d’échange d’information entre INTERPOL/Europol |
| `2456` | Support to employees and veterans experiencing symptoms of or who have been diagnosed with an operational stress injury | Soutien aux employés et vétérans présentant des symptômes ou ayant reçu un diagnostic de traumatisme lié au stress opérationnel |
| `2457` | Canada Recovery Benefit (CRB) | Prestation canadienne de la relance économique (PCRE) |
| `2458` | Canada Recovery Caregiving Benefit (CRCB) | Prestation canadienne de la relance économique pour proches aidants (PCREPA) |
| `2459` | Canada Recovery Sickness Benefit (CRSB) | Prestation canadienne de maladie pour la relance économique (PCMRE) |
| `2460` | Canada Emergency Response Benefit (CERB) | Prestation canadienne d&#39;urgence (PCU) |
| `2461` | Canada Emergency Student Benefit (CESB) | Prestation canadienne d&#39;urgence pour les étudiants (PCUE) |
| `2462` | Canada Emergency Wage Subsidy (CEWS) | Subvention salariale d&#39;urgence du Canada (SSUC) |
| `2463` | Canada Emergency Rent Subsidy (CERS) | Subvention d&#39;urgence du Canada pour le loyer (SUCL) |
| `2464` | 10% Temporary Wage Subsidy for Employers | Subvention salariale temporaire de 10 % pour les employeurs (SST) |
| `2465` | Media Relations. | Relations avec les médias. |
| `2466` | International Real Property Services | Services en biens immobiliers internationaux |
| `2467` | Implementation of the Indian Residential Schools Settlement Agreement and Indian Residential Schools Documents Advisory Committee | Mise en œuvre de la Convention de règlement relative aux pensionnats indiens |
| `2468` | Indigenous Childhood Claims Litigation | Litiges relatifs aux réclamations pour les expériences vécues dans l&#39;enfance |
| `2469` | Canada Treaty Custodian | Gardien des traités du Canada |
| `247` | Climate Change Funding Programs - Low Carbon Economy Challenge: Champions Stream | Défi pour une économie à faibles émissions de carbone: volet des champions |
| `2477` | Support in accordance with the First Nations Fiscal Management Act, and its institutions | Support en lien avec la Loi sur la gestion financière des Premières Nations et ses institutions. |
| `2480` | Manage the Specific Claims Program | Gestion du programme des revendications particulières |
| `249` | Permits of equivalent levels of environmental safety | Permis de sécurité environnementale équivalente |
| `2495` | Impact Assessment Process | Processus d&#39;évaluation d&#39;impact |
| `25` | Access to the natural, historic and recreational site (no fee) | Accès au site naturel, historique et récréatif (sans frais) |
| `2505` | Permits under the Scott Islands Protected Marine Area Regulations | Permis en vertu du Règlement sur la zone marine protégée des îles Scott |
| `2515` | Northern Contaminated Sites Program | Programme des sites contaminés du Nord |
| `2517` | Canada Treaty Adoption Process | Processus canadien d&#39;adoption des traités |
| `2528` | Emergency Watch and Response | Surveillance et d&#39;interventions d&#39;urgence |
| `2531` | Orientation | Orientation |
| `2532` | Grants and Contributions in Aid of Academic Relations | Subventions et contributions en appui aux relations academiques |
| `2534` | Genealogy | Généalogie |
| `2536` | Loans to other institutions | Prêts à d&#39;autres institutions |
| `2537` | LAC User Card Registration Form | Formulaire d&#39;inscription pour la carte d&#39;usager de BAC |
| `2538` | Consultation of published and archival material | Consultation de matériel publié et archivistique |
| `2539` | Respond to requests for information from Parliamentarians. | Répondre aux demandes d&#39;information des parlementaires. |
| `254` | Environmental Funding - Aboriginal Fund for Species at Risk | Fonds autochtone pour les espèces en péril |
| `2540` | Loan request for exhibitions | Demande de prêts pour expositions |
| `2541` | «Listen, Hear Our Voices» Initiative | Initiative «Écoutez pour entendre nos voix» |
| `2542` | Access to records in support of the Federal Indian Day School Class Action Settl | Accès aux dossiers à l&#39;appui du règlement du recours collectif des externats indiens fédéraux |
| `2545` | Access to records of former Canadian Armed Forces members | Accès aux dossiers personnels des anciens membres des Forces armées canadiennes |
| `2549` | Cataloguing in Publication | Catalogage avant publication |
| `255` | Environmental Funding - Atlantic Ecosystems Initiatives | Initiatives des écosystèmes de l&#39;Atlantique |
| `2550` | Contributions Program of the Office of the Privacy Commissioner of Canada. | Programme des contributions du Commissariat à la protection de la vie privée du Canada. |
| `2551` | Surplus Canadian Publications | Publications canadiennes en surplus |
| `2552` | Privacy Impact Assessment (PIAs) Reviews. | Examens de Évaluations des facteurs relatifs à la vie privée (EFVP). |
| `2553` | Consultation services with federal institutions | Services-conseils au gouvernement |
| `2554` | Review and Investigate complaints under the Privacy Act. | Examiner et enquêter sur les plaintes en vertu de la Loi sur la protection des renseignements personnels. |
| `2555` | Receive and review Privacy Act breach reports. | Recevoir et examiner les rapports d&#39;atteintes à la vie privée en vertu de la Loi sur la protection des renseignements personnels. |
| `2556` | Review and investigate complaints under PIPEDA. | Examiner et enquêter les plaintes en vertu de la LPRPDE. |
| `2557` | On-Reserve Other Community Infrastructure Capacity Building | Renforcement des capacités pour les autres infrastructures communautaires pour les collectivités dans les réserves |
| `2558` | Receive and review breach reports under PIPEDA. | Recevoir et examiner les atteintes à la vie privée en vertu de la LPRPDE. |
| `2559` | Missing and Murdered Indigenous Women and Girls Secretariat | Le Secretariat pour les femmes et les filles autochtones disparues et assassinées |
| `2560` | Litigation Management Oversight Team | Direction de la surveillance de la gestion des litiges |
| `2561` | Strategic Policy, Cabinet and Parliamentary Affairs Branch | Direction générale des politiques stratégiques, des affaires du Cabinet et des affaires parlementaires |
| `2562` | Reconciliation Secretariat Branch | Direction générale du Secrétariat de la réconciliation |
| `2563` | Claims Assessment | Évaluation des revendications |
| `2564` | Contribution and Loan Funding to support Indigenous Communities Programs | Fonds de contribution et de prêt pour soutenir les programmes de négociations, de reconstruction des Nation et d’Espaces culturels dans les communautés autochtones. s |
| `2565` | Negotiations | Négociations |
| `2566` | BC Treaty Funding | Financement des traités CB |
| `2567` | Surplus Federal Real Property Initiative | Initiative sur les biens immobiliers excédentaires fédéraux |
| `2568` | Canadian Construction Materials Centre (CCMC) Product Assessments | Évaluation des produits du Centre canadien de matériaux de construction (CCMC) |
| `2569` | Indigenous Capacity Support Program | Programme de soutien des capacités autochtones |
| `2570` | Participant Funding Program | Programme d’aide financière aux participants |
| `2571` | Policy Dialogue Program | Programme de dialogue sur les politiques |
| `2572` | Projects subject to federal assessment under the IAA | Projets assujettis à l&#39;évaluation fédérale en vertu de la Loi sur l&#39;évaluation d’impact (LEI) |
| `2573` | Research Program | Programme de recherche |
| `2574` | Extractive Sector Transparency Measures Act | Loi sur les mesures de transparence dans le secteur extractif |
| `2576` | Pilimmaksaivik&#39;s Inuksugait Inventory | Inventaire des Inuksugait de Pilimmaksaivik |
| `2577` | Contribution in support of Climate Change Adaptation | Contribution à l&#39;appui de l&#39;adaptation au changement climatique |
| `2579` | Grants in support of Geo-Mapping for Energy and Minerals | Subventions à l&#39;appui du Programme Géocartographie de l?énergie et des minéraux |
| `2585` | Contributions in support of the ENERGY Innovation Program | Contributions à l&#39;appui des Programmes d&#39;innovation énergétique |
| `2586` | Electric Vehicle Infrastructure Demonstrations | Démonstrations d&#39;infrastructures pour véhicules électriques |
| `2587` | Smart Grid Infrastructure Demonstrations Program | Programme de démonstration de l&#39;infrastructure des réseaux électriques intelligents |
| `2588` | Clean Growth in the Natural Resources Sectors Innovation Program | Programme d&#39;innovation sur la croissance propre dans les secteurs des ressources naturelles |
| `2589` | Energy Efficient Buildings Program | Programme de bâtiments écoénergétiques |
| `2590` | Clean Energy for Rural and Remote Communities Program - Demonstration | Programme d&#39;énergie propre pour les collectivités rurales et éloignées |
| `2591` | Clean Technology Challenges - Impact Canada Initiative - Grants Portion | Défis de technologies propres - Initiative Impact Canada - subventions |
| `2592` | Clean Technology Challenges - Impact Canada Initiative | Défis de technologies propres - Initiative Impact Canada |
| `2593` | Emissions Reduction Fund Offshore Research, Development and Demonstration | Le programme de recherche, développement et démonstration extracôtière du Fonds de réduction des émissions |
| `2594` | Web content management services | Services de gestion du contenu web |
| `2595` | Contributions in support of Mountain Pine Beetle Management in Alberta | Contributions à l&#39;appui de la gestion du dendroctone du pin ponderosa en Alberta |
| `2596` | Contributions in support of Investments in the Forest Industry Transformation Program | Contribution à l&#39;appui du Programme d&#39;investissements dans la transformation de l&#39;industrie forestière |
| `2597` | Contributions in support of the Forest Innovation Program | Contributions à l&#39;appui du Programme de promotion de ld&#39;innovation forestière en foresterie |
| `2598` | Contribution program for Expanding Market Opportunities | Programme de développement des marchés |
| `2599` | Metallurgical Fuel Testing | Analyse des carburant métallurgique |
| `26` | Access to the Plains of Abraham Museum | Accès au Musée des plaines d&#39;Abraham |
| `2600` | Grants and Contributions in support of the Two Billion Tree Program | Subventions et contributions pour la croissance des forêts du Canada - 2 milliards d&#39;arbres |
| `2601` | Contribution to the Indigenous Forestry Initiative | Contribution à l&#39;Initiative de foresterie autochtone |
| `2602` | Grants and Contributions in support of Geoscience | Subventions et contributions en soutien aux géosciences |
| `2603` | BioHeat component of the Clean Energy for Rural and Remote Communities Program | Volet biothermie du programme Énergie propre pour les collectivités rurales et éloignées (EPCRE) |
| `2604` | CIM&#39;s Our Earth&#39;s Riches Mineral Literacy Installation | Installation Our Earth&#39;s Riches de l&#39;ICM pour mieux faire connaître le domaine minier aux jeunes Canadiens |
| `2605` | Spruce Budworm Early Intervention Strategy – Phase II Contribution Program | Stratégie d’intervention précoce contre la tordeuse des bourgeons de l’épinette – Phase II |
| `2606` | Mining Matters Educational Resources for Students | Ressources éducatives pour les étudiants &#39;Mining Matters&#39; |
| `2607` | Support for research on Woodland Caribou in support of conservation | Appuyer les recherches sur le caribou des bois à l&#39;appui de la conservation de cette espèce en péril |
| `2608` | Development and Delivery of Regional Mining Webinars | Développement et livraison de séminaire en ligne régionaux pour l&#39;exploitation minière |
| `2609` | National Youth Mining Career Awareness Strategy 2021-2026 | Stratégie nationale de sensibilisation aux carrières dans le secteur minier pour les jeunes 2021-2026 |
| `261` | Permit for disposal at sea | Permis pour l&#39;immersion en mer |
| `2610` | Green Construction through Wood (GCWood) Program | Programme de construction verte en bois (CVBois) |
| `2611` | Contributions in support of Indigenous Natural Resource Partnerships | Contributions en faveur des partenariats pour les ressources naturelles autochtones |
| `2612` | Contributions in support of Indigenous Advisory &amp; Monitoring Committees for EIPs (TMX &amp; L3) | Contributions pour appuyer les comités autochtones de consultation et de surveillance de projets d&#39;infrastructure énergétique - comités (TMX &amp; L3) |
| `2613` | Contributions in support of Indigenous Participation in Dialogues | Contributions à l&#39;appui du Fonds d&#39;aide financière aux participants pour les consultations auprès des Autochtones |
| `2614` | Contributions in support of Accommodation Measures for Trans Mountain Expansion | Contributions à l&#39;appui des mesures d&#39;accommodement du projet d&#39;agrandissement du réseau de Trans Mountain |
| `2616` | Funding for COVID-19 Safety Measures in Forest Sector Operations | Financement des mesures de sécurité COVID-19 dans les opérations du secteur forestier |
| `2617` | Industry Energy Management Programs | Programmes de gestion de l&#39;énergie industrielle |
| `2618` | Emissions Reduction Fund - Onshore Program | Fond de réduction des émissions - programme d&#39;installations terrestres |
| `2619` | Clean Energy for Rural and Remote Communities Program - Deployment | Programme d&#39;énergie propre pour les collectivités rurales et éloignées - Déploiement |
| `262` | Hazardous Waste Export and Import Permits | Permis d’exportation et d’importation de déchets dangereux |
| `2620` | Canadian Geospatial Data Infrastructure: Geospatial Web Services | Infrastructure canadienne de données géospatiales: Services web géospatiaux |
| `2621` | Impact Canada Initiative | Initiative Impact Canada |
| `2622` | Impact Canada Fellowship Program | Le programme de Fellowship d&#39;Impact Canada |
| `2623` | Governor-in-Council Appointments - Online account registration | Nominations par le gouverneur en conseil - Création de compte en ligne |
| `2624` | Senate Appointments | Nominations au Sénat |
| `2625` | Ministerial Correspondence | Correspondance ministérielle |
| `2626` | Public enquiries | Renseignements au public |
| `2627` | Horizontal Coordination of Government Communications | Coordination horizontale des communications gouvernementales |
| `2628` | Horizontal Coordination of Government advertising services | Coordination horizontale des services de publicité du gouvernement |
| `2629` | Horizontal Coordination of Government Public opinion research and analysis | Coordination horizontale de la recherche et analyse sur l’opinion publique |
| `263` | Environmental Funding - EcoAction Community Funding Program | Appel de propositions pour ÉcoAction |
| `2630` | Media monitoring and analysis, media relations | Surveillance et analyse médiatiques, relations avec les médias |
| `2631` | Fisheries Act - Aquatic Invasive Species Regulations Authorizations | la Loi sur les pêches - Autorisations en vertu du Règlement sur les especes aquatiques envahisantes |
| `2632` | Fisheries Act - Aquatic Invasive Species Regulations Fishing Licences | La Loi sur les pêches - permis de pêches du Règlement sur les especes aquatiques envahisantes |
| `2633` | Aquatic Invasive Species Program - Contribution Agreements | Programme sur les espèces aquatiques envahissantes - Ententes de contribution |
| `2634` | TMX Accommodation Measure Aquatic Habitat Restoration Program (AHRF) | Les mesures d&#39;accommodement TMX Fonds de restauration de l&#39;habitat aquatique (FRHA) |
| `2635` | TMX Accommodation Measure Terrestrial Cumulative Effects Initiative (TCEI) | Les mesures d&#39;accommodement TMX Initiative sur les effets cumulatifs en milieu terrestre (IECT) |
| `2636` | Contributions in support of the Salmonid and Salmon Enhancement Programming | Contributions à l&#39;appui du Programme de mise en valeur des salmonidés |
| `2637` | Indigenous Fisheries Management | Gestion des pêches autochtones |
| `2638` | Enforcement of Fisheries Legislation and Contaminated Shellfish Harvest Areas Closure Regulations | Application des lois sur les pêches et des règlements de fermeture de secteurs coquilliers contaminés |
| `2641` | CAMPUS - Individual subscription | CAMPUS - Abonnement individuel |
| `2642` | NFB.ca-Digital Store | ONF.ca-Boutique numérique |
| `265` | Environmental Funding - Lake Winnipeg Basin Program | Le programme du bassin du lac Winnipeg |
| `267` | Environmental Funding - Habitat Stewardship Program | Programme d&#39;intendance de l&#39;habitat pour les espèces en péril |
| `268` | Environmental Funding - Great Lakes Protection Initiative | Initiative de protection des Grands Lacs |
| `27` | Access to historic, thematic and educational activities | Accès à des activités historiques, thématiques et éducative |
| `278` | COSPAS-SARSAT Secretariat Contribution | Contribution du secrétariat COSPAS-SARSAT |
| `28` | Access to cultural activities | Accès à des activités culturelles |
| `280` | Heavy Urban Search and Rescue | Recherche et sauvetage en milieu urbain à l&#39;aide d&#39;équipement lourd |
| `282` | Search and Rescue New Initiatives Fund | Fonds des nouvelles initiatives de recherche et sauvetage |
| `283` | Search and Rescue Volunteer Association of Canada Contribution | Programme de contribution de l&#39;Association canadienne des volontaires en recherche et de sauvetage |
| `284` | Workers Compensation Program | Programme d&#39;indemnisation des travailleurs |
| `285` | Disaster Financial Assistance Arrangements | Accords d&#39;aide financière en cas de catastrophe |
| `288` | Youth Gang Prevention Fund | Fonds de lutte contre les activités des gangs de jeunes |
| `289` | Processing Applications under the National Energy Board Act, sections 52, 58 or | Traitement des demandes présentées aux termes de l’article 52, 58 ou 58.16 de la loi sur l&#39;Office national de l&#39;énergie. |
| `29` | Commemorative program (no fee) | Programme de commémoration (sans frais) |
| `290` | Processing Applications for Long-term Export License | Traitement des demandes présentées pour licence d&#39;exportation à long terme |
| `291` | Hearing Recommendations/Decisions | Demandes nécessitant une audience |
| `292` | Export Authorizations | Autorisations d&#39;exportation |
| `293` | Electricity Export Permits | Permis d&#39;exportation d&#39;électricité |
| `294` | Processing Non-hearing Applications under the Canadian Energy Regulator Act S214 | Traitement des demandes n&#39;exigeant pas d&#39;audience publique aux termes de l&#39;article 214 de la loi sur la Régie canadienne de l&#39;énergie. |
| `296` | Processing Landowner Complaints | Règlement des plaintes des propriétaires fonciers |
| `299` | Processing Canada Oil and Gas Operations Act Applications | Traitement des demandes aux termes de la Loi sur les opérations pétrolières au Canada |
| `3` | Export Food - Health/Sanitary Certificate | Exportations d&#39;aliments - Certificats de santé ou de salubrité |
| `30` | Access to information and the protection of personal information | Accès à l&#39;information et protection des renseignements personnels |
| `304` | Processing Canada Petroleum Resources Act Applications | Traitement des demandes aux termes de la Loi fédérale sur les hydrocarbures |
| `309` | Processing Participant Funding Requests | Traitement des demandes d&#39;aide financière aux participants |
| `31` | Refugee Protection | Protection des réfugiés |
| `314` | Responding to Library Requests | Demandes à la bibliothèque |
| `315` | Access to Information Requests | Accès à l&#39;information |
| `32` | Refugee Appeals | Appels des réfugiés |
| `324` | Receipt of requests to use the territory | Réception des demandes d&#39;utilisation du territoire |
| `33` | Toll-free Voice | Appels sans frais |
| `335` | Community Resilience Fund | Fonds pour la résilience communautaire |
| `337` | Crime Prevention Action Fund | Fonds d&#39;action en prévention du crime |
| `339` | International Association of Fire Fighters | Programme de contribution a l&#39;Association international des pompiers |
| `34` | Fixed Line Phones | Téléphones fixes (filaires) |
| `341` | Northern and Indigenous Crime Prevention Fund | Fonds de prévention du crime chez les collectivités Autochtones et du Nord |
| `344` | Communities at Risk: Security Infrastructure Program | Programme de financement des projets d&#39;infrastructure de sécurité pour les collectivités à risque |
| `35` | Bulk Print | Impression en bloc |
| `351` | Gun and Gang Violence Action Fund | Fonds de lutte contre la violence liée aux armes à feu et aux gangs |
| `352` | Funding for First Nation and Inuit Policing Facilities Program (FNIPF) | Programme de financement des installations pour les services de police des Premières Nations et des Inuits (PISPPNI) |
| `353` | Financial assistance agreement – Lac Mégantic | Accord d’aide financière - Lac Mégantic |
| `354` | Shock Trauma Air Rescue Ambulance Service | Shock Trauma Air Rescue Ambulance Service |
| `355` | Avalanche Canada | Avalanche Canada |
| `356` | Memorial Grant Program for First Responders | Programme de subvention commémoratif pour les premiers répondants |
| `357` | Funding Decisions for Institutional Capacity | Décisions sur le financement de la capacité institutionnelle |
| `3570` | Veteran Homelessness (VH) | Programme de lutte contre l&#39;itinérance chez les vétérans (PLIV) |
| `3572` | Events, exhibitions and tours | Événements, expositions et visites |
| `3573` | Copyright | Droits d&#39;auteur |
| `3574` | Information Management and Disposition of Government Records | Gestion de l’information et disposition des documents fédéraux |
| `3575` | International Standard Numbers | Numéros internationaux normalisés |
| `3576` | Loans | Prêts |
| `3577` | Research Support | Soutien à la recherche |
| `3578` | Digital Access to Collections | Accès numérique à la collection |
| `3581` | Funding Programs | Programmes de financement |
| `3584` | Compensation program due to extraordinary security measure during majors events | Programme d&#39;indemnisation dû aux mesures de sécurité extraordinaire durant des événements majeurs |
| `3585` | Business Information Services | Services d&#39;information aux entreprises |
| `3586` | Media Relations | Relations avec les médias |
| `3589` | Shared Human Resources Services | Services partagés en ressources humaines |
| `3590` | Procurement Options Analysis / Procurement Triage Tool/Ongoing Procurement Support and Advisory | Analyse des options d’approvisionnement / l’Outil de triage / Soutien à l’approvisionnement et services consultatifs en continu |
| `3591` | Real Property Disposals Sector | Secteur de l’aliénation des biens immobiliers |
| `3593` | Climate Change Funding Programs - Low Carbon Economy Challenge 2023 | Défi pour une économie à faibles émissions de carbone 2023 |
| `3594` | Community Development Wrap-Around Initiative | Initiative de soutien globale au développement communautaire |
| `3595` | ATSSC Law Library Services | Services de Bibliothèque du SCDATA |
| `3596` | ATSSC General Inquiries | Demandes générales SCDATA |
| `3597` | ATSSC Registry Services | Services de greffe |
| `3598` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `3599` | Global Innovation Clusters Program | grappes mondiales de l’innovation |
| `36` | Internal Credential Management | Gestion des justificatifs internes |
| `3600` | ElevateIP | ÉleverlaPI |
| `3601` | Portfolio Management | de gestion de portefeuille |
| `3602` | Canadian Dental Care Plan Eligibility Verification and Information | Vérification et renseignements sur l’admissibilité au Régime canadien de soins dentaires |
| `3603` | Grants and Contributions in Support of the Global Forest Leadership Program | Subventions et contributions à l&#39;appui du programme de leadership mondial sur les forêts |
| `3604` | Canadian Dental Care Plan eligibility verification and enrollment | Vérification de l&#39;admissibilité et inscription au Régime canadien de soins dentaires |
| `3606` | Multi-Partner Research Initiative | Initiative de recherche multipartenaire |
| `3607` | Public Court Records Access | Accès aux dossiers de cours public |
| `3608` | Litigant &amp; Public Support Services | Services de soutien aux parties et au public |
| `3609` | Courtroom and Hearing Operations | Coordinations des audiences et des salles |
| `3610` | Operational Support to the Judiciary | Soutien opérationnel à la magistrature |
| `3611` | Legal &amp; Judicial Support to the Judiciary | Soutien juridique et judiciaire à la magistrature |
| `3612` | Electricity Predevelopment Program | Programme de prédéveloppement en matière d&#39;électricité |
| `3613` | Enabling Small Modular Reactor Program | Programme facilitant les petits réacteurs modulaires |
| `3614` | National Bovine Spongiform Encephalopathy (BSE) Surveillance Reimbursement Program | Programme national de remboursement pour la surveillance de l&#39;encephalopathie spongiforme bovine (ESB) |
| `3615` | Veterinary Biologics Establishment Licence or Registration | Permis ou enregistrement d&#39;établissement de produits biologiques vétérinaires |
| `3616` | Nuclear Stock Seed Potato Program | Programme des pommes de terre de semence de Matériel nucléaire |
| `3617` | Box Tree Moth Program | Programme de la pyrale du buis |
| `3618` | Hemlock Wooly Adelgid Program | Programme du puceron lanigère de la pruche |
| `3619` | Blueberry Maggot Program | Programme de la mouche du bleuet |
| `3620` | Oak Wilt Program | Programme du flétrissement du chêne |
| `3621` | Prohibited Propagative Plant Material Program | Programme du matériel végétal de multiplication interdit |
| `3622` | Spotted Lanternfly Program | Programme du fulgore tacheté |
| `3623` | Apple (Fresh) Export Program | Programme d&#39;exportation de pommes (fraîches) |
| `3624` | Cherry (Fresh) Export Program | Programme d&#39;exportation de cerises (fraîches) |
| `3625` | Blueberry (Fresh) Export Program | Programme d&#39;exportation de bleuets (frais) |
| `3626` | Pepper (Fresh) Export Program | Programme d&#39;exportation de poivrons (frais) |
| `3628` | Grain Screening Pellets Export Program | Programme d&#39;exportation des agglomérats de criblures de grains |
| `3629` | Drug Submission Evaluations of Human Pharmaceuticals | Évaluation des présentations de médicaments pharmaceutiques à usage humain |
| `3630` | Drug Submission Evaluations of Biologic Products | Évaluation des présentations de médicaments biologiques |
| `3631` | Drug Submission Evaluations of Veterinary Pharmaceuticals and Veterinary Health Products | Évaluation des présentations de médicaments vétérinaires pharmaceutiques et des produits de santé animale |
| `3632` | Medical Device Submission Evaluations | Évaluation des demandes d&#39;instruments médicaux |
| `3633` | Special Access Programs: Human Drugs | Programmes d&#39;accès spéciale: médicaments à usage humain |
| `3634` | Special Access Programs: Medical Devices | Programmes d&#39;accès spéciale: instruments médicaux |
| `3635` | Natural Health Product Application Reviews | Évaluation des applications de produits de santé naturels |
| `3636` | Natural Health Product Site Licence Application Reviews | Évaluation des applications de licence des sites de produits de santé naturels |
| `3637` | Research Ethics Board | Comité d&#39;éthique de la recherche |
| `3638` | Stratospheric Balloon Flight Opportunities (STRATOS) | Opportunités de vols de ballons stratosphériques (STRATOS) |
| `3639` | CCOHS Inquiries Service | Le Service des demandes de renseignements du CCHST |
| `3640` | CCOHS Publications | Publications du CCHST |
| `3641` | CCOHS Legislation Service | Service législation du CCHST |
| `3642` | CCOHS Databases/Collections | Bases de données et collections du CCHST |
| `3643` | Cyber Centre Learning Hub - Learning Management System | Carrefour de l’apprentissage du Centre pour la cybersécurité – Système de gestion de l’apprentissage |
| `3644` | Cyber Centre Learning Hub - Curriculum Review | Carrefour de l’apprentissage du Centre pour la cybersécurité – Examen des programmes |
| `3645` | Advice and Guidance - Supply Chain Integrity | Avis et conseils en matière de cybersécurité – Architecture de sécurité du système |
| `3646` | Compliance Reviews / Certifications - Cryptographic Module Validation Program | Certifications/examens de conformité – Programme de validation des modules cryptographiques |
| `3647` | Compliance Reviews / Certifications - Common Criteria Recognition Arrangement (CCRA) | Certifications/examens de conformité – Arrangement de reconnaissance des Critères communs |
| `3648` | Cyber Centre Learning Hub - Custom Course Development | Carrefour de l’apprentissage du Centre pour la cybersécurité – Élaboration de cours sur mesure |
| `3649` | Digital Communications – Web Communications | Communications numériques – Communications Web |
| `3650` | Cyber Flipbook | Le livre d epoche cybernétique |
| `3651` | Canadian Anti-Fraud Centre-Online Fraud Reporting Systems | Centre Antifraude du Canada - système de signalement en ligne |
| `3652` | Indigenous Policing Services - National Directorate | Service de police autochtone – national |
| `3653` | Issuance of Discharge Books | Délivrance des livrets de service des marins |
| `3654` | Surface Transportation Merger and Acquisition Review and Assessment Process | Processus d&#39;examen et d&#39;évaluation des fusions et acquisitions dans le domaine des transports de surface |
| `3657` | Transportation Data and Information Hub | Carrefour de données et d&#39;information sur les transports |
| `3658` | Motor Vehicle Safety Call Centre | Centre d&#39;appels pour la sécurité des véhicules automobiles |
| `3659` | Assistance for a formal application for certification | Aide fournie en vue de la préparation d’une demande de services de certification |
| `3660` | Administrative changes to amend documents under Schedule V | Modification administrative apportée à un document pour lequel une redevance est exigible en vertu de la présente annexe |
| `3661` | Ministerial exemption to an airworthiness directive pursuant to 605.84(3) | Exemption ministérielle à une consigne de navigabilité en vertu du paragraphe 605.84(3) |
| `3662` | Marine Medical Examiner Designation | Désignation des médecins examinateurs de la marine |
| `3663` | Marine Pilotage Licence or Pilotage Certificate | Brevet de pilote ou certificat de pilotage maritime |
| `3664` | Marking and lighting of obstacles to air navigation | Balisage et éclairage des obstacles à la navigation aérienne |
| `3665` | Flight Tests Conducted by the Department of Transport | Tests en vol effectués par le ministère des Transports |
| `3666` | Outreach and Promotion - Human Rights | Sensibilisation et promotion - Droits de la personne |
| `3667` | Outreach and Education - Pay Equity | Sensibilisation et éducation - Équité salariale |
| `3668` | Outreach and Education - Accessibility | Sensibilisation et éducation - Accessibilité |
| `3669` | Complaint Management - Pay Equity | Gestion des plaintes - Équité salariale |
| `3670` | Complaint Management - Accessibility | Gestion des plaintes - Accessibilité |
| `3671` | Enforcement and Compliance - Pay Equity | Exécution et conformité - Équité salariale |
| `3672` | Enforcement and Compliance - Accessibilty | Exécution et conformité - Accessibilité |
| `3673` | System for Official Languages Obligations (SOLO) | Système pour les obligations en langues officielles (SOLO) |
| `3674` | Job Classification Data | Données sur la classification des emplois |
| `3675` | Finance Data Innovation Radar | Radar de l&#39;innovation en matière de finance |
| `3676` | Diversity and inclusion statistics | Statistiques sur la diversité et l&#39;inclusion |
| `3677` | Student Experience Survey | Sondage sur l&#39;experience etudiante (SEE) |
| `3678` | Human resources statistics | Statistiques concernant les ressources humaines |
| `3684` | Research Support Process | Processus de soutien à la recherche |
| `3685` | Grants and Contributions Programs | Programmes de subventions et contributions |
| `3686` | Indigenous Program Agreements | Accords sur les programmes autochtones |
| `3687` | MPA Activity Plan Application Process | Processus de demande d&#39;activités pour la ZPM - Anguniaqvia niqiqyuam |
| `3688` | Small Craft Harbours | Ports pour petits bateaux |
| `3689` | Small Craft Harbours Grant and Contribution Programs | Programmes de subventions et de contributions pour les ports pour petits bateaux |
| `3690` | Access to activities at the Plains of Abraham Museum | Accès aux activités du Musée des plaines d&#39;Abraham |
| `3691` | Access to social, cultural and heritage content online (no fee) | Accès à du contenu socio-culturel et patrimonial en ligne (sans frais) |
| `3692` | Access to a parking space | Accès à une place de stationnement |
| `3693` | Access to archives (no fee) | Accès aux archives (sans frais |
| `3694` | Receipt of requests from the media and public at large (no fee) | Réception des demandes des médias et du public (sans frais) |
| `3695` | Access to social, cultural, heritage and sports activities for the public at large (no fee) | Accès à des activités socio-culturelles, patrimoniales et sportives gratuites pour le grand public (sans frais) |
| `3698` | Payment of judges&#39; salaries | Paiement des salaires des juges |
| `3699` | Payment of judges&#39; allowance claims | Paiement des indemnités de juges |
| `37` | External Credential Management | Gestion des justificatifs externes |
| `3700` | Indigenous Partnership Fund | Le Fonds pour les partenariats avec les Autochtones |
| `3701` | Innovation for Defence Excellence and Security (IDEaS) Marketplace | Marché Innovation pour la défense, l&#39;excellence et la sécurité (IDEeS) |
| `3702` | Outreach | Rayonnement |
| `3703` | Peer Support Program | Programme de soutien par les pairs |
| `3704` | Independent Legal Assistance | L&#39;assistance juridique indépendante |
| `3705` | Import Admissibility | Admissibilité à l&#39;importation |
| `3707` | Media Relations | Relations avec les médias |
| `3708` | IDEaS Innovation Support Referals (IRS) Program | Programme de références pour le soutien à l’innovation (RSI) d’IDEeS |
| `3709` | Deferred Income and Savings Plans written enquiries | Régimes de revenu différé – Réponse aux demandes écrites |
| `3710` | Deferred Income and savings plans specimens reviews | Régimes de revenu différé et d’épargne (spécimens) |
| `3711` | Applications to register new pension plans and deferred profit sharing plans | Demandes d’agrément des régimes de pension et des régimes de participation différée aux bénéfices |
| `3713` | GST/HST rulings and interpretations - written enquiries | Décisions et interprétations en matière de TPS/TVH – Demandes écrites |
| `3714` | Applications for Charitable registration or re-registration | Demandes d&#39;enregistrement ou de réenregistrement d&#39;organismes de bienfaisance |
| `3716` | Actuarial Validation Report Reviews | Les rapports d’évaluation actuarielle |
| `3717` | Charities written enquiries | Demandes écrites des organismes de bienfaisance |
| `3718` | Problem Resolution | Solution de problèmes |
| `3719` | GST/HST rulings and interpretations - telephone enquiries | Décisions et interprétations en matière de TPS/TVH – Demandes de renseignements téléphoniques |
| `3720` | Charities telephone enquiries | Renseignements téléphoniques sur les organismes de bienfaisance (complexes) |
| `3721` | Clearance Certificate Requests | Demande de certificat de décharge |
| `3722` | One-time top-up to the Canada Housing Benefit (OTCHB)The last day to apply for the one-time top-up to the Canada Housing Benefit was March 31, 2023. | Supplément unique à l’Allocation canadienne pour le logement (SUACL) |
| `3723` | Luxury Tax Rebate Applications | Demande de remboursement de la taxe de luxe |
| `3724` | Luxury Tax Exemption Certificate | Certificat d&#39;exemption de la taxe de luxe |
| `3725` | Luxury Tax and Information Return Filing | Déclaration de la taxe de luxe et de renseignements |
| `3726` | Liaison Officer Service | Service d&#39;agents de liaison |
| `3727` | Canada Dental Benefit (CDB)To note: The interim Canada Dental Benefit ended on June 30, 2024. | Prestation dentaire canadienne (PDC) |
| `3728` | Canada Carbon Rebate (previously known as the Climate action incentive payment) | Remise canadienne sur le carbone (auparavant appelée paiement de l’incitatif à agir pour le climat) |
| `3729` | Community Volunteer Income Tax Program | Programme communautaire des bénévoles en matière d&#39;impôt |
| `3730` | Animal Health Movement Control Permit | Permis de contrôle des déplacements pour santé animale |
| `3731` | Special Outline for Veterinary Biologics | Protocole spécial pour produits biologiques vétérinaires |
| `3732` | Outline of Production - Veterinary Biologics | Protocole de production pour produits biologiques vétérinaires |
| `3733` | Adjudication of Immigration and Refugee cases | Décision des cas d’immigration et de statut de réfugié |
| `3734` | Ministerial Exemption for the Purpose of Selling a Test Market Food | Exemptions ministérielles pour vendre un aliment d&#39;essai |
| `3735` | Federal Policing Security Intelligence | Renseignement de sécurité de la Police Fédérale |
| `3736` | Air Carrier Support Centre (ACSC) | Centre de soutien aux transporteurs aériens (CSTA) |
| `3737` | Trade Compliance Verification | Vérifications de l&#39;observation commerciale |
| `3738` | TCS Website - Inquiries Page | SDC Site web - page de demandes |
| `3739` | Sanctions asset seizure and forfeiture implementation, including review of orders for the seizure of assets. | Mise en œuvre de la saisie et de la confiscation des biens en vertu des sanctions, y compris la révision des ordonnances de saisie des biens. |
| `3740` | Administration to the Canada Fund for Local Initiatives (CFLI) | Administration du Fond Canadien d&#39;Initiative Local |
| `3741` | Coordinate Canada&#39;s engagement in the G7 and G20 at the Leaders and Foreign Ministers levels, including time-sensitive meetings and rapid responses to emerging global events. | Coordonner la participation du Canada au G7 et au G20 au niveau des dirigeants et des ministres des Affaires étrangères, y compris les réunions urgentes et les réponses rapides aux événements mondiaux émergents. |
| `3757` | Short-Term Rental Enforcement Fund (STREF) | Fonds pour l&#39;application des restrictions sur la location de courte durée (FARLCD) |
| `38` | Secure Remote Access | Accès à distance protégé |
| `39` | Midrange | Ordinateurs de milieu de gamme |
| `4` | Food Recalls and safety alerts | Rappels d&#39;aliments et avis de sécurité |
| `40` | Mainframe | Ordinateur central |
| `4000` | School Food Infrastructure Fund | Fonds pour l&#39;infrastructure alimentaire scolaire |
| `4001` | Review of Complaints | L&#39;examen des plaintes |
| `4002` | Review of federal organization’s procurement practices | L’examen des pratiques d’approvisionnement des organisations fédérales |
| `4003` | Alternative Dispute Resolution | Règlement des différends |
| `4004` | Shared Ombuds services | Services d’ombuds partagés |
| `4005` | Enterprise Service Project Management | Gestion de projets de services d’entreprise |
| `4006` | Media Relations | Bureau des relations avec les médias |
| `4007` | Warehouse Assessment Services | Services d&#39;évaluation d&#39;entrepôt |
| `4008` | Events | Événements |
| `4009` | Tours | Visites guidées |
| `4010` | Exhibitions | Expositions |
| `4011` | LiquidFiles | FichersLiquides |
| `4012` | National Communications &amp; Public Affairs (NCPA) - Digital Communications | Communications nationales et Affaires publiques (CNAP) - Communications numériques |
| `4013` | Specialized Digital Systems | Systèmes numériques spécialisés |
| `4014` | Specialized Services | Services spécialisés |
| `4015` | General Consular Guidance | Assistance consulaire générale |
| `4016` | Personnel Security and Contracting | Sécurité du personnel et des marchés |
| `4017` | Domestic Physical Security | Sécurité matérielle nationale |
| `4018` | Registrations of Canadians Abroad (ROCA) | Inscription des Canadiens à l&#39;étranger |
| `4019` | Passport Services | Services de passeports |
| `4020` | Citizenship Services | Services de citoyenneté |
| `4021` | Access to Canadian Top Secret Network | Accès au Réseau canadien très secret |
| `4022` | Administration of Authorization Regime | Administration du régime d’autorisations |
| `4023` | Cyber Attributions | Connaissances des menaces cybernétiques |
| `4024` | Digital Platform for Grants and Contributions Management | Plateforme numérique pour la gestion des subventions et des contributions |
| `4025` | Engineering Service | Service d&#39;ingénierie |
| `4026` | Family Support Unit | Unité de soutien aux familles |
| `4027` | Government in Council (GIC) and Ministerial Appointments | Nominations par le gouverneur en conseil (GEC) et ministérielles |
| `4028` | Integrated support for international assistance programming (G&amp;Cs, RBM, Risk, APP, specialist support: gender, environment, sexual exploitation and abuse) | Ressources en matière de Gestion axée sur les résultats (GAR) |
| `4029` | Labour Relations Centre of Expertise - Corporate Services | Centre d&#39;expertise en relations de travail - Services ministériels |
| `4030` | LES Benefits management - End of service entitlements | Gestion des prestations ERP - indemnités de départ |
| `4031` | LES Benefits management - Financial Operations/Management and Oversight - Contract and invoice Management | Gestion des prestations ERP - opérations financières/gestion et surveillance - Gestion des contrats et des factures |
| `4032` | LES Benefits management - Financial Operations/Management and Oversight - Funds Management | Gestion des prestations ERP - opérations financières/gestion et surveillance - Gestion des fonds |
| `4033` | LES Benefits management - Insured Benefit Plans | Gestion des avantages sociaux des ERP - Régimes de prestations assurées |
| `4034` | LES HR Framework - LES Labour Relations and Terms and Conditions of Employment | Cadre des RH ERP - Relations de travail et termes et conditions d&#39;emploi des ERP |
| `4035` | LES HR Framework -Management of Program and Policy Design for Performance management | Cadre des RH ERP - Gestion de la conception des programmes et politiques pour la gestion du rendement |
| `4036` | LES HR Framework -Policy Stewardship - Management of Program and Policy Design for Staffing, Classification, Labour Relations and Terms and Conditions of Employment | Cadre des RH ERP - Gestion des politiques et direction de la conception des programmes et des politiques pour la dotation, la classification, les relations de travail et les conditions d&#39;emploi |
| `4037` | LES HR Framework- Salary scale determination &amp; administration | Cadre de RH ERP-Établissement et administration des échelles salariales |
| `4038` | LES HR learning Framework -Management of Program and Policy Design for Learning | Cadre des RH ERP - Gestion de la conception des programmes et des politiques pour l’apprentissage |
| `4039` | LES Leave Admin system tool (Avilar) Pilot | Projet pilote (Avilar) du système d&#39;administration des congés ERP |
| `4040` | LES Program co-lead for LES HR systems Software as a service contract requirements | Co-direction du programme ERP pour le contrat de service des logiciels des systèmes de RH ERP |
| `4041` | LES Social Security Participation management | Gestion de la participation des ERP aux régimes locaux de sécurité sociale |
| `4042` | Parliamentary briefing materials for Deputy Ministers and Ministers | Documents de breffage parlementaire à l&#39;intention des sous-ministres et des ministres |
| `4043` | Request for Particulars | Demande de renseignements |
| `4044` | Seasonal Influenza Immunization for Locally Engaged Staff | Vaccination contre la grippe saisonnière pour les employés recrutés sur place |
| `4045` | Electronic Procurement Solution (EPS) | Solutions d&#39;achats électroniques (SAE) |
| `4046` | CanadaBuys Service Desk (Level 1) | Bureau D&#39;aide Achats Canada (Niveau 1) |
| `4047` | Onboarding Services | Services d&#39;intégration |
| `4048` | Federal Policing Border Integrity | Intégrité frontalière de la police fédérale |
| `4049` | Information Requests | Demande d`informations |
| `4050` | Regional Security Operations Division | Direction des opérations de sécurité régionales |
| `4051` | Consular Case Management | Gestion de cas consulaire |
| `4052` | Advice to the Minister | Conseils au ministre |
| `4053` | Canadian Technology Accelerator | Accélérateurs technologiques canadiens |
| `4054` | Consular and emergency communications | Communications consulaires et d&#39;urgence |
| `4055` | Diplomatic Security Liasion Services | Services de liaison pour la protection des diplomates |
| `4056` | Economic modelling | Modélisation économique |
| `4057` | Export Permit Services (Softwood Lumber and Logs) | Service des licences d&#39;exportation (bois d&#39;œuvre résineux and billes de bois) |
| `4058` | Governance of LES-Missions&#39; Management Consultative Board processes | Gouvernance du processus de Consultations entre les Conseils de direction des missions et les ERP |
| `4059` | Provide leadership on Emergency Response and Preparedness for Health International Assistance portfolio. | Assurer la direction en matière de réponse et de préparation aux urgences pour le secteur d&#39;assistance internationale en santé. |
| `4060` | Provision of humanitarian assistance and operational response to natural disasters abroad in developing countries | Prestation d&#39;assistance humanitaire et réponse opérationnelle aux catastrophes naturelles à l&#39;étranger dans les pays en développement |
| `4061` | Rapid Response Mechanism (RRM) | Mécanisme de réponse rapide (MRR) |
| `4062` | Moodle | Moodle |
| `4063` | Reconciliation and Indigenous engagement advice and policy development | Activités de réconciliation et de mobilisation des Autochtones et élaboration de politiques |
| `4064` | Horizontal Policies (Greening) - strategic environmental and economic assessments, compliance management, public statements, and reporting mandatory for all departmental proposals to Cabinet (ie. Budget asks, TB subs, MCs, regulations) | Services d&#39;appoint en matière de politiques (recherche, analyse et conseils en matière de politiques). |
| `4065` | Workstation Software Provisioning | Approvisionnement en logiciels de poste de travail |
| `4066` | Wide Area Network (WAN) | Réseau étendu (RE) |
| `4067` | Intra-building Network | Réseau à l’intérieur des immeubles |
| `4068` | External Network Connectivity | Connectivité au réseau externe |
| `4069` | Parliamentary District Policing Program | Programme de services de police du district parlementaire |
| `4070` | Assault-Style Firearms Compensation Program | Programme d&#39;indemnisation pour les armes à feu de style arme d&#39;assaut (PIAFSAA) |
| `4071` | Preparation of the Federal Budget | Préparation du budget fédéral |
| `4072` | Lead Coordination of Financial Sector | Préparation du budget fédéral |
| `4073` | International Economic Leadership | Préparation du budget fédéral |
| `4074` | Research and Innovation Programs Benefits Administration | Administration des avantages des programmes de recherche et d’innovation |
| `4075` | Online Services | Services en ligne |
| `4076` | ATIP Requests Processing | Traitement des demandes d’AIPRP |
| `4077` | Paper Records Management | gestion des documents papier |
| `4078` | Canadian Grain Sampling Program Sample Inspection | Inspection d’échantillon du Programme canadien d’échantillonnage des grains |
| `4079` | Christmas Tree Export Program | Programme d&#39;exportation d&#39;arbres de Noël |
| `4080` | Disability Benefits Program Benefits Administration | Administration des avantages du Programme de prestations d’invalidité |
| `4081` | Financial Assistance and Income Replacement Programs Benefits Administration | Administration des avantages des programmes d’aide financière et de remplacement du revenu |
| `4082` | Commemorative Benefits and Services | Avantages et services commémoratifs |
| `4083` | Financial Support for Health Care Programs | Soutien financier pour les programmes de soins de santé |
| `4085` | Development of Official-Language Communities – Post-Secondary Sector and Scientific Knowledge in French Support Fund | Développement des communautés de langue officielle - Fonds d’appui au secteur postsecondaire et aux savoirs scientifiques en français |
| `4086` | Multiculturalism and Anti-Racism Initiatives - National Holocaust Remembrance Program | Multiculturalisme et la lutte contre le racisme - Programme national de commémoration de l’Holocauste |
| `4087` | Indigenous Business Navigator Service | Service de navigateur pour les entreprises autochtones |
| `4088` | Commemorating the National Day for Truth and Reconciliation | Commémoration de la Journée nationale de la vérité et de la réconciliation |
| `4089` | Trade Missions and Events | Missions et activités commerciales |
| `4090` | Greener Neighbourhoods Pilot Program | Programme pilote pour des quartiers plus verts |
| `4091` | Oil Spill Response Challenge | Défi d’intervention en cas de déversement d’hydrocarbures |
| `4092` | Clean Energy for Rural and Remote Communities - demonstration stream | Énergie propre pour les collectivités rurales et éloignées - volet démonstration |
| `4093` | Consumer Information Centre | Centre d&#39;information aux consommateurs |
| `4094` | Oral Health Access Funding (OHAF) applications&#39; review and transfer of funds to eligible recipients | Oral Health Access Funding (OHAF) applications&#39; review and transfer of funds to eligible recipients |
| `4095` | Oral health providers claims&#39; and estimates&#39; processing and payment as part of the Canadian Dental Care Plan | Traitement des réclamations et des demandes d&#39;autorisations préalables et paiement aux fournisseurs de soins buccodentaires dans le cadre du Régime canadien de soins dentaires |
| `4096` | Compliance response and enforcement escalation | Réponse en matière de conformité et escalade en matière d&#39;application |
| `4097` | Compliance response and enforcement action to a Type I mandatory recall (MO) | Réponse en matière de conformité et mesures coercitives à la suite d&#39;un rappel obligatoire (MO) de type I |
| `4098` | Regulatory and legislative advice and guidance | Conseils et orientations en matière de réglementation et de legislation |
| `4099` | Education and Outreach | Éducation et sensibilisation |
| `41` | Storage | Stockage |
| `4100` | International, Intergovernmental and Stakeholder Relations | Relations internationales, intergouvernementales et avec les parties prenantes |
| `4101` | Status Confirmation Service | Service de confirmation du statut |
| `4102` | Office of Controlled Substances Licensed Dealer | Bureau des substances contrôlées Distributeur agréé |
| `4103` | Emergency Treatment Fund | Fonds d&#39;urgence pour le traitement |
| `4104` | Medical Access Support | Assistance en matière d&#39;accès aux soins médicaux |
| `4105` | Tobacco Quit Lines | Lignes d&#39;aide pour arrêter de fumer |
| `4106` | Approval of retained controlled substances by law enforcement | Autorisation de conservation des substances contrôlées par les forces de l&#39;ordre |
| `4107` | Licensing and registration recommendation | Recommandation en matière de licences et d’enregistrements |
| `4108` | Regulatory exemption guidance | Orientation sur les exemptions réglementaires |
| `4109` | Canadian Coast Guard Marine Operations and Response Transfer Payment Program | Programme de paiements de transfert pour les opérations maritimes et les interventions de la Garde côtière canadienne |
| `4110` | Certification and Market Access Program for Seals Contribution Agreement (CMAPS) | Le Programme de certification et d&#39;accès aux marchés des produits du phoque (PCAMPP) |
| `4111` | Contribution Program for Pacific Salmon Foundation | Programme de contribution à la Fondation du saumon du Pacifique |
| `4112` | Contribution Program For Salmon Sub-Committee | Programme de contribution au sous-comité du Saumon |
| `4113` | Contribution Program for The T. Buck Suzuki Environmental Foundation | Programme de contribution avec la T. Buck Suzuki Environmental Foundation |
| `4114` | External Dissemination of Commercial Fisheries Statistics | Dissémination externe des statisques des pêches commerciales |
| `4115` | Global oceanographic in situational data from the Global Telecommunication System | Données océanographiques mondiales in situ provenant du Système mondial de télécommunication |
| `4116` | Lost Fishing Gear Reporting Support Service | Service de soutien à la déclaration des engins de pêche perdus |
| `4117` | Marine Spatial Planning Atlas | Atlas de planification spatiale marine |
| `4118` | Media Relations | Relations médias |
| `4119` | Multi-Partners Oil Spill Response Research Contribution Program | Programme de contribution à la recherche en matière d’intervention à partenaires multiples lors d’un déversement d’hydrocarbures |
| `4120` | Offline Licensing Services | Services d&#39;émission de permis hors ligne |
| `4121` | Pacific Salmon Commercial Transition Program | Programme de transition commerciale pour le saumon du Pacifique |
| `4122` | Pacific Salmon Conservation and Stewardship Partnerships Program | Programme de partenariats pour la conservation et la gestion du saumon du Pacifique |
| `4123` | Public Enquiries | Demande de renseignements du public |
| `4124` | Sustainable Fisheries Contribution Program - Shared Ocean Fund (Indo-Pacific Strategy) | Programme de contribution aux pêches durables - Fonds commun pour les océans (Stratégie indo-pacifique) |
| `4125` | Consular Enquiries | Renseignements consulaires |
| `4126` | Cannabis Product Recalls management (type I) | Gestion des rappels de produits à base de cannabis (type I) |
| `4127` | Stakeholder engagement and communications | Engagement des parties prenantes et communications |
| `4128` | Strategic policy and planning for stakeholder relations with various groups on the opioid overdose crisis and chronic pain | Politique stratégique et planification des relations avec les parties prenantes de divers groupes concernant la crise des surdoses d&#39;opioïdes et la douleur chronique |
| `4129` | Provide executive leadership, oversight and decision-making | Assurer la direction exécutive, la supervision et la prise de decisions |
| `4130` | Compliance monitoring and reporting | Surveillance et rapports de conformité |
| `4131` | Policy development and regulatory updates | Élaboration de politiques et mises à jour réglementaires |
| `4132` | Ship Security Alert System (SSAS) Testing | Système d’alerte de sécurité du navire |
| `4133` | CSC National Victim Services Program: Process victim registration request | Programme national de services aux victims du SCC : demande d&#39;inscription |
| `4134` | CSC National Victim Services Program: Process Victim Statement | Programme national de services aux victims du SCC : traiter les déclarations de la victime |
| `4135` | CSC National Victim Services Program: Notify of offender&#39;s conditional release | Programme national de services aux victims du SCC : aviser les victimes de la mise en liberté sous condition d&#39;un délinquant |
| `4136` | GC Workplace Accessibility Passport (My Accessible Workplace) | Passeport pour l’accessibilité en milieu de travail du GC (Mon milieu de travail accessible) |
| `4137` | Pleasure Craft Operator Cards (PCOC) issued | Cartes de conducteur d’embarcation de plaisance (CCEP) délivrée |
| `4138` | Request or extend a certificate of bareboat registry | Demander ou prolonger un certificat d’immatriculation d’un bâtiment en affrètement coque nue |
| `4139` | Ship radio equipment technical review | Examen technique de l’équipement radio maritime |
| `4140` | Determination of Closest Possible Compliance (Marine) | Détermination de la conformité la plus proche possible (maritime) |
| `4141` | Navigation Safety Assessment Process (NSAP) | Processus d’évaluation de la sécurité de la navigation (PESN) |
| `4142` | Automated Emergency Notification Fan-Out Service (AENFOS) | Service automatisé de notification d’urgence en cascade (SANUC) |
| `4143` | Issuance of a certificate or endorsement not requiring examination other than medical examination (marine) | Délivrance d’un brevet ou d’un visa n’exigeant pas d’examen autre qu’un examen médical (marine) |
| `4144` | Issuance of a record of qualifications and examinations | Délivrance d’un relevé de qualifications et d’examens |
| `4145` | Replacement of certificate or endorsement (except for certificate or endorsement lost owing to shipwreck) (marine) | Remplacement d’un brevet, d’un certificat de compétence ou d’un visa, à l’exception d’un brevet, d’un certificat de compétence ou du visa perdu en raison d’un naufrage (marine) |
| `4146` | Development of Official-Language Communities – Post-Secondary Sector and Scientific Knowledge in French Support Fund | Développement des communautés de langue officielle - Fonds d’appui au secteur postsecondaire et aux savoirs scientifiques en français |
| `4147` | Receive and review notification of Public Interest Disclosures under the Privacy Act. | Recevoir et examiner les notifications de communications dans l&#39;intérêt public par les institutions fédérales en vertu de la Loi sur la protection des renseignements personnels. |
| `4148` | CCOHS Business Safety Portal | Portail pour la sécurité en entreprise du CCHST |
| `4149` | Intake and Printing - Personal Registration applications | Réception et impression - Demandes d&#39;enregistrement personnel |
| `4150` | Access to Guided Tours of the Governor General&#39;s Official Residences (free) | Accès aux visites guidées des résidences officielles du gouverneur général (gratuit) |
| `4151` | Provisioning of Greetings and Messages from the Governor General | Envoi de messages et de vœux du gouverneur général |
| `4152` | Recognition of Canadian Excellence with the Canadian Honors and Awards Programs | Reconnaissance de l&#39;excellence canadienne grâce aux programmes d&#39;honneurs et de distinctions canadiens |
| `4153` | Earthquake Early Warning System | Système d&#39;alerte précoce en cas de tremblement de terre |
| `4154` | Conduct a Review | Effectuer un examen |
| `4155` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `4156` | Media and Public Inquiries | Médias et demandes de renseignements du public |
| `4157` | Quasi-judicial review of certain ministerial authorizations | Examen quasi judiciaire de certaines autorisations |
| `4158` | Customs Brokers Professional Examination | Examen de compétences professionnelles des courtiers en douane |
| `4159` | Customs Brokers Licensing | Agrément des courtiers en douane |
| `4160` | Incidents and Investigations | Incidents et investigations - Explosifs |
| `4161` | Outreach | Sensibilisation - Explosifs |
| `4162` | Comprehensive Nuclear-Test-Ban Treaty (CTBT) International Monitoring System (IMS) | Traité d&#39;interdiction complète des essais nucléaires (TICE) Système international de surveillance (SIS) |
| `4163` | Geomagnetic Monitoring and Space Weather Forecasting (GMSWF) | Surveillance géomagnétique et prévisions météorologiques spatiales |
| `4164` | Nuclear Emergency Response (NER) | Intervention en cas d&#39;urgence nucléaire |
| `4165` | Seismic Monitoring (SM) | Surveillance sismique |
| `4166` | Earthquake Early Warning System | Le système d’alerte sismique précoce canadien |
| `4167` | Canada Housing Infrastructure Fund (CHIF) | Fonds canadien pour les infrastructures liées au logement (FCIL) |
| `4168` | Canada Public Transit Fund (CPTF) | Fonds pour le transport en commun du Canada (FTCC) |
| `4169` | Funding for Research Training and Talent Development | Financement de la formation en recherche et du développement des talents |
| `4170` | Funding for Discovery Research | Financement de la recherche axée sur la découverte |
| `4171` | Funding for Research and Technology Partnerships | Financement des partenariats en recherche et en technologie |
| `4172` | EPS Operations | Opérations de la SAE |
| `4173` | AgriAssurance Program: Kosher and Halal Investment Component | Programme Agri-assurance : Volet Investissement casher et halal |
| `4174` | Agricultural Clean Technology Program: Research and Innovation Stream - Accelerator | Programme des technologies propres en agriculture : Volet Recherche et innovation - Accélérateur |
| `4175` | AgriMarketing Program: Kosher and Halal Investment Component | Programme Agri-marketing : Volet Investissement casher et halal |
| `4176` | AgriMarketing Program: Market Diversification - National Industry Association Component | Programme Agri-marketing : Volet Diversification des marchés pour les associations nationales de l’industrie |
| `4177` | AgriMarketing Program: Market Diversification - Small and Medium-sized Entreprise | Programme Agri-marketing : Diversification des marchés pour les petites et moyennes entreprises |
| `4178` | Kosher and Halal Investment Program | Programme d’investissement casher et halal |
| `4179` | Program Payment Services Unit | Unité des services de paiement des programmes |
| `4180` | Tax Payer Relief Provisions | Dispositions d’allègement pour les contribuables |
| `4181` | Canadian Beacon Registry (CBR) | Registre canadien des balises |
| `4182` | Military spouse employment initiative | Initiative d’emploi pour les conjoints de militaires |
| `4183` | National Claims &amp; Litigation Directorate | Direction nationale des réclamations et du contentieux |
| `4184` | Service-related injury or illness benefits administered by Veterans Affairs Canada | Programmes de soins de santé pour une blessure ou une maladie liée au service administrés par Anciens Combattants Canada |
| `4185` | National Communications &amp; Public Affairs (NCPA) - Intellectual Property Office | Communications nationales et Affaires publiques (CNAP) - Bureau de la propriété intellectuelle |
| `4186` | National Armourer Program (IPTMP) | Programme national d’armurerie (SPAPTM) |
| `4187` | Police Dog Service Training Centre (PDSTC) | Centre de dressage des chiens de police (CDCP) |
| `4188` | Physical Security Program - Lead Security Agency for Physical Security and Internal Services for Physical Security | Programme de sécurité matérielle – Le principal organisme responsable de la sécurité matérielle (POSM) et services internes de sécurité matérielle |
| `4189` | Receive and review codes of practice submitted in accordance with Proceeds of Crime (Money Laundering) and Terrorist Financing Regulations (PCMLTFR) | Recevoir et examiner les codes de pratique soumis conformément au Règlement sur le recyclage des produits de la criminalité et le financement des activités terroristes (RRPCFAT) |
| `4190` | Potato Wart Program | Programme de la galle verruqueuse de la pomme de terre |
| `4191` | Livestock Feeds Licence | Licence d&#39;aliments pour animaux de ferme |
| `4192` | Insight Research | Programme de recherche axée sur la connaissance |
| `4193` | Research Partnerships | Programme de partenariats de recherche |
| `4194` | Canada Biomedical Research Fund | Fonds de recherche biomédicale du Canada |
| `4195` | Research Support Fund | Fonds de soutien à la recherche |
| `423` | Conduct Complaints | Plaintes pour inconduites |
| `424` | Interference Complaints | Plaintes pour ingérence |
| `425` | Direct Funding Payments | Paiements d&#39;aide financière directs |
| `426` | Immigration Appeals | Appels en matière d&#39;immigration |
| `427` | Admissibility Hearings | Enquêtes |
| `428` | Detention Reviews | Contrôle des motifs de détention |
| `429` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `44` | Middleware | Intergiciel |
| `45` | Database | Base de données |
| `46` | Cloud Brokering | Courtage infonuagique |
| `47` | Classified Infrastructure | Infrastructure classifiée |
| `48` | Workplace Technology Devices Provisioning | Approvisionnements des appareils technologiques en milieu de travail |
| `49` | Web Conferencing | Cyberconférence |
| `5` | Regulatory Clarification | Clarification règlementaires |
| `50` | Audio Conferencing | Téléconférence |
| `51` | Satellite | Satellite |
| `52` | Internet | Internet |
| `53` | Review and Appeal hearings | Audiences de révision et d&#39;appel |
| `57` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `6` | Service Complaints | Plaintes de service |
| `655` | Grant, Scholarship and Fellowship Funding Transfers to Administering Institution | Transferts de subventions et de bourses d&#39;études et de perfectionnement à des établissements administrateurs |
| `656` | Grant, Scholarship, Fellowship and Award Administration | Administration des subventions, des bourses de perfectionnement et des bourses d&#39;études |
| `657` | CanNor Grants and Contributions | Subventions et contributions CanNor |
| `658` | Access to Information and Privacy (ATIP) | Accès à l&#39;information et protection des renseignements personnels (AIPRP) |
| `659` | Youth Justice Fund | Fonds du système de justice pour les jeunes |
| `660` | Victims Fund | Fonds d&#39;aide aux victimes |
| `661` | Justice Partnership and Innovation Program | Programme juridique de partenariats et d&#39;innovation |
| `662` | Indigenous Justice Program | Programme de justice autochtone |
| `663` | Access to Justice in Both Official Languages Support Fund | Fonds d’appui à l’accès à la justice dans les deux langues officielles |
| `664` | NEXUS Program Application | Traitement des demandes de participation au programme NEXUS |
| `665` | CANPASS Suite of Programs Application | Traitement des demandes de participation à la suite de programmes CANPASS |
| `666` | Remote Area Border Crossing (RABC) Permit Application | Permis de Passage à la frontière dans les régions éloignées (PFRE) |
| `667` | Free and Secure Trade Program (FAST) Driver Application | Traitement des demandes de participation au programme Expéditions rapides et sécuritaires (EXPRES) |
| `668` | Commercial Driver Registration Program (CDRP) Application | Traitement des demandes du Programme d&#39;inscription des chauffeurs du secteur commercial (PICSC) |
| `669` | Traveller Processing | Traitement primaire des voyageurs |
| `670` | Air Traveller Processing | Traitement primaire des voyageurs - mode aérien |
| `671` | Rail Traveller Processing | Traitement primaire des voyageurs - mode ferroviaire |
| `672` | Marine Traveller Processing | Traitement primaire des voyageurs - mode maritime |
| `673` | Immigration Secondary (Temporary Resident Program) Visitor | Immigration secondaire (Programme des résidents temporaires) Visiteur |
| `674` | Immigration Secondary - (Temporary Resident Program) Work Permit | Immigration secondaire (Programme des résidents temporaires) Permis de travail |
| `675` | Immigration Secondary (Temporary Resident Program) Study Permit | Immigration secondaire (Programme des résidents temporaires) Permis d&#39;études |
| `676` | Immigration Secondary - (Temporary Resident Program) Temporary Resident Permit | Immigration secondaire (Programme des résidents temporaires) Visa de résident temporaire |
| `677` | Immigration Secondary - Criminal Rehabilitation | Immigration secondaire - Réhabilitation criminelle |
| `678` | Refugee Claims | Demandes d&#39;asile |
| `679` | Border Information Service (BIS) | Service d&#39;information sur la frontière (SIF) |
| `680` | Customs Special Services | Services spéciaux des douanes |
| `687` | Hydrometric data and information service | Service de données et d&#39;informations hydrométriques |
| `688` | Health and air quality forecast services | Services de prévision relatifs à la santé et à la qualité de l&#39;air |
| `689` | Marine program weather services | Services du programme météorologique maritime |
| `690` | Direct Funding Payments | Versements faits directement aux boursiers |
| `691` | Funding Transfers to Administering Institutions | Transferts des fonds de subventions et de bourses aux établissements administrateurs |
| `694` | Services to Businesses and Business Organizations | Services aux entreprises et aux organismes commerciaux |
| `7` | Canada Pension Plan (CPP) Benefits | Prestations du Régime de pensions du Canada |
| `707` | Services to Communities | Services aux collectivités |
| `712` | Registry Services | Services de greffe |
| `716` | Business Information Services | Service d&#39;information aux entreprises de l&#39;APECA |
| `717` | Public Inquiries | Demandes de renseignements du publique |
| `718` | Provision of Information - Access to Information | Communication de renseignements - Accès à l&#39;information |
| `719` | Carrier Code Application | Code de transporteur - Demande de participation |
| `720` | Courier Low Value Shipments (CLVS) Program Application | Demande de programme des messageries d&#39;expéditions de faible valeur (EFV) |
| `721` | Partners in Protection Program Membership Application Processing | Traitement des demandes d&#39;adhésion au programme Partenaires en protection |
| `722` | Trusted Trader Application- Customs Self-Assessment (CSA) | Demande de négociant digne de confiance - Programme d&#39;autocotisation des douanes (PAD) |
| `723` | Cultural Property Export Permits | Biens culturels - Délivrance des licences d&#39;exportation |
| `724` | Request for Assistance Application for Intellectual Property Rights (IPR) | Demande d&#39;aide de droits de propriété intellectuelle |
| `725` | Employee Assistance Services | Services d’aide aux employés |
| `726` | Employee Assistance Services: Employee Assistance Program | Services d’aide aux employés : Programme d’aide aux employés |
| `728` | Commercial Processing (highway, air, rail, marine, postal and courier) | Traitement commercial (routier, aérien, ferroviaire, maritime, postaux et messageries) |
| `729` | Processing Vehicle Import Forms 1 and 3 | Traitment des formulaires d&#39;importation de véhicles 1 et 3 |
| `730` | Public Service Occupational Health Program: Occupational Health Evaluations | Programme de santé au travail de la fonction publique: Évaluations de la santé au travail |
| `731` | Customs Bonded Warehouse Licence Application | Agrément d&#39;entrepôt de stockage des douanes |
| `732` | Public Service Occupational Health Program: Communicable Disease Prevention and | Programme de santé au travail de la fonction publique: Conseils relatifs à la prévention des maladies transmissibles |
| `733` | Customs Sufferance Warehouse License Application | Agrément d&#39;entrepôt d&#39;attente des douanes |
| `734` | Customs Broker Professional Examination and Customs Broker Licencing | Examen de compétences professionnelles des courtiers en douane et Agrément des courtiers en douane |
| `735` | Public Service Occupational Health Program: Occupational Hygiene Advice and Cons | Programme de santé au travail de la fonction publique: Conseils et consultations en matière d&#39;hygiène du travail |
| `736` | Public Service Occupational Health Program: Fitness to Work Evaluations | Programme de santé au travail de la fonction publique: Évaluations de l&#39;aptitude au travail |
| `737` | Release Prior to Payment Privilege | Privilège de la mainlevée avant le paiement |
| `738` | Public Service Occupational Health Program: Reviews for Pension Purposes | Programme de santé au travail de la fonction publique: Examens aux fins de pension de retraite |
| `739` | Public Service Occupational Health Program: Overseas Services | Programme de santé au travail de la fonction publique: Services à l’étranger |
| `740` | Duties Relief Program Application | Exonération des droits |
| `741` | Duty Free Shop Licence Application | Demandes d&#39;agrément de boutique hors taxes |
| `742` | Coasting Trade License (CTL) Application | Demande de licence de cabotage |
| `743` | Casual Refunds | Remboursement pour les importations occasionnelles |
| `744` | B2 Commercial Adjustments | Rajustements du secteur commercial (B2) |
| `745` | Advance Rulings and National Customs Rulings | Décisions anticipées et décisions nationales des douanes |
| `746` | Drawback Claims | Demandes de drawback |
| `747` | Access to Information and Privacy | Accès à l&#39;information et la protection des renseignements personnels |
| `748` | Feedback Mechanism | Mécanisme de rétroaction |
| `749` | Enforcement and Appeals Litigation | Appels des mesures d&#39;exécution et litige |
| `750` | Trade Appeals and Litigation | Appels des échanges commerciaux et litige |
| `751` | Employee Assistance Services: Specialized Organizational Services | Services d’aide aux employés : Services organisationnels spécialisés |
| `752` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `753` | Employee Assistance Services: Trauma Services | Services d’aide aux employés : Services d’intervention post-traumatique |
| `754` | Employee Assistance Services: Informal Conflict Management Services | Services d’aide aux employés : Services d&#39;assistance aux employés: Services de gestion informelle des conflits |
| `755` | Electronic Data Interchange (EDI) - Application and Testing Process | Échange de données informatisé (EDI) – Processus de demande et d’essai |
| `756` | Employee Assistance Services: Occupational Critical Incident Stress Management ( | Services d&#39;aide aux employés : Gestion du stress professionel à la suite d&#39;un incident critique (GSPIC) |
| `757` | Funding Decisions for Grants to Researchers | Décisions sur le financement des subventions de recherche |
| `758` | Funding Decisions for Institutional Capacity | Décisions de financement relatives à la capacité institutionnelle |
| `759` | Grant, Scholarship, Fellowship and Award Administration | Administration des subventions, des bourses et des octrois |
| `761` | Claim for Exemption under the Hazardous Materials Information Review Act | Demande de dérogation en vertu de la Loi sur le contrôle des renseignements relatifs aux matières dangereuses |
| `762` | National Dose Registry | Fichier dosimétrique national |
| `763` | National Dosimetry Services | Services nationaux de la dosimétrie |
| `764` | Health Care Policy Contribution Program | Programme de contributions pour les politiques en matière de soins de santé |
| `765` | Official Languages Health Program | Programme pour les langues officielles en santé |
| `766` | Canadian Thalidomide Survivors Support Program | Programme canadien de soutien aux survivants de la thalidomide |
| `767` | Policy Development Contribution Program | Programme de contributions pour l&#39;élaboration de politiques |
| `768` | Health Canada General Enquiries | Renseignements généraux pour Santé Canada |
| `770` | Statement of Need Program | Programme de déclaration de besoin pour les médecins diplômés |
| `771` | Health Canada Publications | Publications de Santé Canada |
| `772` | Food and Drugs Act Liaison Office (FDALO) | Bureau de liaison pour la Loi sur les aliments et les drogues (BLLAD) |
| `775` | National Disaster Mitigation Program | Programme national d&#39;atténuation des catastrophes |
| `779` | Emergency Management Exercises | Exercices de gestion des urgences |
| `788` | Virtual Risk Analysis | Analyse virtuelle des risques |
| `789` | Critical Infrastructure Gateway | Portail des infrastructures essentielles |
| `790` | Industrial Control Systems Symposiums and Technical Workshops | Symposium et ateliers techniques pour la sécurité des systèmes de contrôle |
| `792` | Critical Infrastructure Exercises | Exercices des infrastructures essentielles |
| `795` | Cyber Security Cooperation Program | Programme de coopération en matière de cybersécurité |
| `798` | Passenger Protect Inquiries Office (PPIO) | Demandes de renseignement du Programme de protection des passagers (BRPPP) |
| `8` | Email | Courriel (Yes et Legacy) |
| `800` | Access to information and privacy | Accès à l’information et protection des renseignements personnels |
| `801` | Safeguarding Science Outreach | Sensibilisation de la science en sécurité |
| `803` | Listed Terrorist Entities | Entités terroristes inscrites |
| `805` | Ministerial Correspondence | Correspondance ministérielle |
| `806` | Canada Centre for Community Engagement and Prevention of Violence | Centre canadien d&#39;engagement communautaire et de prévention de la violence |
| `808` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnel |
| `809` | Public Awareness Campaigns | Campagnes de sensibilisation auprès de la population |
| `810` | Aboriginal Community Safety Development Contribution | Contribution à l&#39;amélioration de la sécurité des collectivités autochtones |
| `811` | Contribution to Combat Serious and Organized Crime | Programme de contribution pour combattre les crimes graves et le crime organisé |
| `813` | Major International Events Security Cost Framework | Cadre sur les coûts de sécurité des événements internationaux majeurs |
| `814` | Nation&#39;s Capital Extraordinary Policing Costs | Contribution pour les coûts extraordinaire des services de police de la capitale nationale |
| `815` | National Flagging System Class Grant | Global de subventions du système national de repérage |
| `816` | Grants and Contributions Program to National Voluntary Organizations | Programme de subventions et de contributions pour les organismes bénévoles nationaux |
| `817` | Biology Casework Analysis Contribution Program | Programme de contribution aux analyses biologiques |
| `818` | National Office for Victims | Bureau national pour les victimes d&#39;actes criminels |
| `822` | Crime Prevention Inventory | Répertoire en prévention du crime |
| `832` | Federal Leadership on Corrections and Criminal Justice Research | Leadership fédéral en recherche correctionnelle et en justice criminelle |
| `838` | NewsDesk | InfoMedia |
| `839` | Federal Emergency Communications Coordination | Coordination des communications fédérales d&#39;urgence |
| `840` | Coordination of Federal Emergency Management (Government Operations Centre) | Coordination de la gestion fédérale des situations d&#39;urgence (Centre des opérations du gouvernement) |
| `843` | GCdocs | Gcdocs |
| `844` | GCcase | GCcas |
| `845` | Regional Resilience Assessments | Évaluations de la résilience régionale |
| `846` | Grants for the Disposal of Surplus Lighthouses | Programme de subventions et de contributions pour l&#39;aliénation de phares excédentaires |
| `849` | Media Relations | Relations médias |
| `850` | Category A - Authorizations under the Pest Control Product Regulations | Catégorie A - L&#39;autorisation en vertu du Règlement sur les produits antiparasitaires |
| `851` | Grant and contribution programs | Programmes de subventions et contributions |
| `859` | Category B - Authorizations under the Pest Control Product Regulations | Catégorie B - L&#39;autorisation en vertu du Règlement sur les produits antiparasitaires |
| `860` | Category C - Authorizations under the Pest Control Product Regulations | Catégorie C - L&#39;autorisation en vertu du Règlement sur les produits antiparasitaires |
| `861` | Category D - Authorizations under the Pest Control Product Regulations | Catégorie D - L&#39;autorisation en vertu du Règlement sur les produits antiparasitaires |
| `862` | Category E - Authorizations under the Pest Control Product Regulations | Catégorie E - L&#39;autorisation en vertu du Règlement sur les produits antiparasitaires |
| `863` | Category F - Authorizations under the Pest Control Product Regulations | Catégorie F - L&#39;autorisation en vertu du Règlement sur les produits antiparasitaires |
| `864` | Category L - Authorizations under the Pest Control Product Regulations | Catégorie L - L&#39;autorisation en vertu du Règlement sur les produits antiparasitaires |
| `865` | Pest Management Information Service | Service de renseignements sur la lutte antiparasitaire |
| `866` | User Requested Minor Use Label Expansions (URMULE) | Profil d&#39;emploi pour les usages limités à la demande des utilisateurs (PEPUDU) |
| `867` | Application for the Inspection of Confidential Test Data | Demande d&#39;examen des données d&#39;essai confidentielles |
| `868` | Category P – Pre-submission Consultation | Catégorie P - Consultations préalables aux demandes d&#39;homologation |
| `869` | Access to information and privacy | Accès à l’information et protection des renseignements personnels |
| `870` | Translation | Traduction |
| `871` | Interpretation | Interprétation |
| `872` | Terminology Standardization | Normalisation terminologique |
| `873` | Executive Correspondence | Correspondance de la haute gestion |
| `874` | Certificate of Pharmaceutical Product (CPP) &amp; Good Manufacturing Practices (GMP) | Certificat de produit pharmaceutique (CPP) de Bonnes Pratiques de Fabrication (BPF) |
| `875` | Drug Establishment Licensing (DEL) | Les licences d&#39;établissement de produits pharmaceutiques (LEPP) |
| `876` | Manufacturer&#39;s Certificate to Export licenced medical devices from Canada (MCE) | Certificat du fabricant relatif à l&#39;exportation d&#39;instruments médicaux homologués au Canada (CFE) |
| `877` | Medical Device Establishment Licencing (MDEL) | Licence d&#39;établissement pour les instruments médicaux (LEIM) |
| `878` | Registration of a Cells, Tissues and Organs (CTO) Establishment | Inscription d&#39;un établissement des Cellules, des Tissus et des Organes (CTO) |
| `879` | Drug Analysis Service (DAS) - Forensic analysis services | Service d&#39;analyse des drogues (SAD) – Services d&#39;analyse judiciaire |
| `880` | Drug Analysis Service (DAS) - Support services | Service d&#39;analyse des drogues (SAD) – Services de soutien |
| `881` | Federal Leadership on Crime Prevention Research | Leadership fédérale en matière de recherche sur la prévention du crime |
| `882` | First Nations and Inuit Policing Program (FNIPP) | Programme des Services de Police des Premières Nations et des Inuits (PSPPNI) |
| `888` | Grants and Contributions Services | Services des subventions et contributions |
| `890` | National Emergency Strategic Stockpile: Request for Assistance (RFA) | Réserve nationale stratégique d&#39;urgence |
| `891` | Authorization to Conduct Controlled Activities with Pathogens and Toxins | Autorisation d’exercer des activités réglementées avec des agents pathogènes et des toxines |
| `892` | Human Pathogens and Toxins Act Security Clearance | Loi sur les agents pathogènes et les toxines (LAPHT) autorisation de sécurité |
| `895` | Yellow Fever Vaccination Centre Designation | Désignation d&#39;un centre de vaccination contre la fièvre jaune |
| `896` | Access to Information and Privacy (ATIP) | Accès à l&#39;information et la protection des renseignements personnels (AIPRP) |
| `898` | Public Enquiries | Demandes de renseignement |
| `899` | Public Health Agency of Canada Publications | Publications de l&#39;Agence de la santé publique du Canada |
| `900` | Pension Administration – Pension Payments and Services | Administration des pensions – Prestations et services de pension |
| `901` | Receiver General Services – Management of Government of Canada Deposits | Services du receveur général ‒ Gestion des dépôts du gouvernement du Canada |
| `902` | Receiver General Services – Issuing payments | Services du receveur général Émission de paiements |
| `903` | Common Departmental Financial System | Système financier ministériel commun |
| `904` | Document Imaging Services | Services d&#39;imagerie documentaire |
| `905` | Canadian General Standards Board | Office des normes générales du Canada |
| `906` | Seized Property Management Directorate | Direction de la gestion des biens saisis |
| `907` | Complaints Information and Enquiry | Renseignements général et plaintes |
| `908` | GCSurplus | GCSurplus |
| `909` | Advertising – Coordination, Advisory and Training Services | Publicité ‒ Services de coordination, services-conseils et de formation |
| `910` | Public Opinion Research – Coordination, Advisory and Knowledge Management Services | Recherche sur l&#39;opinion publique ‒ Services de coordination, services-conseils et services de gestion des connaissances |
| `911` | Canada Gazette – Publication of Official Notices, Laws and Regulations | Gazette du Canada ‒ Publication des avis officiels, de lois et de règlements |
| `912` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `913` | Centralized Electronic Access to Government of Canada Publications | Accès électronique centralisé aux publications du gouvernement du Canada |
| `914` | Reference Services for Government of Canada Publications | Services de référence pour les publications du gouvernement du Canada |
| `915` | Licence application for nuclear substances and radiation devices | Demandes de permis de substances nucléaires et d’appareils à rayonnement |
| `916` | Copyright Media Clearance Program | Programme d’autorisation pour les médias protégés par les droits d’auteur |
| `917` | Licence application for Class II nuclear facilities and prescribed equipment | Demandes de permis pour installations nucléaires et équipement réglementé de catégorie II |
| `918` | Import or export licence application | Demande de permis d’importation ou d’exportation |
| `919` | Application for certification of exposure device operators | Demande d’accréditation des opérateurs d’appareil d’exposition |
| `920` | Transport licence application | Demande de permis de transport |
| `921` | Participant Funding Program | Programme de financement des participants |
| `9223` | Climate Change Funding Programs - Implementation Readiness Fund | Programmes de financement pour le changement climatique - Fonds de préparation à la mise en œuvre |
| `924` | Professional and Technical Services | Services Professionnels et Techniques |
| `925` | Ministerial Correspondence | Correspondance ministérielle |
| `926` | Canadian Firearms Program (CFP) - Firearms Licensing for individuals | Programme canadien des armes à feu (PCAF) - Permis d&#39;armes à feu pour les particuliers |
| `927` | Canadian Firearms Program (CFP) - Firearms Licensing for businesses | Programme canadien des armes à feu (PCAF) - Permis d&#39;armes à feu pour les entreprises |
| `928` | National Forensic Laboratory Services (NFLS) | Services nationaux de laboratoire judiciaure (SNLJ) |
| `929` | Certified Criminal Record Checks | Attestation de vérification de casier judiciaire |
| `930` | Canadian Criminal Real Time Identification Services (CCRTIS) - Accreditation Services | Les Services canadiens d&#39;identification criminelle en temps réel (SCICTR) - Service d&#39;accréditation |
| `931` | Integrated Forensic Identification Services (IFIS)- Disaster Victim Identification (DVI) | Service intégré de l&#39;identité judiciaire (SIIJ) - d&#39;identification des victimes de catastrophes (IVC). |
| `932` | National DNA Data Bank (NDDB) Indices Comparison | Banque nationale de données génétiques - comparaison des indices (BNDG) |
| `934` | Canadian Police Information Centre (CPI Centre) | Centre d&#39;information de la police canadienne (Centre IPC) |
| `935` | Canadian Police College (CPC) | Collège canadian de police (CCP) |
| `936` | National Law Enforcement Training (NLET) | Groupe de la formation policière nationale (GFPN) |
| `937` | Access to Information and Privacy (ATIP) | Accès à l’information et de protection des renseignements personnels (AIPRP) |
| `938` | Contract Security (Company Registration, Personal Security Screening, Call Centre) | Sécurité des contrats (enregistrement d&#39;une entreprise, filtrage de la sécurité du personnel, centre d&#39;appels) |
| `939` | Integrity Verification Services | Services de vérification d&#39;intégrité |
| `940` | Controlled Goods (Company Registration, Security Assessments, Exemption Applications for Visitors, Temporary Workers and International Students) | Marchandises contrôlées (enregistrement des entreprises, évaluations de sécurité, demandes d&#39;exemption pour les visiteurs, les travailleurs temporaires et étudiants étrangers) |
| `941` | Fairness Monitoring Services | Services de surveillance de l&#39;équité |
| `942` | Business Dispute Management Services | Gestion des conflits d&#39;ordre commercial |
| `943` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `944` | Secure Air Travel Act Recourse | Recours en vertu de la Loi sur la sûretés des déplacement aériens |
| `946` | Federal Leadership on Law Enforcement and Policing Research | Leadership fédéral en recherche en matière d&#39;application de la loi et la police |
| `947` | Passport Cancellation Reconsideration | Réexamen de l&#39;annulation des passeports |
| `949` | Registry Services (Registrar) | Service du greffe (greffier) |
| `95` | Intra-building Network Services | Services de réseau à l’intérieur des immeubles |
| `950` | Library Services | Service de Bibliothèque |
| `951` | Visitor Services and Experiences | Services et expériences aux visiteurs |
| `952` | Accommodation services in Parks Canada&#39;s Places | Services d&#39;hébergement dans les endroits de Parcs Canada |
| `954` | Issuance of Leases and Licenses of Occupation | Émission de baux et de permis d&#39;occupation |
| `955` | Townsite Management | Gestion des lotissements urbains |
| `956` | Atlantic Fisheries Fund | Fonds des pêches de l&#39;Atlantique |
| `957` | Lockage Services | Service d&#39;éclusage |
| `960` | Shared Travel Services | Services de voyage partagés |
| `961` | Access to Information Service | Service d&#39;accès à l&#39;information |
| `962` | Output-Based Pricing System (OPBS) Registration System | Système de tarification fondé sur le rendement |
| `963` | National Environmental Emergencies Centre | Centre National des Urgences Environnementales |
| `965` | Antarctic Environmental Protection Act permitting | Délivrance de permis - Loi sur la protection de l’environnement en Antarctique |
| `966` | GC Accommodations space management system | Système de gestion de l&#39;espace de GC locaux |
| `967` | Property and Facility Management | Gestion des biens et des installations |
| `968` | Events and Conference Management | Gestion d&#39;événements et de conférences |
| `969` | Architecture and Engineering | Architecture et génie |
| `970` | Payments in Lieu of Taxes | Paiements en remplacement d&#39;impôts |
| `971` | Real Estate Services | Services des biens immobiliers |
| `972` | Property Portfolio and Asset Advisory Services | Services consultatifs en matière de gestion de portefeuilles de biens immobiliers et de biens |
| `973` | Environment, Health and Safety Services for Real Property | Services en matière d&#39;environnement, de santé et de sécurité pour les biens immobiliers |
| `974` | Geomatics Services | Services géomatique |
| `975` | Federal Identification Registry for Storage Tank Systems (FIRSTS) | Registre fédéral d&#39;identification des systèmes de stockage (RFISS) |
| `977` | Ecological Gifts Program | Programme des dons écologiques |
| `978` | Public and Media Inquiries | Demandes de renseignements du public et des médias |
| `979` | Climate Change Funding Programs - Low Carbon Economy Challenge: Partnerships | Défi pour une économie à faibles émissions de carbone: volet des partenariats |
| `980` | Climate Change Funding Programs - Climate Action Fund | Le Fonds d&#39;action pour le climat |
| `981` | Public Inquiries Centre | Centre de renseignements à la population |
| `982` | Ministerial Correspondence | Correspondance ministérielle |
| `983` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `984` | Shared Human Resources Services | Services partagés en ressources humaines |
| `985` | Import permits for species harmful to Canadian ecosystems | Permis d&#39;importation d&#39;espèces nuisibles aux écosystèmes du Canada |
| `986` | Permits for trade in protected species | Permis pour le commerce d&#39;espèces protégées |
| `987` | Migratory Birds: all other permits | Oiseaux migrateurs: autres permis |
| `988` | Permits under the Wildlife Area Regulations | Permis en vertu du Règlement sur les réserves d&#39;espèces sauvages |
| `989` | Complaint Investigation of Suspected Inaccurate Measurement | Enquête sur les plaintes concernant les mesures inexactes soupçonnées |
| `990` | Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `991` | Canada Pension Plan Disability Benefits | Prestations d’invalidité du Régime de pensions du Canada |
| `992` | Northern Scientific Training Program (NSTP) | Programme de formation scientifique dans le Nord (PFSN) |
| `993` | Transfer Payments to Support Research and Activities Relating to the Polar Region | Paiements de transfert pour soutenir la recherche et les activités qui ont trait aux régions polaires |
| `994` | Transfer Payments to Support the Advancement of Northern Science and Technology | Programme de paiements de transfert en appui aux progrès scientifiques et technologiques dans le Nord |
| `995` | Access to Information and Privacy | Accès à l&#39;Information et Protection des Renseignements Personnels |
| `996` | Aids to Navigation | Aides à la navigation |
| `997` | British Columbia Aquaculture Regulatory Program | Programme de réglementation de l&#39;aquaculture en Colombie-Britannique - Modifications administratives |
| `998` | British Columbia Aquaculture Regulatory Program - Minor Technical Amendments | Programme de réglementation de l&#39;aquaculture en Colombie-Britannique - Modifications techniques mineures |
| `999` | British Columbia Aquaculture Regulatory Program - Applications for new licenses | Programme de réglementation de l&#39;aquaculture en Colombie-Britannique - Nouveaux sites et modifications techniques majeures |
| `SRV02642` | Test Market Authorization | Autorisation d&#39;essai de mise en marché |
| `SRV02643` | Ministerial Exemptions for the Purpose of Alleviating a Shortage in Canada | Exemptions ministérielles pour atténuer une pénurie d&#39;approvisionnement au Canada |
| `SRV02646` | Ministerial Exemption - Authorization Request, Movement of Products under SFCR | Exemption Ministre - Demande d&#39;autorisation pour mouvement de produits en vertu du RSAC |
| `SRV02647` | Meat Work Shift Agreements | Les ententes relatives aux périodes de travail de viande |
| `SRV02648` | C-PIQ - Canadian Partners in Quality Participation Program | Programme des partenaires pour la qualité au Canada (PPQ-C) |
| `SRV02649` | Certificate of Free Sale | Certificat de vente libre |
| `SRV02650` | Permit to Operate an Animal Semen Production Centre | Permis pour opérer un centre de production de sperme animal |
| `SRV02651` | Licence to operate a hatchery | Licence pour exploiter un couvoir |
| `SRV02652` | Accredited Veterinarian Agreement | Entente d&#39;accréditation des vétérinaires |
| `SRV02653` | Veterinarian Certification Procedure to Export Embryos | Procédure pour des vétérinaires de certification des embryons destinés à l&#39;exportation |
| `SRV02654` | Accredited External Laboratories | Laboratoires d&#39;accrédité externes |
| `SRV02655` | Soil Handling Program | Programme de manipulation de la terre |
| `SRV02656` | Aquatic Animal Domestic Movements | Déplacements d&#39;animaux aquatiques en territoire canadien |
| `SRV02657` | Specified Risk Material (SRM) Permit | Permis pour les matières à risque spécifiées (MRS) |
| `SRV02658` | Time-Sensitive Specified Risk Material (SRM) Permit | Permis de transport rapide pour les matières à risque spécifiées (MRS) |
| `SRV02659` | Cervid Movement Permit | Permis de déplacement des cervidés |
| `SRV02660` | Livestock Feed Registration or Renewal | Enregistrement ou renouvellement des aliments pour animaux de ferme |
| `SRV02661` | Research Exemption with Safety - Research with Livestock Feeds | Dispense de recherche avec la sécurité - Recherche sur les aliments pour animaux de ferme |
| `SRV02662` | Research Exemption - Research with Livestock Feeds | Dispense de recherche - Recherche sur les aliments pour animaux de ferme |
| `SRV02663` | Research Authorization- Research with Livestock Feeds | Autorisation de recherche - Recherche sur les aliments pour animaux de ferme |
| `SRV02664` | Product Licensing Submissions for Veterinary Biologics | Demandes d&#39;homologation de nouveaux produits |
| `SRV02665` | Veterinary Biologics Serial Release | Mise en circulation des séries de produits biologiques vétérinaires |
| `SRV02666` | Label review for major and or minor Veterinary Biologics | Évaluation de l&#39;étiquette |
| `SRV02667` | Aquatic Animal Health Compartmentalization Program | Programme de compartimentation santé des animaux aquatiques |
| `SRV02668` | Equine Infectious Anemia Control Program | Programme de lutte contre l&#39;anémie infectieuse des équidés |
| `SRV02669` | Chronic Wasting Disease Herd Certification Programs | Programmes de certification des troupeaux pour la maladie débilitante chronique |
| `SRV02670` | Scrapie Flock Certification Program | Programme de certification des troupeaux à l&#39;égard de la tremblante |
| `SRV02671` | Canadian Ractopamine-Free Poultry Certification Program | Programme canadien de certification des volailles exemptes de ractopamine |
| `SRV02672` | Canadian Ractopamine-Free Pork Certification Program | Programme canadien de certification des porcs exempts de ractopamine |
| `SRV02673` | Canadian Beta Agonist-Free Beef Certification Program | Programme canadien de certification des bovins exempts de bêta-agonistes |
| `SRV02674` | Certifying Freedom from Growth Enhancing Products - Beef to the EU | Programme Canadien de certification de l&#39;absence de stimulants de croissance pour l&#39;exportation de viande bovine à l&#39;Union Européenne |
| `SRV02675` | Growth Enhancing Products-Free (GEPs-Free) Veal Certification Program | Programme de certification des veaux exempts de produits stimulants de croissance (PSC) |
| `SRV02676` | Permit to release mink coronavirus experimental vaccine for emergency use | Permis de dissémination du vaccin expérimental pour visons contre le coronavirus pour les besoins d&#39;urgence |
| `SRV02677` | Import Plant-based Feed Ingredients | Importation d&#39;ingrédients d&#39;origine végétale destinés aux aliments du bétail |
| `SRV02678` | Import Animal Products and By-Products | Importation des produits et sous-produits d&#39;animaux terrestres |
| `SRV02679` | Import Aquatic Animals | Importation d&#39;animaux aquatiques |
| `SRV02680` | Import Animal Pathogens | Importation des zoonoses pathogènes |
| `SRV02681` | Import Veterinary Biologics | Importation de produits biologiques vétérinaires |
| `SRV02682` | Veterinary Biologics Export Certificates | Certificats d&#39;exportation de produits biologiques vétérinaires |
| `SRV02683` | Export Certificates - live animal, animal products and by-products | Certificats de santé pour l&#39;exportation - des produits et sous-produits d&#39;animaux terrestres |
| `SRV02687` | Licence to Print Official Seed Tag | Licence pour imprimer des etiquettes officielles de semence |
| `SRV02688` | Multiplication Agreement for Varietal Certification of Seed Multiplied Abroad | Entente de multiplication pour la certification variétale des semences à l&#39;étranger |
| `SRV02689` | Recognition of Export Grain Analysis by Authorized Laboratories (REGAL) program | Le Programme de laboratoires autorisé pour l&#39;analyse des grains à l&#39;exportation (PLAAGE) |
| `SRV02690` | Seed Import Conformity Assessor | Évaluateur de la conformité des semences importee |
| `SRV02691` | Research Authorization under the Fertilizers Act and Regulations | Autorisation d&#39; recherches en vertu de la Loi sur les engrais |
| `SRV02692` | Unconfined Environmental Release Authorization | Autorisation de la dissémination en milieu ouvert |
| `SRV02693` | Confined Research Field Trial Authorization (PBO) | Autorisation de la conduite d&#39;essais de recherche au champ en conditions confinées |
| `SRV02694` | Authorized Exporter Program | Programme d&#39;exportateur autorisé |
| `SRV02695` | Evaluation and Recognition of Third Party Auditors | l&#39;évaluation et à la reconnaissance des tiers auditeurs |
| `SRV02696` | Hay Export Program | Programme d&#39;exportation de foin |
| `SRV02697` | Canadian Nursery Certification Program | Programme canadien de certification des pépinières |
| `SRV02698` | Niger Seed Export Program | Programme d&#39;exportation de graines de niger |
| `SRV02699` | Seed Potato Tuber Quality Management Program | Programme de gestion de la qualité des tubercules de pommes de terre de semence |
| `SRV02700` | Canadian Debarking Grub Hole Control Program for Export of Cedar Forest Products | Programme canadien d&#39;écorçage du bois et de contrôle des trous de vers (PCEBCTV) pour l&#39;exportation de produits forestiers de thuya vers l&#39;Union européenne |
| `SRV02701` | Forage (Heated) Export Program | Programme d&#39;exportation des fourrages séchés à la chaleur |
| `SRV02702` | Pre-Shipment Approval Program for the Export of Grain from Canada | Programme d&#39;approbation pré-expédition s&#39;appliquant au grain exporté par le Canada |
| `SRV02703` | Fruit Tree Export Program | Programme d&#39;exportation d&#39;arbres fruitiers |
| `SRV02704` | Grain, Seed, Screening Program | Programme des grains, semences, criblures |
| `SRV02705` | Canadian Heat Treated Wood Products Certification Program | Programme canadien de certification des produits de bois traités à la chaleur |
| `SRV02706` | Canary Seed Export Program | Programme d&#39;exportation de l&#39;alpiste des Canaries |
| `SRV02707` | Hardwood Export Program | Programme d&#39;exportation de bois de feuillus |
| `SRV02708` | Wild Rice Export Program | Programme d&#39;exportation de riz sauvage |
| `SRV02709` | Canadian Sawn Wood Certification Program | Programme canadien de certification du bois scié |
| `SRV02710` | United States – Canada Greenhouse-Grown Plant Certification Program | Programme États-Unis - Canada de certification des végétaux cultivés en serre |
| `SRV02711` | Canadian Growing Media Program, Approval Process and Import Requirements | Programme canadien des milieux de culture, processus d&#39;approbation préalable et exigences en matière d&#39;importation de végétaux enracinés dans des milieux de culture approuvés |
| `SRV02712` | Grapevine Export Program | Programme d&#39;exportation de la vigne |
| `SRV02713` | Systems Approach Based Oriental Fruit Moth Certification Program | Programme de certification visant la tordeuse orientale du pêcher fondé sur une approche systémique |
| `SRV02714` | Plant Pest Containment Program | Programme de confinement pour phytoravageurs |
| `SRV02715` | Canadian Phytosanitary Certification Program for Seed (CPCPS) | Programme canadien de certification phytosanitaire des semences (PCCPS) |
| `SRV02716` | SMSRC Response and Support Coordination program | CSRIS Programme de coordination de l’intervention et du soutien |
| `SRV02717` | Sexual Misconduct Support and Resource Centre 24/7 Support Line | Centre de soutien et de ressources sur l&#39;inconduite sexuelle (CSRIS) Ligne de Soutien 24/7 |
| `SRV02718` | SMRC Contribution Program | Programme de contributions du CIIS |
| `SRV02719` | Restorative Engagement | Démarches Réparatrices |
| `SRV02720` | Licence to Use Seed Potato Certification Tags | Permis pour utiliser des Étiquettes de certification des pommes de terre de semence |
| `SRV02721` | Emerald Ash Borer Program | Programme de l&#39;agrile du frêne |
| `SRV02722` | Japanese Beetle Program | Programme du scarabée japonais |
| `SRV02723` | Apple Maggot Program | Programme de la mouche de la pomme |
| `SRV02724` | Woolly Cup Grass | prévenir la propagation d&#39;Eriochloa villosa (ériochloé velue) |
| `SRV02725` | Canadian Grain Sampling Program | Programme canadien d&#39;échantillonnage des grains |
| `SRV02726` | Barberry Propagation Program | Programme de multiplication de l&#39;épine-vinette |
| `SRV02727` | Blueberry Certification Program | Programme de certification des bleuets |
| `SRV02728` | Crop Variety Registration (VRO) | Enregistrement des variétés |
| `SRV02729` | Fertilizer or Supplement Registration | Enregistrement d&#39;engrais ou de supplément |
| `SRV02730` | Plant Breeders&#39; Rights (PBR Certificate) | Protection des obtentions végétales |
| `SRV02731` | Phytosanitary Certificate for Export | Certificat phytosanitaire pour l&#39;exportation |
| `SRV02732` | Seed Analysis Certificate for Export Purposes (CFIA 1113) | Certificat d&#39;analyse de semences aux fins d&#39;exportation |
| `SRV02733` | Certificate of Origin (Plant Pests / LDD) | Certificat d&#39;origine (spongieuse nord-américaine, Lymantria dispar) |
| `SRV02734` | Re-export Phytosanitary Certificate | certificats phytosanitaires de réexportation |
| `SRV02735` | Request for Opinion or Data Review for Livestock Feeds | Demande d&#39;avis ou d&#39;examen de données pour les aliments du bétail |
| `SRV02736` | Regulatory Opinion PNT/VRO | Avis réglementaire (VCN/BEV) |
| `SRV02737` | Ask CFIA | Demandez à l&#39;ACIA |
| `SRV02738` | General Enquiries | Demande de renseignements |
| `SRV02739` | Plant Health Investigation - Incident Response | Enquête sur la salubrité des végétaux - intervention en cas d’incident |
| `SRV02740` | Non-propagative Potato Program | Programme de pommes de terre non destinées à la multiplication |
| `SRV02741` | Notice of Import Conformity | Ll&#39;avis de libération |
| `SRV02742` | Destination Inspection Service (DIS) | Service d&#39;inspection à destination (SID) |
| `SRV02743` | Licenced Seed Crop Inspector | Inspecteur de cultures de semences agréés |
| `SRV02744` | Authorized Seed Crop Inspection Service | Service d&#39;inspection de cultures de semences autorisés |
| `SRV02745` | Agriculture Climate Solutions | Solutions Agricoles Pour le Climat |
| `SRV02746` | Market Development Program for Turkey and Chicken | Programme de développement des marchés du dindon et du poulet |
| `SRV02747` | The Poultry and Egg-On Farm Investment Program | Le Programme d&#39;investissement à la ferme pour la volaille et les œufs |
| `SRV02748` | Supply Management Processing Investment Fund | Le Fonds d&#39;investissement pour la transformation des produits sous la gestion de l&#39;offre |
| `SRV02750` | Disposal at sea emergency permits | Permis d’immersion en mer d’urgence |
| `SRV02751` | Environmental emergencies | Urgences environnementales |
| `SRV02752` | Accreditation of Seed Graders | Accréditation de classificateurs de semences |
| `SRV02753` | Brown Spruce Longhorned Beetle Program | Programme du longicorne brun de l&#39;épinette |
| `SRV02754` | Growers Crop Certificate - &#34;Seed Potato Certification Program&#34; | Certificat de culture des producteurs - « Programme de certification des pommes de terre de semence » |
| `SRV02755` | Fertilizer Export Certificates | Certificats d&#39;exportation pour l&#39;engrais |
| `SRV02762` | Permit to Import - Plants and Plant Products | Permis d&#39;importation - les végétaux et les produits végétaux |
| `SRV02763` | Notice to Industry | Avis à l&#39;industrie |
| `SRV02764` | Preventative Control Inspection | l&#39;inspection de contrôle préventif |
| `SRV02765` | Supporting a Humanitarian Workforce to Respond to COVID-19 and Other Large-Scale Emergencies | Appuyer une main-d&#39;œuvre humanitaire pour répondre à la COVID-19 et à d&#39;autres urgence de grande envergure |
| `SRV02766` | Building Safer Communities Fund | Fonds pour bâtir des communautés sécuritaires |
| `SRV02767` | Written Authorization to Conduct Activities on Plant Pests | Autorisation écrite de mener des Activités sur des phytoravageurs |
| `SRV02768` | Regional Air Transportation Initiative (RATI) | L’Initiative régionale de transport aérien (ITAR) |
| `SRV02769` | Care and Custody | Prise en charge et garde |
| `SRV02770` | Plant Movement Certificate | Certificat de circulation de végétaux |
| `SRV02771` | Canada Community Revitalization Fund (CCRF) | Le Fonds canadien de revitalisation des communautés (FCRC) |
| `SRV02772` | Tourism Relief Fund (TRF) | Le Fonds d’aide au tourisme |
| `SRV02773` | Jobs and Growth Fund (JGF) | Le Fonds pour l’emploi et la croissance |
| `SRV02774` | Aerospace Regional Recovery Initiative (ARRI) | L’Initiative de relance régionale de l’aérospatiale (IRRA) |
| `SRV02775` | Data Centre Facilities | Installations des centres de données |
| `SRV02776` | Public Awareness Contribution Program (PACP) | Programme de contribution à la sensibilisation du publique (PCEP) |
| `SRV02779` | Real Property Contract Oversight Services | Services de surveillance des contrats immobiliers |
| `SRV02780` | Project Management | Gestion de projet |
| `SRV02783` | Correctional Interventions | Interventions correctionnelles |
| `SRV02784` | Community Supervision | Surveillance dans la collectivité |
| `SRV02785` | Indigenous Reconciliation Transfer Payment Program - RAP - Contributions | Programme de paiements de transfert de la réconciliation avec les Autochtones - contributions |
| `SRV02786` | Treaty Related Measures Contribution Agreement (TRM) | Entente de contribution sur les mesures liées aux traités (ETR) |
| `SRV02787` | Network Services | Services de réseau |
| `SRV02789` | Application for Cannabis Record Suspension | Demande de suspension du casier liée au cannabis |
| `SRV02790` | Intellectual Property Centre of Expertise (IP CoE) | Centre d&#39;expertise en Propriété intellectuelle (CE PI) |
| `SRV02791` | Canada Digital Adoption Program - Boost Your Business Technology | Programme canadien d’adoption du numérique - Améliorez les technologies de votre entreprise |
| `SRV02792` | Weather Information Services to Public Authorities | Services d&#39;informations météorologiques aux autorités publiques |
| `SRV02793` | Meteorological Support for Environmental Emergency Response | Soutien météorologique pour les urgences environnementales |
| `SRV02795` | Temporary exemption for emergency circumstances under the Reduction of Carbon | Exemption temporaire pour situations d&#39;urgence en vertu du Règlement sur la réduction des émissions de dioxyde de carbone |
| `SRV02798` | Temporary waivers to fuel regulations | Exemptions temporaires en vertu des règlements sur les carburants |
| `SRV02800` | Antarctic Environmental Protection Act permitting | Protection de l&#39;environnement en Antarctique |
| `SRV02811` | Enhanced Nature Legacy - Indigenous-led Area Based Conservation | Conservation par zone menée par les Autochtones - Capacité et formation |
| `SRV02812` | Enhanced Nature Legacy - Indigenous-led Area Based Conservation - Establishment | Conservation par zone menée par les Autochtones - Établissement |
| `SRV02813` | Nature Smart Climate Solutions Fund | Fonds des solutions climatiques axées sur la nature |
| `SRV02814` | Avalanche Control | Contrôle des avalanches |
| `SRV02815` | GCXchange | GCéchange |
| `SRV02816` | Taxation Statistical Analyses and Data Processing | Analyse statistique et traitement de données de l’impôt |
| `SRV02817` | Debt Management Call Centre | Centre d’appels de la gestion des créances |
| `SRV02818` | Financial audits of the Public Accounts of Canada | Audit des états financiers des Comptes publics du Canada |
| `SRV02820` | Internal Audit | Audit Interne |
| `SRV02821` | Scientific Research and Experimental Development (SR&amp;ED) Tax Credits, Canadian film or video production tax credit (CPTC), and film or video production services tax credit (PSTC) – Claims not selected for a review or an audit | Crédit d’impôt pour la recherche scientifique et le développement expérimental (RS&amp;DE), crédit d’impôt pour production cinématographique ou magnétoscopique canadienne (CIPC) et crédit d’impôt pour services de production cinématographique ou magnétoscopique (CISP) Demandes non sélectionnées pour un examen ou une vérification |
| `SRV02822` | Scientific Research and Experimental Development (SR&amp;ED) Tax Credits – Refundable claims selected for a review | Crédit d’impôt pour la recherche scientifique et le développement expérimentale (RS&amp;DE) – demandes remboursables sélectionnées pour un examen |
| `SRV02823` | Event Management Service | Service de gestion d&#39;évenements |
| `SRV02824` | Canadian film or video production tax credit (CPTC) and film or video production services tax credit (PSTC) – Claims selected for an audit | Crédit d’impôt pour production cinématographique ou magnétoscopique canadienne (CIPC) et crédit d&#39;impôt pour services de production cinématographique ou magnétoscopique (CISP) – Demandes sélectionnées pour une vérification |
| `SRV02825` | Canada Worker Lockdown Benefit (CWLB) | Prestation canadienne pour les travailleurs en cas de confinement (PCTCC) |
| `SRV02826` | Hardest-Hit Business Recovery Program (HHBRP) | Programme de relance pour les entreprises les plus durement touchées (PREPDT) |
| `SRV02827` | Financial audit of Export Development Canada’s consolidated financial statements | Audit d’états financiers consolidés d’Exportation et développement Canada |
| `SRV02828` | Tourism and Hospitality Recovery Program (THRP) | Programme de relance pour le tourisme et l&#39;accueil (PRTA) |
| `SRV02829` | Financial audits of territorial organizations | Audits financiers des organisations territoriales |
| `SRV02830` | Canada Recovery Hiring Program (CRHP) | Programme d&#39;embauche pour la relance économique du Canada (PEREC) |
| `SRV02831` | Local Lockdown Program (LLP) | Programme de soutien en cas de confinement local |
| `SRV02832` | Internal Communications | Communications internes |
| `SRV02834` | Graphic Design Services | Services de conception graphique |
| `SRV02836` | Editing Services | Services de révision |
| `SRV02838` | Public Enquiries Services | Services de renseignements au public |
| `SRV02840` | Web services | Services web |
| `SRV02841` | Social Media Services | Services des médias sociaux |
| `SRV02842` | Strategic Communications | Communication Stratégiques |
| `SRV02843` | Digital Communications and Design Support | Communications numériques et aide à la conception |
| `SRV02844` | Consular Outreach and Stakeholder Engagement | Service de sensibilisation du Public |
| `SRV02845` | Media Relations | Relations avec les médias |
| `SRV02846` | Media monitoring and analysis | Surveillance et analyse des médias |
| `SRV02848` | Public Opinion Research and Consultations | Recherche en opinion publique et consultations |
| `SRV02849` | Financial audits of international organizations | Audits financiers des organisations internationales |
| `SRV02850` | Performance audits of territorial Organizations | Audit de performance d’organisations territoriales |
| `SRV02851` | International Relations Correspondence | Correspondance pour les relations internationales |
| `SRV02852` | Environmental petitions correspondence | Correspondance pour les pétitions environnementales |
| `SRV02853` | Environmental Petitions | Pétitions environnementales |
| `SRV02854` | Health Policy Branch Transfer Payment Programs | Programmes de paiements de transfert de la Direction générale des politiques de santé |
| `SRV02855` | Public inquiries | Demandes de renseignements du public |
| `SRV02856` | Media relations | Relations avec les médias |
| `SRV02857` | Technical accounting and audit advisory services | Services-conseils spécialisés en comptabilité et en audit |
| `SRV02859` | Grants and Contributions in Aid of Academic Relation | Subventions et contributions en appui aux relations academiques |
| `SRV02860` | Trade commissioner service | Services des délégués commerciaux |
| `SRV02862` | Foreign Direct Investment | Investissement direct étranger |
| `SRV02863` | Requests for designation, regional assessment, and strategic assessment | Des demandes de désignation, d&#39;évaluation régionale et d&#39;évaluation stratégique |
| `SRV02864` | Employee Assistance Services | Services d’aide aux employés |
| `SRV02865` | Public Service Occupational Health Program | Programme de santé au travail de la fonction publique |
| `SRV02866` | Hazardous Waste Export and Import Permits | Permis d’exportation et d’importation de déchets dangereux |
| `SRV02867` | Permit for disposal at sea | Permis pour l&#39;immersion en mer |
| `SRV02868` | Rapid Test Kit Provision (Federal) | Fourniture de kit de test rapide (fédéral) |
| `SRV02869` | International Accommodation Services | Services d&#39;hébergement internationaux |
| `SRV02870` | Client Relations | Relations avec les clients |
| `SRV02871` | Engineering Services | Service d&#39;ingénierie |
| `SRV02872` | Material Management Service | Service de gestion du matériel |
| `SRV02873` | Transfer and diffusion of space technology | Diffusion et transfert de technologies spatiales |
| `SRV02874` | Security Program Management Service | Service de gestion de programme de sécurité |
| `SRV02875` | Atmospheric data on carbon monoxide concentration (MOPITT on Terra) | Données atmosphériques sur la concentration de monoxyde de carbone (MOPITT sur Terra) |
| `SRV02876` | Criminal Code Designations | Désignations du Code criminel |
| `SRV02877` | Atmospheric data on ozone, aerosol &amp; nitrogen dioxide concentration (OSIRIS-Odin) | Données atmosphériques sur la concentration d’ozone, d’aérosols et de dioxyde d’azote (OSIRIS-Odin) |
| `SRV02878` | Atmospheric gas monitoring data (SCISAT) | Données de surveillance des gaz atmosphériques (SCISAT) |
| `SRV02879` | Space imagery data for Space Astronomy (NEOSSAT) | Données d’imagerie spatiale pour l&#39;astronomie (NEOSSAT) |
| `SRV02880` | Space imagery data for Space Surveillance (NEOSSAT) | Données d’imagerie spatiale pour la surveillance de l’espace (NEOSSAT) |
| `SRV02881` | National Information Services | Services national d&#39;information (SNI) |
| `SRV02882` | Earth Observation Data (RCM) | Données d&#39;observation de la Terre (MCR) |
| `SRV02883` | Earth Observation Data (R2) | Données d’observation de la Terre (R2) |
| `SRV02884` | Historical Earth observation data (R1) | Données historiques d&#39;observation de la Terre (R1) |
| `SRV02885` | Guidelines on risk-based monitoring of grants and contributions | Lignes directrices sur le suivi axé sur les risques des subventions et de contributions |
| `SRV02886` | Access to Places Administered by Parks Canada | Accès aux Lieux Administrés par Parcs Canada |
| `SRV02887` | Emergency Dispatch | Envoi d&#39;urgence |
| `SRV02888` | User support for SAR data (Service Desk) | Support aux utilisateurs des données SAR (Service Desk) |
| `SRV02889` | Support for SCISAT data users | Support aux utilisateurs des données SCISAT |
| `SRV02890` | Weights and Measures Calibration | L&#39;étalonnage des appareils de pesage et de mesure |
| `SRV02891` | Connecting Canadians to Canada’s Natural and Cultural Heritage | Connecter les Canadiens au Patrimoine Naturel et Culturel du Canada |
| `SRV02896` | Issuance of Research and Collections Permits | Délivrance de permis de recherche et de collections |
| `SRV02898` | Promotion and Disease Prevention: Communicable Disease Control and Management - Direct Service Delivery | Promotion et prévention des maladies : Contrôle et gestion des maladies transmissibles - Prestation directe de services |
| `SRV02899` | Pathways to Safe Indigenous Communities | Voies vers des communautés autochtones sûres |
| `SRV02900` | National Compensation Services (NCS) | Services nationaux de rémunération (SNR) |
| `SRV02901` | Substance Use and Addictions Program | Programme sur l’usage et des dépendances aux substances |
| `SRV02902` | Respond to requests for information and complaints of Cannabis promotion prohibitions | Répondre aux demandes d&#39;information et aux plaintes relatives aux interdictions de promotion du cannabis |
| `SRV02903` | Screening and Triage-Personal Registration | Examen et triage – Demandes d’inscription personnelle |
| `SRV02904` | Media Enquiries | Demandes des médias |
| `SRV02907` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `SRV02908` | Correspondence Referrals to other Departments (dep&#39;t email, contact us page) | Correspondance Renvois vers d&#39;autres départements (courriel du département, page Contactez-nous) |
| `SRV02909` | Departmental Correspondence (not including referrals) | Correspondance ministérielle (à l&#39;exclusion des renvois) |
| `SRV02910` | Public Enquiries (not referrals) | Demandes de renseignements du public (pas de renvois) |
| `SRV02911` | Ministerial Correspondence (SPB) | Correspondance ministérielle (DGPS) |
| `SRV02912` | Canadian Hazards Information Service (Untargeted) | Service canadien d&#39;information sur les risques (non ciblé) |
| `SRV02913` | GeoConnections Program | Programme GéoConnexions |
| `SRV02914` | Canada Greener Homes Initiative | Initiative canadienne pour des maisons plus vertes |
| `SRV02915` | Youth Employment and Skills Strategy - S &amp; T Internship Program - Green Jobs | Stratégie emploi et compétences jeunesse - le Programme de stages en sciences et technologie - emplois verts |
| `SRV02916` | Departmental Security Management System (DSMS) - Service name updated to :Security Screening Management System (SSMS) | Systeme de gestion du filtrage de sécurité (SGFS) |
| `SRV02917` | Open Science and Data Platform | Plateforme de science et de données ouvertes |
| `SRV02918` | Emissions Reduction Fund Offshore Deployment Program | Programme de déploiement extracôtier du fonds de réduction des émissions |
| `SRV02919` | Smart Grid Deployment Program | Programme de déploiement de réseaux intelligents |
| `SRV02920` | Emerging Renewable Power Program | Programme des énergies renouvelables émergentes |
| `SRV02921` | Smart Renewables and Electrification Pathways Program - Deployment | Programme des énergies renouvelables intelligentes et de trajectoires d’électrification - Déploiement |
| `SRV02922` | Strategic Interties Predevelopment Program | Programme de prédéveloppement des interconnexions stratégiques |
| `SRV02923` | Smart Renewables and Electrification Pathways Program - Capacity Building and Indigenous Engagement Grants | Programme des énergies renouvelables intelligentes et de trajectoires d’électrification - Renforcement des capacités et Subventions pour l’engagement des Autochtones |
| `SRV02924` | Nature Conservation | Conservation de la nature |
| `SRV02925` | Wildfire Emergency Response | Intervention d&#39;urgence en cas d&#39;incendie de forêt |
| `SRV02926` | Large Value Transfer Payment | Paiement de transfert de grande valeur |
| `SRV02927` | Results of the Survey of Private Sector Economic Forecasters | Résultats de l&#39;enquête auprès des prévisionnistes économiques du secteur privé |
| `SRV02928` | Law Enforcement | Forces de l&#39;ordre |
| `SRV02930` | Publication of key economic documents | Publication de documents économiques clés |
| `SRV02932` | CCOHS E-Learning | Apprentissage en ligne du CCHST |
| `SRV02933` | Value-Added Services Provided at Places Administered by Parks Canada | Services à valeur ajoutée offerts dans les lieux administrés par Parcs Canada |
| `SRV02934` | Visitor Safety and Search and Rescue | Sécurité des visiteurs et recherche et sauvetage |
| `SRV02935` | Water and Wastewater Treatment | Traitement de l’eau et des eaux usées |
| `SRV02936` | Clean Growth Hub | Carrefour de la croissance propre |
| `SRV02937` | Emergency geomatics and satellite mapping service | Service de géomatique d&#39;urgence et de cartographie par satellite |
| `SRV02938` | Satellite Ground Stations | Stations-relais pour satellites |
| `SRV02939` | Canada Map Office | Bureau des cartes du Canada |
| `SRV02940` | Clean Energy for Rural and Remote Communities Program - Capacity Building | Programme d&#39;énergie propre pour les collectivités rurales et éloignées - Renforcement des capacités |
| `SRV02941` | Radiological Risk Assessments | Évaluation des risques radiologiques |
| `SRV02942` | Human Monitoring and Assessment | Surveillance et évaluation humaines |
| `SRV02943` | National Calibration Reference Centre Performance Testing Program | Centre national de référenceProgramme de test de performance |
| `SRV02944` | National Radon Program | Programme national sur le radon |
| `SRV02945` | Provide Confidential Business Information Access in Emergencies | Fournir un accès confidentiel aux informations commerciales en cas d&#39;urgence |
| `SRV02946` | Chemical Emergency Response | Intervention d&#39;urgence chimique |
| `SRV02947` | Health Surveillance and Monitoring: Incident Reporting | Surveillance et contrôle de la santé: rapports d&#39;incidents |
| `SRV02948` | Nuclear Emergency Response | Réponse aux urgences nucléaires |
| `SRV02949` | Compliance and Enforcement: Risk Management of Urgent and Serious Events | La conformité et de l’application de la loi: La gestion des risques urgente et serieux |
| `SRV02950` | Congratulatory certificates from the Prime Minister | Certificats de félicitations du premier ministre |
| `SRV02951` | Requests for certified copies of Orders in Council | Demandes de copies certifiées de décrets |
| `SRV02952` | Emergency Air Quality Guidance | Conseils sur la qualité de l&#39;air en cas d&#39;urgence |
| `SRV02953` | Emergency Drinking Water Guidance | Conseils sur l&#39;eau potable en cas d&#39;urgence |
| `SRV02954` | OSFI External Website | Site web du BSIF |
| `SRV02955` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `SRV02956` | Major Rehabilitation Works on Victoria Bridge | Travaux de réhabilitation du pont Victoria |
| `SRV02957` | Contributions to Ensure Air Services to Remote Communities | Contributions visant à assurer le service de transport aérien aux collectivités éloignées |
| `SRV02958` | Airport Critical Infrastructure Program | Programme des infrastructures essentielles des aéroports |
| `SRV02959` | Airport Relief Fund | Fonds de soutien aux aéroports |
| `SRV02960` | Commissioners Office | Bureau du commissaire |
| `SRV02967` | Communication Services | Services de communication |
| `SRV02968` | Executive Services and Ministerial Liaison | Services exécutifs et liaison ministérielle |
| `SRV02969` | RCMP- Criminal Intelligence Service Canada (CISC) | (GRC) Service canadien de renseignements criminels (SCRC) |
| `SRV02970` | Real Property Management | Gestion des biens immobiliers |
| `SRV02972` | Operational Readiness and Response | Préparation et réponse opérationnelles |
| `SRV02973` | National Criminal Operations (NCROPS) | Opérations criminelles nationales (SNPC) |
| `SRV02974` | Operational Communication Centers (OCC) | Stations de transmissions opérationnelles (STO) |
| `SRV02975` | Strategic Policing Agreements and Service | Accords de services de police stratégiques et Service |
| `SRV02976` | Operational Systems Service Centre (OSSC) : | Centre de service des systèmes de la police opérationnels (CSSPO) |
| `SRV02977` | RCMP- National Crime Prevention and Indigenous Policing Services | (GRC) Services nationaux de prévention du crime et de police autochtone |
| `SRV02978` | Federal Policing Criminal Operations (FPCO) | Opérations Criminelles de la Police Fédérale (OCPF) |
| `SRV02979` | National Security | Sécurité nationale |
| `SRV02980` | RCMP- National Critical Infrastructure Team | (GRC) Équipe nationale des infrastructures essentielles |
| `SRV02981` | Canadian Air Carrier Protective Program | Programme de protection des transporteurs aériens canadiens |
| `SRV02982` | Protective Policing | Police de protection |
| `SRV02983` | RCMP- Witness Protection | (GRC) Protection des témoins |
| `SRV02984` | Project Seahorse | Projet Seahorse |
| `SRV02985` | National Intelligence | Renseignement national |
| `SRV02987` | Interpol/Europol | Interpol/Europol |
| `SRV02988` | Passport Selection | Sélection de passeports |
| `SRV02990` | Operational Information Management | Gestion de l&#39;information opérationnelle |
| `SRV02991` | International Operations and, Policing Development | Opérations internationales et développement des services de police |
| `SRV02992` | International Liaison and Coordination Centre | Centre de coordination et de liaison internationale |
| `SRV02993` | International Deployment Services | Services de déploiement international |
| `SRV02994` | International Health, Protection and Wellness | Santé, protection et bien-être international |
| `SRV02997` | RCMP- Canadian Police Information Center | (GRC) Centre d&#39;information de la police canadienne |
| `SRV02998` | RCMP- Canadian Criminal Real Time Identification Services | (GRC) Services canadiens d&#39;identification criminelle en temps réel |
| `SRV02999` | RCMP- Science and Strategic Partnerships | (GRC) Partenariats scientifiques et stratégiques |
| `SRV03000` | Air Services | Services aériens |
| `SRV03001` | Specialized Technical Investigative Services | Services d&#39;enquêtes techniques spécialisées |
| `SRV03002` | Protective Technical Services | Services techniques de protection |
| `SRV03003` | Chemical, Biological, Radiological, Nuclear and Explosives | Chimique, biologique, radiologique, nucléaire et explosifs |
| `SRV03004` | Behavioural Sciences Investigative Services (BSIS) | Services d&#39;enquêtes en sciences du comportement (SESC) |
| `SRV03005` | National Centre for Missing Persons and Unidentified Remains (NCMPUR) | Centre national pour les personnes disparues et les restes non identifiés (CNPDRN) |
| `SRV03006` | National Child Exploitation Crime Centre (NCECC) | Centre national contre l&#39;exploitation des enfants (CNCEE) |
| `SRV03007` | Truth Verification Section (TVS) | Section des contrôles de sincérité (SCS) |
| `SRV03008` | National Radio Services (NRS) | Programme de services radio nationaux (SRN) |
| `SRV03009` | Operations and Platform Support | Soutien des opérations et des plateformes |
| `SRV03010` | Digital Systems and Solutions Delivery | Soutien aux forces de l&#39;ordre des systèmes, applications et services critiques |
| `SRV03012` | Corporate Staffing - Member | Dotation ministérielle - Membre |
| `SRV03014` | Cadet Training Services | Services de formation des cadets |
| `SRV03015` | Legal Services | Services juridiques |
| `SRV03016` | Liaison with national and international enforcement partners | Liaison avec les partenaires nationaux et internationaux chargés de l&#39;application de la loi |
| `SRV03017` | Exemptions from the Controlled Drugs and Substances Act in reponse to emergencies (CSCB) | Exemptions pour l&#39;utilisation de substances contrôlées en réponse à des urgences (DGSCC) |
| `SRV03018` | Issuance of No Objection Letters for imports | Délivrance de lettres de non-objection pour les importations |
| `SRV03019` | Issuance of Designated Device Registrations under the Controlled Drugs and Substances Act | Délivrance de l&#39;enregistrement d&#39;un instruments désignés |
| `SRV03044` | Federal Economic Immigration- Permanent Residence | Immigration économique fédérale- Résidence permanente |
| `SRV03045` | Regional Economic Immigration- Permanent Residence | Immigration économique régionale- Résidence permanente |
| `SRV03046` | Family Reunification- Permanent Residence | Regroupement familial- Résidence permanente |
| `SRV03047` | Humanitarian/Compassionate and Discretionary Immigration- Permanent Residence | Immigration pour considérations d’ordre humanitaire et discrétionnaire- Résidence permanente |
| `SRV03048` | Grant of Citizenship | Attribution de citoyenneté |
| `SRV03049` | Passports &amp; Travel Documents | Délivrance de passeports et de titres de voyage |
| `SRV03050` | Passport Administrative Services | Services administratifs des passeports |
| `SRV03051` | Work Permit | Permis de travail |
| `SRV03054` | African Swine Fever Industry Preparedness Program: Prevention and Preparedness Stream | Programme de préparation de l’industrie à la peste porcine africaine : Volet Prévention et préparation |
| `SRV03055` | African Swine Fever Industry Preparedness Program: Welfare Slaughter and Disposal Stream | Programme de préparation de l’industrie à la peste porcine africaine : Volet Abattage par compassion et élimination |
| `SRV03056` | AgriCommunication | Programme Agri-communication |
| `SRV03057` | Agricultural Clean Technology:Research and Innovation Stream | Programme des technologies propres en agriculture : Volet Recherche et innovation |
| `SRV03058` | Wine Sector Support Program | Programme d&#39;aide au secteur du vin |
| `SRV03060` | The Victim Liaison Officer | L&#39;agent de liaison de la victime |
| `SRV03061` | Sexual Misconduct Support and Resource Center&#39;s Community Support for Sexual Misconduct Survivors Grant Program | Le programme de subventions pour le soutien communitaire pour les personnes surviantes d&#39;inconduite sexuelle du Centre de soutien et de resources sur l&#39;inconduite sexuelle |
| `SRV03062` | Veterans Ombud Intervention Services | Services d’intervention de l’ombud des vétérans |
| `SRV03063` | Clothing Allowance | Allocation vestimentaire |
| `SRV03064` | eServiceCanada | eServiceCanada |
| `SRV03065` | Outreach Support Centre | Centre d’appui des services mobiles |
| `SRV03066` | Dispute resolution on Canadian business operations abroad | Résolution des litiges concernant les activités des entreprises canadiennes à l&#39;étranger |
| `SRV03069` | Canada Community Building Fund (CCBF) | Le Fonds pour le développement des collectivités du Canada (FDCC) |
| `SRV03070` | Accreditation of foreign representatives services | Services d&#39;accréditation des représentants étrangers |
| `SRV03072` | Advice to Canadian garment, mining and oil &amp; gas companies operating outside Canada | Conseils aux entreprises canadiennes du secteur de l&#39;habillement, de l&#39;exploitation minière et du pétrole et du gaz opérant à l&#39;étran |
| `SRV03084` | Digital Marketing Platform for EduCanada (DMPE) | Plateform de Marketing Digital pour EduCanada |
| `SRV03085` | Diplomatic Security Liaison Services | Services de liaison pour la protection des diplomates |
| `SRV03089` | Enabling the coordination of activities related Trade mission/events/initiatives | Permettre la coordination des activités liées aux missions/événements/initiatives commerciales |
| `SRV03091` | Enterprise Systems Support | Soutien des système d&#39;entreprise |
| `SRV03093` | Foreign Heads of Mission Agrément and Ceremonies | Services d’agrément et des cérémonies pour les chefs de mission étrangers |
| `SRV03094` | Foreign military attachés and honorary consuls approvals services | Services d&#39;approbation des attachés militaires et des consuls honoraires |
| `SRV03095` | Geographic Reporting | Rapports géographiques |
| `SRV03097` | Grants and Contributions - CanExport Associations | Subventions et contributions - CanExport Associations |
| `SRV03098` | Grants and Contributions - CanExport Innovation | Subventions et contributions - CanExport Innovation |
| `SRV03099` | Grants and Contributions - CanExport SMEs | Subventions et contributions - CanExport PME |
| `SRV03100` | Heads of Mission Outreach Services | Services de rayonnement pour les chefs de mission |
| `SRV03111` | IRCC Liaison Services | Services de liaision d&#39;IRCC |
| `SRV03126` | Mission Readiness &amp; Security Operations | Préparation des Missions et Opérations de Sécurité |
| `SRV03133` | Privileges and Immunities services | Services des privilèges et immunités |
| `SRV03143` | Trade Commissioner Service | Service des délégués commerciaux |
| `SRV03144` | Strategic communications | Communications stratégiques |
| `SRV03145` | Canada&#39;s Toll-Free Number for Poison Centre Service (1-844-POISON-X) | Numéro sans frais du Canada pour le service des centres antipoison (1-844-POISON-X) |
| `SRV03146` | Cannabis Laboratory (CL) - Forensic analysis services | Laboratoire Cannabis (LC) - Services d&#39;analyse judiciaire |
| `SRV03147` | Retransformation Authorization | Autorisation de retransformation |
| `SRV03148` | Vitis hot water treatment Program | Programme de traitement à l&#39;eau chaude pour Vitis |
| `SRV03149` | Spongy Moth Program | Programme de la spongieuse nord-américaine |
| `SRV03151` | Advice on Women Peace and Security | Conseils sur les femmes, la paix et la sécurité |
| `SRV03153` | LDD Forest Products - Receiving Regulated Product | Produits forestiers LDD - Réception de produits réglementés |
| `SRV03154` | License for Removal of Animals or Things Under the authority of The Health of Animals Act | Permis pour l&#39;enlèvement d&#39;animaux ou de choses en vertu de la Loi sur la santé des animaux |
| `SRV03155` | Anti-Crime and Counter-Terrorism Capacity Building Programs (AC/CTCBP) | Programme d’aide au renforcement des capacités en matière de lute contre la criminalité et le terrorism |
| `SRV03156` | Application for a certificate - Mistaken identity | Demande d&#39;attestation - erreur d&#39;identité |
| `SRV03157` | Application for Review of Seizure Order | Demande d&#39;examination de décret concernant la saisie de biens situés au Canada |
| `SRV03158` | Application to no longer be a designated person | Demande de radiation |
| `SRV03159` | Shipborne Dunnage Program | Programme du bois de calage transporté par les navires |
| `SRV03160` | Avian Influenza Movement - General Permit | Mouvement de la grippe aviaire – Permis général |
| `SRV03161` | Peat Export Program | Programme d&#39;exportation de tourbe |
| `SRV03162` | Compliance Letter (Animal Pathogen Laboratories) | Lettre de conformité (Laboratoires d&#39;agents pathogènes animaux) |
| `SRV03164` | Baseline Threat Assessments (BTAs) | L’évaluation de base des menaces(EBM) |
| `SRV03168` | Cancellation and revocation of passports and refusal of passport services | Annulation et révocation de passeports et refus de services de passeport |
| `SRV03170` | Research Security Centre | Centre de la sécurité de la recherche |
| `SRV03171` | Canada Arts Presentation Fund - Presenter Support Organizations | Fonds du Canada pour la présentation des arts - Organismes d&#39;appui à la diffusion |
| `SRV03172` | Canada Arts Presentation Fund - Development | Fonds du Canada pour la présentation des arts - Soutien au développement |
| `SRV03173` | Bilateral agreements and joint working groups | Ententes bilatérales et groupes de travail |
| `SRV03175` | Canada Book Fund - Support for Publishers- Publishing Support | Fonds du livre du Canada - Soutien aux éditeurs - Soutien à l’édition |
| `SRV03176` | Canadian International Innovation Program (CIIP) | Le programme canadien de l&#39; innovation à l&#39;internationale (PCII) |
| `SRV03177` | Development of Emergency Economic Stimulus Packages | Élaboration de plans de relance économique d’urgence |
| `SRV03178` | Canadian Police Arrangement and Civilian Deployment Platform | l’Arrangement sur la police civile canadienne (APCC)/la Plateforme de déploiements de ressources civiles |
| `SRV03179` | Canada Book Fund - Support for Organizations | Fonds du livre du Canada - Soutien aux organismes |
| `SRV03181` | Cyber Defence Services | Services de cyberdéfense |
| `SRV03182` | Certificates under the United Nations Act | Certification en vertu de la Loi sur les Nations Unies |
| `SRV03183` | Canada Book Fund - Support for Booksellers | Fonds du livre du Canada - Soutien aux librairies |
| `SRV03184` | Canada Cultural Investment Fund - Endowment Incentives | Fonds du Canada pour l&#39;investissement en culture - Incitatifs aux fonds de dotation |
| `SRV03185` | Canada Cultural Investment Fund - Limited Support to Endangered Arts Organizations | Fonds du Canada pour l&#39;investissement en culture - Appui limité aux organismes artistiques en situation précaire |
| `SRV03186` | Federal Cyber Incident Response Plan (FCIRP) | Plan fédéral de réponse aux cyberincidents (PFRC) |
| `SRV03187` | Digital Citizen Contribution Program - Digital Citizen Initiative | Programme de contributions en matière de citoyenneté numérique - Initiative de citoyenneté |
| `SRV03188` | ATSSC Access to Information and Privacy | Accès à l’information et protection des renseignements personnels |
| `SRV03189` | Canada Periodical Fund - Aid to publishers- Digital Periodical | Fonds du Canada pour les périodiques - Aide aux éditeurs - Périodique numérique |
| `SRV03190` | Canada Periodical Fund - Aid to publishers - Community Newspaper | Fonds du Canada pour les périodiques - Aide aux éditeurs - Journal communautaire |
| `SRV03191` | Canada Periodical Fund- Business Innovation - Magazines | Fonds du Canada pour les périodiques - Innovation commerciale - Magazines |
| `SRV03192` | Canada Periodical Fund - Business Innovation - Community Newspapers | Fonds du Canada pour les périodiques - Innovation commerciale - Journaux communautaires |
| `SRV03193` | Administration of the Explosives Act and Explosives Regulations, 2013 | Administration de la loi sur les explosifs et du règlement sur les explosifs de 2013 |
| `SRV03194` | Canada Periodical Fund - Collective Initiatives | Fonds du Canada pour les périodiques - Initiatives collectives |
| `SRV03195` | GC Accommodation Booking system | Système de réservation de GC locaux |
| `SRV03196` | Weapons Threat Reduction Program (WTRP) | Programme de réduction de la menace liée aux armes |
| `SRV03197` | Vetting | Vérification |
| `SRV03199` | Venture Capital Attraction | Attraction du capital de risque |
| `SRV03200` | Chemical Weapons Convention Implementation Act (CWCIA) administration | Gestion de la loi sur la mise en oeuvre de la Convention sur les armes chimiques |
| `SRV03203` | FSD Claim and entitlement administration | Administration des réclamations et des droits liés aux DSE |
| `SRV03204` | Training: Governance, Access, Technical Security and Espionage (GATE) | Formation : Gouvernance, accès, sécurité technique et espionnage (GATE) |
| `SRV03207` | Canada Periodical Fund - Special Measures for Journalism | Fonds du Canada pour les périodiques - Mesures spéciales pour appuyer le journalisme |
| `SRV03209` | Celebration and Commemoration - Commemorate Canada | Célébrations et commémorations - Commémoration Canada |
| `SRV03212` | Support for Hosting - International Multisport Games for Aboriginal Peoples and Persons with a Disability | Soutien pour l&#39;acceuil - Jeux internationaux multisports pour les Autochtones et les personnes ayant un handicap |
| `SRV03214` | Support for Hosting - International Single Sport Events | Soutien pour l&#39;acceuil - Manifestations internationales unisport |
| `SRV03215` | Zero Emission Vehicles Infrastructure Program (ZEVIP) | Programme d’infrastructure pour les véhicules à émission zéro (PIVEZ) |
| `SRV03216` | International Major Multisport Games | Grands Jeux internationaux multisports |
| `SRV03219` | Support the TCS clients (external) and the TCS Network (internal) with the Canadian Technology Accelerator applications (external) and assessments (internal) | Accélérateurs technologiques canadiens - support aux clients du SDC (externe) et au réseau interne |
| `SRV03220` | Zero Emission Vehicle Awareness Initiative (ZEVAI) | Initiative de sensibilisation aux véhicules à émission zéro (ISVEZ) |
| `SRV03221` | Fuel Consumption Guide (FCG) | Guide de consommation de carburant |
| `SRV03222` | Green Freight Program (GFP) | Programme de transport écoénergétique de marchandises |
| `SRV03223` | Electric Charging and Alternative Fuel Station Locator | Localisateur de stations de recharge et de stations de ravitaillement en carburants de remplacement |
| `SRV03224` | Critical Infrastructure and Manufacturing Plan (CIMP): Reporting on manufacturing sector impacts from critical infrastructure disruptions | Plan relatif aux infrastructures critiques et à l&#39;industrie manufacturière (ICIM) : Rapport sur l&#39;impact des perturbations des infrastructures critiques dans le secteur manufacturier |
| `SRV03225` | Spectrum Auction | Enchères du spectre |
| `SRV03226` | Satellite Operations | Opérations par satellite |
| `SRV03227` | International Radio Frequency Coordination | Coordination internationale des radiofréquences |
| `SRV03228` | Information and Communications Technology Critical Infrastructure Resilience – Cyber Security | Résilience des infrastructures essentielles des technologies de l’information et des communications – Cybersécurité |
| `SRV03229` | EcoDriving | Cours d’écoConduite en ligne gratuit |
| `SRV03230` | Emergency Telecommunications | Télécommunications d’urgence |
| `SRV03231` | EnerGuide for Vehicles | ÉnerGuide pour les véhicules |
| `SRV03232` | Remediation of Terrestrial Interference | Réparation du brouillage des stations terrestres |
| `SRV03233` | Auto$mart driver training | Programme de formation des conducteurs Le bon $ens au volant |
| `SRV03235` | Affixing the Great Seal of Canada on formal documents | Apposition du Grand Sceau du Canada sur les documents officiels |
| `SRV03236` | Fuel-efficient driving techniques | Techniques de conduite écoénergétique |
| `SRV03237` | Strategic direction/support/training relating to FDI | Orientation stratégique/contribution/formation aux activités d’attraction et d’IDE |
| `SRV03238` | Weights and Measures Inspection | Services d&#39;inspection poids et mesures |
| `SRV03239` | Sport Support - National Multisport Services Organization | Soutien au sport - Organismes nationaux de services multisports |
| `SRV03240` | Speechwriting | Rédaction de discours |
| `SRV03242` | SmartDriver | Conducteur averti |
| `SRV03243` | Weights and Measures Approvals | L&#39;approbation des appareils de pesage et de mesure |
| `SRV03244` | Sport Support - Canadian Sport Centre | Soutien au sport - Centre canadien multisport |
| `SRV03246` | Sport Support - Sport for Social Development in Indigenous Communities | Soutien au sport - Sport au service du développement social dans les communautés autochtones |
| `SRV03248` | Electricity and Natural Gas Meter Inspection | Inspections de compteurs d&#39;électricité et de gaz naturel |
| `SRV03250` | Research Security | Sécurité de la recherche |
| `SRV03251` | Clean Fuels Fund (CFF) | Fonds pour les combustibles propres |
| `SRV03253` | Remote Sensing Space Systems Act (RSSSA) administration, including licensing and regulatory activities | Administration de la Loi sur les systèmes de télédétection spatiaux (LSTS), y compris les activités de licence et de réglementation |
| `SRV03254` | Regulatory Affairs and Litigation Support | Affaires réglementaires et d&#39;appui au litige |
| `SRV03255` | Building Communities through Arts and Heritage - Community Anniversaries | Développement des communautés par le biais des arts et du patrimoine - Commémorations communautaires |
| `SRV03256` | Providing statistical analysis and reports (CFO-Stats) | Fournir de l&#39;analyse et des rapports statistiques (DPF-Stats) |
| `SRV03257` | Building Communities through Arts and Heritage - Legacy Fund | Développement des communautés par le biais des arts et du patrimoine - Fonds des legs |
| `SRV03258` | Grants and Contribution Programs | Programmes de subentions et contributions |
| `SRV03259` | Public Enquiries | Enquêtes publiques |
| `SRV03261` | Authorized Service Provider Recognized Technician Training | Formation des fournisseur services autorisés techniciens reconnus |
| `SRV03263` | Promoting and Protecting Democracy Fund (Pro-Dem) and the Inclusion, Diversity and Human Rights Fund (IDHR) | Fonds pour la promotion et la protection de la démocratie (Pro-Dem) et Fonds pour l&#39;inclusion, la diversité et les droits de la personne (IDHR) |
| `SRV03264` | Electricity and Natural Gas Approvals | Approbation de compteurs d&#39;électricité et de gaz naturel |
| `SRV03267` | Electricity and Natural Gas Measuring Apparatus Accuracy | Précision des appareils de mesure de l&#39;électricité et de gaz naturel |
| `SRV03268` | Coordination of international STI Canadian priorities with SBDA&#39;s | Coordination des priorités internationales en STI avec les ministères et agences fédéraux à vocation scientifique |
| `SRV03270` | FSD Policy compliance and guidance | Conformité et orientation en matière de politique des DSE |
| `SRV03272` | Corporate Governance | Gouvernance |
| `SRV03276` | Permits under the Special Economic Measures Act and the Justice for Victims of Corrupt Foreign Officials Act | Permis en vertu de la Loi sur les mesures économiques spéciales et de la Loi sur la justice pour les victimes de dirigeants étrangers corrompus |
| `SRV03278` | Corporate Performance and Reporting | Rendement et rapports de l&#39;entreprise |
| `SRV03279` | Peace and Stabilization Operations Program | Programme pour la stabilisation et les opérations de paix |
| `SRV03284` | Economic Analysis and Evaluation | Analyse et évaluation économiques |
| `SRV03286` | EduCanada Extranet | Extranet EduCanada |
| `SRV03289` | Indigenous Languages and Cultures - Northern Aboriginal Broadcasting | Langues et cultures autochtones - Radiodiffusion autochtone dans le Nord |
| `SRV03291` | Multiculturalism and Anti-Racism Initiatives - Projects | Multiculturalisme et la lutte contre le racisme - Projets |
| `SRV03296` | Multiculturalism and Anti-Racism Initiatives - Organizational Capacity Building | Multiculturalisme et la lutte contre le racisme - Renforcement des capacités organisationnelles |
| `SRV03297` | Networks support for International STI | Appui aux Réseaux en STI international |
| `SRV03298` | Museums Assistance - Exhibition Circulation Fund | Aide aux musées - Fonds des expositions itinérantes |
| `SRV03301` | Museums Assistance - Indigenous Heritage | Aide aux musées - Patrimoine autochtone |
| `SRV03303` | Ministerial Liaison | Liaison ministerielle |
| `SRV03304` | Museums Assistance - Collections Management | Aide aux musées - Gestion des collections |
| `SRV03305` | Military and Scientific Overflight Clearance request management | Gestion des demandes d&#39;autorisation de survol militaire et scientifique |
| `SRV03306` | Museums Assistance - Canada-France Agreement | Aide aux musées - Accord Canada-France |
| `SRV03307` | Canada Travelling Exhibitions Indemnification | Indemnisation pour les expositions itinérantes au Canada |
| `SRV03308` | Cultural Property Export and Import Act - Movable Cultural Property Grants | Loi sur l’exportation et l’importation de biens culturels - Subventions de biens culturels mobiliers |
| `SRV03309` | Cultural Property Export and Import Act - Designation of institutions and public authorities | Loi sur l’exportation et l’importation de biens culturels - Désignation d’établissements et d’administrations publiques |
| `SRV03311` | Marine Scientific Research (MSR) request management | Gestion des demandes de recherche scientifique marine |
| `SRV03316` | Management of FDI events | Gestion des évènements IDE |
| `SRV03322` | Canadian Conservation Institute and Canadian Heritage Information Network - Scientific Services | Institut canadien de conservation et Réseau canadien d&#39;information sur le patrimoine - Services scientifiques |
| `SRV03323` | Canadian Conservation Institute and Canadian Heritage Information Network - General Information Requests | Institut canadien de conservation et Réseau canadien d&#39;information sur le patrimoine - Demandes d&#39;informations générales |
| `SRV03325` | Canadian Conservation Institute and Canadian Heritage Information Network- In-person and Online Workshops and Webinars | Institut canadien de conservation et Réseau canadien d&#39;information sur le patrimoine - Ateliers et webinaires en personne et en ligne |
| `SRV03327` | Canadian Conservation Institute and Canadian Heritage Information Network - Advanced Professional Development Workshops | Institut canadien de conservation et Réseau canadien d&#39;information sur le patrimoine - Ateliers de développement professionnel avancé |
| `SRV03330` | Development of Official-Language Communities –Community Cultural Action Fund | Développement des communautés de langue officielle - Fonds d’action culturelle communautaire |
| `SRV03332` | Development of Official-Language Communities - Teacher Recruitment and Retention Strategy in Minority French Language Schools | Développement des communautés de langue officielle - Stratégie de recrutement et de rétention d’enseignants pour les écoles de langue française en situation minoritaire |
| `SRV03333` | International Relations and Border Policy | Les relations internationales et la politique frontalière |
| `SRV03334` | Development of Official-Language Communities - Cooperation with the Non-Governmental Sector | Développement des communautés de langue officielle - Collaboration avec le secteur non gouvernemental |
| `SRV03335` | Enabling the coordination of Matchmaking/B2B | Jumelages/B2B |
| `SRV03336` | Enterprise Architecture | Architecture d&#39;Entreprise |
| `SRV03339` | Evaluation Publications | Publications d&#39;évaluation |
| `SRV03343` | Ghost Gear Fund | Fonds pour les engins fantômes |
| `SRV03345` | Development of Official-Language Communities – Community Spaces Fund | Développement des communautés de langue officielle - Fonds pour les espaces communautaires |
| `SRV03349` | International bilateral STI agreements and arrangements | Accords et arrangements bilatéraux de cooperation internationale bilatéraux en STI |
| `SRV03350` | Enhancement of Official Languages - Teacher Recruitment and Retention Strategy in French Immersion and French Second-Language Programs | Mise en valeur des langues officielles - Stratégie de recrutement et de rétention d’enseignants dans les programmes d’immersion et de français langue seconde |
| `SRV03351` | Enhancement of Official Language - Promotion of Bilingual Services | Mise en valeur des langues officielles - Promotion de l’offre de services bilingues |
| `SRV03353` | Enhancement of Official Language - Support for Interpretation and Translation | Mise en valeur des langues officielles - Appui à l’interprétation et à la traduction |
| `SRV03355` | Enhancement of Official Language - Appreciation and Rapprochement | Mise en valeur des langues officielles - Appréciation et rapprochement |
| `SRV03359` | Executive Briefing | La division du breffage de la haute direction |
| `SRV03360` | Federal-Provincial Consultative Committee on Education-related International Activities (FPCCERIA) | Comité consultatif fédéral-provincial sur les activités internationales liées à l&#39;éducation (CCFPAIE) |
| `SRV03365` | Foreign military ship visit request management | Visite de navires militaires étrangers |
| `SRV03368` | Geographic Advice | Conseil géographique |
| `SRV03370` | Global Security Reporting Program (GSRP) | Programme des rapports sur la securité mondiale (PRSM) |
| `SRV03371` | Grants and Contributions - CanExport Community Investments | Subventions et contributions - CanExport investissements des communautés |
| `SRV03374` | Monitoring and Compliance | Surveillance et conformité |
| `SRV03375` | Fighting and Managing Wildfires in a Changing Climate | Combattre et gérer les feux de forêt dans un climat en changement |
| `SRV03376` | Aquatic Invasive Species Prevention Fund | Fonds de prévention des espèces aquatiques envahissantes |
| `SRV03377` | Training And Exercising Participation Contribution Program | Programme de contribution pour la participation aux activités de formation et d&#39;exercice |
| `SRV03378` | Wildland Fire Resilience | Contribution à l&#39;appui de Programme Résilience des feux de forêt |
| `SRV03379` | Residential Schools Legacy | Séquelles des pensionnats |
| `SRV03380` | Aboriginal Entrepreneurship Program - Access to Business Opportunities stream | Programme d&#39;entrepreneuriat autochtone - Accès à des possibilités d&#39;affaires |
| `SRV03381` | Jordan&#39;s Principle: Funding | Principe de Jordan: financement |
| `SRV03382` | Inuit Child First Initiative: Direct Service Delivery | L&#39;Initiative : Les enfants inuits d&#39;abord : Prestation directe de services |
| `SRV03383` | Inuit Child First Initiative: Funding | L&#39;Initiative : Les enfants inuits d&#39;abord : financement |
| `SRV03384` | Contribution Agreement Funding related to Article 24 of the Nunavut Agreement | Financement de l&#39;accord de contribution lié à l&#39;article 24 de l&#39;Accord du Nunavut |
| `SRV03385` | New Frontiers in Research Fund | Fonds Nouvelles frontières en recherche |
| `SRV03386` | Coastal Environmental Baseline Contribution Program | Programme de contribution environnementale côtière de référence |
| `SRV03387` | Indigenous Community-Boat Volunteer Contribution Program | Programme de contribution des bénévoles des communautés autochtones sur les bateaux |
| `SRV03388` | Certification for Canadian exporters of aquatic products under the Convention on International Trade in Endangered Species of Wild Fauna and Flora (CITES) | Certification pour les exportateurs canadiens d&#39;espèces aquatiques assujettis à la Convention sur le commerce international des espèces de faune et de flore sauvages menacées d&#39;extinction (CITES) |
| `SRV03389` | National Emergency Management Governance | Gouvernance de la gestion des urgences nationales |
| `SRV03390` | Alerts and Advisories | Alertes et Avis |
| `SRV03391` | Immigration Detentions | Détention d&#39;immigrants |
| `SRV03392` | Critical Construction Project Assurance | Assurance des Projets de Construction Critiques |
| `SRV03393` | Immigration Hearings Representation | Représentation aux audiences d&#39;immigration |
| `SRV03394` | Removal | Renvois |
| `SRV03395` | Immigration Investigations | Enquêtes d&#39;immigration |
| `SRV03396` | Immigration National Security Screening | Filtrage de sécurité nationale de l&#39;immigration |
| `SRV03399` | Criminal Investigations | Enquêtes criminelles |
| `SRV03400` | Waste Diversion of Office Supplies | Réacheminement des déchets de fournitures de bureau |
| `SRV03401` | Community Participation And Co-Development Contribution Program | Fonds de subventions et de contributions pour la participation communautaire et le codéveloppement |
| `SRV03402` | Canadian Coast Guard Auxiliary Contribution Fund | Fonds de contribution de la Garde côtière auxiliaire canadienne |
| `SRV03403` | Collaboration with Priority Critical Infrastructure Owners and Operators | Collaboration avec des propriétaires et exploitants d’infrastructures essentielles prioritaires |
| `SRV03404` | Incident Handling and Support | Intervention et soutien en cas d’incident |
| `SRV03408` | Service Coordination | Coordination des services |
| `SRV03410` | Cyber Threat Surface Analysis | Analyse de l’exposition aux cybermenaces |
| `SRV03411` | Cybersecurity Advice &amp; Guidance - System Security Architecture | Avis et conseils en matière de cybersécurité – Architecture de sécurité du système |
| `SRV03413` | Access to Information and Privacy - Privacy Act | Accès à l’information et protection des renseignements personnels - Loi sur la protection des renseignements personnels |
| `SRV03414` | Access to Information and Privacy - Access to Information Act | Accès à l’information et protection des renseignements personnels - Loi sur l&#39;accès à l&#39;information |
| `SRV03415` | Work Point Booking Tool | Outil de réservation pour postes de travail |
| `SRV03416` | Whale Protection And Recovery Initiative Contribution Program | Programme de contribution de l’Initiative de protection et de rétablissement des baleines |
| `SRV03417` | Commonwealth Blue Charter Champion Contribution Program | Programme de contribution des champions de la Charte bleue du Commonwealth |
| `SRV03418` | Sustainable Fisheries Science Fund Contribution Program (SFSRSP) | Programme de contributions du Fonds des sciences halieutiques durables |
| `SRV03419` | Marine Environmental Quality Regulatory / Non Regulatory Measures Contribution Program | Qualité du milieu marin réglementaire / non réglementaire |
| `SRV03420` | Pacific Integrated Commercial Fisheries Initiative (PICFI) | Initiative des pêches commerciales intégrées du Pacifique (IPCIP) |
| `SRV03421` | Human-Wildlife Coexistence- Incident Response and Safety Management | Coexistence entre l&#39;homme et la faune - Réponse aux incidents et gestion de la sécurité |
| `SRV03422` | Library Services | Services de bibliothèque |
| `SRV03423` | Reducing The Threat Of Vessel Traffic On Marine Mammals Contribution Program | Programme de contribution pour réduire la menace du trafic maritime sur les mammifères marins |
| `SRV03424` | Media and Promotion of Canada&#39;s Natural and Cultural Heritage | Médias et promotion du patrimoine naturel et culturel du Canada |
| `SRV03425` | Environmental Protection Services | Services de protection de l’environnement |
| `SRV03426` | Ocean And Climate Change Science Contribution Program | Programme de contributions pour les sciences des océans et des changements climatiques |
| `SRV03427` | National Contaminants Advisory Group Contribution Program | Programme de contributions du Groupe consultatif national sur les contaminants |
| `SRV03428` | Marine Spatial Planning Contribution Program | Programme de contributions pour la planification spatiale marine |
| `SRV03429` | Core geospatial observation sites in remote locations of Canada (GO Canada) | Sites de base d&#39;observation géospatiale en régions éloignées du Canada (GO Canada) |
| `SRV03430` | Freshwater Habitat Science Contribution Program | Programme de contributions pour les sciences des océans et des eaux douces |
| `SRV03431` | Ontario Waterways and Water Management | Voies navigables et gestion de l&#39;eau en Ontario |
| `SRV03432` | Freshwater Research Contribution Program | Programme de contributions pour la recherche sur l’eau douce |
| `SRV03433` | Ocean And Freshwater Science Contribution Program | Programme de contributions pour la science de l’habitat d’eau douce |
| `SRV03434` | Ground support for space science (THEMIS) | Soutien au sol des sciences spatiales (THEMIS) |
| `SRV03435` | Wildfire Prevention and Risk Mitigation | Prévention des incendies de forêt et atténuation des risques |
| `SRV03436` | National Infrastructure Component (NIC) | Volet Infrastructures nationales (VIN) |
| `SRV03437` | Clean Water and Wastewater Fund (CWWF) | Le Fonds pour l&#39;eau potable et le traitement des eaux usées (FEPTEU) |
| `SRV03438` | Disaster Mitigation and Adaptation Fund | Fonds d&#39;atténuation et d&#39;adaptation en matière de catastrophes |
| `SRV03440` | Investing in Canada Infrastructure Program (ICIP) | Programme d&#39;infrastructure Investir dans le Canada (PIIC) |
| `SRV03441` | Active Transportation Fund (ATF) | Le Fonds pour le transport actif (FTA) |
| `SRV03442` | National and Regional Projects (NRP) | Projets nationaux et régionaux (PNR) |
| `SRV03443` | Public Transit Infrastructure Fund (PTIF) | Le Fonds pour l&#39;infrastructure de transport en commun (FITC) |
| `SRV03444` | Rural Transit Solutions Fund (RTSF) | Fonds pour les solutions de transport en commun en milieu rural (FSTCMR) |
| `SRV03445` | Small Communities Fund (SCF) | Fonds des petites collectivités (FPC) |
| `SRV03446` | Zero Emissions Transit Fund (ZETF) | Fonds pour le transport en commun à zéro émission (FTCZE) |
| `SRV03447` | Copyright Services | Services des droits d&#39;auteur |
| `SRV03448` | Frontline Avalanche Safety and Control Service | Service de sécurité et de contrôle des avalanches en première ligne |
| `SRV03449` | Backcountry Avalanche Monitoring and Reporting | Surveillance et Rapport sur les Avalanches en Arrière-Pays |
| `SRV03450` | Canadian Heritage accessibility feedback process | Processus de rétroaction sur l&#39;accessibilité de Patrimoine canadien |
| `SRV03451` | Access to Information and Privacy (ATIP) | Demande d&#39;accès à l&#39;information et de protection des renseignements personnels (AIPRP) |
| `SRV03452` | Reaching Home (RH) | Directives de Vers un chez-soi (DVC) |
| `SRV03453` | Public Service Employee Survey (PSES) | Sondage auprès des fonctionnaires fédéraux (SAFF) |
| `SRV03454` | Cyber Maturity Self-Assessment (CMSA) | Autoévaluation de la cybermaturité (AECM) |
| `SRV03455` | GC Digital Talent | Talents numériques du GC |
| `SRV03456` | Tracker | Suivi |
| `SRV03457` | Grants and Contribution Programs | Programmes de subventions et de contributions |
| `SRV03458` | Web Inquiries | Demandes de renseignements sur le Web |
| `SRV03459` | Policy, Advocacy, and Coordination | Politique, représentation et coordination |
| `SRV03461` | Ministerial exemption under subsection 5.9(2) of the Aeronautics Act | Exemption ministérielle en vertu du paragraphe 5.9(2) de la Loi sur l&#39;aéronautique |
| `SRV03462` | Statement of aerobatic competency | Énoncé de compétence en voltige aérienne |
| `SRV03463` | Aviation Exams | Examens aéronautiques |
| `SRV03464` | Ministerial authorization under Part VII, other than under section 701.10 | Autorisation ministérielle en vertu de la partie VII, autre qu&#39;en vertu de l&#39;article 701.10 |
| `SRV03465` | Aircraft Parking | Stationnement des aéronefs |
| `SRV03466` | Vehicle Parking | Stationnement des véhicules |
| `SRV03467` | General Terminal: Domestic and International | Accès à l&#39;aérogare : Vols intérieurs et internationaux |
| `SRV03468` | Aircraft Landing and Flying Training | Formation à l&#39;atterrissage et au vol d&#39;avions |
| `SRV03469` | Emergency Response Services | Services d&#39;intervention d&#39;urgence |
| `SRV03470` | Annual Mobile Equipment Registration | L&#39;enregistrement annuelle d&#39;équipement mobile |
| `SRV03471` | Coasting Trade inspections : Letters of Compliance Issued | Inspections des métiers du cabotage : Lettres de conformité émises |
| `SRV03472` | Air cargo screening equipment certification | Certification des équipements de contrôle du fret aérien |
| `SRV03473` | Inspection on a domestic vessel | Inspection à bord d’un bâtiment canadien |
| `SRV03475` | Ministerial and Deputy Correspondence | Correspondance ministérielle et du sous-ministre |
| `SRV03476` | Education and awareness on rail and intermodal transportation security | Éducation et sensibilisation à la sûreté du transport ferroviaire et intermodal |
| `SRV03477` | Access to Information and Privacy | Accès à l&#39;information et protection des renseignements personnels |
| `SRV03478` | Safe Manning Document Review | Examen du Document d&#39;effectifs de sécurité |
| `SRV03479` | Vessel Plan Document Review | Examen des documents du plan du bâtiment |
| `SRV03480` | Licensing for aviation personnel | Licences pour le personnel en aviation |
| `SRV03481` | Seafarer examination and/or assessment of qualification | Examen et/ou évaluation des qualifications des gens de mer |
| `SRV03482` | Certification for a seafarer | Certification des gens de mer |
| `SRV03483` | Search for Sea Service | Recherche de service en mer |
| `SRV03484` | Identity document for a seafarer | Document d&#39;identité pour un marin |
| `SRV03485` | Register a vessel | Immatriculer un bâtiment |
| `SRV03486` | Transfer of Vessel Ownership | Transfert de propriété d&#39;un navire |
| `SRV03487` | Register a mortgage for a vessel | Enregistrer une hypothèque sur un bâtiment |
| `SRV03488` | Vessel History | Historique du bâtiment |
| `SRV03489` | Replacement of a Canadian aviation document | Remplacement d&#39;un document d&#39;aviation canadien |
| `SRV03490` | Access Public Ports Facilities | Accès aux Installations des Ports Publics |
| `SRV03491` | Issuance, in response to a request by industry, of an evaluation or authorization of industry training products. | Délivrance, à la suite d’une demande de l’industrie, d’une évaluation ou d’une autorisation concernant des produits de formation de l’industrie. |
| `SRV03492` | Marine Insurance Certificate for a Vessel | Certificat d&#39;assurance maritime pour un bâtiment |
| `SRV03493` | Vessel Operations Restriction Regulation (VORR) Permit | Règlement sur les restrictions visant l’utilisation des bâtiments (RRVUB) permis |
| `SRV03494` | Cargo Inspection | Inspection des cargaisons |
| `SRV03495` | Dangerous Goods inspection | Inspection des marchandises dangereuses |
| `SRV03496` | Canadian Flagged Vessels (SOLAS &amp; Domestic Ferries) Security Certification | Certification de sûreté pour les bâtiments battant Pavillon canadien (SOLAS et traversiers intérieurs) |
| `SRV03497` | Verification of outstanding deficiencies for foreign vessels | Vérification des déficiences en suspens pour les navires étrangers |
| `SRV03498` | Type certificate for an aeronautical product | Certificat de type pour un produit aéronautique |
| `SRV03499` | Supplemental type certificate for an aeronautical product | Certificat de type supplémentaire pour un produit aéronautique |
| `SRV03500` | Canadian Technical Standard Order (CAN-TSO) for an appliance or part | Ordonnance sur les normes techniques canadiennes (CAN-TSO) pour un appareil ou une pièce |
| `SRV03501` | Repair design approval for an aeronautical product | Approbation de conception de réparation pour un produit aéronautique |
| `SRV03502` | Licensing for air traffic controllers | Licence pour les contrôleurs aériens |
| `SRV03503` | Part design approval for an aeronautical product | Approbation de conception de pièce pour un produit aéronautique |
| `SRV03504` | Access Importation and Manufacturing protocols and guidance | Accéder aux protocoles et aux conseils d’importation et de fabrication |
| `SRV03505` | Access Connected and Automated Vehicles information | Accéder aux informations sur les véhicules connectés et automatisés |
| `SRV03506` | Air carrier joint venture review and authorization process | Processus d&#39;examen et d&#39;autorisation des coentreprises de transporteurs aériens |
| `SRV03507` | Certificate of registration for a means of containment facility | Certificat d&#39;enregistrement pour une installation de confinement |
| `SRV03508` | Exemption by Order under subsection 24(1) of the Canadian Navigable Waters Act | Exemption par décret en vertu du paragraphe 24(1) de la Loi sur les eaux navigables canadiennes |
| `SRV03509` | Pleasure Craft Licence | Délivrance des permis d&#39;embarcations de plaisance |
| `SRV03510` | Railway Operating Certificate | Certificat d&#39;exploitation ferroviaire |
| `SRV03511` | Transportation Security Clearance | Autorisation de sécurité des transports |
| `SRV03512` | Licensing for aircraft maintenance engineers | Licences pour les ingénieurs en maintenance d&#39;aéronefs |
| `SRV03513` | Canadian Airline Designations and Airline Capacity Allocation | Désignations des compagnies aériennes canadiennes |
| `SRV03514` | Education and Awareness | Éducation et sensibilisation |
| `SRV03515` | Equivalency and Temporary Certificates | Certificats d’équivalence et certificats temporaires |
| `SRV03516` | General Inquiries related to the TDG Program, including means of containment, regulations and legislation | Demandes de renseignements généraux concernant le programme du TMD, y compris les contenants, les règlements et les lois. |
| `SRV03517` | Reservation of an aircraft registration mark | Réservation d&#39;une marque d&#39;immatriculation d&#39;aéronef |
| `SRV03518` | Approval of Emergency Response Assistance Plans (ERAP) | Approbation des plans d’intervention d’urgence (PIU) |
| `SRV03519` | Canadian Transport Emergency Centre (CANUTEC) | Centre canadien d’urgence transport |
| `SRV03520` | Canadian Transport Emergency Centre (CANUTEC) - Publication of the Emergency Response Guidebook (ERG) | Centre canadien d&#39;urgence transport (CANUTEC) - Publication du Guide des interventions d&#39;urgence (ERG) |
| `SRV03521` | CANUTEC Registration system | Service à l&#39;inscription de CANUTEC |
| `SRV03522` | Approval for a marine training program or course provided by a marine training institution | Approbation d&#39;un programme ou d&#39;un cours de formation maritime dispensé par un établissement d&#39;enseignement maritime reconnu |
| `SRV03523` | Maritime Labour Convention Certificates | Certificat de travail maritime. |
| `SRV03524` | Seafarer Recruitment and Placement Service (SRPS) provider licensing | Licence de service de recrutement et de placement des gens de mer (SRPGM) |
| `SRV03525` | TC Situation Centre (SitCen) | Centre d’intervention de Transports Canada (SitCen) |
| `SRV03526` | Marine Medical Certificate | Certificat médical de la marine |
| `SRV03527` | Access National Collision Database (NCDB) | Accéder à la base de données nationale sur les collisions (BNDC) |
| `SRV03528` | Air transportation merger and acquisition review and authorization process | Processus d&#39;examen et d&#39;autorisation des fusions et acquisitions de transport aérien |
| `SRV03529` | Approved training organization certificate | Certificat pour organismes de formation agréés |
| `SRV03530` | Alternative means of compliance (AMOC) with an airworthiness directive | Moyens alternatifs de conformité (AMOC) à une consigne de navigabilité |
| `SRV03531` | Administration of the Marine War Risk Act and the agreement with the Canadian Shipowners Mutual Assurance Association | Administration de la Loi sur les risques de guerre en matière d&#39;assurance maritime et de l&#39;accord avec l&#39;Association pour assurance mutuelle d&#39;armateurs canadiens |
| `SRV03532` | Approval of Air Cargo Security Program Participants | Approbation des participants au Programme de sûreté du fret aérien |
| `SRV03533` | Small Vessel Compliance Program (SVCP) | Programme de conformité des petits bâtiments (PCPB) |
| `SRV03534` | Medical certificates for aviation personnel | Certificats médicaux pour le personnel en aviation |
| `SRV03535` | Marine Security Operations Centres : Pre-Arrival Information Report Screening | Centres des opérations de la sûreté maritime : Contrôle des rapports d&#39;information préalables à l&#39;arrivée |
| `SRV03536` | Ports &amp; Marine Facilities Security Certification | Certification de sûreté des ports et des installations maritimes |
| `SRV03537` | Grants and Contributions | Subventions et contributions |
| `SRV03538` | Access defect and recall information | Accéder aux informations sur les défauts et les rappels |
| `SRV03539` | Access Road Safety standards information | Accéder aux informations sur les normes de sécurité routière |
| `SRV03540` | Access Motor Vehicle Safety Best practices information | Accéder aux informations sur les meilleures pratiques en matière de sécurité des véhicules automobiles |
| `SRV03541` | Approval of ‘works’ under the Canadian Navigable Waters Act | Approbation des « ouvrages » en vertu de la Loi sur les eaux navigables canadiennes |
| `SRV03542` | Dispensation for a seafarer | Dispense pour un gens de mer |
| `SRV03543` | Manufacturer Identification Codes (MIC) | Codes d&#39;identification du fabricant (MIC) |
| `SRV03544` | Declarations of Conformity (DOC) | Déclarations de conformité (DOC) |
| `SRV03545` | Continuous Synopsis Records | Fiche synoptique continue |
| `SRV03546` | Delegated Statutory Inspection Program (DSIP) exemption request applications received | Demandes de dérogation au Programme de Délégation des Inspections Obligatoires (PDIO) reçues |
| `SRV03547` | Marine Technical Review Board Decision | Décision du Comité d&#39;examen technique maritime |
| `SRV03548` | Explosives Detection Dog and Handler Teams (EDDHT) Certification | Certification d&#39;équipe maître et chien entraînée à la détection d’explosifs (EMCEDE) |
| `SRV03549` | Access Driver Assistance Technologies information | Accéder aux informations sur les technologies d&#39;aide à la conduite |
| `SRV03550` | Access School bus safety information | Accès aux informations sur la sécurité des autobus scolaires |
| `SRV03551` | Aircraft registration | Immatriculation d&#39;aéronef |
| `SRV03552` | Flight authority | Autorité de vol |
| `SRV03553` | Certificate of approval for a maintenance or manufacturing organization | Certificat d&#39;approbation pour une organisation de maintenance ou de fabrication |
| `SRV03554` | Approval of an aircraft maintenance schedule | Approbation des calendriers de maintenance d&#39;aéronefs |
| `SRV03555` | Restricted certification authority for an individual | Autorité de certification restreinte pour un particulier |
| `SRV03556` | Inspection of an amateur-built aircraft | Inspection d&#39;un avion de construction amateur |
| `SRV03557` | Prewash Endorsement | Approbation du prélavage |
| `SRV03558` | Verification of Shipper&#39;s procedures | Vérification des procédures de l&#39;Expéditeur |
| `SRV03559` | Rescinding detention of a foreign vessel | Annuler une ordonnance de détention pour un bâtiment étranger |
| `SRV03560` | Report a safety defect | Signaler un défaut de sécurité |
| `SRV03561` | Request a Motor Vehicle Transport Act Exemption | Demander une exemption prévue par la Loi sur les transports routiers |
| `SRV03562` | Authorization to take possession under the Wrecked, Abandoned or Hazardous Vessels Act | Autorisation de prendre possession en vertu de la Loi sur les bâtiments naufragés, abandonnés ou dangereux |
| `SRV03563` | Media enquiries | Demandes médiatiques |
| `SRV03564` | Certification of a flight training unit | Certification d&#39;une unité de formation au pilotage |
| `SRV03565` | Letter of acceptance for foreign maintenance organizations | Lettre d&#39;acceptation pour les organismes de maintenance étrangères |
| `SRV03566` | Aircraft leasing | Location d&#39;aéronefs |
| `SRV03567` | Special flight operations certificate | Certificat d’opérations aériennes spécialisées |
| `SRV03568` | Air operator certificate | Certificat d&#39;exploitant aérien |
| `SRV03569` | Adjudication of Immigration and Refugee cases | Décision des cas d’immigration et de statut de réfugié |




---

#### `service_name_en` – Service Name (English) / Nom du service (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field has a maximum length of 350 characters.
 / Ce champ ne doit pas être vide.
Ce champ a une longueur maximale de 350 caractères.
  


**Description:**  
EN: Identifies the official name of the service.  
FR: Indique le nom officiel du service.


---

#### `service_name_fr` – Service Name (French) / Nom du service (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field has a maximum length of 350 characters.
 / Ce champ ne doit pas être vide.
Ce champ a une longueur maximale de 350 caractères.
  


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
  
FR: Indique le numéro unique attribué à chaque norme de service pour ce service. Facilite le référencement, car un service peut avoir de multiples normes.



---

#### `service_standard_en` – Service Standard (English) / Norme relative aux services (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field has a maximum length of 500 characters.
 / Ce champ ne doit pas être vide.
Ce champ a une longueur maximale de 500 caractères.
  


**Description:**  
EN: Identifies the service standard related to a particular service. See Guideline on Service and Digital for format to be used when defining service standards.
  
FR: Indique la norme de service ayant trait à un service en particulier. Voir la Ligne directrice sur les services et le numérique afin de connaître le format à utiliser pour définir une norme de service.



---

#### `service_standard_fr` – Service Standard (French) / Norme relative aux services (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field has a maximum length of 500 characters.
 / Ce champ ne doit pas être vide.
Ce champ a une longueur maximale de 500 caractères.
  


**Description:**  
EN: Identifies the service standard related to a particular service. See Guideline on Service and Digital for format to be used when defining service standards.
  
FR: Indique la norme de service ayant trait à un service en particulier. Voir la Ligne directrice sur les services et le numérique afin de connaître le format à utiliser pour définir les normes relatives aux services.



---

#### `type` – Service Standard Type / Type de norme relative aux services

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty. / Ce champ ne doit pas être vide.  
**Choice Set:** type (4 values)  


**Description:**  
EN: Identifies the type of service standard as defined in the Guideline on Service and Digital. Access: a commitment outlining the ease and convenience the client should experience when attempting to access a service. Accuracy: a commitment stipulating that the client will receive a service that is up to date, free of errors, and complete. Timeliness: a commitment stating how long the client should expect to wait to receive a service once the service has been accessed.
  
FR: Indique le type de norme de service défini selon la Ligne directrice sur les services et le numérique. Accès : un engagement qui décrit la facilité et la convivialité que devrait connaître le client lorsqu'il essaie d'accéder à un service. Exactitude : un engagement qui stipule que le client recevra un service complet et à jour qui est exempt d'erreurs. Délai : un engagement qui indique le temps d'attente que devrait connaître le client pour recevoir un service une fois qu'il y a accédé.



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
FR: Indique le mode de prestation de service à laquelle s'applique la norme de service


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
**Validation:** This field has a maximum length of 1500 characters. / Ce champ a une longueur maximale de 1500 caractères.  


**Description:**  
EN: Comments related to the service standard channel and provides explanation of "Other" channel selection.  
FR: Commentaires en lien au mode de prestation de la norme de service et fournit une explication de la sélection des modes de prestation « Autre ».


---

#### `channel_comments_fr` – Comments on the service standard channel (French) / Commentaires sur le mode de prestation de la norme de service (Francais)

**Type:** `text`  
**Required:** No  
**Validation:** This field has a maximum length of 1500 characters. / Ce champ a une longueur maximale de 1500 caractères.  


**Description:**  
EN: Comments related to the service standard channel and provides explanation of "Other" channel selection.  
FR: Commentaires en lien au mode de prestation de la norme de service et fournit une explication de la sélection des modes de prestation « Autre ».


---

#### `target` – Service Standard Target / Cible de la norme relative aux services

**Type:** `numeric`  
**Required:** No  
**Validation:** This field must be a single number between 0 and 1 representing a percentage. / Ce champ doit contenir un seul chiffre entre 0 et 1 représentant un pourcentage.  


**Description:**  
EN: The frequency that the organization expects to meet service standard (reported as a percentage).  
FR: Fréquence à laquelle l'organisation s'attend à respecter la norme de service (exprimée en pourcentage).


---

#### `volume_meeting_target` – Business Volume That Met Service Standard Target / Volume d'activités qui respectent la norme de service

**Type:** `bigint`  
**Required:** No  
**Validation:** This value must not be negative.
Volume Meeting Target can not exceed Total Volume.
 / Cette valeur ne doit être négative.
Les volumes atteignant la cible ne peuvent pas dépasser le volume total.
  


**Description:**  
EN: Identifies the number of final outputs issued appropriate to the service (eg. payments issued, requests completed, etc) during the fiscal year that met a particular service standard target for a service. Blank indicates no information available, while 0 indicates that no final outputs issued met service standard targets. Note, this value must be less than or equal to the Total Volume.
  
FR: Indique le nombre total d'opérations de service effectuées (p. ex. les paiements émis, les demandes traitées, etc.) au cours de l'exercice auxquelles s'appliquent cette norme de service. Un champ vide indique qu'aucune information n'est disponible, tandis que 0 indique qu'aucune opération n'a été effectuée. Remarque : cette valeur doit être inférieure ou égale au volumes totaux.



---

#### `total_volume` – Total Volume / Volumes totaux

**Type:** `bigint`  
**Required:** No  
**Validation:** This value must not be negative. / Cette valeur ne doit pas être négative.  


**Description:**  
EN: Identifies the total number of final outputs issued appropriate to the service (eg. payments issued, requests completed, etc) during the fiscal year. Blank indicates no information available, while 0 indicates no final outputs issued.
  
FR: Indique le nombre total d'opérations de service effectuées (p. ex. les paiements émis, les demandes traitées, etc.) au cours de l'exercice auxquelles s'appliquent cette norme de service. Un champ vide indique qu'aucune information n'est disponible, tandis que 0 indique qu'aucune opération n'a été effectuée.



---

#### `comments_en` – Comments on the service standard in general (English) / Commentaires sur la norme de service en général (anglais)

**Type:** `text`  
**Required:** No  
**Validation:** This field has a maximum length of 2000 characters. / Ce champ a une longueur maximale de 2000 caractères.  


**Description:**  
EN: Comments related to the service standard in general.  
FR: Commentaires en lien à la norme de service en general.


---

#### `comments_fr` – Comments on the service standard in general (French) / Commentaires sur la norme de service en général (français)

**Type:** `text`  
**Required:** No  
**Validation:** This field has a maximum length of 2000 characters. / Ce champ a une longueur maximale de 2000 caractères.  


**Description:**  
EN: Comments related to the service standard in general.  
FR: Commentaires en lien à la norme de service en general.


---

#### `standards_targets_uri_en` – URL to Service Standards and Targets (English) / URL vers les normes de service et les cibles (anglais)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field has a maximum length of 1500 characters.
 / Ce champ ne doit pas être vide.
Ce champ a une longueur maximale de 1500 caractères.
  


**Description:**  
EN: Identifies the departmental webpage (Canada.ca) where the service standards and targets are published.  
FR: Indique la page Web ministérielle (Canada.ca) où les normes de service et les cibles sont publiées.


---

#### `standards_targets_uri_fr` – URL to Service Standards and Targets (French) / URL vers les normes de service et les cibles (français)

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field has a maximum length of 1500 characters.
 / Ce champ ne doit pas être vide.
Ce champ a une longueur maximale de 1500 caractères.
  


**Description:**  
EN: Identifies the departmental webpage (Canada.ca) where the service standards and targets are published.  
FR: Indique la page Web ministérielle (Canada.ca) où les normes de service et les cibles sont publiées.


---

#### `performance_results_uri_en` – URL to Real-Time Performance Results (English) / URL aux résultats de rendement en temps réel (anglais)

**Type:** `text`  
**Required:** No  
**Validation:** This field has a maximum length of 1500 characters. / Ce champ a une longueur maximale de 1500 caractères.  


**Description:**  
EN: Identifies the departmental webpage where the real-time performance results for a service are published.  
FR: Indique la page Web (en anglais) sur laquelle les résultats de rendement en temps réel d'un service sont publiés.


---

#### `performance_results_uri_fr` – URL to Real-Time Performance Results (French) / URL aux résultats de rendement en temps réel (français)

**Type:** `text`  
**Required:** No  
**Validation:** This field has a maximum length of 1500 characters. / Ce champ a une longueur maximale de 1500 caractères.  


**Description:**  
EN: Identifies the departmental webpage where the real-time performance results for a service are published.  
FR: Indique la page Web (en anglais) sur laquelle les résultats de rendement en temps réel d'un service sont publiés.


---




## Appendix

### Choice Sets Summary (All Resources)
| Choice Set | Field(s) | Values | Standalone Doc |
|------------|----------|--------|----------------|


### Generation Metadata

- Generated: 2026-10-04T04:26:54 (UTC)
- Source: dictionaries/service.json
- Commit: `22ad121`
- Tool Version: simple-1

### Validation

- JSON Schema Validation: **PASSED**


### Notes

This documentation is auto-generated. Do not hand-edit; instead update the source recombinant JSON and re-run generation.