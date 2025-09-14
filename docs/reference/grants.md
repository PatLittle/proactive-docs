
# Proactive Publication - Grants and Contributions / Publication proactive - Subventions et les contributions

**Dataset Type:** `grants`  
**Last Generated:** 2025-09-14T01:24:39 (UTC)  
**Source:** dictionaries/grants.json  
**Commit:** `322574e`

Access, upload and modify the Grants and Contributions reports for your organization / Accès, téléversement et modifications des rapports sur les contributions et les subventions pour votre organisation

---

## Resources


- [Proactive Publication - Grants and Contributions / Publication proactive - Subventions et les contributions](#grants)

- [Proactive Publication - Grants and Contributions Nothing to Report / Publication proactive – Subventions et contributions, rien à signalerPublication proactive - Subventions et les contributions  (Rien à signaler)](#grants-nil)


---


## Proactive Publication - Grants and Contributions / Publication proactive - Subventions et les contributions 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `ref_number` | Reference Number / Numéro de référence | `text` | Yes |  |  | The Reference number is populated by departments. It is a unique reference numb… |
| `amendment_number` | Amendment Number / Numéro de modification | `int` | Yes |  |  | This field is populated by departments and identifies that an amendment is occu… |
| `amendment_date` | Amendment Date / Date de modification | `date` | No |  |  | This field is populated by departments and indicates the date on which an amend… |
| `agreement_type` | Agreement Type / Type d’entente | `text` | Yes |  | agreement_type | This field is populated by departments and indicates whether the agreement sign… |
| `recipient_type` | Recipient Type / Type de bénéficiaire | `text` | No |  | recipient_type | The recipient type helps identify who is receiving the money. |
| `recipient_business_number` | Recipient Business Number / Numéro d&#39;entreprise du bénéficiaire | `text` | No |  |  | The Business Number is a nine digit number issued by the Canada Revenue Agency … |
| `recipient_legal_name` | Recipient Legal Name (English|French) / Nom légal du bénéficiaire (anglais|français) | `text` | Yes |  |  | The recipient legal name is meant to complement the existing “Recipient busines… |
| `recipient_operating_name` | Recipient Operating Name (English|French) / Nom commercial du bénéficiaire (anglais|français) | `text` | No |  |  | The “Recipient operating name” is an optional field used when an organization o… |
| `research_organization_name` | Research Organization (English|French) / Organisme de recherche (anglais|français) | `text` | No |  |  | The “Research organization” is an optional field for including information abou… |
| `recipient_country` | Recipient Country / Pays du bénéficiaire | `text` | Yes |  | recipient_country | The “Recipient country” is a mandatory field. It is the country in which the re… |
| `recipient_province` | Recipient Province or Territory / Province ou territoire du bénéficiaire | `text` | No |  | recipient_province | The "Recipient province or territory" is a mandatory field if the Recipient Cou… |
| `recipient_city` | Recipient City (English|French) / Ville du bénéficiaire (anglais|français) | `text` | Yes |  |  | The "Recipient city" is a mandatory field that identifies which city the recipi… |
| `recipient_postal_code` | Recipient Postal Code / Code postal du bénéficiaire | `text` | No |  |  | The "Recipient postal code" is a mandatory field that serves to identify the sp… |
| `federal_riding_name_en` | Federal Riding Name (English) / Nom de la circonscription fédérale (anglais) | `text` | No |  |  | The federal riding name is the name of the riding in which the recipient resides. |
| `federal_riding_name_fr` | Federal Riding Name (French) / Nom de la circonscription fédérale (français) | `text` | No |  |  | The federal riding name is the name of the riding in which the recipient resides. |
| `federal_riding_number` | Federal Riding Number / Numéro de la circonscription fédérale | `text` | No |  |  | The federal riding number is based on the riding in which the recipient resides… |
| `prog_name_en` | Program Name (English) / Nom du programme (anglais) | `text` | No |  |  | The program name is the name of the program, according to the terms and conditi… |
| `prog_name_fr` | Program Name (French) / Nom du programme (français) | `text` | No |  |  | The program name is the name of the program, according to the terms and conditi… |
| `prog_purpose_en` | Program Purpose (English) / But du programme (anglais) | `text` | No |  |  | The program purpose is the program’s purpose according to the Ts&Cs. |
| `prog_purpose_fr` | Program Purpose (French) / But du programme (français) | `text` | No |  |  | The program purpose is the program’s purpose according to the Ts&Cs. |
| `agreement_title_en` | Agreement Title (English) / Titre de l’entente (anglais) | `text` | No |  |  | The agreement title is the title of the project or agreement that the recipient… |
| `agreement_title_fr` | Agreement Title (French) / Titre de l’entente (français) | `text` | No |  |  | The agreement title is the title of the project or agreement that the recipient… |
| `agreement_number` | Agreement Number / Numéro de l’entente | `text` | No |  |  | The agreement number should be the number on the agreement and/or in the depart… |
| `agreement_value` | Agreement Value in CAD / Valeur de l’entente en dollars canadiens | `money` | Yes |  |  | The agreement value is the dollar amount stated in the grant or contribution ag… |
| `foreign_currency_type` | Foreign Currency Type / Type de monnaie étrangère | `text` | No |  | foreign_currency_type | The foreign currency type should be selected if a recipient is paid in a curren… |
| `foreign_currency_value` | Foreign Currency Value / Valeur de la monnaie étrangère | `money` | No |  |  | The foreign currency value is the amount as signed in the grant or contribution… |
| `agreement_start_date` | Agreement Start Date / Date de début de l’entente | `date` | Yes |  |  | The agreement start date is the assumed start of the agreement, or when the pro… |
| `agreement_end_date` | Projected Agreement End Date / Date de fin prévue de l’entente | `date` | No |  |  | The projected agreement end date is the assumed end of the agreement, or when t… |
| `coverage` | Coverage (English|French; ...) / Portée (anglais|français; ...) | `text` | No |  |  | Coverage provides information about what will benefit from the project or agree… |
| `description_en` | Description (English) / Description (anglais) | `text` | Yes |  |  | The description explains why the recipient received funding. It should provide … |
| `description_fr` | Description (French) / Description (français) | `text` | Yes |  |  | The description explains why the recipient received funding. It should provide … |
| `naics_identifier` | NAICS Identifier / Identificateur du SCIAN | `text` | No |  |  | The North American Industry Classification System (NAICS) is an industry classi… |
| `expected_results_en` | Expected Results or Intended Outcome (English) / Résultats attendus ou visés (anglais) | `text` | No |  |  | The expected results or intended outcome is the assumed result of project compl… |
| `expected_results_fr` | Expected Results or Intended Outcome (French) / Résultats attendus ou visés (français) | `text` | No |  |  | The expected results or intended outcome is the assumed result of project compl… |
| `additional_information_en` | Additional Information (English) / Renseignements supplémentaires (anglais) | `text` | No |  |  | Additional information is information that departments are required to enter un… |
| `additional_information_fr` | Additional Information (French) / Renseignements supplémentaires (français) | `text` | No |  |  | Additional information is information that departments are required to enter un… |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `ref_number` – Reference Number / Numéro de référence

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: The Reference number is populated by departments. It is a unique reference number given to each entry. Having a unique identifier for each item will allow departments to locate a specific item in the registry should they need to modify or delete.

Controlled format; This field is populated in the following format DDD-YYYY-YYYY-QX-XXXXX
 1. DDD represents the department number – Use the same three-digit number as the ‘Departmental Identifier’, which is the department number per the Chart of Accounts list of departments. Ensure you are reviewing the most current year: https://www.tpsgc-pwgsc.gc.ca/recgen/pceaf-gwcoa/2425/txt/rg-3-num-eng.html
 2. YYYY-YYYY represents the fiscal year
 3. QX represents the fiscal quarter
 4. XXXXX represents the unique number assigned by the department for each entry.

For example, entries in the 2018-2019 Q1 fiscal year should be assigned numbers as follows: 001-2018-2019-Q1-00001, 001-2018-2019-Q1-00002, 001-2018-2019-Q1-00003, etc.'
  
FR: Ce champ est rempli par l’utilisateur. L’identificateur de projet ministériel permet aux ministères d’identifier rapidement les rapports produits dans leur propre système. Les ministères devraient utiliser un chiffre qui est logique pour le ministère. Ces renseignements seront publiés dans le cadre du rapport.

Format contrôlé; Ce champ est rempli au format suivant: DDD-YYYY-YYYY-QX-XXXXX
 1.	DDD représente le numéro du ministère - Utilisez le même numéro à trois chiffres que l’«Identificateur ministériel», qui est le numéro de ministère selon la liste du plan comptable des ministères. Assurez-vous de consulter l’année la plus récente : https://www.tpsgc-pwgsc.gc.ca/recgen/pceaf-gwcoa/2425/txt/rg-3-num-fra.html
 2.	AAAA-AAAA représente l'année fiscale
 3.	QX représente le trimestre fiscal
 4.	XXXXX représente le numéro unique attribué par le département pour chaque entrée.

Par exemple, les numéros de l'exercice 2018-2019 du T1 devraient recevoir les numéros suivants: 001-2018-2019-Q1-00001, 001-2018-2019-Q1-00002, 001-2018-2019-Q1-00003, etc.'



---

#### `amendment_number` – Amendment Number / Numéro de modification

**Type:** `int`  
**Required:** Yes  


**Description:**  
EN: This field is populated by departments and identifies that an amendment is occurring to original information. Use 0 for original records.  
FR: Ce champ est rempli par les ministères et indique qu'une modification est apportée aux renseignements originaux. Utiliser 0 pour les enregistrements originaux.


---

#### `amendment_date` – Amendment Date / Date de modification

**Type:** `date`  
**Required:** No  


**Description:**  
EN: This field is populated by departments and indicates the date on which an amendment (or amendments) took place. If the amendment number is not zero, this field is required.  
FR: Ce champ est rempli par les ministères et indique la date à laquelle une modification (ou des modifications) a été apportée. Vous devez remplir ce champ si le numéro de la modification indique un autre chiffre que 0.


---

#### `agreement_type` – Agreement Type / Type d’entente

**Type:** `text`  
**Required:** Yes  
**Choice Set:** agreement_type (3 values)  


**Description:**  
EN: This field is populated by departments and indicates whether the agreement signed is a grant, contribution or other transfer payment.  
FR: Ce champ est rempli par les ministères et indique si l'entente signée vise une subvention, une contribution ou un autre paiement de transfert.


##### Allowed Values (agreement_type)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `C` | Contribution | contribution |
| `G` | Grant | subvention |
| `O` | Other transfer payment | autre |




---

#### `recipient_type` – Recipient Type / Type de bénéficiaire

**Type:** `text`  
**Required:** No  
**Choice Set:** recipient_type (8 values)  


**Description:**  
EN: The recipient type helps identify who is receiving the money.  
FR: Le type de bénéficiaire permet d'identifier qui reçoit l'argent.


##### Allowed Values (recipient_type)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `A` | Indigenous recipients | bénéficiaire autochtone |
| `F` | For-profit organizations | organisme à but lucratif |
| `G` | Government | gouvernement |
| `I` | International (non-government) | organisation internationale (non gouvernementale) |
| `N` | Not-for-profit organizations and charities | organisme à but non lucratif et organisme de bienfaisance |
| `O` | Other | autre |
| `P` | Individual or sole proprietorships | particulier ou entreprise à propriétaire unique |
| `S` | Academia | établissement universitaire et institution publique |




---

#### `recipient_business_number` – Recipient Business Number / Numéro d'entreprise du bénéficiaire

**Type:** `text`  
**Required:** No  


**Description:**  
EN: The Business Number is a nine digit number issued by the Canada Revenue Agency since 1994. Per the Directive on the Business Number, it has been identified as the standard identifier for all transactions between businesses and the Government of Canada, including transactions linked to grant and/or contribution funding.

The business number should be populated for an organization or charity.

Real-time validation of business identity information linked to the Business Number, including legal name and operating name, for sole proprietorship, partnerships and incorporations, is available to departments through the Business Number Web Validation Service. For more details contact ic.bnadoptionne.ic@canada.ca.

To validate a Business Number associated with a charity, departments can access the List of Charities basic search on the Canada.ca website. Enter the Charity name and click the Search button. Then click the Charity name of the search result to find additional information about the charity (e.g., Charity Program number, charity status, effective date of status, designation, etc.) Legal name and operating name cannot be validated using this basic search.

A business number is issued when an organization is registered federally, provincially or municipally. It does not change and will allow for consistent identification even if the legal name, the operation name or the organization changes over the life cycle of the grant or contribution.
  
FR: Depuis 1994, l’Agence du revenu du Canada émet des numéros d’entreprise à neuf chiffres. Aux termes de la Directive sur le numéro d’entreprise, le numéro d’entreprise constitue l’identificateur standard de toutes les opérations effectuées entre une entreprise et le gouvernement du Canada, y compris les opérations associées à une subvention ou à un financement de contribution.

Le numéro d’entreprise devrait être consigné pour une organisation ou un organisme de bienfaisance.

Les ministères peuvent obtenir la validation en temps réel de l’identité d’une entreprise en saisissant son numéro d’entreprise dans le Service de validation du numéro d’entreprise en ligne, qui inclut le nom légal et le nom commercial pour les entreprises individuelles, les partenariats et les constitutions en personne morale. Si vous voulez obtenir de plus amples renseignements, envoyez un courriel à ic.bnadoptionne.ic@canada.ca.

Pour valider un numéro d’entreprise associé à un organisme de bienfaisance, les ministères peuvent effectuer une recherche de base dans la Liste d’organismes de bienfaisance, sur le site Web Canada.ca. Entrez le nom de l’organisme de bienfaisance, puis cliquez sur le bouton de Recherche. Ensuite, cliquez sur le nom de l’organisme de bienfaisance tiré du résultat de la recherche afin de trouver de plus amples renseignements sur l’organisme de bienfaisance (p. ex., le numéro du programme de bienfaisance, le statut de l’organisme de bienfaisance, la date d’entrée en vigueur du statut et la désignation de l’organisme de bienfaisance). Il est impossible de valider le nom légal et le nom commercial au moyen de la fonction de recherche de base.



---

#### `recipient_legal_name` – Recipient Legal Name (English|French) / Nom légal du bénéficiaire (anglais|français)

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: The recipient legal name is meant to complement the existing “Recipient business number” field. It is the legal name of the recipient. This information should be taken from the agreement.

Only translated if the legal name is provided in both official languages by the recipient.  Provide in the following format: name English|name French.
  
FR: Le nom légal du bénéficiaire se veut complémentaire au champ « Numéro d'entreprise du bénéficiaire ». Cette information devrait être tirée de l'entente de subvention ou de contribution.

Traduction seulement si le nom légal est fourni dans les deux langues officielles par le bénéficiaire. Fournir dans le format suivant : nom anglais|nom français.



---

#### `recipient_operating_name` – Recipient Operating Name (English|French) / Nom commercial du bénéficiaire (anglais|français)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: The “Recipient operating name” is an optional field used when an organization operates under a name that differs from its legal name or business number. When a researcher receives funding through a university, this information would be populated here. This field is not intended to capture the ultimate recipient of a grant or contribution; instead, the name of the person receiving funding from the Government of Canada should be entered.

Only translated if the name is provided in both official languages by the recipient. Provide in the following format: Legal name English|Legal name French.
  
FR: Le champ « Nom commercial du bénéficiaire » est un champ facultatif utilisé dans le cas d'organisations qui exercent leurs activités sous un nom différent de leur nom légal ou de leur numéro d'entreprise. Dans le cas de chercheurs qui reçoivent leur financement par l'entremise d'une université, cette information doit être entrée ici. Ce champ ne sert pas à saisir le nom du bénéficiaire ultime de la subvention ou de la contribution, mais plutôt celui de la personne qui reçoit le financement du gouvernement du Canada.

Traduction seulement si le nom est fourni dans les deux langues officielles par le bénéficiaire. Fournir dans le format suivant : nom anglais|nom français.



---

#### `research_organization_name` – Research Organization (English|French) / Organisme de recherche (anglais|français)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: The “Research organization” is an optional field for including information about the organization that the recipient represents. This field will be used mainly to highlight academic organizations that researchers have partnered with.

Only translated if the organization name is provided in both official languages by the recipient in the following format: name English|name French.
  
FR: Le champ « Organisme de recherche » est facultatif. Il sert à inclure les renseignements sur l'organisation que le bénéficiaire représente. Ce champ sera surtout utilisé pour mettre en évidence les organisations avec lesquelles les chercheurs ont formé un partenariat.

Traduction seulement si le nom de l'organisme est fourni dans les deux langues officielles par le bénéficiaire. Fournir dans le format suivant : nom anglais|nom français.



---

#### `recipient_country` – Recipient Country / Pays du bénéficiaire

**Type:** `text`  
**Required:** Yes  
**Choice Set:** recipient_country (250 values)  


**Description:**  
EN: The “Recipient country” is a mandatory field. It is the country in which the recipient resides.  
FR: Le « Pays du bénéficiaire » est un champ obligatoire qui indique le pays de résidence du bénéficiaire.


##### Allowed Values (recipient_country)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `AD` | Andorra | Andorre |
| `AE` | United Arab Emirates | Émirats arabes unis |
| `AF` | Afghanistan | Afghanistan |
| `AG` | Antigua and Barbuda | Antigua-et-Barbuda |
| `AI` | Anguilla | Anguilla |
| `AL` | Albania | Albanie |
| `AM` | Armenia | Arménie |
| `AO` | Angola | Angola |
| `AQ` | Antarctica | Antarctique |
| `AR` | Argentina | Argentine |
| `AS` | American Samoa | Samoa américaines |
| `AT` | Austria | Autriche |
| `AU` | Australia | Australie |
| `AW` | Aruba | Aruba |
| `AX` | Åland Islands | Îles d’Åland |
| `AZ` | Azerbaijan | Azerbaïdjan |
| `BA` | Bosnia and Herzegovina | Bosnie-Herzégovine |
| `BB` | Barbados | Barbade |
| `BD` | Bangladesh | Bangladesh |
| `BE` | Belgium | Belgique |
| `BF` | Burkina Faso | Burkina Faso |
| `BG` | Bulgaria | Bulgarie |
| `BH` | Bahrain | Bahreïn |
| `BI` | Burundi | Burundi |
| `BJ` | Benin | Bénin |
| `BL` | Saint Barthélemy | Saint-Barthélemy |
| `BM` | Bermuda | Bermudes |
| `BN` | Brunei Darussalam | Brunéi Darussalam |
| `BO` | Bolivia (Plurinational State of) | Bolivie (État plurinational de) |
| `BQ` | Bonaire, Sint Eustatius and Saba | Bonaire, Saint-Eustache et Saba |
| `BR` | Brazil | Brésil |
| `BS` | Bahamas | Bahamas |
| `BT` | Bhutan | Bhoutan |
| `BV` | Bouvet Island | Île Bouvet |
| `BW` | Botswana | Botswana |
| `BY` | Belarus | Bélarus |
| `BZ` | Belize | Belize |
| `CA` | Canada | Canada |
| `CC` | Cocos (Keeling) Islands | Îles des Cocos (Keeling) |
| `CD` | Democratic Republic of the Congo | République démocratique du Congo |
| `CF` | Central African Republic | République centrafricaine |
| `CG` | Congo | Congo |
| `CH` | Switzerland | Suisse |
| `CI` | Ivory Coast | Côte d’Ivoire |
| `CK` | Cook Islands | Îles Cook |
| `CL` | Chile | Chili |
| `CM` | Cameroon | Cameroun |
| `CN` | China | Chine |
| `CO` | Colombia | Colombie |
| `CR` | Costa Rica | Costa Rica |
| `CU` | Cuba | Cuba |
| `CV` | Cabo Verde | Cabo Verde |
| `CW` | Curaçao | Curaçao |
| `CX` | Christmas Island | Île Christmas |
| `CY` | Cyprus | Chypre |
| `CZ` | Czechia | Tchéquie |
| `DE` | Germany | Allemagne |
| `DJ` | Djibouti | Djibouti |
| `DK` | Denmark | Danemark |
| `DM` | Dominica | Dominique |
| `DO` | Dominican Republic | République dominicaine |
| `DZ` | Algeria | Algérie |
| `EC` | Ecuador | Équateur |
| `EE` | Estonia | Estonie |
| `EG` | Egypt | Égypte |
| `EH` | Western Sahara | Sahara occidental |
| `ER` | Eritrea | Érythrée |
| `ES` | Spain | Espagne |
| `ET` | Ethiopia | Éthiopie |
| `FI` | Finland | Finlande |
| `FJ` | Fiji | Fidji |
| `FK` | Falkland Islands | Îles Falkland (Malvinas) |
| `FM` | Micronesia (Federated States of) | Micronésie (États fédérés de) |
| `FO` | Faroe Islands | Îles Féroé |
| `FR` | France | France |
| `GA` | Gabon | Gabon |
| `GB` | United Kingdom of Great Britain and Northern Ireland | Royaume-Uni de Grande-Bretagne et d’Irlande du Nord |
| `GD` | Grenada | Grenade |
| `GE` | Georgia | Géorgie |
| `GF` | French Guiana | Guyane française |
| `GG` | Guernsey | Guernesey |
| `GH` | Ghana | Ghana |
| `GI` | Gibraltar | Gibraltar |
| `GL` | Greenland | Groenland |
| `GM` | Gambia | Gambie |
| `GN` | Guinea | Guinée |
| `GP` | Guadeloupe | Guadeloupe |
| `GQ` | Equatorial Guinea | Guinée équatoriale |
| `GR` | Greece | Grèce |
| `GS` | South Georgia and the South Sandwich Islands | Géorgie du Sud-et-les Îles Sandwich du Sud |
| `GT` | Guatemala | Guatemala |
| `GU` | Guam | Guam |
| `GW` | Guinea-Bissau | Guinée-Bissau |
| `GY` | Guyana | Guyana |
| `HK` | China, Hong Kong Special Administrative Region | Chine, région administrative spéciale de Hong Kong |
| `HM` | Heard Island and McDonald Islands | Île Heard-et-Îles MacDonald |
| `HN` | Honduras | Honduras |
| `HR` | Croatia | Croatie |
| `HT` | Haiti | Haïti |
| `HU` | Hungary | Hongrie |
| `ID` | Indonesia | Indonésie |
| `IE` | Ireland | Irlande |
| `IL` | Israel | Israël |
| `IM` | Isle of Man | Île de Man |
| `IN` | India | Inde |
| `IO` | British Indian Ocean Territory | Territoire britannique de l&#39;océan Indien |
| `IQ` | Iraq | Iraq |
| `IR` | Iran (Islamic Republic of) | Iran (République islamique d’) |
| `IS` | Iceland | Islande |
| `IT` | Italy | Italie |
| `JE` | Jersey | Jersey |
| `JM` | Jamaica | Jamaïque |
| `JO` | Jordan | Jordanie |
| `JP` | Japan | Japon |
| `KE` | Kenya | Kenya |
| `KG` | Kyrgyzstan | Kirghizistan |
| `KH` | Cambodia | Cambodge |
| `KI` | Kiribati | Kiribati |
| `KM` | Comoros | Comores |
| `KN` | Saint Kitts and Nevis | Saint-Kitts-et-Nevis |
| `KP` | Democratic People&#39;s Republic of Korea | République populaire démocratique de Corée |
| `KR` | Republic of Korea | République de Corée |
| `KW` | Kuwait | Koweït |
| `KY` | Cayman Islands | Îles Caïmanes |
| `KZ` | Kazakhstan | Kazakhstan |
| `LA` | Lao People&#39;s Democratic Republic | République démocratique populaire lao |
| `LB` | Lebanon | Liban |
| `LC` | Saint Lucia | Sainte-Lucie |
| `LI` | Liechtenstein | Liechtenstein |
| `LK` | Sri Lanka | Sri Lanka |
| `LR` | Liberia | Libéria |
| `LS` | Lesotho | Lesotho |
| `LT` | Lithuania | Lituanie |
| `LU` | Luxembourg | Luxembourg |
| `LV` | Latvia | Lettonie |
| `LY` | Libya | Libye |
| `MA` | Morocco | Maroc |
| `MC` | Monaco | Monaco |
| `MD` | Republic of Moldova | République de Moldova |
| `ME` | Montenegro | Monténégro |
| `MF` | Saint Martin (French Part) | Saint-Martin (partie française) |
| `MG` | Madagascar | Madagascar |
| `MH` | Marshall Islands | Îles Marshall |
| `MK` | North Macedonia | Macédoine du Nord |
| `ML` | Mali | Mali |
| `MM` | Myanmar | Myanmar |
| `MN` | Mongolia | Mongolie |
| `MO` | China, Macao Special Administrative Region | Chine, région administrative spéciale de Macao |
| `MP` | Northern Mariana Islands | Îles Mariannes du Nord |
| `MQ` | Martinique | Martinique |
| `MR` | Mauritania | Mauritanie |
| `MS` | Montserrat | Montserrat |
| `MT` | Malta | Malte |
| `MU` | Mauritius | Maurice |
| `MV` | Maldives | Maldives |
| `MW` | Malawi | Malawi |
| `MX` | Mexico | Mexique |
| `MY` | Malaysia | Malaisie |
| `MZ` | Mozambique | Mozambique |
| `NA` | Namibia | Namibie |
| `NC` | New Caledonia | Nouvelle-Calédonie |
| `NE` | Niger | Niger |
| `NF` | Norfolk Island | Île Norfolk |
| `NG` | Nigeria | Nigéria |
| `NI` | Nicaragua | Nicaragua |
| `NL` | Netherlands | Pays-Bas (Royaume des) |
| `NO` | Norway | Norvège |
| `NP` | Nepal | Népal |
| `NR` | Nauru | Nauru |
| `NU` | Niue | Nioué |
| `NZ` | New Zealand | Nouvelle-Zélande |
| `OM` | Oman | Oman |
| `PA` | Panama | Panama |
| `PE` | Peru | Pérou |
| `PF` | French Polynesia | Polynésie française |
| `PG` | Papua New Guinea | Papouasie-Nouvelle-Guinée |
| `PH` | Philippines | Philippines |
| `PK` | Pakistan | Pakistan |
| `PL` | Poland | Pologne |
| `PM` | Saint Pierre and Miquelon | Saint-Pierre-et-Miquelon |
| `PN` | Pitcairn | Pitcairn |
| `PR` | Puerto Rico | Porto Rico |
| `PS` | State of Palestine | État de Palestine |
| `PT` | Portugal | Portugal |
| `PW` | Palau | Palaos |
| `PY` | Paraguay | Paraguay |
| `QA` | Qatar | Qatar |
| `RE` | Réunion | Réunion |
| `RO` | Romania | Roumanie |
| `RS` | Serbia | Serbie |
| `RU` | Russian Federation | Fédération de Russie |
| `RW` | Rwanda | Rwanda |
| `SA` | Saudi Arabia | Arabie saoudite |
| `SB` | Solomon Islands | Îles Salomon |
| `SC` | Seychelles | Seychelles |
| `SD` | Sudan | Soudan |
| `SE` | Sweden | Suède |
| `SG` | Singapore | Singapour |
| `SH` | Saint Helena | Sainte-Hélène |
| `SI` | Slovenia | Slovénie |
| `SJ` | Svalbard and Jan Mayen Islands | Îles Svalbard-et-Jan Mayen |
| `SK` | Slovakia | Slovaquie |
| `SL` | Sierra Leone | Sierra Leone |
| `SM` | San Marino | Saint-Marin |
| `SN` | Senegal | Sénégal |
| `SO` | Somalia | Somalie |
| `SR` | Suriname | Suriname |
| `SS` | South Sudan | Soudan du Sud |
| `ST` | Sao Tome and Principe | Sao Tomé-et-Principe |
| `SV` | El Salvador | El Salvador |
| `SX` | Sint Maarten (Dutch part) | Saint-Martin (partie néerlandaise) |
| `SY` | Syrian Arab Republic | République arabe syrienne |
| `SZ` | Eswatini | Eswatini |
| `TC` | Turks and Caicos Islands | Îles Turques-et-Caïques |
| `TD` | Chad | Tchad |
| `TF` | French Southern Territories | Terres australes françaises |
| `TG` | Togo | Togo |
| `TH` | Thailand | Thaïlande |
| `TJ` | Tajikistan | Tadjikistan |
| `TK` | Tokelau | Tokélaou |
| `TL` | Timor-Leste | Timor-Leste |
| `TM` | Turkmenistan | Turkménistan |
| `TN` | Tunisia | Tunisie |
| `TO` | Tonga | Tonga |
| `TR` | Turkey | Türkiye |
| `TT` | Trinidad and Tobago | Trinité-et-Tobago |
| `TV` | Tuvalu | Tuvalu |
| `TW` | Taiwan | Taïwan |
| `TZ` | United Republic of Tanzania | République-Unie de Tanzanie |
| `UA` | Ukraine | Ukraine |
| `UG` | Uganda | Ouganda |
| `UM` | United States Minor Outlying Islands | Îles mineures éloignées des États-Unis |
| `US` | United States of America | États-Unis d’Amérique |
| `UY` | Uruguay | Uruguay |
| `UZ` | Uzbekistan | Ouzbékistan |
| `VA` | Holy See | Saint-Siège |
| `VC` | Saint Vincent and the Grenadines | Saint-Vincent-et-les Grenadines |
| `VE` | Venezuela (Bolivarian Republic of) | Venezuela (République bolivarienne du) |
| `VG` | British Virgin Islands | Îles Vierges britanniques |
| `VI` | United States Virgin Islands | Îles Vierges américaines |
| `VN` | Viet Nam | Viet Nam |
| `VU` | Vanuatu | Vanuatu |
| `WF` | Wallis and Futuna Islands | Îles Wallis-et-Futuna |
| `WS` | Samoa | Samoa |
| `XK` | Kosovo | Kosovo |
| `YE` | Yemen | Yémen |
| `YT` | Mayotte | Mayotte |
| `ZA` | South Africa | Afrique du Sud |
| `ZM` | Zambia | Zambie |
| `ZW` | Zimbabwe | Zimbabwe |




---

#### `recipient_province` – Recipient Province or Territory / Province ou territoire du bénéficiaire

**Type:** `text`  
**Required:** No  
**Choice Set:** recipient_province (13 values)  


**Description:**  
EN: The "Recipient province or territory" is a mandatory field if the Recipient Country is Canada and identifies where, within Canada, the recipient resides.  
FR: Le champ « province ou territoire du bénéficiaire » est un champ obligatoire si le pays destinataire est le Canada et indique le lieu de résidence du bénéficiaire au Canada.


##### Allowed Values (recipient_province)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `AB` | Alberta | Alberta |
| `BC` | British Columbia | Colombie-Britannique |
| `MB` | Manitoba | Manitoba |
| `NB` | New Brunswick | Nouveau-Brunswick |
| `NL` | Newfoundland &amp; Labrador | Terre-Neuve-et-Labrador |
| `NS` | Nova Scotia | Nouvelle-Écosse |
| `NT` | Northwest Territories | Territoires du Nord-Ouest |
| `NU` | Nunavut | Nunavut |
| `ON` | Ontario | Ontario |
| `PE` | Prince Edward Island | Île-du-Prince-Édouard |
| `QC` | Quebec | Québec |
| `SK` | Saskatchewan | Saskatchewan |
| `YT` | Yukon | Yukon |




---

#### `recipient_city` – Recipient City (English|French) / Ville du bénéficiaire (anglais|français)

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: The "Recipient city" is a mandatory field that identifies which city the recipient operates in. This field can be populated with Canadian or foreign cities.

Official city names should be provided, including both official languages (where applicable in the following format: name English|name French

Free text, but a controlled list from Canada Revenue Agency’s qualified donees list of municipalities can be consulted: Canada Revenue Agency website (http://www.cra-arc.gc.ca/chrts-gvng/qlfd-dns/mncplts-eng.html).
  
FR: La « Ville du bénéficiaire » est un champ obligatoire qui indique la ville où le bénéficiaire exerce ses activités. On peut y inscrire le nom de villes canadiennes ou de villes étrangères.

Nom officiel exact de la ville, y compris dans les deux langues officielles (le cas échéant) au format suivant : nom anglais|nom français

Texte libre, mais une liste contrôlée de la liste des municipalités désignées donataires de l’Agence du revenu du Canada peut être consultée: site Web de l’Agence du revenu du Canada (http://www.cra-arc.gc.ca/chrts-gvng/qlfd-dns/mncplts-fra.html).



---

#### `recipient_postal_code` – Recipient Postal Code / Code postal du bénéficiaire

**Type:** `text`  
**Required:** No  


**Description:**  
EN: The "Recipient postal code" is a mandatory field that serves to identify the specific area in which the recipient operates. In cases where this field cannot be populated this field may be left blank.

Text format locked to "X#X #X#"; The Canada Post tool for looking up a postal code can be found on the Canada Post website.
  
FR: Le « Code postal du bénéficiaire » est un champ obligatoire qui sert à identifier avec précision la région où le bénéficiaire exerce ses activités. Si le fait de remplir ce champ suscite des préoccupations à l'égard de la vie privée, il est possible de le laisser vide.

Format de texte : "X#X #X#"; L'outil de Postes Canada permettant de rechercher un code postal se trouve sur le site Web de Postes Canada.



---

#### `federal_riding_name_en` – Federal Riding Name (English) / Nom de la circonscription fédérale (anglais)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: The federal riding name is the name of the riding in which the recipient resides.  
FR: Le nom de la circonscription fédérale où réside le bénéficiaire.


---

#### `federal_riding_name_fr` – Federal Riding Name (French) / Nom de la circonscription fédérale (français)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: The federal riding name is the name of the riding in which the recipient resides.  
FR: Le nom de la circonscription fédérale où réside le bénéficiaire.


---

#### `federal_riding_number` – Federal Riding Number / Numéro de la circonscription fédérale

**Type:** `text`  
**Required:** No  


**Description:**  
EN: The federal riding number is based on the riding in which the recipient resides.  Departments can consult the Elections Canada website in order to retrieve the federal riding number. http://www.elections.ca/content.aspx?section=res&dir=cir/list&document=index338&lang=e  
FR: Numéro de la circonscription fédérale où réside le bénéficiaire.  Les départements peuvent consulter le site-web d’Élections Canada pour trouver le numéro de la circonscription fédérale. http://www.elections.ca/content.aspx?section=res&dir=cir/list&document=index338&lang=f


---

#### `prog_name_en` – Program Name (English) / Nom du programme (anglais)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: The program name is the name of the program, according to the terms and conditions (Ts&Cs), under which a recipient is funded.  
FR: Le nom du programme selon les modalités en vertu desquelles le financement est versé au bénéficiaire.


---

#### `prog_name_fr` – Program Name (French) / Nom du programme (français)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: The program name is the name of the program, according to the terms and conditions (Ts&Cs), under which a recipient is funded.  
FR: Le nom du programme selon les modalités en vertu desquelles le financement est versé au bénéficiaire.


---

#### `prog_purpose_en` – Program Purpose (English) / But du programme (anglais)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: The program purpose is the program’s purpose according to the Ts&Cs.  
FR: Le but du programme est celui dans lequel le programme a été créé, selon les modalités du programme.


---

#### `prog_purpose_fr` – Program Purpose (French) / But du programme (français)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: The program purpose is the program’s purpose according to the Ts&Cs.  
FR: Le but du programme est celui dans lequel le programme a été créé, selon les modalités du programme.


---

#### `agreement_title_en` – Agreement Title (English) / Titre de l’entente (anglais)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: The agreement title is the title of the project or agreement that the recipient is undertaking. In cases where there is no title, the agreement number will be duplicated here.  
FR: Le nom de l'entente est le titre du projet ou de l'entente à l'égard duquel s'engage le bénéficiaire. S'il n'y a pas de titre, le numéro de l'entente peut être réinscrit ici.


---

#### `agreement_title_fr` – Agreement Title (French) / Titre de l’entente (français)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: The agreement title is the title of the project or agreement that the recipient is undertaking. In cases where there is no title, the agreement number will be duplicated here.  
FR: Le nom de l'entente est le titre du projet ou de l'entente à l'égard duquel s'engage le bénéficiaire. S'il n'y a pas de titre, le numéro de l'entente peut être réinscrit ici.


---

#### `agreement_number` – Agreement Number / Numéro de l’entente

**Type:** `text`  
**Required:** No  


**Description:**  
EN: The agreement number should be the number on the agreement and/or in the departmental Gs&Cs system.  
FR: Le numéro de l'entente est celui qui figure à l'entente et/ou dans le système de subventions et de contributions du ministère.


---

#### `agreement_value` – Agreement Value in CAD / Valeur de l’entente en dollars canadiens

**Type:** `money`  
**Required:** Yes  


**Description:**  
EN: The agreement value is the dollar amount stated in the grant or contribution agreement. This field should be populated with a monetary value in Canadian dollars.  
FR: La valeur de l'entente est le montant en dollars indiqué dans l'entente de subvention ou de contribution. Ce champ doit indiquer une valeur monétaire en dollars canadiens.


---

#### `foreign_currency_type` – Foreign Currency Type / Type de monnaie étrangère

**Type:** `text`  
**Required:** No  
**Choice Set:** foreign_currency_type (94 values)  


**Description:**  
EN: The foreign currency type should be selected if a recipient is paid in a currency other than Canadian dollars. Select the type of foreign currency in this field (for example, US dollar (USD), Australian dollar (AUD), British pound (GBP)). This field is mandatory if the agreement is awarded in foreign currency.'

Foreign currency type is populated using the ISO 4217 alphabetic codes for foreign currency. This list can be found on the XE website. Entry is selected from a drop-down list.
  
FR: Le champ Type de monnaie étrangère doit être rempli si le bénéficiaire est payé dans une devise autre que le dollar canadien. Il faut sélectionner le type de monnaie étrangère; par exemple, dollar américain (USD), dollar australien (AUD), livre sterling (GBP). Ce champ est obligatoire si l'entente est en devise étrangère.

Le type de monnaie étrangère est complété à l'aide des codes alphabétiques ISO 4217 pour les monnaie étrangères. Cette liste se trouve sur le site Web XE. L'entrée est sélectionnée dans une liste déroulante.



##### Allowed Values (foreign_currency_type)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `ALL` | Lek | Lek |
| `AMD` | Armenian Dram | Dram arménien |
| `ANG` | Netherlands Antillean Guilder | Florin des Antilles |
| `AOA` | Kwanza | Kwanza |
| `ARS` | Argentine Peso | Peso argentin |
| `AUD` | Australian Dollar | Dollar australien |
| `AWG` | Aruban Florin | Aruba Florin |
| `AZN` | Azerbaijanian Manat | Azerbaïdjan Manat |
| `BAM` | Convertible Mark | Mark convertible |
| `BBD` | Barbados Dollar | Dollar de la Barbade |
| `BDT` | Taka | Taka |
| `BGN` | Bulgarian Lev | Lev bulgare |
| `BHD` | Bahraini Dinar | Dinar de Bahreïn |
| `BIF` | Burundi Franc | Burundi Franc |
| `BND` | Brunei Dollar | Dollar de Brunei |
| `BOB` | Boliviano | bolivien |
| `BOV` | Mvdol | Mvdol |
| `BRL` | Brazilian Real | Real brésilien |
| `BSD` | Bahamian Dollar | Dollar Bahaméen |
| `BTN` | Ngultrum | Ngultrum |
| `BWP` | Pula | Pula |
| `BYR` | Belarussian Ruble | Rouble biélorusse |
| `BZD` | Belize Dollar | Belize Dollar |
| `CAD` | Canadian Dollar | Dollar canadien |
| `CDF` | Congolese Franc | Franc Congolais |
| `CHF` | Swiss Franc | Franc suisse |
| `CLF` | Unidad de Fomento | Unidad de Fomento  td&gt; |
| `CLP` | Chilean Peso | Peso chilien |
| `CNY` | Yuan Renminbi | Yuan Renminbi |
| `COP` | Colombian Peso | Peso colombien |
| `CRC` | Costa Rican Colon | Colon Costa Rica |
| `CUC` | Peso Convertible | Peso Convertible |
| `CVE` | Cabo Verde Escudo | Escudo Cabo Verde |
| `CZK` | Czech Koruna | Couronne tchèque |
| `DJF` | Djibouti Franc | Djibouti Franc |
| `DKK` | Danish Krone | Couronne danoise |
| `DOP` | Dominican Peso | Peso dominicain |
| `DZD` | Algerian Dinar | Dinar algérien |
| `EGP` | Egyptian Pound | Livre égyptienne |
| `ERN` | Nakfa | Nakfa |
| `ETB` | Ethiopian Birr | Birr éthiopien |
| `EUR` | Euro | Euro |
| `FJD` | Fiji Dollar | Fidji Dollar |
| `GBP` | Pound Sterling | Livre Sterling |
| `GEL` | Lari | Lari |
| `GIP` | Gibraltar Pound | Livre de Gibraltar |
| `GMD` | Dalasi | Dalasi |
| `GNF` | Guinea Franc | Guinée Franc |
| `GTQ` | Quetzal | Quetzal |
| `GYD` | Guyana Dollar | Dollar de Guyana |
| `HKD` | Hong Kong Dollar | Dollar de Hong Kong |
| `HNL` | Lempira | Lempira |
| `HRK` | Kuna | Kuna |
| `HTG` | Gourde | Gourde |
| `HUF` | Forint | Forint |
| `IDR` | Rupiah | Rupiah |
| `ILS` | New Israeli Sheqel | Nouveau Shekel Israelien |
| `INR` | Indian Rupee | Roupie indienne |
| `IQD` | Iraqi Dinar | Dinar irakien |
| `IRR` | Iranian Rial | Rial iranien |
| `ISK` | Iceland Krona | Couronne islandaise |
| `JMD` | Jamaican Dollar | Dollar Jamaïquain |
| `JOD` | Jordanian Dinar | Dinar jordanien |
| `JPY` | Yen | Yen |
| `KES` | Kenyan Shilling | Shilling kenyan |
| `KGS` | Som | Som |
| `KHR` | Riel | Riel |
| `KMF` | Comoro Franc | Comores Franc |
| `KRW` | Won | Won |
| `KWD` | Kuwaiti Dinar | Dinar koweïtien |
| `KYD` | Cayman Islands Dollar | Dollar des Iles Caïmans |
| `KZT` | Tenge | Tenge |
| `LAK` | Kip | Kip |
| `LBP` | Lebanese Pound | Livre libanaise |
| `LRD` | Liberian Dollar | Dollar libérien |
| `LSL` | Loti | Loti |
| `LYD` | Libyan Dinar | Dinar libyen |
| `MGA` | Malagasy Ariary | Ariary Malgache |
| `MKD` | Denar | Denar |
| `MOP` | Pataca | Pataca |
| `MUR` | Mauritius Rupee | Roupie de Maurice |
| `MVR` | Rufiyaa | Rufiyaa |
| `MWK` | Kwacha | Kwacha |
| `MYR` | Malaysian Ringgit | Ringgit malaisien |
| `NOK` | Norwegian Krone | Couronne norvégienne |
| `NZD` | New Zealand Dollar | Dollar néo-zélandais |
| `SVC` | El Salvador Colon | Colon El Salvador |
| `USD` | US Dollar | Dollar US |
| `XAF` | CFA Franc BEAC | Franc CFA BEAC |
| `XCD` | East Caribbean Dollar | Dollar des Caraïbes orientales |
| `XDR` | SDR (Special Drawing Right) | DTS (droit de tirage spécial) |
| `XOF` | CFA Franc BCEAO | Franc CFA BCEAO |
| `XPF` | CFP Franc | Franc CFP |
| `ZAR` | Rand | Rand |




---

#### `foreign_currency_value` – Foreign Currency Value / Valeur de la monnaie étrangère

**Type:** `money`  
**Required:** No  


**Description:**  
EN: The foreign currency value is the amount as signed in the grant or contribution agreement with the recipient. This field should be populated with a monetary value in the foreign currency. This field is mandatory if the agreement is awarded in a foreign currency.  
FR: La valeur en monnaie étrangère est le montant convenu aux termes de l'entente de subvention ou de contribution avec le bénéficiaire. Ce champ doit être rempli en inscrivant la valeur dans la monnaie étrangère. Ce champ est obligatoire si l'entente est en devise étrangère.


---

#### `agreement_start_date` – Agreement Start Date / Date de début de l’entente

**Type:** `date`  
**Required:** Yes  


**Description:**  
EN: The agreement start date is the assumed start of the agreement, or when the project is supposed to begin, as captured in the initial agreement.  
FR: La date de début de l'entente est la date d'entrée en vigueur présumée de l'entente ou la date à laquelle le projet est censé commencer, conformément à l'entente initiale.


---

#### `agreement_end_date` – Projected Agreement End Date / Date de fin prévue de l’entente

**Type:** `date`  
**Required:** No  


**Description:**  
EN: The projected agreement end date is the assumed end of the agreement, or when the project is supposed to end, as captured in the initial agreement.  
FR: La date de fin prévue de l'entente est la date de fin présumée de l'entente, ou la date à laquelle le projet est censé prendre fin, conformément à l'entente initiale.


---

#### `coverage` – Coverage (English|French; ...) / Portée (anglais|français; ...)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: Coverage provides information about what will benefit from the project or agreement. Departments should populate this with any information they have available.  
FR: Le champ « Portée » fournit des renseignements sur l'incidence générale prévue du projet ou de l'entente. Les ministères peuvent entrer ici tout renseignement dont ils disposent.


---

#### `description_en` – Description (English) / Description (anglais)

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: The description explains why the recipient received funding. It should provide a brief yet accurate description of what the recipient is undertaking.  
FR: La description explique à quelles fins le bénéficiaire a reçu le financement. Elle doit décrire de façon brève, mais explicite, en quoi consistent les travaux du bénéficiaire.


---

#### `description_fr` – Description (French) / Description (français)

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: The description explains why the recipient received funding. It should provide a brief yet accurate description of what the recipient is undertaking.  
FR: La description explique à quelles fins le bénéficiaire a reçu le financement. Elle doit décrire de façon brève, mais explicite, en quoi consistent les travaux du bénéficiaire.


---

#### `naics_identifier` – NAICS Identifier / Identificateur du SCIAN

**Type:** `text`  
**Required:** No  


**Description:**  
EN: The North American Industry Classification System (NAICS) is an industry classification system developed by the statistical agencies of Canada, Mexico and the United States.  
FR: Le Système de classification des industries de l'Amérique du Nord (SCIAN) est un système de classification des industries conçu par les organismes statistiques du Canada, du Mexique et des États-Unis.


---

#### `expected_results_en` – Expected Results or Intended Outcome (English) / Résultats attendus ou visés (anglais)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: The expected results or intended outcome is the assumed result of project completion. It should be populated in accordance with the project that the recipient is undertaking or the program under which it is funded. This field will attempt to explain why the project is being undertaken, and what the final results should be.  
FR: Les résultats attendus ou visés sont les résultats présumés qui découlent de l'exécution d'un projet. Le champ doit être rempli en fonction du projet qu'entreprend le bénéficiaire ou conformément au programme en vertu duquel il est financé. Ce champ vise à offrir une description de la raisond'être du projet et de ce que devraient être les résultats finaux.


---

#### `expected_results_fr` – Expected Results or Intended Outcome (French) / Résultats attendus ou visés (français)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: The expected results or intended outcome is the assumed result of project completion. It should be populated in accordance with the project that the recipient is undertaking or the program under which it is funded. This field will attempt to explain why the project is being undertaken, and what the final results should be.  
FR: Les résultats attendus ou visés sont les résultats présumés qui découlent de l'exécution d'un projet. Le champ doit être rempli en fonction du projet qu'entreprend le bénéficiaire ou conformément au programme en vertu duquel il est financé. Ce champ vise à offrir une description de la raisond'être du projet et de ce que devraient être les résultats finaux.


---

#### `additional_information_en` – Additional Information (English) / Renseignements supplémentaires (anglais)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: Additional information is information that departments are required to enter under the guidance instructions for exceptions but that is not captured in any of the aforementioned fields. It may contain information on:
•additional funding departments
•funding through a third party
•ministerial announcements
•research fields
•joint funding
•collaborators and partners
•keywords
•belated reporting
•novation agreements
•terminations
•repayability
  
FR: Lorsqu'ils sont tenus de le faire conformément aux « Indications » qui traitent des exceptions, les ministères doivent entrer ici les renseignements supplémentaires qui ne sont pas saisis dans les champs précédents. Il peut s'agir de renseignements comme ceux-ci :
•autres ministères participent au financement;
•financement par l'intermédiaire d'un tiers;
•annonces ministérielles;
•domaines de recherche;
•financement conjoint;
•collaborateurs et partenaires;
•mots-clés;
•divulgation tardive;
•entente d'innovation;
•résiliations;
•remboursement.



---

#### `additional_information_fr` – Additional Information (French) / Renseignements supplémentaires (français)

**Type:** `text`  
**Required:** No  


**Description:**  
EN: Additional information is information that departments are required to enter under the guidance instructions for exceptions but that is not captured in any of the aforementioned fields. It may contain information on:
•additional funding departments
•funding through a third party
•ministerial announcements
•research fields
•joint funding
•collaborators and partners
•keywords
•belated reporting
•novation agreements
•terminations
•repayability
  
FR: Lorsqu'ils sont tenus de le faire conformément aux « Indications » qui traitent des exceptions, les ministères doivent entrer ici les renseignements supplémentaires qui ne sont pas saisis dans les champs précédents. Il peut s'agir de renseignements comme ceux-ci :
•autres ministères participent au financement;
•financement par l'intermédiaire d'un tiers;
•annonces ministérielles;
•domaines de recherche;
•financement conjoint;
•collaborateurs et partenaires;
•mots-clés;
•divulgation tardive;
•entente d'innovation;
•résiliations;
•remboursement.



---



## Proactive Publication - Grants and Contributions Nothing to Report / Publication proactive – Subventions et contributions, rien à signalerPublication proactive - Subventions et les contributions  (Rien à signaler) 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `fiscal_year` | Year / Année | `text` | Yes |  | fiscal_year |  |
| `quarter` | Quarter / Trimestre | `text` | Yes |  | quarter |  |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `fiscal_year` – Year / Année

**Type:** `text`  
**Required:** Yes  
**Choice Set:** fiscal_year (25 values)  


**Description:**  
EN:   
FR: 


##### Allowed Values (fiscal_year)

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

#### `quarter` – Quarter / Trimestre

**Type:** `text`  
**Required:** Yes  
**Choice Set:** quarter (4 values)  


**Description:**  
EN:   
FR: 


##### Allowed Values (quarter)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `Q1` | April 1 - June 30 | 1 avril - 30 juin |
| `Q2` | July 1 - September 30 | 1 juillet - 30 septembre |
| `Q3` | October 1 - December 31 | 1 octobre - 31 décembre |
| `Q4` | January 1 - March 31 | 1 janvier - 31 mars |




---




## Appendix

### Choice Sets Summary (All Resources)
| Choice Set | Field(s) | Values | Standalone Doc |
|------------|----------|--------|----------------|


### Generation Metadata

- Generated: 2025-09-14T01:24:39 (UTC)
- Source: dictionaries/grants.json
- Commit: `322574e`
- Tool Version: simple-1

### Validation

- JSON Schema Validation: **PASSED**


### Notes

This documentation is auto-generated. Do not hand-edit; instead update the source recombinant JSON and re-run generation.