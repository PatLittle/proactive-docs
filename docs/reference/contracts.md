
# Proactive Publication - Contracts over $10,000 / Publication proactive - Contrats attribués de plus de 10 000 $

**Dataset Type:** `contracts`  
**Last Generated:** 2025-07-25T10:32:45 (UTC)  
**Source:** dictionaries/contracts.json  
**Commit:** `0a495f5`

Access, upload and modify the Contracts over 10K reports for your organization / Accès, téléversement et modification des rapports  sur les contrats attribués de plus de 10 000 $ pour votre organisation

---

## Resources


- [Proactive Publication - Contracts over $10,000 / Publication proactive - Contrats attribués de plus de 10 000 $](#contracts)

- [Proactive Publication - Contracts Nothing to Report / Publication proactive - Contrats (Rien à signaler)](#contracts-nil)


---


## Proactive Publication - Contracts over $10,000 / Publication proactive - Contrats attribués de plus de 10 000 $ 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `reference_number` | Reference Number / Numéro de référence | `text` | Yes |  |  | It is a unique identifier given to each line item in the spreadsheet. Having a … |
| `procurement_id` | Procurement Identification Number / Numéro d’identification d’approvisionnement | `text` | No |  |  | It is recommended that the procurement identification number be the contract nu… |
| `vendor_name` | Vendor Name / Nom du fournisseur | `text` | No |  |  | It is recommended that the vendor name be the legal name of the contractor, as … |
| `vendor_postal_code` | Vendor Postal Code / Code postal du fournisseur | `text` | No |  |  | i. It is recommended that this field be populated with the first three digits o… |
| `buyer_name` | Buyer Name / Nom de l’acheteur | `text` | No |  |  | i. It is recommended that the field be populated with the name of the buyer, as… |
| `contract_date` | Contract Date / Date du contrat | `date` | Yes |  |  | i. It is recommended that the contract date be the date the contract is awarded… |
| `economic_object_code` | Economic Object Code / Code d’article économique | `text` | No |  |  | i. It is recommended that this field be populated with the contract’s numeric e… |
| `description_en` | Description of Work English / Description du travail Anglais | `text` | No |  |  | It is recommended that this field be populated with the economic object code’s … |
| `description_fr` | Description of Work French / Description du travail Français | `text` | No |  |  | It is recommended that this field be populated with the economic object code’s … |
| `contract_period_start` | Contract Period Start Date / Date de début du contrat | `date` | No |  |  | i. For a services or construction services contract, it is recommended that the… |
| `delivery_date` | Contract Period End Date or Delivery Date / Date de clôture du contrat ou Date de livraison | `date` | No |  |  | i. For a goods contract, it is recommended that this field be the date when goo… |
| `contract_value` | Total Contract Value / Valeur totale du contrat | `money` | No |  |  | i. It is recommended that the total contract value be the amount of the hard co… |
| `original_value` | Original Contract Value / Valeur d&#39;origine du contrat | `money` | No |  |  | i. It is recommended that the original contract value be the amount of the hard… |
| `amendment_value` | Contract Amendment Value / Valeur de modification | `money` | No |  |  | i. For an amendment, it is recommended that the contract amendment value be the… |
| `comments_en` | Comments English / Commentaires en anglais | `text` | No |  |  | i. Standardized comments are recommended to be used (refer to Appendix C). Avoi… |
| `comments_fr` | Comments French / Commentaires en français | `text` | No |  |  | i. Standardized comments are recommended to be used (refer to Appendix C). Avoi… |
| `additional_comments_en` | Additional Comments English / Commentaires additionnels en anglais | `text` | No |  |  | The additional comments English field may be populated with additional comments… |
| `additional_comments_fr` | Additional Comments French / Commentaires additionnels en français | `text` | No |  |  | The additional comments French field may be populated with additional comments … |
| `agreement_type_code` | Agreement Type / Type d’accord | `text` | No |  | agreement_type_code | This data field is archived and replaced by the Appendix A data fields for Trad… |
| `trade_agreement` | Trade Agreement / Accord commercial | `_text` | No |  | trade_agreement | i. It is recommended that this field indicate whether the procurement is covere… |
| `land_claims` | Comprehensive Land Claims Agreement / Entente sur les revendications territoriales globales | `_text` | No |  | land_claims | It is recommended that this field indicate whether the procurement is for goods… |
| `commodity_type` | Commodity Type / Type de produit | `text` | No |  | commodity_type | It is recommended that the commodity type be populated with the one of the thre… |
| `commodity_code` | Commodity Code / Code de produit | `text` | No |  |  | i. It is recommended that the commodity code be populated with the generic prod… |
| `country_of_vendor` | Country of Vendor / Pays du fournisseur | `text` | No |  | country_of_vendor | i. It is recommended that this data field be populated with the country of the … |
| `solicitation_procedure` | Solicitation Procedure / Méthode d’invitation à soumissionner | `text` | No |  | solicitation_procedure | It is recommended that this field be populated with one of the five solicitatio… |
| `limited_tendering_reason` | Limited Tendering Reason / Raisons justifiant le recours à l’appel d’offres limité | `_text` | No |  | limited_tendering_reason | It is recommended that this field be populated with one or more of the limited … |
| `trade_agreement_exceptions` | Trade Agreement Exceptions and Exclusions / Exceptions et exclusions applicables aux accords commerciaux | `_text` | No |  | trade_agreement_exceptions | It is recommended that this field to be populated with one or more of the excep… |
| `indigenous_business` | Procurement Strategy for Indigenous Business / Stratégie d’approvisionnement auprès des entreprises autochtones | `text` | No |  | indigenous_business | It is recommended that this field indicate whether the Procurement Strategy for… |
| `indigenous_business_excluding_psib` | Indigenous Business excluding PSIB (formerly PSAB incidental indicator) / Entreprises autochtones excluant le marché réservé en vertu de la SAEA (anciennement Indicateur d’incidence de la SAEA) | `text` | No |  | indigenous_business_excluding_psib | i. It is recommended that this field indicate whether a contract was awarded to… |
| `intellectual_property` | Intellectual Property Indicator / Indicateur de propriété intellectuelle | `text` | No |  | intellectual_property | It is recommended that this field identify whether there are terms and conditio… |
| `potential_commercial_exploitation` | Potential for Commercial Exploitation / Potentiel d&#39;exploitation commerciale | `text` | No |  | potential_commercial_exploitation | It is recommended that this field identify whether intellectual property genera… |
| `former_public_servant` | Former Public Servant in receipt of a PSSA pension / Ancien fonctionnaire recevant une pension en vertu de la LPFP | `text` | No |  | former_public_servant | It is recommended that this field identify whether the contractor is a former p… |
| `contracting_entity` | Contracting Entity / Entité contractante | `text` | No |  | contracting_entity | i. It is recommended that this field identify whether the procurement is a cont… |
| `standing_offer_number` | Standing Offer or Supply Arrangement Number / Numéro de l’offre à commandes | `text` | No |  |  | It is recommended that this field be populated with the Standing Offer or Suppl… |
| `instrument_type` | Instrument Type / Type d’instrument | `text` | No |  | instrument_type | i. It is recommended that the instrument type identify whether the transaction … |
| `ministers_office` | Minister&#39;s Office Contracts / Marchés du cabinet du ministre | `text` | No |  | ministers_office | It is recommended that this field indicate whether the transaction is for the M… |
| `number_of_bids` | Number of Bids / Nombre do soumissions | `int` | No |  |  | It is recommended that this field be populated with the total number of complia… |
| `article_6_exceptions` | Section 6 Government Contracts Regulations Exceptions / Article 6 – Exceptions au Règlement concernant les marches de l’État | `text` | No |  | article_6_exceptions | i. The Government Contracts Regulations requires the solicitation of bids unles… |
| `award_criteria` | Award Criteria / Critères d’attribution | `text` | No |  | award_criteria | It is recommended that this field be populated with one of the bid evaluation m… |
| `socioeconomic_indicator` | Socio-Economic Indicator / Indicateur socioéconomique | `text` | No |  | socioeconomic_indicator | It is recommended for this field to indicate whether the procurement is subject… |
| `reporting_period` | Reporting Period / Periode de déclaration | `text` | No |  | reporting_period | It is recommended that this field be populated in the standard format described… |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `reference_number` – Reference Number / Numéro de référence

**Type:** `text`  
**Required:** Yes  


**Description:**  
EN: It is a unique identifier given to each line item in the spreadsheet. Having a unique identifier for each item will allow users to locate a specific item should they need to modify or delete.  
FR: Un identificateur unique est attribué à chaque article d’exécution du gabarit de rapport.


---

#### `procurement_id` – Procurement Identification Number / Numéro d’identification d’approvisionnement

**Type:** `text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2019-01-01 / Obligatoire pour les marchés conclus après le 2019-01-01  


**Description:**  
EN: It is recommended that the procurement identification number be the contract number. Alternatively, the procurement identification number may be the commitment number or requisition number if this is the standard practice in the department.  
FR: Il est recommandé que le numéro d’identification de l’approvisionnement corresponde au numéro du marché. Sinon, le numéro d’identification de l’approvisionnement peut correspondre au numéro d’engagement ou au numéro de la demande d’achat, s’il s’agit de la pratique courante du ministère.


---

#### `vendor_name` – Vendor Name / Nom du fournisseur

**Type:** `text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2019-01-01 / Obligatoire pour les marchés conclus après le 2019-01-01  


**Description:**  
EN: It is recommended that the vendor name be the legal name of the contractor, as indicated on the contract. Alternatively, the vendor name may be the name in the financial system if this is the standard practice in the department.  
FR: Il est recommandé que le nom du fournisseur corresponde à la dénomination sociale de l’entrepreneur, telle qu’elle est indiquée dans le marché. Sinon, le nom du fournisseur peut correspondre au nom indiqué dans le système financier, s’il s’agit de la pratique courante du ministère.


---

#### `vendor_postal_code` – Vendor Postal Code / Code postal du fournisseur

**Type:** `text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2022-01-01
This field must contain the first three digits of a postal code in A1A format or the value “NA”
 / Obligatoire pour les marchés conclus après le 2022-01-01
Ce champ doit contenir les trois premiers chiffres d’un code postal dans le format A1A ou la valeur « NA »
  


**Description:**  
EN: i. It is recommended that this field be populated with the first three digits of the postal code for the vendor identified in the contract.
ii. Alternatively, the vendor postal code may be the first three digits of the postal code identified in the procurement or financial system if this is the standard practice in the department.
iii. This field is to be populated with “NA” if the vendor is located outside of Canada, as the value “NA” for this field indicates not applicable.
  
FR: i. Il est recommandé de saisir dans ce champ les trois premiers chiffres du code postal du fournisseur indiqué dans le marché.
ii. Sinon, le code postal du fournisseur peut être les trois premiers chiffres du code postal inscrits dans le système financier ou d’approvisionnement s’il s’agit de la pratique courante du ministère.
iii. Il faut indiquer « NA » dans ce champ si le fournisseur se trouve à l’étranger, car la valeur « NA » dans ce champ indique qu’il ne s’applique pas.



---

#### `buyer_name` – Buyer Name / Nom de l’acheteur

**Type:** `text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2022-01-01
This field must be populated with an NA if an amendment is reported under Instrument Type.
 / Obligatoire pour les marchés conclus après le 2022-01-01
Ce champ doit contenir NA si une modification est déclarée sous l’élément Type d’instrument.
  


**Description:**  
EN: i. It is recommended that the field be populated with the name of the buyer, as indicated on the original contract or, alternatively, the individual responsible for the procurement at the department.
ii. For the establishment of a standing offer or supply arrangement agreement, it is recommended that this field be populated with the name of the buyer that issued the original standing offer or supply arrangement agreement.
iii. For a call-up contract against a standing offer or supply arrangement, this field should be the name of the buyer identified in the original call-up contract.
iv. For a contract with task authorizations, this field may be populated with the name of the buyer indicated in the original contract or in the individual task authorization.
v. For amendments, it is recommended that this field be populated with the value “NA,” as the value “NA” for this field indicates not applicable.
vi. For contracts awarded by PSPC or Shared Services Canada (SSC) on behalf of the client department, it is recommended that this field be populated with the name of the PSPC or SSC contracting authority. If this is not available, indicate the values, “PSPC-SPAC” or “SSC-SPC” as applicable.
  
FR: i. Il est recommandé de saisir dans ce champ le nom de l’acheteur, comme il est indiqué dans le marché initial, sinon il faut saisir celui de la personne responsable de l’approvisionnement au ministère.
ii. Dans le cas de l’établissement d’une offre à commandes ou d’un arrangement en matière d’approvisionnement, il est recommandé de saisir dans ce champ le nom de l’acheteur qui a émis l’offre à commandes ou l’arrangement en matière d’approvisionnement initial.
iii. Dans le cas d’une commande subséquente à une offre à commandes ou à un arrangement en matière d’approvisionnement, ce champ devrait indiquer le nom de l’acheteur mentionné dans le marché ou la commande subséquente initial.
iv. Dans le cas d’un marché comportant des autorisations de tâches, ce champ peut comprendre le nom de l’acheteur indiqué dans le marché initial ou dans chaque autorisation de tâches.
v. Pour les modifications de marché, il est recommandé que ce champ soit rempli avec la valeur « NA », car la valeur « NA » pour ce champ indique qu’il ne s’applique pas.
vi. Pour les marchés attribués par SPAC ou SPC pour le compte du ministère client, il est recommandé de saisir le nom de l’autorité contractante de SPAC ou de SPC dans ce champ. S’il n’est pas disponible, il faut indiquer la valeur «  PSPC-SPAC  » ou «  SSC-SPC  », selon le cas.



---

#### `contract_date` – Contract Date / Date du contrat

**Type:** `date`  
**Required:** Yes  


**Description:**  
EN: i. It is recommended that the contract date be the date the contract is awarded by the government. Alternatively, the contract date may be the hard commitment date (the date that the financial commitment is recorded in the departmental financial system) if this is the standard practice in the department.
ii. It is recommended that the contract date for a contract with task authorizations be the date that the contract is awarded (or the hard commitment date) for the contract. When the full value of the contract with task authorizations is likely not to be used, the contract date for each task authorization may be the date that each task authorization is issued (or the hard commitment date).
iii. It is recommended that the contract date for an amended contract or the exercising of an option be the date that the contract is awarded (or the hard commitment date).
iv. It is recommended that the contract date for a confirming order be the date of the verbal contract for goods, services or an amendment. If the date of the verbal contract cannot be determined, the contract date may be the date that the confirming order is issued.
  
FR: i. Il est recommandé que la date du marché corresponde à la date à laquelle le marché a été attribué par le gouvernement. Sinon, il peut s’agir de la date de l’engagement ferme (la date à laquelle l’engagement financier est consigné dans le système financier ministériel) s’il s’agit de la pratique courante du ministère.
ii. Il est recommandé que la date d’un marché qui comprend des autorisations de tâches corresponde à la date d’adjudication du marché (ou à la date de l’engagement ferme) du marché. S’il est probable que le montant du marché comprenant des autorisations de tâches ne sera pas utilisé en totalité, la date du marché pour chaque autorisation de tâche peut être la date à laquelle chaque autorisation de tâche a été accordée (ou la date de l’engagement ferme).
iii. Il est recommandé que la date du marché pour un marché modifié ou l’exercice d’une option corresponde à la date d’adjudication du marché (ou à la date de l’engagement ferme).
iv. Il est recommandé que la date du marché pour une commande de confirmation corresponde à la date du marché verbal de biens ou de services ou d’une modification de marché. Si la date du marché verbal ne peut pas être déterminée, la date du marché peut être la date de la commande de confirmation.



---

#### `economic_object_code` – Economic Object Code / Code d’article économique

**Type:** `text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2019-01-01
This field is limited to only 3 or 4 digits.
If NA, then Instrument Type must be identified as a standing offer/supply arrangement (SOSA).
 / Obligatoire pour les marchés conclus après le 2019-01-01
Ce champ est limité à 3 ou 4 caractères.
Si NA, alors le Type d’instrument doit être identifié comme étant une offre à commandes ou un arrangement en matière d’approvisionnement (SOSA).
  


**Description:**  
EN: i. It is recommended that this field be populated with the contract’s numeric economic object code. Economic object codes are listed in the government-wide chart of accounts. The use of accurate economic object codes is important for maintaining the integrity of the Public Accounts of Canada. Departments are to ensure that all expenditures are coded appropriately in accordance with the Directive on Accounting Standards: GC 5000 Recording Financial Transactions in the Accounts of Canada.
ii. For standing offers and supply arrangement agreements, this field may be populated with the data value “NA” as the value “NA” for this field means not applicable.
iii. When a contract involves more than one economic object, it is recommended that the economic object associated with the largest dollar value be used. A department may use a different approach if this is the standard practice in the department.
  
FR: i.  Il est recommandé de saisir dans ce champ les chiffres du code d’article économique du marché. Les codes d’article économique sont indiqués dans le plan comptable à l’échelle de l’administration fédérale. Il est important d’utiliser les bons codes d’article économique pour préserver l’intégrité des Comptes publics du Canada. Il y aurait lieu pour les ministères de s’assurer que toutes les dépenses sont codées de manière appropriée, conformément à la Directive sur les normes comptables : GC 5000 Inscription des opérations financières dans les comptes du Canada.
ii. Pour les offres à commandes et les arrangements en matière d’approvisionnement, il est recommandé que ce champ soit rempli avec la valeur « NA », car la valeur « NA » pour ce champ indique qu’il ne s’applique pas.
iii. Quand un marché porte sur plus d’un article économique, il est recommandé d’utiliser celui qui correspond à la valeur monétaire la plus élevée. Un ministère peut employer une approche différente si elle correspond à sa pratique courante.



---

#### `description_en` – Description of Work English / Description du travail Anglais

**Type:** `text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2019-01-01 / Obligatoire pour les marchés conclus après le 2019-01-01  


**Description:**  
EN: It is recommended that this field be populated with the economic object code’s text description as listed in the government-wide chart of accounts ( http://www.tpsgc-pwgsc.gc.ca/recgen/pceaf-gwcoa/index-eng.html ). For standing offers and supply arrangement agreements, this field may be populated with the commodity code’s text description used by the federal government for procurement activities.  
FR: Il est recommandé de saisir dans ce champ le texte de description du code d’article économique figurant dans le plan comptable à l’échelle de l’administration fédérale ( http://www.tpsgc-pwgsc.gc.ca/recgen/pceaf-gwcoa/index-fra.html ). Pour les offres à commande et les arrangements en matière d’approvisionnement, ce champ peut comprendre une description du code de produit utilisée par le gouvernement fédéral pour les activités relatives à l’approvisionnement.


---

#### `description_fr` – Description of Work French / Description du travail Français

**Type:** `text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2019-01-01 / Obligatoire pour les marchés conclus après le 2019-01-01  


**Description:**  
EN: It is recommended that this field be populated with the economic object code’s text description as listed in the government-wide chart of accounts ( http://www.tpsgc-pwgsc.gc.ca/recgen/pceaf-gwcoa/index-eng.html ). For standing offers and supply arrangement agreements, this field may be populated with the commodity code’s text description used by the federal government for procurement activities.
  
FR: Il est recommandé de saisir dans ce champ le texte de description du code d’article économique figurant dans le plan comptable à l’échelle de l’administration fédérale ( http://www.tpsgc-pwgsc.gc.ca/recgen/pceaf-gwcoa/index-fra.html ). Pour les offres à commande et les arrangements en matière d’approvisionnement, ce champ peut comprendre une description du code de produit utilisée par le gouvernement fédéral pour les activités relatives à l’approvisionnement.



---

#### `contract_period_start` – Contract Period Start Date / Date de début du contrat

**Type:** `date`  
**Required:** No  
**Validation:** Mandatory for contracts after 2019-01-01
If Commodity Type is a Service (S) or Construction (C) this field must not be empty and must be a valid date.
 / Obligatoire pour les marchés conclus après le 2019-01-01
Si le Type de produit est un service (S) ou une construction (C), ce champ ne doit pas être vide et doit contenir une date valide.
  


**Description:**  
EN: i. For a services or construction services contract, it is recommended that the contract period start date be the starting date for the period of time over which the services are provided.
ii. For a standing or supply arrangement, it is recommended that this field be populated with the starting date for the period of time over which a call-up may be entered into.
iii. For a contract with task authorizations, it is recommended that this field be populated with the starting date for the period of time over the entire contract. For a contract with task authorizations where the full value of a contract with task authorizations is likely not to be used, it is recommended for this field be populated with the starting date for each task authorization.
  
FR: i. Pour un marché de services ou de services de construction, il est recommandé que la date de début du marché corresponde à la date de début de la période au cours de laquelle les services sont fournis.
ii. Pour une offre à commandes ou un arrangement en matière d’approvisionnement, il est recommandé de saisir dans ce champ la date de début de la période au cours de laquelle une commande subséquente est passée.
iii. Pour un marché comprenant des autorisations de tâches, il est recommandé de saisir dans ce champ la date de début de la période correspondant à l’ensemble du marché. Pour un marché comportant des autorisations de tâches et pour lequel il est probable que le montant ne soit pas utilisé au complet, il est recommandé de saisir dans ce champ la date de début de chaque autorisation de tâches.



---

#### `delivery_date` – Contract Period End Date or Delivery Date / Date de clôture du contrat ou Date de livraison

**Type:** `date`  
**Required:** No  
**Validation:** Mandatory for contracts after 2019-01-01 / Obligatoire pour les marchés conclus après le 2019-01-01  


**Description:**  
EN: i. For a goods contract, it is recommended that this field be the date when goods are to be delivered, which may be the contract period end date. The department may use the last delivery date if the contract involves multiple items on multiple dates.
ii. For a services or construction services contract, it is recommended that this field be the end date for the period of time over which the services are provided.
iii. For a standing offer or supply arrangement, it is recommended that this field be the end date for the period of time over which a call-up may be entered into.
iv. For a contract with task authorizations, it is recommended that this field be populated with the end date for the period of time over the entire contract. For a contract with task authorizations where the full value of a contract with task authorization is likely not to be used, it is recommended for this field to be populated with the end date for each task authorization.
  
FR: i. Pour un marché de biens, il est recommandé de saisir dans ce champ la date à laquelle les biens seront livrés, ce qui peut correspondre à la date de fin de la période du marché. Le ministère peut utiliser la dernière date de livraison, si le marché prévoit différentes dates pour différents articles.
ii. Pour un marché de services ou de services de construction, il est recommandé de saisir dans ce champ la date de fin de la période au cours de laquelle les services sont fournis.
iii. Pour une offre à commandes ou un arrangement en matière d’approvisionnement, il est recommandé de saisir dans ce champ la date de fin de la période au cours de laquelle une commande subséquente est passée.
iv. Pour un marché comportant des autorisations de tâches, il est recommandé de saisir dans ce champ la date de fin de la période correspondant à l’ensemble du marché. Pour un marché comportant des autorisations de tâches et pour lequel il est probable que le montant ne soit pas utilisé au complet, il est recommandé de saisir dans ce champ la date de fin de chaque autorisation de tâches.



---

#### `contract_value` – Total Contract Value / Valeur totale du contrat

**Type:** `money`  
**Required:** No  
**Validation:** Mandatory for contracts after 2019-01-01 / Mandatory for contracts after 2019-01-01  


**Description:**  
EN: i. It is recommended that the total contract value be the amount of the hard commitment recorded in the departmental financial system for all contracts and all subsequent amendments regardless of dollar value. It is recommended for this field be in Canadian currency and for it to include all applicable taxes.
ii. For a multi-year contract, it is recommended for this field to be the total amount of the contract for all years.
iii. For a contract amendment, it is recommended for this field to be the amended contract value.
iv. For a contract with task authorizations, the full potential value of the contract may be reported upon contract award unless the full value is not expected to be used. In the latter situation, each task authorization may be reported individually or cumulatively. When a contract includes a fixed deliverable and another deliverable that requires a task authorization, the department may report the contract and task authorizations in any manner that is transparent.
v. The value of this field for the reporting of a standing offer agreement or supply arrangement agreement is $0.
  
FR: i. Il est recommandé que la valeur totale du marché corresponde au montant de l’engagement ferme consigné dans le système financier ministériel pour le marché et toutes les modifications subséquentes, peu importe la valeur en dollars. Il est recommandé d’inscrire dans ce champ les montants en dollars canadiens et d’y ajouter toutes les taxes applicables.
ii. Pour un marché pluriannuel, il est recommandé, de fournir dans ce champ le montant total du marché pour toutes les années.
iii. Pour une modification d’un marché, il est recommandé de saisir dans ce champ la valeur modifiée du marché.
iv. Dans le cas d’un marché comportant des autorisations de tâches, la valeur totale éventuelle du marché peut être déclarée à la date d’adjudication du marché, sauf s’il n’est pas prévu d’utiliser la valeur totale du marché. Dans ce dernier cas, les autorisations de tâches peuvent être déclarées séparément ou en bloc. Si le marché comporte un produit livrable fixe et un autre qui doit être accompagné d’une autorisation de tâches, le ministère peut déclarér le marché et les autorisations de tâches de n’importe quelle façon jugée transparente.
v. La valeur inscrite dans ce champ pour la déclaration d’une offre à commandes ou d’un arrangement en matière d’approvisionnement doit être de 0 $.



---

#### `original_value` – Original Contract Value / Valeur d'origine du contrat

**Type:** `money`  
**Required:** No  
**Validation:** Mandatory for contracts after 2019-01-01 / Obligatoire pour les marchés conclus après le 2019-01-01  


**Description:**  
EN: i. It is recommended that the original contract value be the amount of the hard commitment recorded in the departmental financial system at the time of contract award for a contract or amended contract. It is recommended for this field be in Canadian currency and for it to include all applicable taxes.
ii. For a multi-year contract, it is recommended for this field to be the amount at the time of contract award for the multi-year contract period.
iii. For a contract option, it is recommended for this field to be excluded from the original contract value and for it to be reported at a later date as an amendment when the contract option is exercised. Alternatively, the full value of a contract, including options, may be reported at the time of contract award.
iv. For a contract with task authorizations, it is recommended that the original contract value be for the full amount of the contract rather than the amount specified within the minimum work guarantee clause. The full potential value of the contract may be reported in the original contract value unless the full value is not expected to be used. In the latter situation, each task authorization may be reported individually or cumulatively. When a contract includes a fixed deliverable and another deliverable that requires a task authorization, the department may report the contract and task authorizations in any manner that is transparent.
v. The value of this field for the reporting of a standing offer agreement or supply arrangement agreement should be $0.
  
FR: i. Il est recommandé que la valeur d’origine du marché corresponde au montant de l’engagement ferme consigné dans le système financier ministériel au moment de l’attribution du marché pour un marché ou un marché modifié. Il est recommandé d’inscrire dans ce champs les montants en dollars canadiens et d’y ajouter toutes les taxes applicables.
ii. Pour un marché pluriannuel, il est recommandé d’inscrire dans ce champ la valeur correspondant au montant au moment de l’attribution du marché pour la période du marché pluriannuel.
iii. Pour une option de marché, il est recommandé pour ce champ d’exclure le montant de l’option de l’élément de données « valeur d’origine du marché » pour le déclarer à une date ultérieure à titre de modification lorsqu’elle est exercée. Sinon, la valeur totale du marché, y compris les options, peut être déclarée à la date d’adjudication du marché.
iv. Dans le cas d’un marché comportant des autorisations de tâches, il est recommandé de déclarer dans ce champ la valeur d’origine du marché au lieu du montant précisé dans la clause de garantie des travaux minimums. La valeur totale éventuelle du marché peut être déclarée dans l’élément de données « valeur d’origine du marché », à moins qu’il ne soit par prévu d’utiliser la valeur totale du marché. Dans ce dernier cas, les autorisations de tâches peuvent être déclarées séparément ou en bloc. Si le marché comporte un produit livrable fixe et un autre qui doit être accompagné d’une autorisation de tâches, le ministère peut déclarer le marché et les autorisations de tâches de n’importe quelle façon jugée transparente.
v. La valeur inscrite dans ce champ pour la déclaration d’une offre à commandes ou d’un arrangement en matière d’approvisionnement devrait être de 0 $.



---

#### `amendment_value` – Contract Amendment Value / Valeur de modification

**Type:** `money`  
**Required:** No  
**Validation:** This field must be populated if Amendment (A) was selected as the Instrument Type / Ce champ doit être rempli si Modification (A) a été sélectionné comme Type d’instrument  


**Description:**  
EN: i. For an amendment, it is recommended that the contract amendment value be the value of the contract amendment. Negative amendments should include a minus sign in front of the value. It is recommended for this field to be in Canadian currency and for it to include all applicable taxes.
ii. Multiple amendment(s) to a contract that take place in the same fiscal quarter may be reported either individually or combined. Positive or negative amendments over $10,000 are to be reported quarterly in accordance with Appendix A. Positive or negative amendments of $10,000 and under are to be reported annually via email to PSPC in accordance with Appendix A, and to be reported annually on the Open Government Portal in accordance with Appendix B. An amendment should be reported either quarterly or annually. Reporting an amendment both quarterly and annually would result in double counting of the amendment’s value when calculating the total contracting activity of an organization.
iii. When a contract is entered into and subsequently amended in the same fiscal quarter, the two transactions should be reported separately. Entry into the contract should be reported as a separate entry with the value at contract entry in the original contract value and should not include the value of the contract amendment. The contract amendment should also be reported as a separate entry with the value of the amendment in the contract amendment value and the contract entry value in the original contract value.
iv. For a contract with task authorizations, when the full value is likely not to be used, the value of any subsequent task authorization may be reported as an amendment with its value reported in the contract amendment value.
v. A “0” value should be included if there are no amendments associated with the contract.
  
FR: i. Pour une modification, il est recommandé que l’élément de données « valeur de modification » corresponde à la valeur de la modification. Les modifications de marché négatives doivent inclure un signe négatif devant la valeur. Il est recommandé d’inscrire dans ce champ les montants en dollars canadiens et d’y ajouter toutes les taxes applicables.
ii. Les modifications multiples apportées à un marché au cours du même trimestre de l’exercice financier peuvent être déclarée séparément ou en bloc. Les modifications de marché positives ou négatives de plus de 10 000 $ sont à déclarer tous les trois mois, conformément à l’annexe A. Les modifications positives et négatives de 10 000 $ ou moins sont à déclarer une fois par an au moyen d’un courriel à SPAC, conformément à l’annexe A, et elles doivent être déclarée une fois par an dans le Portail du gouvernement ouvert, conformément à l’annexe B. Une modification de marché doit être déclarée tous les trois mois ou une fois par an. La déclaration d’une modification de marché de façon trimestrielle et annuelle donnerait lieu à un double dénombrement de la valeur de la modification au moment de calculer le total de l’activité contractuelle d’une organisation.
iii. Lorsqu’un marché est conclu, puis modifié au cours du même trimestre d’exercice, les deux opérations doivent être déclarées séparément. La signature du marché doit être saisie comme une entrée séparée, et la valeur au moment de la signature du marché doit être consignée dans l’élément de données « valeur d’origine du marché », sans la valeur de modification. La valeur de modification sera également déclarée dans une entrée distincte qui comprend la valeur de la modification figurant dans le champ de la « valeur de la modification du marché », et la valeur au moment de la signature du marché sera saisie dans l’élément de données « valeur d’origine du marché ».
iv. Dans le cas d’un marché comportant des autorisations de tâches, lorsqu’il est improbable que la valeur totale soit utilisée, la valeur de toute autorisation de tâche ultérieure peut être déclarée en tant que modification, sa valeur étant comprise dans la valeur de la modification.
v. Il faut inscrire « 0 » s’il n’y a pas de modification de marché.



---

#### `comments_en` – Comments English / Commentaires en anglais

**Type:** `text`  
**Required:** No  


**Description:**  
EN: i. Standardized comments are recommended to be used (refer to Appendix C). Avoid the use of acronyms within this field.
ii. Departments are encouraged to provide a brief description of each contract.
iii. When a contract involves an economic object code specified in Appendix D, departments are to fulfill the reporting requirements specified in Appendix D.
  
FR: i. Il est recommandé d’utiliser les commentaires normalisés (consultez l’annexe C). Il faut éviter d’utiliser des acronymes dans ce champ.
ii. Les ministères sont invités à fournir une brève description de chaque marché.
iii. Lorsqu’un marché comprend un code d’article économique précisé à l’annexe D, les ministères doivent satisfaire aux exigences en matière de déclaration précisées à l’annexe D.



---

#### `comments_fr` – Comments French / Commentaires en français

**Type:** `text`  
**Required:** No  


**Description:**  
EN: i. Standardized comments are recommended to be used (refer to Appendix C). Avoid the use of acronyms within this field.
ii. Departments are encouraged to provide a brief description of each contract.
iii. When a contract involves an economic object code specified in Appendix D, departments are to fulfill the reporting requirements specified in Appendix D.
  
FR: i. Il est recommandé d’utiliser les commentaires normalisés (consultez l’annexe C). Évitez d’utiliser des acronymes dans ce champ.
ii. Les ministères sont invités à fournir une brève description de chaque marché.
iii. Lorsqu’un marché comprend un code d’article économique précisé à l’annexe D, les ministères doivent satisfaire aux exigences en matière de déclaration précisées à l’annexe D.



---

#### `additional_comments_en` – Additional Comments English / Commentaires additionnels en anglais

**Type:** `text`  
**Required:** No  


**Description:**  
EN: The additional comments English field may be populated with additional comments when an organization needs additional capacity to fulfill the reporting requirements under the comments English data field.  
FR: Ce champ sert à consigner tout commentaire additionnel lorsqu’une organisation a besoin d’une capacité additionnelle pour répondre aux exigences de déclaration dans le champ « commentaires en anglais ».


---

#### `additional_comments_fr` – Additional Comments French / Commentaires additionnels en français

**Type:** `text`  
**Required:** No  


**Description:**  
EN: The additional comments French field may be populated with additional comments when an organization needs additional capacity to fulfill the reporting requirements under the comments French data field.  
FR: Ce champ sert à consigner tout commentaire additionnel lorsqu’une organisation a besoin d’une capacité additionnelle pour répondre aux exigences de déclaration dans le champ « commentaires en   français ».


---

#### `agreement_type_code` – Agreement Type / Type d’accord

**Type:** `text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2019-01-01, unless Trade Agreement specified.

This field must be blank if the Trade Agreement field Type is not blank.
 / Obligatoire pour les marchés conclus après le 2019-01-01, sauf si on précise un accord commercial.

Ce champ doit être vide si le champ Accord commercial n’est pas vide.
  
**Choice Set:** agreement_type_code (45 values)  


**Description:**  
EN: This data field is archived and replaced by the Appendix A data fields for Trade Agreement, Comprehensive Land Claims Agreement and Procurement Strategy for Indigenous Business.  
FR: Ce champ de données est archivé et remplacé par les champs de données de l’annexe A pour l’Accord de libre-échange, l’entente sur les revendications territoriales globales et la Stratégie d’approvisionnement auprès des entreprises autochtones.


##### Allowed Values (agreement_type_code)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `0` | None | Aucun |
| `A` | ABSA | MREA |
| `C` | NAFTA / CFTA | ALENA / ALEC |
| `D` | CETA / TCA / CFTA | AECG / ACC / ALEC |
| `E` | CETA / TCA / WTO-AGP / CFTA / CCFTA / CCoFTA / CHFTA / CPaFTA / CPFTA / CKFTA | AECG / ACC / AMP-OMC / ALEC / ALECC / ALECCo / ALECH / ALECPa / ALECP / ALECCS |
| `F` | CETA / TCA / WTO-AGP / NAFTA / CFTA / CCFTA / CCoFTA / CHFTA / CPaFTA / CPFTA / CKFTA | AECG / ACC / AMP-OMC / ALENA / ALEC / ALECC / ALECCo / ALECH / ALECPa / ALECP / ALECCS |
| `I` | CFTA | ALEC |
| `R` | LCSA | MRERT |
| `S` | NAFTA / CFTA / CCFTA / CCoFTA / CHFTA / CPaFTA / CKFTA | ALENA / ALEC / ALECC / ALECCo / ALECH / ALECPa / ALECCS |
| `T` | NAFTA / CFTA / CCFTA / CCoFTA / CHFTA / CPaFTA / CPFTA / CKFTA | ALENA / ALEC / ALECC / ALECCo / ALECH / ALECPa / ALECP / ALECCS |
| `V` | CFTA / CCFTA / CKFTA | ALEC / ALECC / ALECCS |
| `W` | WTO-AGP / CFTA / CCFTA / CCoFTA / CHFTA / CPaFTA / CPFTA / CKFTA | AMP-OMC / ALEC / ALECC / ALECCo / ALECH / ALECPa / ALECP / ALECCS |
| `X` | WTO-AGP / CFTA / CCFTA / CKFTA | AMP-OMC / ALEC / ALECC / ALECCS |
| `Y` | WTO-AGP / NAFTA / CFTA / CCFTA / CCoFTA / CHFTA / CPaFTA / CPFTA / CKFTA | AMP-OMC / ALENA / ALEC / ALECC / ALECCo / ALECH / ALECPa / ALECP / ALECCS |
| `Z` | WTO-AGP / NAFTA | AMP-OMC / ALENA |
| `AB` | CFTA / CCFTA / CCoFTA / CHFTA / CPaFTA / CKFTA | ALEC / ALECC / ALECCo / ALECH / ALECPa / ALECCS |
| `AC` | CFTA / CCFTA / CCoFTA / CHFTA / CPaFTA / CPFTA / CKFTA | ALEC / ALECC / ALECCo / ALECH / ALECPa / ALECP / ALECCS |
| `AD` | CETA / TCA / WTO-AGP / CFTA / CCFTA / CKFTA | AECG / ACC / AMP-OMC / ALEC / ALECC / ALECCS |
| `AF` | CFTA / CHFTA | ALEC / ALECH |
| `AG` | CETA / TCA / CFTA / CHFTA | AECG / ACC / ALEC / ALECH |
| `AH` | CKFTA | ALECCS |
| `AI` | CFTA / CKFTA | ALEC / ALECCS |
| `AJ` | CFTA / NAFTA / CKFTA | ALEC / ALENA / ALECCS |
| `AK` | CPTPP | PTPGP |
| `AN` | CFTA / CHFTA / CETA / TCA / CPTPP | ALEC / ALECH / AECG / ACC / PTPGP |
| `AO` | CFTA / CCFTA / CKFTA / WTO-AGP / CPTPP | ALEC / ALECC / ALECCS / AMP-OMC / PTPGP |
| `AP` | CFTA / NAFTA / CCFTA / CCoFTA / CHFTA / CPaFTA / CPFTA / CKFTA / WTO-AGP / CETA / TCA / CPTPP | ALEC / ALENA / ALECC / ALECCo / ALECH / ALECPa / ALECP / ALECCS / AMP-OMC / AECG / ACC / PTPGP |
| `AQ` | CFTA / CCFTA / CCoFTA / CHFTA / CPaFTA / CPFTA / CKFTA / WTO-AGP / CETA / TCA / CPTPP | ALEC / ALECC / ALECCo / ALECH / ALECPa / ALECP / ALECCS / AMP-OMC / AECG / ACC / PTPGP |
| `AR` | CFTA / NAFTA / CCFTA / CCoFTA / CHFTA / CPaFTA / CPFTA / CKFTA / WTO-AGP / CPTPP | ALEC / ALENA / ALECC / ALECCo / ALECH / ALECPa / ALECP / ALECCS / AMP-OMC / PTPGP |
| `AS` | CFTA / CCFTA / CCoFTA / CHFTA / CPaFTA / CPFTA / CKFTA / WTO-AGP / CPTPP | ALEC / ALECC / ALECCo / ALECH / ALECPa / ALECP / ALECCS / AMP-OMC / PTPGP |
| `AT` | CFTA / CCFTA / CKFTA | ALEC / ALECC / ALECCS |
| `AU` | CFTA / CCFTA / CKFTA / WTO-AGP / CETA / TCA / CPTPP | ALEC / ALECC / ALECCS / AMP-OMC / AECG / ACC / PTPGP |
| `AV` | CFTA / CCFTA | ALEC / ALECC |
| `AW` | CFTA / CCFTA / CPTPP | ALEC / ALECC / PTPGP |
| `AX` | CFTA / CKFTA / WTO-AGP / CETA / TCA | ALEC / ALECCS / AMP-OMC / AECG / ACC |
| `AY` | CFTA / CKFTA / WTO-AGP / CETA / TCA / CPTPP | ALEC / ALECCS / AMP-OMC / AECG / ACC / PTPGP |
| `AZ` | CFTA / CKFTA / WTO-AGP / CPTPP | ALEC / ALECCS / AMP-OMC / PTPGP |
| `BA` | ABSA / LCSA | MREA / MRERT |
| `N` | (discontinued) NAFTA / CCFTA / CCoFTA / CHFTA / CPaFTA | (discontinué) ALENA / ALECC / ALECCo / ALECH / ALECPa |
| `P` | (discontinued) NAFTA / CFTA / CCFTA / CCoFTA / CHFTA / CPaFTA | (discontinué) ALENA / ALEC / ALECC / ALECCo / ALECH / ALECPa |
| `U` | (discontinued) CCFTA | (discontinué) ALECC |
| `AA` | (discontinued) CCFTA / CCoFTA / CHFTA / CPaFTA | (discontinué) ALECC / ALECCo / ALECH / ALECPa |
| `AE` | (discontinued) CHFTA | (discontinué) ALECH |
| `AL` | (discontinued) CFTA / CPTPP | (discontinué) ALEC / PTPGP |
| `AM` | (discontinued) CFTA / CETA / TCA / CPTPP | (discontinué) ALEC / AECG / ACC / PTPGP |




---

#### `trade_agreement` – Trade Agreement / Accord commercial

**Type:** `_text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2022-01-01

If the value XX (none) is entered, then no other value can be entered in this field.

This field must be blank if the Agreement Type field is not blank.
 / Obligatoire pour les marchés conclus après le 2022-01-01

Si la valeur XX (aucun) est inscrite, alors aucune autre valeur ne peut être inscrite dans ce champ.

Ce champ doit être vide si le champ Type d’accord n’est pas vide.
  
**Choice Set:** trade_agreement (14 values)  


**Description:**  
EN: i. It is recommended that this field indicate whether the procurement is covered by each of the applicable trade agreements.
ii. It is recommended that this field be populated with one or more of the following alphabetic characters. Report the alphabetic characters only. All text after the alphabetic characters, including the colon, is for information purposes only. For example, a procurement covered by the Canadian Free Trade Agreement and the Comprehensive Economic Free Trade Agreement is reported as CA, EU.
  
FR: i. Il est recommandé d’indiquer dans ce champ si l’approvisionnement est visé par chacun des accords commerciaux applicables.
ii. Il est recommandé de remplir ce champ avec un ou plusieurs des caractères alphabétiques suivants. Il faut indiquer uniquement les caractères alphabétiques. Tout le texte après les caractères alphabétiques, y compris les deux-points, est fourni à titre informatif uniquement. À titre d’exemple, un approvisionnement visé par l’Accord de libre-échange canadien et l’Accord économique et commercial global entre le Canada et l’Union européenne est déclaré sous le code CA, EU.



##### Allowed Values (trade_agreement)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `CA` | Canadian Free Trade Agreement | Accord de libre-échange Canadien |
| `CL` | Canada-Chile Free Trade Agreement | Accord de libre-échange Canada-Chili |
| `CO` | Canada-Colombia Free Trade Agreement | Accord de libre-échange Canada-Colombie |
| `EU` | Comprehensive Economic Free Trade Agreement | Accord économique et commercial global |
| `GP` | World Trade Organization – Agreement on Government Procurement | Accord sur les marchés publics de l’Organisation mondiale du commerce |
| `HN` | Canada-Honduras Free Trade Agreement | Accord de libre-échange Canada-Honduras |
| `KR` | Canada-Korea Free Trade Agreement | Accord de libre-échange Canada-Corée du Sud |
| `NA` | North American Free Trade Agreement | Accord de libre-échange nord-américain |
| `PA` | Canada-Panama Free Trade Agreement | Accord de libre-échange Canada-Panama |
| `PE` | Canada-Peru Free Trade Agreement | Accord de libre-échange Canada-Pérou |
| `TP` | Comprehensive and Progressive Agreement for Trans-Pacific Partnership | Accord de Partenariat transpacifique global et progressiste |
| `UA` | Canada-Ukraine Free Trade Agreement | Accord de libre-échange Canada-Ukraine |
| `UK` | Canada-United Kingdom Trade Continuity Agreement | Accord de continuité commerciale Canada Royaume-Uni |
| `XX` | None | Aucune valeur |




---

#### `land_claims` – Comprehensive Land Claims Agreement / Entente sur les revendications territoriales globales

**Type:** `_text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2022-01-01.

If the value NA (not applicable) is entered, then no other value can be entered in this field.
 / Obligatoire pour les marchés conclus après le 2022-01-01.

Si la valeur NA (sans objet) est inscrite, alors aucune autre valeur ne peut être inscrite dans ce champ.
  
**Choice Set:** land_claims (27 values)  


**Description:**  
EN: It is recommended that this field indicate whether the procurement is for goods, services or construction services to be delivered to an area that is within one or more of the Comprehensive Land Claims Agreements.  
FR: Il est recommandé d’indiquer dans ce champ si l’approvisionnement concerne des biens, des services ou des services de construction qui doivent être fournis dans une région visée par l’une des ententes sur les revendications territoriales globales.


##### Allowed Values (land_claims)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `CH` | Champagne and Aishihik First Nations Final Agreement | Entente définitive des Premières Nations de Champagne et de Aishihik |
| `CT` | Carcross/Tagish First Nation Final Agreement | Entente définitive de la Première Nation de Carcross-Tagish |
| `EM` | Eeyou Marine Region Land Claims Agreement | Accord sur les revendications territoriales concernant la région marine d’Eeyou |
| `FN` | First Nation of Nacho Nyak Dun Final Agreement | Entente définitive de la Première nation des Nacho Nyak Dun |
| `GW` | Gwich&#39;in Comprehensive Land Claim Agreement | Entente sur la revendication territoriale globale des Gwich’in |
| `IF` | Inuvialuit Final Agreement | Convention définitive des Inuvialuits |
| `JN` | James Bay and Northern Quebec Agreement | Convention de la Baie James et du Nord québécois |
| `KD` | Kwanlin Dun First Nation Final Agreement | Entente définitive de la Première nation des Kwanlin Dun |
| `KF` | Kluane First Nation Final Agreement | Entente définitive avec la Première nation de Kluane |
| `LI` | Labrador Inuit Land Claim Agreement | Accord sur les revendications territoriales des Inuit du Labrador |
| `LS` | Little Salmon/Carmacks First Nation Final Agreement | Entente définitive de la Première nation de Little Salmon/Carmacks |
| `MF` | Maa-nulth First Nations Final Agreement | Accord définitif des premières nations maa-nulthes |
| `NA` | Not Applicable | Sans objet |
| `NF` | Nisga&#39;a Final Agreement | Accord définitif Nisga’a |
| `NI` | Nunavik Inuit Land Claims Agreement | Accord sur les revendications territoriales des Inuit du Nunavik |
| `NQ` | Northeastern Quebec Agreement | Convention du Nord-Est québécois |
| `NU` | Nunavut Agreement (Agreement between the Inuit of the Nunavut Settlement Area and Her Majesty the Queen in right of Canada) | Accord du Nunavut (Accord entre les Inuit de la région du Nunavut et Sa Majesté la Reine du chef du Canada) |
| `SD` | Sahtu Dene and Metis Comprehensive Land Claim Agreement | Entente sur la revendication territoriale globale des Dénés et des Métis du Sahtu |
| `SF` | Selkirk First Nation Final Agreement | Entente définitive de la Première nation de Selkirk |
| `TA` | Tlicho Agreement | Accord tlicho |
| `TF` | Tsawwassen First Nation Final Agreement | Accord définitif de la Première Nation de Tsawwassen |
| `TH` | Tr&#39;ondëk Hwëch&#39;in Final Agreement | Entente définitive des Tr’ondëk Hwëch’in |
| `TK` | Ta&#39;an Kwach&#39;an Council Final Agreement | Entente définitive du conseil des Ta’an Kwach’an |
| `TL` | Tla&#39;amin Final Agreement | Accord définitif des Tla’amins |
| `TT` | Teslin Tlingit Council Final Agreement | Entente définitive du Conseil des Tlingits de Teslin |
| `VG` | Vuntut Gwitchin First Nation Final Agreement | Entente définitive de la Première nation des Gwitchin Vuntut |
| `YA` | Yale First Nations Final Agreement | Accord définitif de la Première Nation de Yale |




---

#### `commodity_type` – Commodity Type / Type de produit

**Type:** `text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2019-01-01 / Obligatoire pour les marchés conclus après le 2019-01-01  
**Choice Set:** commodity_type (3 values)  


**Description:**  
EN: It is recommended that the commodity type be populated with the one of the three commodity types (Good, Service or Construction). When a contract involves more than one commodity type, the commodity type associated with the largest dollar value should be used. A department may use a different approach if this is the standard practice in the department.  
FR: Il est recommandé de saisir dans ce champ l’un des trois types de produits (bien, service ou construction). Lorsqu’un marché comprend plus d’un type de produit, il faut utiliser celui qui correspond à la valeur monétaire la plus élevée. Un ministère peut employer une approche différente si elle correspond à sa pratique courante.


##### Allowed Values (commodity_type)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `C` | Construction | Construction |
| `G` | Good | Biens |
| `S` | Service | Services |




---

#### `commodity_code` – Commodity Code / Code de produit

**Type:** `text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2019-01-01
The field is limited to eight alpha-numeric digits or less.
 / Obligatoire pour les marchés conclus après le 2019-01-01 Ce champ est limité à 8 caractères alphanumériques.  


**Description:**  
EN: i. It is recommended that the commodity code be populated with the generic product descriptions used by the federal government for procurement activities.
ii. When using the Goods and Services Identification Number (GSIN), only those GSINs published by PSPC may be used. The commodity code for goods must use a minimum of four numeric characters. The commodity code for services must use either a minimum of one alphabetic character and three numeric characters or, two alphabetic characters and two numeric characters. The commodity code for construction must use a minimum of “51” and one or two numeric characters.
iii. When a contract involves more than one commodity code, the commodity code associated with the largest dollar value should be used. A department may use a different approach if this is the standard practice in the department.
  
FR: i. Il est recommandé de saisir dans ce champ les descriptions de produits génériques utilisées par le gouvernement fédéral pour les activités relatives à l’approvisionnement.
ii. Lorsqu’il s’agit d’utiliser le numéro d’identification des biens et services (NIBS), seulement les NIBS publiés par SPAC peuvent être utilisés. Le code de produit pour les biens doit comprendre un minimum de quatre caractères numériques. Le code de produit pour les services doit comprendre au minimum un caractère alphabétique et trois caractères numériques ou deux caractères alphabétiques et deux caractères numériques. Le code de produit pour la construction doit comprendre au minimum « 51 », suivi d’un ou de deux caractères numériques.
iii. Lorsqu’un marché comprend plus qu’un code de produit, il faut utiliser celui qui correspond à la valeur monétaire la plus élevée. Un ministère peut employer une approche différente si elle correspond à sa pratique courante.



---

#### `country_of_vendor` – Country of Vendor / Pays du fournisseur

**Type:** `text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2019-01-01 / Obligatoire pour les marchés conclus après le 2019-01-01  
**Choice Set:** country_of_vendor (250 values)  


**Description:**  
EN: i. It is recommended that this data field be populated with the country of the vendor’s address identified in the contract.
ii. Alternatively, the country of the vendor may be the country of the vendor’s address identified in the procurement or financial system if this is the standard practice in the department.
iii. The country of vendor must be alphabetic characters listed in the International Organization for Standardization (ISO) 3166 Country Codes.
  
FR: i. Il est recommandé de remplir ce champ de données en indiquant le pays indiqué dans l’adresse du fournisseur qui figure dans le marché.
ii. Par ailleurs, le pays du fournisseur peut être le pays indiqué dans l’adresse du fournisseur qui figure dans le système financier ou d’approvisionnement s’il s’agit de la pratique courante au sein du ministère.
iii. Le pays du fournisseur doit comprendre les caractères alphabétiques répertoriés dans les Codes des nom des pays - 3166 de l’Organisation internationale de normalisation (ISO).



##### Allowed Values (country_of_vendor)

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

#### `solicitation_procedure` – Solicitation Procedure / Méthode d’invitation à soumissionner

**Type:** `text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2022-01-01

If “TC” (Competitive - Traditional), “TN” (Non-Competitive) or “AC” (Advanced Contract Award Notice) is selected and trade agreement with a value other than “XX” (None) is selected, limited tendering cannot have a value of “0” or “00” (None), for contracts after 2022-01-01.
 / Obligatoire pour les marchés conclus après le 2022-01-01

Si les options « TC » (Concurrentielle - Traditionnelle), « TN » (non concurrentielle) ou « AC » (préavis d’attribution de contrat) sont sélectionnées et qu’une entente de marché ayant une valeur autre que « XX » (nulle) est sélectionnée, le champ Appel d’offres restreint ne peut avoir la valeur « 0 » ou « 00 » (nulle), pour les marchés conclus après le 2022-01-01.
  
**Choice Set:** solicitation_procedure (5 values)  


**Description:**  
EN: It is recommended that this field be populated with one of the five solicitation procedures listed below:
  •	AC: Advance Contract Award Notice (ACAN) refers to a contract awarded to a supplier identified under an ACAN process where it was determined that there were no other statements of capabilities that could successfully meet the government’s requirements.
  • OB: Competitive – Open Bidding (Government Electronic Tendering System (GETS)) refers to a competitive contract where bids were solicited via GETS.
  •	TC: Competitive – Traditional refers to a competitive contract where bids were not solicited via GETS, but through another medium, such as soliciting bids directly from suppliers by email or phone.
  •	ST: Competitive – Selective Tendering refers to a solicitation procedure permitted under Canada’s trade agreements where qualified suppliers are selected from a source list (including single-use or multi-use lists) under the selective tendering procedural rules in Canada’s trade agreements.
  •	TN: Non-competitive refers to a contract awarded to a supplier without soliciting bids.
  
FR: Il est recommandé de saisir dans ce champ l’une des cinq méthodes d’invitation à soumissionner énumérées ci-dessous.
  •	AC: Préavis d’adjudication de contrat (PAC) fait référence à un contrat attribué à un fournisseur dans le cadre du processus de PAC lorsqu’il a été déterminé qu’aucun autre énoncé de capacités ne répondait aux exigences du gouvernement.
  •	OB: Concurrentielle – Invitation ouverte à soumissionner (Service électronique d’appels d’offres – SEAO) fait référence à un marché concurrentiel pour lequel l’appel d’offres a été fait par le biais du SEAO.
  •	TC: Concurrentielle – Traditionnelle fait référence à un marché concurrentiel l’appel d’offres n’a pas été fait par le biais du SEAO, mais par un autre moyen, comme la demande de soumissions directement auprès des fournisseurs par courriel ou par téléphone.
  •	ST: Concurrentielle – Appel d’offres sélectif fait référence à une procédure de sollicitation autorisée en vertu des accords commerciaux du Canada selon laquelle les fournisseurs qualifiés sont sélectionnés à partir d’une liste de sources (y compris des listes à usage unique ou à usage multiple) en vertu des règles procédurales d’appel d’offres sélectif des accords commerciaux du Canada.
  •	TN: Non concurrentielle fait référence à un marché attribué à un fournisseur sans appel d’offres.



##### Allowed Values (solicitation_procedure)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `AC` | Advance Contract Award Notice | Préavis d’adjudication de contrat |
| `OB` | Competitive – Open Bidding (GETS) | Concurrentielle – Invitation ouverte à soumissionner (SEAOG) |
| `ST` | Competitive – Selective Tendering | Concurrentielle – Appel d’offres sélectif |
| `TC` | Competitive – Traditional | Concurrentielle – Traditionnelle |
| `TN` | Non-Competitive | Non concurrentielle |




---

#### `limited_tendering_reason` – Limited Tendering Reason / Raisons justifiant le recours à l’appel d’offres limité

**Type:** `_text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2022-01-01.

If the value 00 (none) is entered, then no other value can be entered in this field.

If TC, TN or AC is selected in the Solicitation Procedure data field with a value other than XX (None) selected in the Trade Agreement data field, then a Limited Tendering value other than 00 (none) must be entered, for contracts after 2022-01-01.
 / Obligatoire pour les marchés conclus après le 2022-01-01.

Si la valeur 00 (aucune) est inscrite, alors aucune autre valeur ne peut être inscrite dans ce champ.

Si TC, TN ou AC est sélectionné dans le champ de données Méthode d’invitation à soumissioner avec une valeur autre que XX (Aucune) sélectionnée dans le champ de données Accord commercial, une valeur d'offre limitée autre que 0 (aucune) doit être entrée, pour les marchés conclus après le 2022-01-01.
  
**Choice Set:** limited_tendering_reason (20 values)  


**Description:**  
EN: It is recommended that this field be populated with one or more of the limited tendering reasons listed below.  
FR: Il est recommandé de saisir dans ce champ une ou plusieurs raisons justifiant le recours à l’appel d’offres limité énumérées ci-dessous.


##### Allowed Values (limited_tendering_reason)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `00` | None | Aucune |
| `05` | No response to bid solicitation | Aucune réponse à une invitation à soumissionner |
| `20` | Goods purchased on a commodity market | Biens achetés conformément à un marché de produits de base |
| `21` | Purchases made under exceptionally advantageous conditions | Achats effectués selon des conditions exceptionnellement avantageuses |
| `22` | Winner of an architectural design contest | Lauréat d’un concours de conception architecturale |
| `23` | Consulting services regarding matters of a confidential nature (for contracts not covered by CETA, TCA ,WTO-GPA, CPTPP, CKFTA and CUFTA) | Services confidentiels d’experts-conseils (pour les marchés non visés par l’AECG, l’ACC, l’AMP-OMC, le PTPGP, l’ALECC et l’ALECU) |
| `30` | Work on a property by a contractor according to a warranty or guarantee (for contracts that are only covered by the CFTA) | Travaux exécutés sur un bien par un entrepreneur conformément à une garantie (pour les marchés qui sont visés par l’ALEC seulement) |
| `31` | Work on a leased building or related property performed only by the lessor (for contracts that are only covered by the CFTA) | Travaux exécutés sur un édifice loué ou un bien connexe qui sont réalisés par le locateur seulement (pour les marchés qui sont visés par l’ALEC seulement) |
| `32` | Subscriptions to newspapers, magazines, or other periodicals (for contracts that are only covered by the CFTA) | Abonnements à des journaux, des magazines ou d’autres périodiques (pour les marchés qui sont visés par l’ALEC seulement) |
| `33` | Goods regarding matters of a confidential or privileged nature (for contracts that are only covered by the CFTA) | Biens concernant des questions de nature confidentielle ou privilégiée (pour les marchés qui sont visés par l’ALEC seulement) |
| `71` | Exclusive rights | Droits exclusifs |
| `72` | Prototype purchase | Achat de prototype |
| `74` | Additional deliveries (formerly Interchangeable Parts) | Livraisons supplémentaires (anciennement Pièces interchangeables) |
| `81` | Extreme urgency | Urgence extrême |
| `24` | Additional construction services (discontinued as of 2022-01-01) | Services de construction supplémentaire (discontinué à partir de 2022-01-01) |
| `25` | New construction services (discontinued as of 2022-01-01) | Nouveaux services de construction (discontinué à partir de 2022-01-01) |
| `85` | Low dollar-value (discontinued as of 2022-01-01) | Faible valeur (discontinué à partir de 2022-01-01) |
| `86` | Prices and/or sources fixed by government regulations (discontinued as of 2022-01-01) | Prix ou fournisseurs déterminés par des règlements gouvernementaux (discontinué à partir de 2022-01-01) |
| `87` | Government objectives representing best interests/value (discontinued as of 2022-01-01) | Objectifs gouvernementaux représentant les meilleurs (discontinué à partir de 2022-01-01) |
| `90` | Protection of human, animal, or plant Life or health (discontinued as of 2022-01-01) | Protection de la vie ou de la santé des personnes, animaux, plantes (discontinué à partir de 2022-01-01) |




---

#### `trade_agreement_exceptions` – Trade Agreement Exceptions and Exclusions / Exceptions et exclusions applicables aux accords commerciaux

**Type:** `_text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2019-01-01

If the value 00 (none) is entered, then no other value can be entered in this field.
 / Obligatoire pour les marchés conclus après le 2019-01-01

Si la valeur 00 (aucune) est inscrite, alors aucune autre valeur ne peut être inscrite dans ce champ.
  
**Choice Set:** trade_agreement_exceptions (15 values)  


**Description:**  
EN: It is recommended that this field to be populated with one or more of the exceptions or exclusions listed below.  
FR: Il est recommandé de saisir dans ce champ une ou plusieurs des exceptions ou exclusions énumérées ci-dessous.


##### Allowed Values (trade_agreement_exceptions)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `00` | None | Aucune |
| `01` | Shipbuilding and repair (applies to all agreements except the CFTA) | Contrats de construction et réparation de navires (s’applique à tous les accords sauf l’ALEC) |
| `02` | Urban rail and urban transportation equipment systems, components and materials (applies to all agreements except CFTA, CETA, TCA and CPTPP) | Marchés portant sur du matériel et des systèmes de transport ferroviaire urbain et de transport en commun urbain, les éléments et matériaux servant à leur fabrication, ainsi que tous les matériaux de fer ou d’acier reliés à ces projets (s’applique à tous les accords sauf l’ALEC, l’AECG, l’ACC et le PTPGP) |
| `03` | Contracts respecting FSC 58 (communications, detection and coherent radiation equipment) (applies to all agreements except CFTA, CETA, TCA and CPTPP) | Marchés relevant de la Classification fédérale des approvisionnements (CFA) 58 (matériel de communications, de détection et de rayonnement cohérent) (s’applique à tous les accords sauf l’ALEC, l’AECG, l’ACC et le PTPGP) |
| `04` | Set-asides for small and minority businesses (discontinued as of 2022-01-01) | Marchés réservés aux petites entreprises et aux entreprises minoritaires (discontinué à partir de 2022-01-01) |
| `05` | Agricultural products made in furtherance of agricultural support programs or human feeding programs (applies to all agreements except for CFTA) | Achats de produits agricoles effectués dans le cadre de programmes de soutien à l’agriculture ou de programmes d’aide alimentaire (s’applique à tous les accords sauf l’ALEC) |
| `06` | The Depts. of Transport, Communications and Fisheries &amp; Oceans respecting FSC 70, 74, 36 (applies to all agreements except CFTA, CKFTA, WTO-AGP, CUFTA, CETA, TCA and CPTPP) | Marchés de Transports Canada, du ministère des Communications et de Pêches et Océans dans les catégories FSC 70, 74, 36 (s’applique à tous les accords sauf l’ALEC, l’ALECC, l’AMP-OMC, l’ALECU, l’AECG, l’ACC et le PTPGC) |
| `07` | Any measures for Indigenous peoples and businesses, including set asides for Indigenous businesses (applies to all agreements) | Toute mesure en faveur des peuples et des entreprises autochtones, y compris les marchés réservés aux entreprises autochtones (s’applique à tous les accords) |
| `08` | Set-asides for small businesses other than Indigenous businesses (applies to all agreements except for CETA and TCA) | Marchés réservés aux petites entreprises (autres que des entreprises autochtones) (s’applique à tous les accords sauf l’AECG et l’ACC) |
| `09` | Measures necessary to protect public morals, order or safety (applies to all agreements) | Mesures nécessaires à la protection de la moralité publique, de l’ordre public ou de la sécurité publique (s’applique à tous les accords) |
| `10` | Measures necessary to protect human, animal or plant life or health (applies to all agreements) | Mesures nécessaires à la protection de la santé et de la vie des personnes et des animaux ou à la préservation des végétaux (s’applique à tous les accords) |
| `11` | Measures necessary to protect intellectual property (applies to all agreements) | Mesures nécessaires à la protection de la propriété intellectuelle (s’applique à tous les accords) |
| `12` | Measures relating to goods or services of persons with disabilities, philanthropic institutions or prison labour (applies to all agreements) | Mesures concernant des biens ou des services fournis par des personnes handicapées ou des organismes philanthropiques, ou encore dans le cadre du travail en milieu carcéral (s’applique à tous les accords) |
| `13` | Services procured in support of military forces located overseas (applies to all agreements) | Services obtenus à l’appui des forces militaires stationnées à l’étranger (s’applique à tous les accords) |
| `14` | Research and development services (applies to all trade agreements except for CFTA) | Services de recherche et de développement (s’applique à tous les accords commerciaux autres que l’ALEC) |




---

#### `indigenous_business` – Procurement Strategy for Indigenous Business / Stratégie d’approvisionnement auprès des entreprises autochtones

**Type:** `text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2022-01-01
 / Obligatoire pour les marchés conclus après le 2022-01-01
  
**Choice Set:** indigenous_business (3 values)  


**Description:**  
EN: It is recommended that this field indicate whether the Procurement Strategy for Indigenous Business mandatory or voluntary set-aside applies to the procurement transaction.  
FR: Il est recommandé que ce champ indique si un marché réservé aux entreprises autochtones, obligatoire ou facultatif dans le cadre de la Stratégie d’approvisionnement auprès des entreprises autochtones, s’applique à l’opération liée à l’approvisionnement.


##### Allowed Values (indigenous_business)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `MS` | Mandatory Set-Aside | Contrat réservé obligatoire |
| `NA` | None | Aucune valeur |
| `VS` | Voluntary Set-Aside | Contrat réservé facultatif |




---

#### `indigenous_business_excluding_psib` – Indigenous Business excluding PSIB (formerly PSAB incidental indicator) / Entreprises autochtones excluant le marché réservé en vertu de la SAEA (anciennement Indicateur d’incidence de la SAEA)

**Type:** `text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2019-01-01

This field must be N, No or Non if the Procurement Strategy for Indigenous Business field is MS or VS.
 / Obligatoire pour les marchés conclus après le 2019-01-01

Ce champ doit être N, No ou Non, si le champ Stratégie d’approvisionnement auprès des entreprises autochtones contient MS ou VS.
  
**Choice Set:** indigenous_business_excluding_psib (2 values)  


**Description:**  
EN: i. It is recommended that this field indicate whether a contract was awarded to an Indigenous business.
ii. Any contract awarded to an Indigenous business where the procurement is subject to a mandatory or voluntary set-aside under the Procurement Strategy for Indigenous Business should be reported as “No” under this data field as such contracts are already reported under the Procurement Strategy for Indigenous Business data field.
  
FR: i. Il est recommandé que ce champ indique si un marché a été attribué à une entreprise autochtone.
ii. Tout marché attribué à une entreprise autochtone lorsque l’approvisionnement est assujetti aux exigences relatives aux marchés réservés obligatoirement ou volontairement en vertu de la Stratégie d’approvisionnement auprès des entreprises autochtones devrait être déclaré comme étant « Non » dans ce champ, puisque de tels marchés sont déjà déclarés dans le champ de données « Stratégie d’approvisionnement auprès des entreprises autochtones ».



##### Allowed Values (indigenous_business_excluding_psib)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `N` | No | Non |
| `Y` | Yes | Oui |




---

#### `intellectual_property` – Intellectual Property Indicator / Indicateur de propriété intellectuelle

**Type:** `text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2019-01-01 / Obligatoire pour les marchés conclus après le 2019-01-01  
**Choice Set:** intellectual_property (13 values)  


**Description:**  
EN: It is recommended that this field identify whether there are terms and conditions in the contract related to intellectual property and whether those terms would result in Crown or contractor ownership of the rights to the intellectual property.  
FR: Il est recommandé d’indiquer dans ce champ si le marché comporte des modalités se rapportant à la propriété intellectuelle et si, selon ces modalités, les droits de propriété intellectuelle appartiendront à l’État ou à l’entrepreneur.


##### Allowed Values (intellectual_property)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `A2` | Crown owned – exception 2 | Droits appartenant à l&#39;État exception 2 |
| `A3` | Crown owned – exception 3 | Droits appartenant à l&#39;État exception 3 |
| `A41` | Crown owned – exception 4.1 | Droits appartenant à l&#39;État exception 4.1 |
| `A42` | Crown owned – exception 4.2 | Droits appartenant à l&#39;État exception 4.2 |
| `A43` | Crown owned – exception 4.3 | Droits appartenant à l&#39;État exception 4.3 |
| `A5` | Crown owned – exception 5 | Droits appartenant à l&#39;État exception 5 |
| `A8` | Crown owned – exemption 8 (note: must have received approval of the Treasury Board via a Treasury Board submission) | Droits appartenant à l&#39;État exemption 8 (nota : doit avoir reçu l’approbation du Conseil du Trésor par le \ biais d’une présentation) |
| `B` | Contractor Owned | Droits appartenant à l&#39;entrepreneur |
| `C` | No IP Terms in Contract | Aucune modalité sur les DPI indiquée au contrat |
| `A1` | Crown owned – exception 1 (discontinued as of 2022-01-01) | Droits appartenant à l&#39;État exception 1 (discontinué à partir de 2022-01-01) |
| `A65` | Crown owned – exception 6.5 (discontinued as of 2017-01-01) | Droits appartenant à l&#39;État exception 6.5 (discontinué à partir de 2017-01-01) |
| `D` | Organization Not Subject to IP Policy (discontinued as of 2017-01-01) | Organisation non assujettie à la Politique sur le titre de propriété intellectuel (discontinué à partir de 2017-01-01) |
| `NA` | Not Applicable (discontinued as of 2022-01-01) | Sans objet (discontinué à partir de 2022-01-01) |




---

#### `potential_commercial_exploitation` – Potential for Commercial Exploitation / Potentiel d'exploitation commerciale

**Type:** `text`  
**Required:** No  
**Validation:** This field must not be empty when the Intellectual Property data field is one of the following values (A2, A3, A41, A42, A43, A5, A8 or B). This field may be left empty if none of the Intellectual Property data field values apply. Valid formats include: Yes or No.
 / Ce champ ne doit pas être vide lorsque le champ Propriété intellectuelle contient l’une des valeurs suivantes : A2, A3, A41, A42, A43, A5, A8 ou B. Ce champ peut demeurer vide si aucune des valeurs de Propriété intellectuelle ne s’applique. Les formats valides incluent : Oui ou Non.
  
**Choice Set:** potential_commercial_exploitation (2 values)  


**Description:**  
EN: It is recommended that this field identify whether intellectual property generated under the contract has the potential for commercial exploitation.  
FR: Il est recommandé d’indiquer dans ce champ si la propriété intellectuelle produite en vertu du marché présente un potentiel d’exploitation commerciale.


##### Allowed Values (potential_commercial_exploitation)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `N` | No | Non |
| `Y` | Yes | Oui |




---

#### `former_public_servant` – Former Public Servant in receipt of a PSSA pension / Ancien fonctionnaire recevant une pension en vertu de la LPFP

**Type:** `text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2019-01-01 / Obligatoire pour les marchés conclus après le 2019-01-01  
**Choice Set:** former_public_servant (2 values)  


**Description:**  
EN: It is recommended that this field identify whether the contractor is a former public servant in receipt of a pension under the Public Service Superannuation Act (PSSA).  
FR: Il est recommandé pour ce champ d’indiquer si l’entrepreneur est un ancien fonctionnaire touchant une pension en vertu de la Loi sur la pension de la fonction publique (LPFP).


##### Allowed Values (former_public_servant)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `N` | No | Non |
| `Y` | Yes | Oui |




---

#### `contracting_entity` – Contracting Entity / Entité contractante

**Type:** `text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2022-01-01 / Obligatoire pour les marchés conclus après le 2022-01-01  
**Choice Set:** contracting_entity (7 values)  


**Description:**  
EN: i. It is recommended that this field identify whether the procurement is a contract awarded by the client department, PSPC, SSC or another departmental entity or a call-up contract against a standing offer agreement or supply arrangement agreement established by PSPC, SSC or the department.
ii. If PSPC awards a contract against a PSPC SOSA on behalf of a client department, it is recommended that the contract be reported as “PWC” for this field.
iii. If SSC awards a contract against a SSC SOSA on behalf of a client department, it is recommended that the contract be reported as “SSCC” for this field.
iv. If a department awards a contract against a PSPC or SSC SOSA, it is recommended that the contract be reported as “PWSOSA” or “SSCSOSA” as applicable.
  
FR: i. Il est recommandé d’indiquer dans ce champ si l’approvisionnement est visé par un marché attribué par le ministère client, SPAC, SPC ou une autre entité ministérielle, ou bien une commande subséquente à une offre à commandes ou à un arrangement en matière d’approvisionnement établi par SPAC, SPC ou le ministère.
ii. Si SPAC attribue un marché dans le cadre d’une OCAMA de SPAC au nom d’un ministère client, il est recommandé que le marché soit déclaré comme « PWC » pour ce champ.
iii. Si SPC attribue un marché dans le cadre d’une OCAMA des SPC au nom d’un ministère client, il est recommandé que le marché soit déclaré comme « SSCC » pour ce champ.
iv. Si un ministère attribue un marché dans le cadre d’une OCAMA de SPAC ou de SPC, il est recommandé que le marché soit déclaré comme « PWSOSA » ou « SSCSOSA », selon le cas.



##### Allowed Values (contracting_entity)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `DC` | Contract awarded by the department. | Marché attribué par le ministère |
| `DSOSA` | Call-up or Contract Against a Standing Offer or Supply Arrangement Agreement established by the department | Commande subséquente ou marché à une offre à commandes ou arrangements en matière d’approvisionnement conclu par le ministère. |
| `OGDC` | Contract awarded by another department on behalf of the client department. | Marché attribué par un autre ministère au nom du ministère client. |
| `PWC` | Contract or Call-up awarded by PSPC on behalf of the client department. | Marché ou commande subséquente attribué par SPAC au nom du ministère client. |
| `PWSOSA` | Call-up or Contract awarded by client department against a Standing Offer or Supply Arrangement Agreement established by Public Services and Procurement Canada | Commande subséquente ou marché attribué par le ministère client par rapport à une l’offre à commandes ou arrangements en matière d’approvisionnement conclu par SPAC. |
| `SSCC` | Contract awarded or Call-up by SSC on behalf of the client department. | Marché ou commande subséquente attribué par SPC au nom du ministère client. |
| `SSCSOSA` | Call-up or Contract awarded by client department against a Standing Offer or Supply Arrangement Agreement established by Shared Services Canada | Commande subséquente ou marché attribué par le ministère client par rapport à une l’offre à commandes ou arrangements en matière d’approvisionnement conclu par SPC. |




---

#### `standing_offer_number` – Standing Offer or Supply Arrangement Number / Numéro de l’offre à commandes

**Type:** `text`  
**Required:** No  
**Validation:** This field must be populated if a Call-up against a standing offer or supply arrangement was identified as PWSOSA or SSCSOSA
If this field is populated, the Contracting Entity data field must be populated.
 / Ce champ doit être rempli si une commande subséquente à une offre à commandes ou un arrangement en matière d’approvisionnement a été identifié comme PWSOSA ou SSCSOSA
Si ce champ est rempli, le champ Entité contractante doit être rempli.
  


**Description:**  
EN: It is recommended that this field be populated with the Standing Offer or Supply Arrangement Number applicable to this contract. This field should be left blank if there is no standing offer or supply arrangement established by PSPC or SSC associated with this contract.  
FR: Il est recommandé de saisir dans ce champ le numéro de l’offre à commandes ou de l’arrangement en matière d’approvisionnement qui s’applique au marché. Ce champ demeure vide en l’absence d’une offre à commandes ou d’un arrangement en matière d’approvisionnement établi par SPAC ou SPC relativement à ce marché.


---

#### `instrument_type` – Instrument Type / Type d’instrument

**Type:** `text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2019-01-01 / Obligatoire pour les marchés conclus après le 2019-01-01  
**Choice Set:** instrument_type (3 values)  


**Description:**  
EN: i. It is recommended that the instrument type identify whether the transaction being reported is a contract, contract amendment, or a standing offer or supply arrangement agreement.
ii. The instrument type for:
  -	A contract is “C”;
  -	An amendment is “A”;
  -	A standing offer agreement or supply arrangement agreement is “SOSA”;
  -	Issuing a call-up against a standing offer or supply arrangement is “C”; and
  -	An amendment to a call-up is “A” for this field.
iii. When a contract is entered into and subsequently amended in the same fiscal quarter, the two transactions should be reported separately. Entry into the contract should be reported as one entry and should be identified as a contract by entering “C” for this field. The contract amendment should be reported as a separate entry and be identified as an amendment by entering “A” for this field.
iv. When a standing offer or supply arrangement agreement is amended, it should continue to be identified as an “SOSA” for this field.
  
FR: i. Il est recommandé d’indiquer dans ce champ si l’opération déclarée est un marché, une modification de marché, une offre à commandes ou un arrangement en matière d’approvisionnement.
ii. Voici le type d’instrument :
  -	un marché est « C »;
  -	une modification est « A »;
  -	une offre à commandes ou un arrangement en matière d’approvisionnement est « SOSA »;
  -	l’émission d’une commande subséquente à une offre à commandes ou à un arrangement en matière d’approvisionnement est « C »;
  -	une modification d’une commande subséquente est « A » pour ce champ.
iii. Lorsqu’un marché est conclu, puis modifié au cours du même trimestre de l’exercice, les deux opérations doivent être déclarées séparément. La signature du marché sera déclarée comme une seule entrée et devrait être indiquée comme étant un marché, soit « C », dans ce champ. Une modification de marché sera déclarée comme une entrée séparée et indiquée comme telle, en inscrivant « A » dans ce champ.
iv. Lorsqu’une offre à commandes ou un arrangement en matière d’approvisionnement est modifié, il convient de saisir le code « SOSA » dans ce champ.



##### Allowed Values (instrument_type)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `A` | Amendment | Modification |
| `C` | Contract | Marché |
| `SOSA` | Standing Offer or Supply Arrangement Agreement | Offre à commandes ou Arrangement en matière d’approvisionnement |




---

#### `ministers_office` – Minister's Office Contracts / Marchés du cabinet du ministre

**Type:** `text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2019-06-21 / Obligatoire pour les marchés conclus après le 2019-06-21  
**Choice Set:** ministers_office (2 values)  


**Description:**  
EN: It is recommended that this field indicate whether the transaction is for the Minister’s office. Ministers’ offices contracts are any contracts for goods and services entered into by a minister or their exempt staff. In accordance with the Policies for Ministers’ Offices, such contracts should be charged to either a Minister’s other operating budget or to the Parliamentary Secretary’s Assistant/Advisor operating budget. Please refer to the Policies for Ministers’ Offices for more information on the Minister’s office budgets. This data field should be entered for contracts and amendments awarded effective June 21, 2019, or, alternatively, for the contracts and amendments awarded within the month of this effective date.  
FR: Dans ce champ, il est recommandé d’indiquer si l’opération concerne le cabinet d’un ministre. Les marchés des cabinets de ministre sont des marchés de biens et de services qui sont conclus par un ministre ou son personnel exonéré. Conformément aux Politiques à l’intention des cabinets des ministres, les dépenses liées à ces marchés doivent être imputées aux autres budgets de fonctionnement d’un ministre ou au budget de fonctionnement de l’adjoint ou du conseiller du secrétaire parlementaire. Se reporter aux Politiques à l’intention des cabinets des ministres pour obtenir de plus amples renseignements sur les budgets des cabinets de ministre. Les données dans ce champ doivent être saisies dans le cas des marchés et des modifications de marché entrés en vigueur le 21 juin 2019 ou dans le cas des marchés attribués et des modifications de marché acceptées dans le mois de cette date d’entrée en vigueur.


##### Allowed Values (ministers_office)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `N` | No | Non |
| `Y` | Yes | Oui |




---

#### `number_of_bids` – Number of Bids / Nombre do soumissions

**Type:** `int`  
**Required:** No  
**Validation:** This field must be populated with a “1” if the solicitation procedure is identified as non-competitive (TN) or Advance Contract Award Notice (ACAN).
 / Ce champ doit contenir un « 1 » si la méthode d’invitation à soumissionner est identifiée comme étant non concurrentielle (TN) ou un préavis d’attribution de contrat (AC).
  


**Description:**  
EN: It is recommended that this field be populated with the total number of compliant and non-compliant bids received in the procurement.
i. For a competitive contract, it is recommended for this field to be the number of bids received pursuant to a bid solicitation.
ii. For a call-up contract against a standing offer agreement established under a competitive process, it is recommended that a value of “0” be entered for this field. In this instance, the value of “0” represents not applicable.
iii. For a contract with task authorizations, the number of bids of the contract may be reported if this value is known when the task authorization is issued. If the number of bids is unknown, the department may input a value of 0 to indicate it is not applicable.
iv. If the contract was awarded using an Advance Contract Award Notice (ACAN) and it was determined that there were no statements of capabilities that met the ACAN requirements, it is recommended that a value of “1” be entered for this field.
iv. For non-competitive contract, it is recommended that a value of “1” be entered for this field.
vi. For the establishment of a standing offer or supply arrangement agreement, it is recommended for this field to be the number of standing offer or supply arrangement bids received. If the standing offer was established under a non-competitive or an ACAN procurement process where it was determined that there were no statements of capabilities that meet the ACAN requirements, it is recommended that a value of “1” be entered for this field for subsequent contracts awarded under the standing offer.
vii. For a competitive contract awarded by PSPC, SSC or another department on behalf of the client department, a value of “0” may be entered if the information is not available within the reporting period for which the contract was awarded. Once the information is available, the contract record is to be updated at the next subsequent reporting period, or as soon as practicable.
  
FR: Il est recommandé de saisir dans ce champ le nombre total de soumissions conformes et non conformes qui ont été reçues dans le cadre du processus d’approvisionnement.
i. Pour un marché concurrentiel, il est recommandé que ce champ indique le nombre de soumissions reçues conformément à une invitation à soumissionner.
ii. Dans le cas d’une commande subséquente à une offre à commandes établie dans le cadre d’un processus concurrentiel, il est recommandé de saisir la valeur « 0 » dans ce champ. En pareil cas, la valeur « 0 » signifie sans objet.
iii. Pour un marché comprenant des autorisations de tâches, le nombre de soumissions pour le marché peut être déclaré si cette donnée est connue au moment de donner l’autorisation de tâches. Si le nombre de soumissions est inconnu, le ministère peut saisir la valeur « 0 ». En pareil cas, la valeur « 0 » signifie sans objet.
iv. Si le marché a été attribué au moyen d’un préavis d’adjudication de contrat (PAC) et qu’il a été déterminé qu’aucun énoncé de capacités ne répondait aux exigences du PAC, il est recommandé de saisir la valeur « 1 » dans ce champ.
v. Dans le cas d’un marché non concurrentiel, il est recommandé de saisir la valeur « 1 » dans ce champ.
vi. Dans le cas de l’établissement d’une offre à commandes ou d’un arrangement en matière d’approvisionnement, il est recommandé d’indiquer dans ce champ le nombre de soumissions reçues relativement à l’offre à commandes ou à l’arrangement en matière d’approvisionnement. Si l’offre à commandes a été établie dans le cadre d’un processus d’approvisionnement non concurrentiel ou d’un PAC et qu’il a été déterminé qu’il n’y avait pas d’énoncés de capacités qui répondent aux exigences du PAC, il est recommandé qu’une valeur de « 1 » soit inscrite dans ce champ pour les marches subséquents attribués en fonction de l’offre à commandes.
vii. Dans le cas d’un marché concurrentiel attribué par SPAC, SPC ou un autre ministère au nom du ministère client, il faut saisir la valeur « 0 » si les renseignements ne sont pas disponibles au cours de la période de déclaration au cours de laquelle le marché a été attribué. Une fois que les renseignements sont disponibles, le dossier contractuel doit être mis à jour au cours de la période de déclaration suivante, ou dès que cela est possible.



---

#### `article_6_exceptions` – Section 6 Government Contracts Regulations Exceptions / Article 6 – Exceptions au Règlement concernant les marches de l’État

**Type:** `text`  
**Required:** No  
**Validation:** This field may only be populated with “0” if the procurement was identified as competitive (open bidding (OB), traditional competitive (TC) or selective tendering (ST)).
 / Ce champ peut seulement contenir « 0 » si l’acquisition a été identifiée comme étant concurrentielle (invitation ouverte à soumissionner (OB) ou concurrentielle - traditionnelle (TC) ou Concurrentielle – Appel d’offres sélectif (ST)).
  
**Choice Set:** article_6_exceptions (5 values)  


**Description:**  
EN: i. The Government Contracts Regulations requires the solicitation of bids unless one of the s.6 exceptions to the Government Contracts Regulations applies to the contract.
ii. It is recommended that this field be populated with one of the s.6 exceptions to solicit bids if bids have not been solicited for the contract.
iii. It is recommended that this field be populated with one of the s.6 exceptions to solicit bids if the contract was awarded using an Advance Contract Award Notice (ACAN) and it was determined that there were no statements of capabilities that met the ACAN requirements.
iv. For contracts whereby bids have been solicited or if the procurement is not a contract subject to the Government Contracts Regulations, the value of “0” should be entered. For this data value, the value of “0” represents not applicable.
  
FR: i. Le Règlement sur les marchés de l’État exige le recours à un appel d’offres, à moins que l’une des exceptions prévues à l’article 6 dudit règlement ne s’applique au marché.
ii. Il est recommandé de saisir dans ce champ l’une des exceptions à l’appel d’offres prévues à l’article 6 si aucun appel d’offres n’a été lancé à l’égard du marché.
iii. Il est recommandé de saisir dans ce champ l’une des exceptions à l’appel d’offres prévues à l’article 6 si le marché a été attribué au moyen d’un préavis d’adjudication de contrat (PAC) et qu’il a été déterminé qu’aucun énoncé de capacités ne répondait aux exigences du PAC.
iv. Dans le cas des marchés pour lesquels un appel d’offres a été lancé, ou si l’approvisionnement n’est pas visé par un marché assujetti au Règlement sur les marchés de l’État, il faut saisir la valeur « 0 ». Pour cette valeur de données, la valeur « 0 » signifie sans objet."



##### Allowed Values (article_6_exceptions)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `0` | Not applicable | Sans objet |
| `1` | Pressing emergency in which delay would be injurious to the public interest | Extrême urgence où un retard serait préjudiciable à l’intérêt public. |
| `2` | Does not exceed s.6 (b) Government Contracts Regulations prescribed dollar limits. | N’excède pas la limite financière prescrite à l’alinéa 6 b) du Règlement sur les marchés de l’État. |
| `3` | Not in the public interest to solicit bids | Situation dans laquelle un appel d’offres ne servirait pas l’intérêt public. |
| `4` | Only one person is capable of performing the contract | Une seule personne est en mesure d’exécuter le marché. |




---

#### `award_criteria` – Award Criteria / Critères d’attribution

**Type:** `text`  
**Required:** No  
**Validation:** If this field is populated, it must be with a “0” if the procurement was identified
as non-competitive (TN) or advance contract award notice (AC) in the solicitation procedure data field or was
identified as an Amendment (A) in the Instrument type data field.
 / Si ce champ est rempli, il doit contenir un « 0 » si l’acquisition a été identifiée
comme étant non concurrentielle (TN) ou un préavis d’attribution de contrat
(AC) ou si l’acquisition a été identifiée comme un modification (A) dans le
champ Type d’instrument.
  
**Choice Set:** award_criteria (6 values)  


**Description:**  
EN: It is recommended that this field be populated with one of the bid evaluation methodologies below if bids have been solicited for the contract:
i. If bids have not been solicited, the value of “0” is to be selected.
ii. For ACANs whereby it was determined that there were no statements of capabilities that met the ACAN requirements, the value of “0” should be entered.
iii. For amendments, select the value of “0” of this field.
iv. For a competitive contract awarded by PSPC, SSC or another department on behalf of the client department, a value of “0” may be entered if the information is not available within the reporting period for which the contract was awarded. Once information is available, the contract record is to be updated at the next subsequent reporting period, or as soon as practicable.
  
FR: Il est recommandé de saisir dans ce champ l’une des méthodes d’évaluation des soumissions indiquées ci-dessous, si un appel d’offres a été lancé à l’égard du marché :
i. S’il n’y a pas eu d’appel d’offres, il faut choisir la valeur « 0 ».
ii. Dans le cas d’un PAC à l’égard duquel il a été déterminé qu’aucun énoncé de capacités ne répondait aux exigences du PAC, il faut saisir la valeur « 0 ».
iii. S’il s’agit d’une modification, il faut choisir la valeur « 0 » pour ce champ.
iv. Dans le cas d’un marché concurrentiel attribué par SPAC, SPC ou un autre ministère au nom du ministère client, il faut saisir la valeur « 0 » si les renseignements ne sont pas disponibles au cours de la période de déclaration au cours de laquelle le marché a été attribué. Une fois que les renseignements sont disponibles, le dossier contractuel doit être mis à jour au cours de la période de déclaration suivante, ou dès que cela est possible.



##### Allowed Values (award_criteria)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `0` | Not applicable | Sans objet |
| `1` | Lowest Price | Prix le plus bas |
| `2` | Lowest Cost-per-Point | Coût par point le plus bas |
| `3` | Highest Combined Rating of Technical Merit and Price | Cote combinée la plus élevée pour les qualités techniques et le meilleur prix |
| `4` | Highest Technical Merit within a Stipulated Maximum Budget | Cote la plus élevée pour les qualités techniques dans le cadre d’un budget maximal imparti |
| `5` | Variations or combinations of the above methods | Variations ou combinaisons des méthodes ci-dessus |




---

#### `socioeconomic_indicator` – Socio-Economic Indicator / Indicateur socioéconomique

**Type:** `text`  
**Required:** No  
**Choice Set:** socioeconomic_indicator (2 values)  


**Description:**  
EN: It is recommended for this field to indicate whether the procurement is subject to one or more of the applicable Socio-economic indicators.  
FR: Il est recommandé d’indiquer dans ce champ si l’approvisionnement est relié à au moins un des indicateurs socioéconomiques applicables.


##### Allowed Values (socioeconomic_indicator)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `FP` | Federal Contractors Program for Employment Equity | Programme de contrats fédéraux pour l’équité en matière d’emploi |
| `NA` | None | Aucune valeur |




---

#### `reporting_period` – Reporting Period / Periode de déclaration

**Type:** `text`  
**Required:** No  
**Validation:** Mandatory for contracts after 2019-01-01 / Obligatoire pour les marchés conclus après le 2019-01-01  
**Choice Set:** reporting_period (124 values)  


**Description:**  
EN: It is recommended that this field be populated in the standard format described below.
When published on the Open Government portal, this field will contain the fiscal quarter this particular contract entry was reported to the public. For example if a contract is being amended on May 3, 2017, and reported in the first fiscal quarter of 2017-–2018, the entry should be 2017-2018-Q1.
  
FR: Il est recommandé de remplir ce champ dans le format standard décrit ci-dessous.
Lorsqu’il est publié sur le portail du Gouvernement Ouvert, ce champ contiendra le quartier fiscal dont cette donné était déclarée. Par exemple, si un marché est modifié le 3 mai 2017, et la modification est déclarée au cours du premier trimestre de l’exercice 2017-2018, il convient d’indiquer : 2017 à 2018-Q1).



##### Allowed Values (reporting_period)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `1995-1996-Q1` | 1995-1996-Q1 | 1995-1996-Q1 |
| `1995-1996-Q2` | 1995-1996-Q2 | 1995-1996-Q2 |
| `1995-1996-Q3` | 1995-1996-Q3 | 1995-1996-Q3 |
| `1995-1996-Q4` | 1995-1996-Q4 | 1995-1996-Q4 |
| `1996-1997-Q1` | 1996-1997-Q1 | 1996-1997-Q1 |
| `1996-1997-Q2` | 1996-1997-Q2 | 1996-1997-Q2 |
| `1996-1997-Q3` | 1996-1997-Q3 | 1996-1997-Q3 |
| `1996-1997-Q4` | 1996-1997-Q4 | 1996-1997-Q4 |
| `1997-1998-Q1` | 1997-1998-Q1 | 1997-1998-Q1 |
| `1997-1998-Q2` | 1997-1998-Q2 | 1997-1998-Q2 |
| `1997-1998-Q3` | 1997-1998-Q3 | 1997-1998-Q3 |
| `1997-1998-Q4` | 1997-1998-Q4 | 1997-1998-Q4 |
| `1998-1999-Q1` | 1998-1999-Q1 | 1998-1999-Q1 |
| `1998-1999-Q2` | 1998-1999-Q2 | 1998-1999-Q2 |
| `1998-1999-Q3` | 1998-1999-Q3 | 1998-1999-Q3 |
| `1998-1999-Q4` | 1998-1999-Q4 | 1998-1999-Q4 |
| `1999-2000-Q1` | 1999-2000-Q1 | 1999-2000-Q1 |
| `1999-2000-Q2` | 1999-2000-Q2 | 1999-2000-Q2 |
| `1999-2000-Q3` | 1999-2000-Q3 | 1999-2000-Q3 |
| `1999-2000-Q4` | 1999-2000-Q4 | 1999-2000-Q4 |
| `2000-2001-Q1` | 2000-2001-Q1 | 2000-2001-Q1 |
| `2000-2001-Q2` | 2000-2001-Q2 | 2000-2001-Q2 |
| `2000-2001-Q3` | 2000-2001-Q3 | 2000-2001-Q3 |
| `2000-2001-Q4` | 2000-2001-Q4 | 2000-2001-Q4 |
| `2001-2002-Q1` | 2001-2002-Q1 | 2001-2002-Q1 |
| `2001-2002-Q2` | 2001-2002-Q2 | 2001-2002-Q2 |
| `2001-2002-Q3` | 2001-2002-Q3 | 2001-2002-Q3 |
| `2001-2002-Q4` | 2001-2002-Q4 | 2001-2002-Q4 |
| `2002-2003-Q1` | 2002-2003-Q1 | 2002-2003-Q1 |
| `2002-2003-Q2` | 2002-2003-Q2 | 2002-2003-Q2 |
| `2002-2003-Q3` | 2002-2003-Q3 | 2002-2003-Q3 |
| `2002-2003-Q4` | 2002-2003-Q4 | 2002-2003-Q4 |
| `2003-2004-Q1` | 2003-2004-Q1 | 2003-2004-Q1 |
| `2003-2004-Q2` | 2003-2004-Q2 | 2003-2004-Q2 |
| `2003-2004-Q3` | 2003-2004-Q3 | 2003-2004-Q3 |
| `2003-2004-Q4` | 2003-2004-Q4 | 2003-2004-Q4 |
| `2004-2005-Q1` | 2004-2005-Q1 | 2004-2005-Q1 |
| `2004-2005-Q2` | 2004-2005-Q2 | 2004-2005-Q2 |
| `2004-2005-Q3` | 2004-2005-Q3 | 2004-2005-Q3 |
| `2004-2005-Q4` | 2004-2005-Q4 | 2004-2005-Q4 |
| `2005-2006-Q1` | 2005-2006-Q1 | 2005-2006-Q1 |
| `2005-2006-Q2` | 2005-2006-Q2 | 2005-2006-Q2 |
| `2005-2006-Q3` | 2005-2006-Q3 | 2005-2006-Q3 |
| `2005-2006-Q4` | 2005-2006-Q4 | 2005-2006-Q4 |
| `2006-2007-Q1` | 2006-2007-Q1 | 2006-2007-Q1 |
| `2006-2007-Q2` | 2006-2007-Q2 | 2006-2007-Q2 |
| `2006-2007-Q3` | 2006-2007-Q3 | 2006-2007-Q3 |
| `2006-2007-Q4` | 2006-2007-Q4 | 2006-2007-Q4 |
| `2007-2008-Q1` | 2007-2008-Q1 | 2007-2008-Q1 |
| `2007-2008-Q2` | 2007-2008-Q2 | 2007-2008-Q2 |
| `2007-2008-Q3` | 2007-2008-Q3 | 2007-2008-Q3 |
| `2007-2008-Q4` | 2007-2008-Q4 | 2007-2008-Q4 |
| `2008-2009-Q1` | 2008-2009-Q1 | 2008-2009-Q1 |
| `2008-2009-Q2` | 2008-2009-Q2 | 2008-2009-Q2 |
| `2008-2009-Q3` | 2008-2009-Q3 | 2008-2009-Q3 |
| `2008-2009-Q4` | 2008-2009-Q4 | 2008-2009-Q4 |
| `2009-2010-Q1` | 2009-2010-Q1 | 2009-2010-Q1 |
| `2009-2010-Q2` | 2009-2010-Q2 | 2009-2010-Q2 |
| `2009-2010-Q3` | 2009-2010-Q3 | 2009-2010-Q3 |
| `2009-2010-Q4` | 2009-2010-Q4 | 2009-2010-Q4 |
| `2010-2011-Q1` | 2010-2011-Q1 | 2010-2011-Q1 |
| `2010-2011-Q2` | 2010-2011-Q2 | 2010-2011-Q2 |
| `2010-2011-Q3` | 2010-2011-Q3 | 2010-2011-Q3 |
| `2010-2011-Q4` | 2010-2011-Q4 | 2010-2011-Q4 |
| `2011-2012-Q1` | 2011-2012-Q1 | 2011-2012-Q1 |
| `2011-2012-Q2` | 2011-2012-Q2 | 2011-2012-Q2 |
| `2011-2012-Q3` | 2011-2012-Q3 | 2011-2012-Q3 |
| `2011-2012-Q4` | 2011-2012-Q4 | 2011-2012-Q4 |
| `2012-2013-Q1` | 2012-2013-Q1 | 2012-2013-Q1 |
| `2012-2013-Q2` | 2012-2013-Q2 | 2012-2013-Q2 |
| `2012-2013-Q3` | 2012-2013-Q3 | 2012-2013-Q3 |
| `2012-2013-Q4` | 2012-2013-Q4 | 2012-2013-Q4 |
| `2013-2014-Q1` | 2013-2014-Q1 | 2013-2014-Q1 |
| `2013-2014-Q2` | 2013-2014-Q2 | 2013-2014-Q2 |
| `2013-2014-Q3` | 2013-2014-Q3 | 2013-2014-Q3 |
| `2013-2014-Q4` | 2013-2014-Q4 | 2013-2014-Q4 |
| `2014-2015-Q1` | 2014-2015-Q1 | 2014-2015-Q1 |
| `2014-2015-Q2` | 2014-2015-Q2 | 2014-2015-Q2 |
| `2014-2015-Q3` | 2014-2015-Q3 | 2014-2015-Q3 |
| `2014-2015-Q4` | 2014-2015-Q4 | 2014-2015-Q4 |
| `2015-2016-Q1` | 2015-2016-Q1 | 2015-2016-Q1 |
| `2015-2016-Q2` | 2015-2016-Q2 | 2015-2016-Q2 |
| `2015-2016-Q3` | 2015-2016-Q3 | 2015-2016-Q3 |
| `2015-2016-Q4` | 2015-2016-Q4 | 2015-2016-Q4 |
| `2016-2017-Q1` | 2016-2017-Q1 | 2016-2017-Q1 |
| `2016-2017-Q2` | 2016-2017-Q2 | 2016-2017-Q2 |
| `2016-2017-Q3` | 2016-2017-Q3 | 2016-2017-Q3 |
| `2016-2017-Q4` | 2016-2017-Q4 | 2016-2017-Q4 |
| `2017-2018-Q1` | 2017-2018-Q1 | 2017-2018-Q1 |
| `2017-2018-Q2` | 2017-2018-Q2 | 2017-2018-Q2 |
| `2017-2018-Q3` | 2017-2018-Q3 | 2017-2018-Q3 |
| `2017-2018-Q4` | 2017-2018-Q4 | 2017-2018-Q4 |
| `2018-2019-Q1` | 2018-2019-Q1 | 2018-2019-Q1 |
| `2018-2019-Q2` | 2018-2019-Q2 | 2018-2019-Q2 |
| `2018-2019-Q3` | 2018-2019-Q3 | 2018-2019-Q3 |
| `2018-2019-Q4` | 2018-2019-Q4 | 2018-2019-Q4 |
| `2019-2020-Q1` | 2019-2020-Q1 | 2019-2020-Q1 |
| `2019-2020-Q2` | 2019-2020-Q2 | 2019-2020-Q2 |
| `2019-2020-Q3` | 2019-2020-Q3 | 2019-2020-Q3 |
| `2019-2020-Q4` | 2019-2020-Q4 | 2019-2020-Q4 |
| `2020-2021-Q1` | 2020-2021-Q1 | 2020-2021-Q1 |
| `2020-2021-Q2` | 2020-2021-Q2 | 2020-2021-Q2 |
| `2020-2021-Q3` | 2020-2021-Q3 | 2020-2021-Q3 |
| `2020-2021-Q4` | 2020-2021-Q4 | 2020-2021-Q4 |
| `2021-2022-Q1` | 2021-2022-Q1 | 2021-2022-Q1 |
| `2021-2022-Q2` | 2021-2022-Q2 | 2021-2022-Q2 |
| `2021-2022-Q3` | 2021-2022-Q3 | 2021-2022-Q3 |
| `2021-2022-Q4` | 2021-2022-Q4 | 2021-2022-Q4 |
| `2022-2023-Q1` | 2022-2023-Q1 | 2022-2023-Q1 |
| `2022-2023-Q2` | 2022-2023-Q2 | 2022-2023-Q2 |
| `2022-2023-Q3` | 2022-2023-Q3 | 2022-2023-Q3 |
| `2022-2023-Q4` | 2022-2023-Q4 | 2022-2023-Q4 |
| `2023-2024-Q1` | 2023-2024-Q1 | 2023-2024-Q1 |
| `2023-2024-Q2` | 2023-2024-Q2 | 2023-2024-Q2 |
| `2023-2024-Q3` | 2023-2024-Q3 | 2023-2024-Q3 |
| `2023-2024-Q4` | 2023-2024-Q4 | 2023-2024-Q4 |
| `2024-2025-Q1` | 2024-2025-Q1 | 2024-2025-Q1 |
| `2024-2025-Q2` | 2024-2025-Q2 | 2024-2025-Q2 |
| `2024-2025-Q3` | 2024-2025-Q3 | 2024-2025-Q3 |
| `2024-2025-Q4` | 2024-2025-Q4 | 2024-2025-Q4 |
| `2025-2026-Q1` | 2025-2026-Q1 | 2025-2026-Q1 |
| `2025-2026-Q2` | 2025-2026-Q2 | 2025-2026-Q2 |
| `2025-2026-Q3` | 2025-2026-Q3 | 2025-2026-Q3 |
| `2025-2026-Q4` | 2025-2026-Q4 | 2025-2026-Q4 |




---



## Proactive Publication - Contracts Nothing to Report / Publication proactive - Contrats (Rien à signaler) 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `reporting_period` | Reporting Period / Periode de declaration | `text` | Yes |  | reporting_period |  |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `reporting_period` – Reporting Period / Periode de declaration

**Type:** `text`  
**Required:** Yes  
**Choice Set:** reporting_period (124 values)  


**Description:**  
EN:   
FR: 


##### Allowed Values (reporting_period)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `1995-1996-Q1` | 1995-1996-Q1 | 1995-1996-Q1 |
| `1995-1996-Q2` | 1995-1996-Q2 | 1995-1996-Q2 |
| `1995-1996-Q3` | 1995-1996-Q3 | 1995-1996-Q3 |
| `1995-1996-Q4` | 1995-1996-Q4 | 1995-1996-Q4 |
| `1996-1997-Q1` | 1996-1997-Q1 | 1996-1997-Q1 |
| `1996-1997-Q2` | 1996-1997-Q2 | 1996-1997-Q2 |
| `1996-1997-Q3` | 1996-1997-Q3 | 1996-1997-Q3 |
| `1996-1997-Q4` | 1996-1997-Q4 | 1996-1997-Q4 |
| `1997-1998-Q1` | 1997-1998-Q1 | 1997-1998-Q1 |
| `1997-1998-Q2` | 1997-1998-Q2 | 1997-1998-Q2 |
| `1997-1998-Q3` | 1997-1998-Q3 | 1997-1998-Q3 |
| `1997-1998-Q4` | 1997-1998-Q4 | 1997-1998-Q4 |
| `1998-1999-Q1` | 1998-1999-Q1 | 1998-1999-Q1 |
| `1998-1999-Q2` | 1998-1999-Q2 | 1998-1999-Q2 |
| `1998-1999-Q3` | 1998-1999-Q3 | 1998-1999-Q3 |
| `1998-1999-Q4` | 1998-1999-Q4 | 1998-1999-Q4 |
| `1999-2000-Q1` | 1999-2000-Q1 | 1999-2000-Q1 |
| `1999-2000-Q2` | 1999-2000-Q2 | 1999-2000-Q2 |
| `1999-2000-Q3` | 1999-2000-Q3 | 1999-2000-Q3 |
| `1999-2000-Q4` | 1999-2000-Q4 | 1999-2000-Q4 |
| `2000-2001-Q1` | 2000-2001-Q1 | 2000-2001-Q1 |
| `2000-2001-Q2` | 2000-2001-Q2 | 2000-2001-Q2 |
| `2000-2001-Q3` | 2000-2001-Q3 | 2000-2001-Q3 |
| `2000-2001-Q4` | 2000-2001-Q4 | 2000-2001-Q4 |
| `2001-2002-Q1` | 2001-2002-Q1 | 2001-2002-Q1 |
| `2001-2002-Q2` | 2001-2002-Q2 | 2001-2002-Q2 |
| `2001-2002-Q3` | 2001-2002-Q3 | 2001-2002-Q3 |
| `2001-2002-Q4` | 2001-2002-Q4 | 2001-2002-Q4 |
| `2002-2003-Q1` | 2002-2003-Q1 | 2002-2003-Q1 |
| `2002-2003-Q2` | 2002-2003-Q2 | 2002-2003-Q2 |
| `2002-2003-Q3` | 2002-2003-Q3 | 2002-2003-Q3 |
| `2002-2003-Q4` | 2002-2003-Q4 | 2002-2003-Q4 |
| `2003-2004-Q1` | 2003-2004-Q1 | 2003-2004-Q1 |
| `2003-2004-Q2` | 2003-2004-Q2 | 2003-2004-Q2 |
| `2003-2004-Q3` | 2003-2004-Q3 | 2003-2004-Q3 |
| `2003-2004-Q4` | 2003-2004-Q4 | 2003-2004-Q4 |
| `2004-2005-Q1` | 2004-2005-Q1 | 2004-2005-Q1 |
| `2004-2005-Q2` | 2004-2005-Q2 | 2004-2005-Q2 |
| `2004-2005-Q3` | 2004-2005-Q3 | 2004-2005-Q3 |
| `2004-2005-Q4` | 2004-2005-Q4 | 2004-2005-Q4 |
| `2005-2006-Q1` | 2005-2006-Q1 | 2005-2006-Q1 |
| `2005-2006-Q2` | 2005-2006-Q2 | 2005-2006-Q2 |
| `2005-2006-Q3` | 2005-2006-Q3 | 2005-2006-Q3 |
| `2005-2006-Q4` | 2005-2006-Q4 | 2005-2006-Q4 |
| `2006-2007-Q1` | 2006-2007-Q1 | 2006-2007-Q1 |
| `2006-2007-Q2` | 2006-2007-Q2 | 2006-2007-Q2 |
| `2006-2007-Q3` | 2006-2007-Q3 | 2006-2007-Q3 |
| `2006-2007-Q4` | 2006-2007-Q4 | 2006-2007-Q4 |
| `2007-2008-Q1` | 2007-2008-Q1 | 2007-2008-Q1 |
| `2007-2008-Q2` | 2007-2008-Q2 | 2007-2008-Q2 |
| `2007-2008-Q3` | 2007-2008-Q3 | 2007-2008-Q3 |
| `2007-2008-Q4` | 2007-2008-Q4 | 2007-2008-Q4 |
| `2008-2009-Q1` | 2008-2009-Q1 | 2008-2009-Q1 |
| `2008-2009-Q2` | 2008-2009-Q2 | 2008-2009-Q2 |
| `2008-2009-Q3` | 2008-2009-Q3 | 2008-2009-Q3 |
| `2008-2009-Q4` | 2008-2009-Q4 | 2008-2009-Q4 |
| `2009-2010-Q1` | 2009-2010-Q1 | 2009-2010-Q1 |
| `2009-2010-Q2` | 2009-2010-Q2 | 2009-2010-Q2 |
| `2009-2010-Q3` | 2009-2010-Q3 | 2009-2010-Q3 |
| `2009-2010-Q4` | 2009-2010-Q4 | 2009-2010-Q4 |
| `2010-2011-Q1` | 2010-2011-Q1 | 2010-2011-Q1 |
| `2010-2011-Q2` | 2010-2011-Q2 | 2010-2011-Q2 |
| `2010-2011-Q3` | 2010-2011-Q3 | 2010-2011-Q3 |
| `2010-2011-Q4` | 2010-2011-Q4 | 2010-2011-Q4 |
| `2011-2012-Q1` | 2011-2012-Q1 | 2011-2012-Q1 |
| `2011-2012-Q2` | 2011-2012-Q2 | 2011-2012-Q2 |
| `2011-2012-Q3` | 2011-2012-Q3 | 2011-2012-Q3 |
| `2011-2012-Q4` | 2011-2012-Q4 | 2011-2012-Q4 |
| `2012-2013-Q1` | 2012-2013-Q1 | 2012-2013-Q1 |
| `2012-2013-Q2` | 2012-2013-Q2 | 2012-2013-Q2 |
| `2012-2013-Q3` | 2012-2013-Q3 | 2012-2013-Q3 |
| `2012-2013-Q4` | 2012-2013-Q4 | 2012-2013-Q4 |
| `2013-2014-Q1` | 2013-2014-Q1 | 2013-2014-Q1 |
| `2013-2014-Q2` | 2013-2014-Q2 | 2013-2014-Q2 |
| `2013-2014-Q3` | 2013-2014-Q3 | 2013-2014-Q3 |
| `2013-2014-Q4` | 2013-2014-Q4 | 2013-2014-Q4 |
| `2014-2015-Q1` | 2014-2015-Q1 | 2014-2015-Q1 |
| `2014-2015-Q2` | 2014-2015-Q2 | 2014-2015-Q2 |
| `2014-2015-Q3` | 2014-2015-Q3 | 2014-2015-Q3 |
| `2014-2015-Q4` | 2014-2015-Q4 | 2014-2015-Q4 |
| `2015-2016-Q1` | 2015-2016-Q1 | 2015-2016-Q1 |
| `2015-2016-Q2` | 2015-2016-Q2 | 2015-2016-Q2 |
| `2015-2016-Q3` | 2015-2016-Q3 | 2015-2016-Q3 |
| `2015-2016-Q4` | 2015-2016-Q4 | 2015-2016-Q4 |
| `2016-2017-Q1` | 2016-2017-Q1 | 2016-2017-Q1 |
| `2016-2017-Q2` | 2016-2017-Q2 | 2016-2017-Q2 |
| `2016-2017-Q3` | 2016-2017-Q3 | 2016-2017-Q3 |
| `2016-2017-Q4` | 2016-2017-Q4 | 2016-2017-Q4 |
| `2017-2018-Q1` | 2017-2018-Q1 | 2017-2018-Q1 |
| `2017-2018-Q2` | 2017-2018-Q2 | 2017-2018-Q2 |
| `2017-2018-Q3` | 2017-2018-Q3 | 2017-2018-Q3 |
| `2017-2018-Q4` | 2017-2018-Q4 | 2017-2018-Q4 |
| `2018-2019-Q1` | 2018-2019-Q1 | 2018-2019-Q1 |
| `2018-2019-Q2` | 2018-2019-Q2 | 2018-2019-Q2 |
| `2018-2019-Q3` | 2018-2019-Q3 | 2018-2019-Q3 |
| `2018-2019-Q4` | 2018-2019-Q4 | 2018-2019-Q4 |
| `2019-2020-Q1` | 2019-2020-Q1 | 2019-2020-Q1 |
| `2019-2020-Q2` | 2019-2020-Q2 | 2019-2020-Q2 |
| `2019-2020-Q3` | 2019-2020-Q3 | 2019-2020-Q3 |
| `2019-2020-Q4` | 2019-2020-Q4 | 2019-2020-Q4 |
| `2020-2021-Q1` | 2020-2021-Q1 | 2020-2021-Q1 |
| `2020-2021-Q2` | 2020-2021-Q2 | 2020-2021-Q2 |
| `2020-2021-Q3` | 2020-2021-Q3 | 2020-2021-Q3 |
| `2020-2021-Q4` | 2020-2021-Q4 | 2020-2021-Q4 |
| `2021-2022-Q1` | 2021-2022-Q1 | 2021-2022-Q1 |
| `2021-2022-Q2` | 2021-2022-Q2 | 2021-2022-Q2 |
| `2021-2022-Q3` | 2021-2022-Q3 | 2021-2022-Q3 |
| `2021-2022-Q4` | 2021-2022-Q4 | 2021-2022-Q4 |
| `2022-2023-Q1` | 2022-2023-Q1 | 2022-2023-Q1 |
| `2022-2023-Q2` | 2022-2023-Q2 | 2022-2023-Q2 |
| `2022-2023-Q3` | 2022-2023-Q3 | 2022-2023-Q3 |
| `2022-2023-Q4` | 2022-2023-Q4 | 2022-2023-Q4 |
| `2023-2024-Q1` | 2023-2024-Q1 | 2023-2024-Q1 |
| `2023-2024-Q2` | 2023-2024-Q2 | 2023-2024-Q2 |
| `2023-2024-Q3` | 2023-2024-Q3 | 2023-2024-Q3 |
| `2023-2024-Q4` | 2023-2024-Q4 | 2023-2024-Q4 |
| `2024-2025-Q1` | 2024-2025-Q1 | 2024-2025-Q1 |
| `2024-2025-Q2` | 2024-2025-Q2 | 2024-2025-Q2 |
| `2024-2025-Q3` | 2024-2025-Q3 | 2024-2025-Q3 |
| `2024-2025-Q4` | 2024-2025-Q4 | 2024-2025-Q4 |
| `2025-2026-Q1` | 2025-2026-Q1 | 2025-2026-Q1 |
| `2025-2026-Q2` | 2025-2026-Q2 | 2025-2026-Q2 |
| `2025-2026-Q3` | 2025-2026-Q3 | 2025-2026-Q3 |
| `2025-2026-Q4` | 2025-2026-Q4 | 2025-2026-Q4 |




---




## Appendix

### Choice Sets Summary (All Resources)
| Choice Set | Field(s) | Values | Standalone Doc |
|------------|----------|--------|----------------|


### Generation Metadata

- Generated: 2025-07-25T10:32:45 (UTC)
- Source: dictionaries/contracts.json
- Commit: `0a495f5`
- Tool Version: simple-1

### Validation

- JSON Schema Validation: **PASSED**


### Notes

This documentation is auto-generated. Do not hand-edit; instead update the source recombinant JSON and re-run generation.