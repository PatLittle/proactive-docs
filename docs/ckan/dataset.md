# CKAN Dataset Schema

Generated 2025-07-25T23:27:08 UTC

## Dataset Fields
| Field | Label (EN) | Label (FR) | Required | Choices |
|-------|------------|------------|----------|---------|
| `id` |  |  | No |  |
| `name` |  |  | No |  |
| `collection` | Collection Type | Type de collection | Yes | collection |
| `metadata_contact` | Metadata contact | Contact métadonnée | No |  |
| `parent_id` | Parent identifier | Identifiant parent | Yes |  |
| `hierarchy_level` | Hierarchy level | Portée hiérarchique | Yes |  |
| `file_id` | File Identifier | Identifiant métadonnées | Yes |  |
| `short_key` | Short Key | Identifiant court | Yes |  |
| `title_translated` | Title | Titre | Yes |  |
| `owner_org` | Publisher - Current Organization Name | Éditeur - Nom actuel de l’organisation | Yes |  |
| `org_title_at_publication` | Publisher - Organization Name at Publication | Organisation - Titre lors de la publication | Yes |  |
| `org_section` | Publisher - Organization Section Name | Éditeur - Organisation - Nom de la section | No |  |
| `creator` | Creator | Auteur | No |  |
| `position_name` | Position Name | Nom position | No |  |
| `responsible_role` | Role | Rôle | Yes |  |
| `contact_information` | Contact Information | Information contact | Yes |  |
| `topic_category` | Topic category | Catégorie thématique | No | topic_category |
| `contributor` | Contributor | Contributeur | No |  |
| `maintainer_email` | Contact Email | Courriel - Personne-ressource | Yes |  |
| `maintainer_contact_form` | Contact Form | Formulaire de contact | No |  |
| `credit` | Credit | Reconnaissance | No |  |
| `notes_translated` | Description | Description | Yes |  |
| `keywords` | Keywords | Mots clés | Yes |  |
| `subject` | Subject | Sujet | Yes | subject |
| `audience` | Audience | Audience | No | audience |
| `place_of_publication` | Place of Publication | Endroit de publication | No | place_of_publication |
| `spatial` | Spatial | Élément spatial | Yes |  |
| `geographic_region` | Geographic Region Name | Nom de la région géographique | No | geographic_region |
| `time_period_coverage_start` | Time Period Coverage Start | Couverture de la période de temps - date de début | Yes |  |
| `time_period_coverage_end` | Time Period Coverage End | Couverture de la période de temps - date de fin | Yes |  |
| `frequency` | Maintenance and Update Frequency | Fréquence d'entretien et de mise à jour | Yes | frequency |
| `date_published` | Date Published | Date de publication | Yes |  |
| `date_modified` | Date Modified | Date de modification | Yes |  |
| `program_page_url` | Homepage | URL de la page d'accueil | No |  |
| `federated_date_modified` | Federated Dateset Modified Date | Date de modification de l'jeu de données fédérées | Yes |  |
| `data_series_name` | Series Title | Nom de la série | No |  |
| `data_series_issue_identification` | Series Issue ID | Numéro de publication de la série | No |  |
| `digital_object_identifier` | Digital Object Identifier (DOI) | Identificateur d’objet numérique | No |  |
| `reference_system_information` | Reference System Information | Information système référence | Yes |  |
| `distributor` | Distributor | Distributeur | Yes |  |
| `status` | Status | État | Yes | status |
| `association_type` | Association Type | Type association | No | association_type |
| `aggregate_identifier` | Aggregate dataset identifier | Identifiant jeu données aggrégées | Yes |  |
| `spatial_representation_type` | Spatial Representation Type | Type représentation spatiale | No | spatial_representation_type |
| `jurisdiction` | Jurisdiction | Juridiction | Yes | jurisdiction |
| `license_id` | Licence | Licence | Yes |  |
| `restrictions` | Access Restrictions | Restrictions d'accès | Yes | restrictions |
| `imso_approval` | Approval | Approbation | Yes | imso_approval |
| `ready_to_publish` | Ready to Publish | Prêt à publier | Yes | ready_to_publish |
| `portal_release_date` | Portal Release Date | Date de lancement du portail | Yes |  |
| `presentation_form` | Presentation Form | Type de représentation spatiale | Yes | presentation_form |
| `display_flags` | Display Flags |  | No | display_flags |
| `relationship` | Relationship | Relation | No |  |

## Resource Fields
| Field | Label (EN) | Label (FR) | Required | Choices |
|-------|------------|------------|----------|---------|
| `unique_identifier` | Unique Identifier | Identificateur unique | No |  |
| `name_translated` | Title | Titre | Yes |  |
| `relationship` | Relationship | Relation | No |  |
| `date_published` | Date Published | Date de publication | Yes |  |
| `resource_type` | Resource Type | Type de contenu | Yes | resource_type |
| `size` | Size | Taille | No |  |
| `character_set` | Character Set | Jeu de caractères | Yes | character_set |
| `format` | Format | Format | Yes | format |
| `language` | Language | Langue | Yes | language |
| `url` | Download URL | Télécharger un URL | Yes |  |
| `data_quality` | Data Includes URIs and Links | Les données comprennent les URI et les liens | No | data_quality |
| `schema` |  |  | No |  |
| `validation_options` |  |  | No |  |
| `validation_status` | Validation status | Statut de validation | No |  |
| `validation_timestamp` | Validation timestamp | Horodatage de la validation | No |  |
| `related_type` |  |  | No |  |
| `related_relationship` |  |  | Yes |  |
