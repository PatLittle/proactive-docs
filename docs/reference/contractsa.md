
# Proactive Publication - Aggregated Contracts from -$10,000 to $10,000 / Publication proactive - Contrats agrégés de -10 000$ à 10 000$

**Dataset Type:** `contractsa`  
**Last Generated:** 2025-10-26T01:28:01 (UTC)  
**Source:** dictionaries/contractsa.json  
**Commit:** `8e7c49b`

Access, upload and modify the aggregated Contracts from -$10K to $10K reports for your organization / Accès, téléversement et modification des rapports sur les Contrats agrégés de -10 000$ à 10 000$ pour votre organisation

---

## Resources


- [Proactive Publication - Aggregated Contracts from -$10,000 to $10,000 / Publication proactive - Contrats agrégés de -10 000$ à 10 000$](#contractsa)


---


## Proactive Publication - Aggregated Contracts from -$10,000 to $10,000 / Publication proactive - Contrats agrégés de -10 000$ à 10 000$ 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `year` | Calendar Year Reporting Period / Période de déclaration | `year` | Yes |  |  | It is recommended for this field to be populated in the standard format describ… |
| `contract_goods_number_of` | Number of Goods Contracts $10K and under / Nombre de marchés de biens de 10 000 $ et moins | `int` | Yes |  |  | It is recommended for this field to be populated with the total number of goods… |
| `contracts_goods_original_value` | Goods Contracts $10K and under - Original Value / Marchés de biens de 10 000 $ et moins - Valeur d’origine | `money` | Yes |  |  | It is recommended for this field to be populated with the value of all goods co… |
| `contracts_goods_amendment_value` | Goods Contracts Amendments from -$10K to $10K - Net Amendment Value / Modifications de marchés de biens de -10 000 $ à 10 000 $ - Valeur nette des modifications | `money` | Yes |  |  | It is recommended for this field to be populated with the value of all net amen… |
| `contract_service_number_of` | Number of Service Contracts $10K and under / Nombre de marchés de services de 10 000 $ et moins | `int` | Yes |  |  | It is recommended for this field to be populated with the total number of servi… |
| `contracts_service_original_value` | Service Contracts $10K and under - Original Value / Marchés de services de 10 000 $ ou moins - Valeur d’origine | `money` | Yes |  |  | It is recommended for this field to be populated with the value of all service … |
| `contracts_service_amendment_value` | Service Contracts from -$10K to $10K - Net Amendment Value / Modifications de marché de services de -10 000 $ à 10 000 $ - Valeur nette des modifications | `money` | Yes |  |  | It is recommended for this field to be populated with the value of all net amen… |
| `contract_construction_number_of` | Number of Construction Contracts $10K and under / Nombre de marchés de services de construction de 10 000 $ et moins | `int` | Yes |  |  | It is recommended for this field to be populated with the total number of const… |
| `contracts_construction_original_value` | Construction Contracts $10K and under - Original Value / Marchés de services de construction de 10 000 $ et moins - Valeur d’origine | `money` | Yes |  |  | It is recommended for this field to be populated with the value of all construc… |
| `contracts_construction_amendment_value` | Construction Contracts Amendments from -$10K to $10K - Net Amendment Value / Modifications de marché de services de construction de -10 000 $ à 10 000 $ - Valeur nette des modifications | `money` | Yes |  |  | It is recommended for this field to be populated with the value of all net amen… |
| `acquisition_card_transactions_number_of` | Number of Acquisition Card Transactions for all Dollar Values / Nombre d&#39;opérations réalisées au moyen de la carte d&#39;acquisition pour toutes les valeurs en dollars | `int` | Yes |  |  | It is recommended for this field to be populated with the total number of all a… |
| `acquisition_card_transactions_total_value` | Acquisition Card Transactions for all Dollar Values – Total Value / Carte d&#39;acquisition pour toutes les valeurs en dollars – Valeur totale | `money` | Yes |  |  | It is recommended for this field to be populated with the sum of all dollar val… |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `year` – Calendar Year Reporting Period / Période de déclaration

**Type:** `year`  
**Required:** Yes  


**Description:**  
EN: It is recommended for this field to be populated in the standard format described below. For example, if the template is being reported for the 2017 calendar year, the entry will be populated as 2017.  
FR: Il est recommandé de remplir ce champ en utilisant le format standard décrit ci-dessous. Par exemple, si le modèle est déclaré pour l’année civile 2017, il faut inscrire 2017.


---

#### `contract_goods_number_of` – Number of Goods Contracts $10K and under / Nombre de marchés de biens de 10 000 $ et moins

**Type:** `int`  
**Required:** Yes  


**Description:**  
EN: It is recommended for this field to be populated with the total number of goods contracts entered into with a value of $10,000 and under. This includes goods contracts entered into and subsequently amended in the same calendar year to an amended contract value of $10,000 and under.  
FR: Il est recommandé de saisir dans ce champ le nombre total de marchés de biens conclus d’une valeur de 10 000 $ ou moins, ce qui comprend les marchés de biens conclus et modifiés par la suite au cours de la même année civile et d’une valeur de 10 000 $ ou moins.


---

#### `contracts_goods_original_value` – Goods Contracts $10K and under - Original Value / Marchés de biens de 10 000 $ et moins - Valeur d’origine

**Type:** `money`  
**Required:** Yes  


**Description:**  
EN: It is recommended for this field to be populated with the value of all goods contracts with a value of $10,000 and under, at the time of contract entry. This value should be in Canadian currency and include all applicable taxes.  
FR: Il est recommandé de saisir dans ce champ la valeur des marchés de biens de 10 000 $ ou moins au moment de la conclusion du marché. Cette valeur doit être exprimée en dollars canadiens et inclure toutes les taxes qui s’appliquent.


---

#### `contracts_goods_amendment_value` – Goods Contracts Amendments from -$10K to $10K - Net Amendment Value / Modifications de marchés de biens de -10 000 $ à 10 000 $ - Valeur nette des modifications

**Type:** `money`  
**Required:** Yes  


**Description:**  
EN: It is recommended for this field to be populated with the value of all net amendments to goods contracts (that is, all positive and negative amendments) with a value from -$10,000 to $10,000. This value should be in Canadian currency and include all applicable taxes. An amendment should be reported either quarterly or annually. Reporting an amendment both quarterly and annually would result in double counting of the amendment’s value when calculating the total contracting activity of an organization.  
FR: Il est recommandé de saisir dans ce champ la valeur nette de toutes les modifications de marché de biens (c’est-à-dire, toutes les modifications positives et négatives) de -10 000 $ à 10 000 $. Cette valeur doit être exprimée en dollars canadiens et inclure toutes les taxes qui s’appliquent. Une modification doit faire l’objet d’une déclaration trimestrielle ou annuelle. La déclaration d’une modification de façon trimestrielle et annuelle donnerait lieu au double dénombrement de la valeur de la modification au moment de calculer le total de l’activité contractuelle d’une organisation.


---

#### `contract_service_number_of` – Number of Service Contracts $10K and under / Nombre de marchés de services de 10 000 $ et moins

**Type:** `int`  
**Required:** Yes  


**Description:**  
EN: It is recommended for this field to be populated with the total number of services contracts entered into with a value of $10,000 and under. This includes services contracts entered into and subsequently amended in the same calendar year to an amended contract value of $10,000 and under.  
FR: Il est recommandé de saisir dans ce champ le nombre total de marchés de services conclus d’une valeur de 10 000 $ ou moins, ce qui comprend les marchés de services conclus et modifiés par la suite au cours de la même année civile et d’une valeur de 10 000 $ ou moins.


---

#### `contracts_service_original_value` – Service Contracts $10K and under - Original Value / Marchés de services de 10 000 $ ou moins - Valeur d’origine

**Type:** `money`  
**Required:** Yes  


**Description:**  
EN: It is recommended for this field to be populated with the value of all service contracts with a value $10,000 and under, at the time of contract entry. This value should be in Canadian currency and include all applicable taxes.  
FR: Il est recommandé de saisir dans ce champ la valeur des marchés de services de 10 000 $ ou moins au moment de la conclusion du marché. Cette valeur doit être exprimée en dollars canadiens et inclure toutes les taxes qui s’appliquent.


---

#### `contracts_service_amendment_value` – Service Contracts from -$10K to $10K - Net Amendment Value / Modifications de marché de services de -10 000 $ à 10 000 $ - Valeur nette des modifications

**Type:** `money`  
**Required:** Yes  


**Description:**  
EN: It is recommended for this field to be populated with the value of all net amendments to service contracts (that is, all positive and negative amendments) with a value from -$10,000 to $10,000. This value should be in Canadian currency and include all applicable taxes. An amendment should be reported either quarterly or annually. Reporting an amendment both quarterly and annually would result in double counting of the amendment’s value when calculating the total contracting activity of an organization.  
FR: Il est recommandé de saisir dans ce champ la valeur nette de toutes les modifications de marchés de services (c’est-à-dire, toutes les modifications positives et négatives) de -10 000 $ à 10 000 $. Cette valeur doit être exprimée en dollars canadiens et inclure toutes les taxes qui s’appliquent. Une modification doit faire l’objet d’une déclaration trimestrielle ou annuelle. La déclaration d’une modification de façon trimestrielle et annuelle donnerait lieu au double dénombrement de la valeur de la modification au moment de calculer le total de l’activité contractuelle d’une organisation.


---

#### `contract_construction_number_of` – Number of Construction Contracts $10K and under / Nombre de marchés de services de construction de 10 000 $ et moins

**Type:** `int`  
**Required:** Yes  


**Description:**  
EN: It is recommended for this field to be populated with the total number of construction contracts entered into with a value of $10,000 and under. This includes construction contracts entered into and subsequently amended in the same calendar year to an amended contract value of $10,000 and under.  
FR: Il est recommandé de saisir dans ce champ le nombre total de marchés de services de construction conclus d’une valeur de 10 000 $ ou moins, ce qui comprend les marchés de services de construction conclus et modifiés par la suite au cours de la même année civile et d’une valeur de 10 000 $ ou moins.


---

#### `contracts_construction_original_value` – Construction Contracts $10K and under - Original Value / Marchés de services de construction de 10 000 $ et moins - Valeur d’origine

**Type:** `money`  
**Required:** Yes  


**Description:**  
EN: It is recommended for this field to be populated with the value of all construction contracts with a value $10,000 and under, at the time of contract entry. This value should be in Canadian currency and include all applicable taxes.  
FR: Il est recommandé de saisir dans ce champ la valeur des marchés de services de construction de 10 000 $ ou moins au moment de la conclusion du marché. Cette valeur doit être exprimée en dollars canadiens et inclure toutes les taxes qui s’appliquent.


---

#### `contracts_construction_amendment_value` – Construction Contracts Amendments from -$10K to $10K - Net Amendment Value / Modifications de marché de services de construction de -10 000 $ à 10 000 $ - Valeur nette des modifications

**Type:** `money`  
**Required:** Yes  


**Description:**  
EN: It is recommended for this field to be populated with the value of all net amendments to construction contracts (that is, all positive and negative amendments) with a value from -$10,000 to $10,000. This value should be in Canadian currency and include all applicable taxes. An amendment should be reported either quarterly or annually. Reporting an amendment both quarterly and annually would result in double counting of the amendment’s value when calculating the total contracting activity of an organization.  
FR: Il est recommandé de saisir dans ce champ la valeur nette de toutes les modifications de marchés de services de construction (c’est-à-dire, toutes les modifications positives et négatives) de -10 000 $ à 10 000 $. Cette valeur doit être exprimée en dollars canadiens et inclure toutes les taxes qui s’appliquent. Une modification doit faire l’objet d’une déclaration trimestrielle ou annuelle. La déclaration d’une modification de façon trimestrielle et annuelle donnerait lieu au double dénombrement de la valeur de la modification au moment de calculer le total de l’activité contractuelle d’une organisation.


---

#### `acquisition_card_transactions_number_of` – Number of Acquisition Card Transactions for all Dollar Values / Nombre d'opérations réalisées au moyen de la carte d'acquisition pour toutes les valeurs en dollars

**Type:** `int`  
**Required:** Yes  


**Description:**  
EN: It is recommended for this field to be populated with the total number of all acquisition card transactions for all dollar values.  
FR: Il est recommandé de saisir dans ce champ le nombre total d’opérations effectuées par carte d’achat, peu importe le montant.


---

#### `acquisition_card_transactions_total_value` – Acquisition Card Transactions for all Dollar Values – Total Value / Carte d'acquisition pour toutes les valeurs en dollars – Valeur totale

**Type:** `money`  
**Required:** Yes  


**Description:**  
EN: It is recommended for this field to be populated with the sum of all dollar values for all acquisition card transactions. This value should be in Canadian currency and include all applicable taxes.  
FR: Il est recommandé de saisir dans ce champ la somme des montants de toutes les opérations effectuées par carte d’achat. Cette valeur doit être exprimée en dollars canadiens et inclure toutes les taxes qui s’appliquent.


---




## Appendix

### Choice Sets Summary (All Resources)
| Choice Set | Field(s) | Values | Standalone Doc |
|------------|----------|--------|----------------|


### Generation Metadata

- Generated: 2025-10-26T01:28:01 (UTC)
- Source: dictionaries/contractsa.json
- Commit: `8e7c49b`
- Tool Version: simple-1

### Validation

- JSON Schema Validation: **PASSED**


### Notes

This documentation is auto-generated. Do not hand-edit; instead update the source recombinant JSON and re-run generation.