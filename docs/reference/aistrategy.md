
# AI Strategy Implementation Tracker / Outil de suivi de la mise en œuvre de la stratégie en matière d'IA

**Dataset Type:** `aistrategy`  
**Last Generated:** 2025-10-12T01:23:32 (UTC)  
**Source:** dictionaries/aistrategy.json  
**Commit:** `d437fb3`

Access, upload and modify the AI Strategy Implementation Tracker for your organization / Accédez, téléchargez et modifiez l'outil de la mise en œuvre de la stratégie en matière d'IA pour votre organisation

---

## Resources


- [AI Strategy Implementation Tracker / Outil de suivi de la mise en œuvre de la stratégie en matière d'IA](#aistrategy)


---


## AI Strategy Implementation Tracker / Outil de suivi de la mise en œuvre de la stratégie en matière d'IA 

### Field Summary

| Field ID | Label (EN / FR) | Type | Required | Max Chars | Choices | Description (EN) |
|----------|-----------------|------|----------|-----------|---------|------------------|
| `ref_number` | Reference Number / Numéro de référence | `text` | Yes |  |  | The unique number assigned to a service using AI to make it easier to refer to … |
| `reporting_period` | Reporting Period / Période de déclaration | `text` | Yes |  | reporting_period | Year and month of the update |
| `priority_area` | Priority Area / Domaine Prioritaire | `text` | Yes |  | priority_area | The strategic focus area within the AI Strategy Implementation |
| `key_action` | Key Action / Action Clé | `text` | Yes |  | key_action | The key action described in the AI Strategy |
| `sub_action` | Strategic sub-action / Sous-action stratégique | `text` | Yes |  | sub_action | Specific sub-action under the AI Strategy |
| `activity` | Activity / Activité | `text` | Yes |  | activity | Activity in support of the AI Strategy |
| `description_en` | Description (English) / Description (anglais) | `text` | No |  |  | Operational description in the AI Strategy |
| `description_fr` | Description (French) / Description (français) | `text` | No |  |  | Operational description in the AI Strategy |
| `expected_completion` | Expected Completion / Achèvement attendu | `text` | Yes |  | expected_completion | Completion of activity |
| `lead_department` | Lead Department(s) / Ministère(s) responsable(s) | `_text` | Yes |  | lead_department | Primary departments involved |
| `status` | Status / État | `text` | Yes |  | status | AI Strategy tracker status |
| `progress_en` | Progress Made (English) / Progrès réalisés (anglais) | `text` | No |  |  | Describes any progress made |
| `progress_fr` | Progress Made (French) / Progrès réalisés (français) | `text` | No |  |  | Describes any progress made |


**Legend:** *Required* = must appear in uploads; *Choices* = enumerated allowed values (shows choice set name when multiple sets exist).

### Detailed Fields


#### `ref_number` – Reference Number / Numéro de référence

**Type:** `text`  
**Required:** Yes  
**Validation:** This field must not be empty.
This field cannot contain commas.
 / Ce champ ne doit pas être vide.
Ce champ ne peut pas contenir de virgules.
  


**Description:**  
EN: The unique number assigned to a service using AI to make it easier to refer to specific services.  
FR: Le numéro unique attribué à un service à l'aide de l'IA pour faciliter le référencement à des services précis.


---

#### `reporting_period` – Reporting Period / Période de déclaration

**Type:** `text`  
**Required:** Yes  
**Validation:** Must match expected completion options in the controlled list. / Doit correspondre aux options d'achèvement prévues de la liste contrôlée.  
**Choice Set:** reporting_period (8 values)  


**Description:**  
EN: Year and month of the update  
FR: Année et mois de la mise à jour


##### Allowed Values (reporting_period)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `2025-Q3` | 2025-Q3 | 2025-T3 |
| `2025-Q4` | 2025-Q4 | 2025-T4 |
| `2026-Q1` | 2026-Q1 | 2026-T1 |
| `2026-Q2` | 2026-Q2 | 2026-T2 |
| `2026-Q3` | 2026-Q3 | 2026-T3 |
| `2026-Q4` | 2026-Q4 | 2026-T4 |
| `2027-Q1` | 2027-Q1 | 2027-T1 |
| `2027-Q2` | 2027-Q2 | 2027-T2 |




---

#### `priority_area` – Priority Area / Domaine Prioritaire

**Type:** `text`  
**Required:** Yes  
**Validation:** Must match one of the values in the controlled list. / Doit correspondre à l'une des valeurs de la liste contrôlée.  
**Choice Set:** priority_area (4 values)  


**Description:**  
EN: The strategic focus area within the AI Strategy Implementation  
FR: Le domaine d'action stratégique dans le cadre de la mise en œuvre de la stratégie en matière d'IA


##### Allowed Values (priority_area)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `A` | Central AI Capacity | Capacité centrale d’IA |
| `B` | Policy, Legislation, and Governance | Politiques, lois et gouvernance |
| `C` | Talent and Training | Talents et formation |
| `D` | Engagement, Transparency, and Value to Canadians | Engagement, transparence et valeur pour les Canadiens |




---

#### `key_action` – Key Action / Action Clé

**Type:** `text`  
**Required:** Yes  
**Validation:** Must match predefined action statements. / Doit correspondre à des déclarations d'action prédéfinies.  
**Choice Set:** key_action (12 values)  


**Description:**  
EN: The key action described in the AI Strategy  
FR: L'action clé décrite dans la stratégie en matière d'IA


##### Allowed Values (key_action)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `A.1` | Establish an AI Centre of Expertise for the Government of Canada | Établir un Centre d’expertise en IA pour le gouvernement du Canada |
| `A.2` | Enable common infrastructure for AI adoption and promote adoption of existing approved enterprise solutions | Mettre en place une infrastructure commune pour permettre l’adoption de l’IA et favoriser l’utilisation des solutions intégrées existantes qui sont autorisées |
| `A.3` | Identify and develop a lighthouse project | Cerner et élaborer un projet phare |
| `B.1` | Establish common AI governance and risk management frameworks | Établir des cadres communs de gouvernance et de gestion des risques en matière d&#39;IA |
| `B.2` | Address policy and legislative alignment, gaps, and barriers | Surmonter les lacunes, les obstacles et le manque d’harmonie dans les politiques et lois |
| `B.3` | Adopt a “think AI” approach | Adopter une approche axée sur l’IA |
| `C.1` | Benchmark talent needs | Évaluer les besoins en matière de talents |
| `C.2` | Develop a training plan | Élaborer un plan de formation |
| `C.3` | Develop a talent plan | Élaborer un plan de gestion des talents |
| `D.1` | Strengthen accountability and transparency on AI use | Accroître la responsabilisation et la transparence quant à l’utilisation de l’IA |
| `D.2` | Demonstrate impact and value to Canadians | Démontrer l’incidence et la valeur pour les Canadiens |
| `D.3` | Commit to engagement on AI | Prendre des engagements de mobilisation sur l’IA |




---

#### `sub_action` – Strategic sub-action / Sous-action stratégique

**Type:** `text`  
**Required:** Yes  
**Validation:** Must match one of the AI Strategy defined sub-action statements. / Doit correspondre à l'une des sous-actions définies dans la stratégie IA.  
**Choice Set:** sub_action (34 values)  


**Description:**  
EN: Specific sub-action under the AI Strategy  
FR: Sous-action spécifique dans le cadre de la stratégie d'IA


##### Allowed Values (sub_action)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `A.1.1` | Establish an AI Centre of Expertise for the Government of Canada | Créer un centre d&#39;expertise en IA pour le gouvernement du Canada |
| `A.1.2` | Identify high value use cases for AI Integration | Identifier les cas d&#39;utilisation à forte valeur ajoutée pour l&#39;intégration de l&#39;IA |
| `A.2.1` | Provide high-performance computing (HPC) and cloud infrastructure that is available, secure, and scalable to meet the demands of AI projects | Fournir une infrastructure de calcul haute performance (CHP) et d&#39;informatique en nuage disponible, sécurisée et évolutive pour répondre aux exigences des projets d&#39;IA |
| `A.2.2` | Provide common data and information management systems and practices to support sharing, scaling, and agentic capabilities across Government of Canada platforms | Fournir des systèmes et des pratiques communs de gestion des données et de l&#39;information pour soutenir le partage, l&#39;extension et les capacités agentiques à travers les plateformes du gouvernement du Canada |
| `A.2.3` | Provide access to approved models, services, and application programming interfaces (APIs) within common Government of Canada cloud platforms to build or deploy systems | Fournir un accès aux modèles, services et interfaces de programmation d&#39;applications (API) approuvés au sein des plates-formes en nuage communes du gouvernement du Canada pour construire ou déployer des systèmes |
| `A.2.4` | Provide access to common AI solutions and capabilities in vendor solutions through a standard Government of Canada platform service | Fournir un accès aux solutions et capacités communes en matière d&#39;IA dans les solutions des fournisseurs par l&#39;intermédiaire d&#39;un service de plateforme standard du gouvernement du Canada |
| `A.2.5` | Support Canadian suppliers and vendors to promote the growth of the Canadian AI industry and ensure secure sovereign infrastructure and solutions | Soutenir les fournisseurs et les vendeurs canadiens afin de promouvoir la croissance de l&#39;industrie canadienne de l&#39;IA et de garantir la sécurité des infrastructures et des solutions souveraines |
| `A.3.1` | Self-serve language hub for the Government of Canada | Carrefour linguistique libre-service pour le gouvernement du Canada |
| `B.1.1` | Establish common governance framework for the AI lifecycle to provide clear guidance to AI project teams | Établir un cadre de gouvernance commun pour le cycle de vie de l&#39;IA afin de fournir des orientations claires aux équipes chargées des projets d&#39;IA |
| `B.1.2` | Establish a common risk management framework for the AI lifecycle | Établir un cadre commun de gestion des risques pour le cycle de vie de l&#39;IA |
| `B.1.3` | Establish a government-wide governance structure | Établir une structure de gouvernance à l&#39;échelle du gouvernement |
| `B.2.1` | Review, identify and address legal and policy gaps and ambiguities | Examiner, identifier et traiter les lacunes et les ambiguïtés juridiques et politiques |
| `B.2.2` | Develop agile process to review and update policy, guidance, tools and resources | Développer un processus agile pour réviser et mettre à jour la politique, les orientations, les outils et les ressources |
| `B.2.3` | Identify opportunities to synthesize or interpret existing policy to increase usability | Identifier les possibilités de synthétiser ou d&#39;interpréter la politique existante afin d&#39;en améliorer l&#39;utilité |
| `B.2.4` | Update procurement policies, instruments, and processes | Mettre à jour les politiques, les instruments et les procédures de passation de marchés |
| `B.2.5` | Align internal AI policy with domestic policy or law and with international treaties, legislation and norms | Aligner la politique interne en matière d&#39;IA sur la politique ou la législation nationale, ainsi que sur les traités, la législation et les normes internationales |
| `B.3.1` | Adopt a &#34;think AI&#34; approach | Adopter une approche axée sur l’IA |
| `C.1.1` | Assess talent needs | Évaluer les besoins en talents |
| `C.2.1` | Develop a training plan | Élaborer un plan de formation |
| `C.3.1` | Explore obstacles to recruitment and retention and ways to establish flexible data science career pathways for AI practitioners | Explorer les obstacles au recrutement et à la fidélisation et les moyens d&#39;établir des parcours de carrière flexibles en science des données pour les praticiens de l&#39;IA |
| `C.3.2` | Expand interchanges, apprenticeships, co-op programs, and partnerships with AI institutes and research centres to create a talent pipeline | Développer les échanges, l&#39;apprentissage, les programmes coopératifs et les partenariats avec les instituts d&#39;IA et les centres de recherche pour créer un vivier de talents |
| `C.3.3` | Optimize use of AI talent through flexible assignments | Optimiser l&#39;utilisation des talents en IA grâce à des affectations flexibles |
| `C.3.4` | Competitions and challenges to meet some project-based needs | Compétitions et défis pour répondre à certains besoins liés à des projets |
| `D.1.1` | Strengthen and clarify accountabilities for AI use in policy | Renforcer et clarifier les responsabilités en matière d&#39;utilisation de l&#39;IA dans les politiques |
| `D.1.2` | New requirements and standard language for the disclosure of AI use, explanations of how an AI system reaches a decision, and information about rights and protections, including how to seek explanations or recourse and how to report problems | De nouvelles exigences et un langage standard pour la divulgation de l&#39;utilisation de l&#39;IA, des explications sur la manière dont un système d&#39;IA prend une décision, et des informations sur les droits et les protections, y compris la manière de demander des explications ou des recours et de signaler les problèmes |
| `D.1.3` | Identification of AI capabilities and uses that GC will not pursue | Identification des capacités et des utilisations de l&#39;IA que le GC ne poursuivra pas |
| `D.1.4` | Establishment of a public register of its AI systems within a defined scope | Mise en place d&#39;un registre public de ses systèmes d&#39;IA dans un périmètre défini |
| `D.1.5` | Develop and publish alternative oversight processes for systems that cannot be included in register | Élaborer et publier des processus de surveillance alternatifs pour les systèmes qui ne peuvent pas être inclus dans le registre |
| `D.2.1` | Develop metrics and performance indicators to demonstrate the impact and value of AI initiatives | Élaborer des mesures et des indicateurs de performance pour démontrer l&#39;impact et la valeur des initiatives en matière d&#39;intelligence artificielle |
| `D.2.2` | Develop a framework to track AI adoption | Élaborer un cadre pour suivre l&#39;adoption de l&#39;IA |
| `D.3.1` | Commitment to early and meaningful public and stakeholder engagement on AI initiatives of significant public interest or concern, including targeted engagement of communities that face greater impacts, risks or barriers from AI systems | Engagement en faveur d&#39;une participation précoce et significative du public et des parties prenantes aux initiatives d&#39;IA présentant un intérêt ou une préoccupation publique importants, y compris une participation ciblée des communautés qui sont confrontées à des impacts, des risques ou des obstacles plus importants liés aux systèmes d&#39;IA |
| `D.3.2` | Union and employee engagement on workforce impacts | L&#39;engagement des syndicats et des employés sur l&#39;impact de la main-d&#39;oeuvre |
| `D.3.3` | Client participation in system design to ensure that AI systems do not create or perpetuate barriers to access for clients | Participation des clients à la conception du système afin de s&#39;assurer que les systèmes d&#39;IA ne créent pas ou ne perpétuent pas d&#39;obstacles à l&#39;accès pour les clients |
| `D.3.4` | Provide mechanisms for ongoing public feedback and questions on AI used by the federal government | Mettre en place des mécanismes permettant au public de formuler des commentaires et des questions sur l&#39;IA utilisée par le gouvernement fédéral |




---

#### `activity` – Activity / Activité

**Type:** `text`  
**Required:** Yes  
**Validation:** Must match predefined activities. / Doit correspondre à des activités prédéfinies.  
**Choice Set:** activity (58 values)  


**Description:**  
EN: Activity in support of the AI Strategy  
FR: Activité de soutien à la stratégie en matière d'IA


##### Allowed Values (activity)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `A.1.1.1` | Develop operating and business models, organizational and governance structures, key performance indicators, and ways to prioritize the use of the AI centre&#39;s resources | Élaborer des modèles opérationnels et intégrés, des structures organisationnelles et de gouvernance, des indicateurs de rendement clés et des procédures visant à établir l’ordre de priorité de l’utilisation des ressources du Centre d’expertise en IA |
| `A.1.1.2` | Consolidate the AI communities of practice under an information hub to support knowledge sharing and prevent duplication | Regrouper les communautés de pratique de l’IA sous un centre d’information afin d’améliorer l’échange des connaissances et d’éviter les chevauchements |
| `A.1.2.1` | Identify other high value use cases that could be pursued as lighthouse projects | Cerner les cas d’utilisation ayant une grande valeur qui pourraient être réalisés en tant que projets phares |
| `A.2.1.1` | Provide high-performance computing (HPC) and cloud infrastructure that is available, secure, and scalable to meet the demands of AI projects | Fournir une infrastructure infonuagique et des capacités de calcul à haute performance qui sont accessibles, sécurisées et évolutives afin de répondre aux exigences des projets d’IA |
| `A.2.2.1` | Provide common data and information management systems and practices to support sharing, scaling, and agentic capabilities across Government of Canada platforms | Mettre en oeuvre des pratiques et des systèmes communs de gestion des données et de l’information pour appuyer les échanges, la mise à l’échelle et les capacités agentiques dans l’ensemble des plateformes du GC |
| `A.2.3.1` | Provide access to approved models, services, and application programming interfaces (APIs) within common Government of Canada cloud platforms to build or deploy systems | Offrir l’accès à des services, des interfaces de programmation d’applications (API) et des modèles autorisés dans les plateformes infonuagiques communes du GC pour concevoir ou déployer des systèmes |
| `A.2.4.1` | Provide access to common AI solutions and capabilities in vendor solutions through a standard Government of Canada platform service | Donner l’accès à des solutions et capacités communes en matière d’IA dans les solutions de fournisseurs au moyen d’une plateforme de service standard du GC |
| `A.2.5.1` | Streamline the AI Source list and develop tools for institutions to procure faster with a focus on Canadian service providers | Simplifier la liste des fournisseurs d’IA et créer des outils permettant aux institutions de réaliser des achats plus rapidement, en mettant l’accent sur les fournisseurs de services canadiens |
| `A.3.1.1` | Develop and scale machine translation tool using GC data, ensuring that translation services are provided at the same time and quality in both official languages | Élaborer et déployer un outil de traduction automatique à partir des données du gouvernement du Canada, assurant l’accès à des services de traduction sécurisés disponibles en temps réel et de qualité égale dans les deux langues officielles |
| `A.3.1.2` | Document project processes and lessons to identify policy and procedural barriers, and project teams’ needs for support, to develop and test governance processes, and to demonstrate how AI can be successfully scaled where necessary for Government of Canada requirements | Consigner les processus du projet et les leçons apprises pour repérer les obstacles liés aux politiques et aux procédures et les besoins des équipes de projet en matière de soutien. Cette procédure permet d’élaborer et de mettre à l’essai des processus de gouvernance et de démontrer la façon dont l’IA peut être mise à l’échelle avec succès pourraient être adaptés aux exigences du gouvernement du Canada, le cas échéant |
| `B.1.1.1` | Identify best practice departmental and international governance frameworks which could be adapted where necessary for Government of Canada requirements | Cerner les pratiques exemplaires internationales et ministérielles sur les cadres de gouvernance qui pourraient être adaptés aux exigences du gouvernement du Canada, le cas échéant des organes de gouvernance ministériels et des propriétaires de solutions |
| `B.1.1.2` | Develop GC governance framework in a user-friendly format structured around the AI lifecycle with varying governance requirements according to system risk, sensitivity, and impact | Établir un cadre de gouvernance pour le gouvernement du Canada dans un format convivial structuré en fonction du cycle de vie de l’IA avec des exigences de gouvernance variables selon les risques, la sensibilité et l’incidence des systèmes |
| `B.1.2.1` | Identify best practice risk frameworks which could be adapted where necessary for Government of Canada requirements | Cerner les pratiques exemplaires sur les cadres de gestion des risques qui pourraient être adaptés aux exigences du gouvernement du Canada, le cas échéant |
| `B.1.3.1` | Scale PSPC’s Operational Ethics Review Board to become a government-wide AI ethics review board | Élargir le Conseil d’examen de l’éthique opérationnelle de SPAC pour qu’il devienne un conseil d’examen de l’éthique en matière d’IA à l’échelle du gouvernement |
| `B.1.3.2` | Develop AI program governance structures for technical assessment and review, including determining role of existing bodies such as GCEARB | Mettre sur pied des structures de gouvernance concernant le programme d’IA pour effectuer des évaluations et des examens techniques, notamment déterminer le rôle des organes existants comme le Conseil d’examen de l’architecture intégrée (CEAI) du gouvernement du Canada |
| `B.2.1.1` | Develop Policy Implementation Notice on AI roles and responsibilities, including those of chief information, data, privacy, and security offices, chief architects, departmental governance bodies, and solution owners | Élaborer un avis de mise en œuvre de la politique sur les rôles et les responsabilités en matière d’IA, y compris ceux des dirigeants principaux de l’information et des données et les chefs de la protection des renseignements personnels et de la sécurité, des architectes en chef, des organes de gouvernance ministériels et des propriétaires de solutions |
| `B.2.1.2` | Define acceptable use of AI by outside organizations in their interactions with the Government of Canada, including AI meeting transcription tools | Définir l’utilisation acceptable de l’IA par des organisations externes dans leurs interactions avec le gouvernement du Canada, y compris les outils d’IA pour la transcription de réunions |
| `B.2.1.3` | Address legal and policy ambiguities related to privacy and training data, including guidance on de-identification for data sharing | Corriger les ambiguïtés juridiques et politiques liées aux données sur la protection de la vie privée et la formation, y compris des directives sur la dépersonnalisation pour l’échange des données |
| `B.2.1.4` | Define scope and application of national security systems in PSD s6.3 and the national security exemption in PIN | Définir la portée et l’application des systèmes de sécurité nationale à la section 6.3 de la Politique sur les services et le numérique et l’exemption relative à la sécurité nationale dans un avis de mise en oeuvre de la politique |
| `B.2.2.1` | Establish agile process to review and update policy, guidance, tools and resources, develop new policy and guidance for emerging technologies and applications, and identify opportunities to synthesize or interpret existing policy to increase usability | Établir un processus agile pour examiner et mettre à jour les politiques, les directives, les outils et les ressources, élaborer de nouvelles politiques et directives sur des technologies et des applications émergentes et cerner les possibilités de synthétiser ou d’interpréter les politiques existantes afin de les rendre plus faciles à utiliser |
| `B.2.3.1` | Review the Directive on Automated Decision-Making and Algorithmic Impact assessment tool, publish guidance, and consider their usability and design to ensure they remain relevant to support departments in a changing technological and legislative landscape | Examiner la Directive sur la prise de décisions automatisée et l’outil d’évaluation de l’incidence algorithmique, publier des directives et examiner leur convivialité et leur conception pour s’assurer qu’elles sont toujours adaptées aux réalités des ministères dans un paysage technologique et législatif en évolution |
| `B.2.3.2` | Update the Guide on the Use of Generative AI to adapt to reflect technological changes and address regular questions received from departments | Mettre à jour le Guide sur l’utilisation de l’intelligence artificielle générative pour qu’il soit adapté aux changements technologiques et en tienne compte et afin de répondre aux questions que reçoivent régulièrement les ministères |
| `B.2.3.3` | Identify policy approaches needed to ensure the responsible use of AI for non-administrative purposes and propose action-oriented and department-focused mechanisms to address them | Cerner les approches stratégiques nécessaires pour assurer l’utilisation responsable de l’IA à des fins non administratives et proposer des mécanismes axés sur l’action et les ministères pour y remédier |
| `B.2.4.1` | Review and update procurement policies, instruments and processes to make them more responsive to pace and requirements of AI procurement | Passer en revue et mettre à jour les politiques, les instruments et les processus d’approvisionnement afin de mieux les adapter au rythme de l’IA et aux exigences d’approvisionnement en matière d’IA |
| `B.2.5.1` | Review existing AI commitments in domestic policy and law, identifying where alignment is required | Examiner les engagements existants en matière d’IA dans les politiques et les lois nationales et déterminer les domaines où l’harmonisation est nécessaire |
| `B.2.5.2` | Identify opportunities to align Pan-Canadian AI Strategy Review and action the United Nations Declaration Act Action Plan commitments to Indigenous Data Sovereignty | Trouver des possibilités d’harmoniser la Stratégie pancanadienne en matière d’intelligence artificielle et la Stratégie en matière d’intelligence artificielle pour la fonction publique fédérale Examiner et mettre en oeuvre les engagements du Plan d’action de la Loi sur la Déclaration des Nations Unies sur les droits des peuples autochtones à l’égard de la souveraineté des |
| `B.2.5.3` | Review and action the United Nations Declaration Act Action Plan commitments to Indigenous Data Sovereignty | Examiner et mettre en œuvre les engagements du Plan d’action de la Loi sur la Déclaration des Nations Unies sur les droits des peuples autochtones à l’égard de la souveraineté des données autochtones |
| `B.2.5.4` | Identify opportunities to increase alignment with relevant international treaties, legislation and norms | Trouver des moyens de mieux harmoniser les normes, les lois et les traités internationaux applicables |
| `B.3.1.1` | Update MC drafter&#39;s guide to include AI and data consideration | Mettre à jour le guide du rédacteur des mémoires au Cabinet pour inclure les considérations relatives à l’IA et aux données |
| `B.3.1.2` | Update TB Submission guide to include AI and data considerations, including data, AI, compute and other relevant resource needs and to prompt exploration of collaboration with other departments or scaling existing projects before building or buying new | Mettre à jour le guide des présentations au Conseil du Trésor afin d’inclure les considérations relatives à l’IA et aux données, y compris les besoins en matière de données, d’IA, de calcul et d’autres ressources pertinentes. Trouver des moyens de collaborer avec d’autres ministères ou d’adapter des projets existants avant d’en créer ou d’en acheter de nouveaux |
| `B.3.1.3` | Strengthen TBS challenge function for AI and data | Renforcer la fonction de remise en question du SCT relativement à l’IA et aux données |
| `B.3.1.4` | Clarify EARB expectations regarding the deployment of IT that includes AI or other intelligence automation including common architecture questions or presentation requirements, such as on model selection assessment, costs, and performance | Clarifier les attentes du CEAI concernant le déploiement de la technologie de l’information qui comprend l’IA ou d’autres formes d’automatisation, y compris les questions courantes sur l’architecture ou les exigences de présentation, comme l’évaluation de la sélection des modèles, les coûts et le rendement |
| `B.3.1.5` | Require departments to consider and prioritize AI infrastructure and adoption within integrated IT planning | Exiger des ministères qu’ils tiennent compte de l’infrastructure et de l’adoption de l’IA dans la planification intégrée de la TI et qu’ils leur accordent la priorité |
| `B.3.1.6` | Support the implementation of the GC Data Strategy mission and actions on data stewardship models, expectations, and common practices to ensure high quality data is available for AI implementation | Faciliter la mise en oeuvre des missions et des actions de la Stratégie relative aux données du gouvernement du Canada sur les modèles d’intendance des données, les attentes et les pratiques communes afin de s’assurer que des données de haute qualité sont disponibles pour la mise en oeuvre de l’IA |
| `C.1.1.1` | Assess digital talent needs to the extent possible by leveraging available data on the Digital Talent Platform | Évaluer les besoins en matière de talents numériques en utilisant les données disponibles sur la plateforme Talents numériques dans la mesure du possible |
| `C.2.1.1` | Meet AI training objectives by leveraging existing efforts under multiple plans, including the CSPS Annual Digital Academy Plan, OCHRO’s Public Service Skills Strategy, and TBS-OCIO’s Digital Talent Strategy. These coordinated plans support an evergreen, role-based approach to AI training that includes foundational and advanced skills | Atteindre les objectifs de formation en matière d’IA au moyen des nombreux plans existants, notamment l’Académie du numérique de l’EFPC, la Stratégie relative aux compétences de la fonction publique du Bureau du dirigeant principal des ressources humaines et la Stratégie en matière de talents numériques du Bureau du dirigeant principal de l’information. Ces plans coordonnés favorisent une approche évolutive et axée sur les rôles de la formation en IA qui comprend des compétences de base et avancées |
| `C.2.1.2` | Curate and promote tailored training and learning paths to address advanced technical skills for IT, AI and data practitioners | Organiser et promouvoir des parcours de formation et d’apprentissage personnalisés sur des compétences techniques avancées à l’intention des spécialistes de la TI, de l’IA et des données |
| `C.2.1.3` | Develop, curate, and promote foundational core learning products and learning paths on AI for all public servants, including executives | Élaborer, organiser et promouvoir des parcours et des produits d’apprentissage de base sur l’IA pour tous les fonctionnaires, y compris la haute direction |
| `C.2.1.4` | Convene working group for key stakeholders in the AI learning space to discuss and evaluate ongoing needs and effectiveness of the centralized learning the GC is providing to all public servants | Convoquer un groupe de travail pour les principaux intervenants dans le domaine de l’apprentissage de l’IA afin de discuter et d’évaluer les besoins continus et l’efficacité de l’apprentissage centralisé que le gouvernement du Canada offre à tous les fonctionnaires |
| `C.2.1.5` | Work with public servants through their bargaining agents to prepare the workforce through upskilling and retraining for changes resulting from AI | Travailler avec les fonctionnaires et leurs agents négociateurs afin de préparer la main-d’oeuvre aux changements découlant de l’IA en lui offrant du perfectionnement et du recyclage professionnel |
| `C.3.1.1` | Develop mobility, recruitment, exchanges, and/or other types of opportunities on the GC Digital Talent Platform to recruit, develop, and retain AI and data talent | Accroître la mobilité, le recrutement, les échanges ou d’autres types d’occasions sur la plateforme Talents numériques du gouvernement du Canada pour recruter, perfectionner et maintenir en poste les talents en IA et en données |
| `C.3.2.1` | Review and scale successful departmental initiatives | Examiner et reproduire les initiatives ministérielles réussies |
| `C.3.3.1` | Explore options to use existing provisions for short-term and flexible staffing to optimize talent use | Étudier les options permettant d’inclure des dispositions existantes liées à la dotation à court terme et flexible afin d’optimiser l’utilisation des talents |
| `C.3.4.1` | Explore reuse of challenge programs for specific projects | Étudier la possibilité de réutiliser les programmes Défi pour des projets particuliers |
| `D.1.1.1` | Review Policy on Service and Digital to clarify roles and responsibilities for AI use | Examiner la Politique sur les services et le numérique pour clarifier les rôles et les responsabilités liés à l’utilisation de l’IA |
| `D.1.2.1` | Develop and publish language for disclosure of AI use based on previously used examples | Élaborer et publier des libellés pour la divulgation de l’utilisation de l’IA en se fondant sur des exemples déjà utilisés |
| `D.1.3.1` | Identify and publish list of prohibited uses based on existing commitments in law, policy, or treaties, with commitment to annual review and update | Établir et publier une liste des utilisations interdites en fonction des engagements existants dans les lois, les politiques ou les traités. Cette liste doit être examinée et mise à jour chaque année |
| `D.1.4.1` | Define and publish register scope | Définir et publier la portée du registre |
| `D.1.4.2` | Develop a minimal viable product AI register that connects to personal information banks (PIBS), the Service Inventory, and AIAs | Créer un registre de l’IA de type « produit minimum viable » qui se connecte aux jeux de données existants comme les fichiers de renseignements personnels, le répertoire des services et les évaluations de l’incidence algorithmique |
| `D.1.4.3` | Engage internal and external stakeholders to refine registry format and content to increase value and usability | Mobiliser les intervenants internes et externes pour améliorer le format et le contenu du registre afin d’accroître sa valeur et sa convivialité |
| `D.1.5.1` | Define and publish alternative oversight processes for AI use that cannot be publicly reported in the register | Définir et publier d’autres processus de surveillance de l’utilisation de l’IA qui ne peuvent pas être déclarés publiquement dans le registre |
| `D.2.1.1` | Develop metrics and performance indicators to demonstrate the impact and value of AI initiatives | Élaborer des mesures et des indicateurs de rendement pour démontrer l’incidence et la valeur des initiatives en matière d’IA |
| `D.2.2.1` | Develop a consolidated dashboard that supports the outcomes and performance indicators of the AI and Data Strategies and the Digital Ambition | Élaborer un tableau de bord consolidé qui consigne les résultats et les indicateurs de rendement de la Stratégie en matière d’IA, de la Stratégie relative aux données et de l’Ambition numérique |
| `D.2.2.2` | Develop metrics for deployment, collaboration, sharing and scaling of solutions, departmental investment in AI and enablers, and financial and non-financial ROI for integration into dashboard | Élaborer des mesures liées au déploiement, à la collaboration, aux échanges et aux mises à l’échelle des solutions, aux investissements des ministères dans l’IA et les outils habilitants, ainsi qu’au retour sur les investissements financiers et non financiers aux fins d’intégration dans le tableau de bord |
| `D.3.1.1` | Develop and publish expectations for meaningful public, Indigenous, and stakeholder engagement, using existing resources | Formuler et publier les attentes en matière de mobilisation constructive du public, des Autochtones et des intervenants à l’aide des ressources existantes |
| `D.3.2.1` | Develop expectations and processes for engagement with bargaining agents | Formuler les attentes et établir les processus de mobilisation des agents négociateurs |
| `D.3.3.1` | Develop expectations and processes for engagement with bargaining agents | Formuler les attentes et établir les processus de mobilisation des utilisateurs |
| `D.3.4.1` | Provide mechanisms for ongoing public feedback and questions on AI used by the federal government | Fournir des mécanismes facilitant la rétroaction continue et les questions du public sur l’IA utilisée par le gouvernement fédéral |




---

#### `description_en` – Description (English) / Description (anglais)

**Type:** `text`  
**Required:** No  
**Validation:** Limit the number of characters, free text (maximum 1500 characters). / Limiter le nombre de caractères, libre texte (maximum 1500 caractères).  


**Description:**  
EN: Operational description in the AI Strategy  
FR: Description opérationnelle de la stratégie en matière d'IA


---

#### `description_fr` – Description (French) / Description (français)

**Type:** `text`  
**Required:** No  
**Validation:** Limit the number of characters, free text (maximum 1500 characters). / Limiter le nombre de caractères, libre texte (maximum 1500 caractères).  


**Description:**  
EN: Operational description in the AI Strategy  
FR: Description opérationnelle de la stratégie en matière d'IA


---

#### `expected_completion` – Expected Completion / Achèvement attendu

**Type:** `text`  
**Required:** Yes  
**Validation:** Must match expected completion options in the controlled list. / Doit correspondre aux options d'achèvement prévues de la liste contrôlée.  
**Choice Set:** expected_completion (8 values)  


**Description:**  
EN: Completion of activity  
FR: Achèvement de l'activité


##### Allowed Values (expected_completion)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `2025-Q3` | 2025-Q3 | 2025-T3 |
| `2025-Q4` | 2025-Q4 | 2025-T4 |
| `2026-Q1` | 2026-Q1 | 2026-T1 |
| `2026-Q2` | 2026-Q2 | 2026-T2 |
| `2026-Q3` | 2026-Q3 | 2026-T3 |
| `2026-Q4` | 2026-Q4 | 2026-T4 |
| `2027-Q1` | 2027-Q1 | 2027-T1 |
| `2027-Q2` | 2027-Q2 | 2027-T2 |




---

#### `lead_department` – Lead Department(s) / Ministère(s) responsable(s)

**Type:** `_text`  
**Required:** Yes  
**Validation:** Must match departments and organizations in the controlled list. / Doit correspondre aux départements et organisations de la liste contrôlée.  
**Choice Set:** lead_department (11 values)  


**Description:**  
EN: Primary departments involved  
FR: Principaux départements concernés


##### Allowed Values (lead_department)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `CDS` | Canadian Digital Service | Service Numérique Canadien |
| `CSE` | Communications Security Establishment | Centre de la sécurité des télécommunications Canada |
| `CSPS` | Canadian School of Public Service | École de la fonction publique du Canada |
| `GAC` | Global Affairs Canada | Affaires Mondiales Canada |
| `ISC` | Indigenous Services Canada | Services aux Autochtones Canada |
| `ISED` | Innovation, Science, and Economic Development | Innovation, Sciences et Développement économique Canada |
| `NRC` | National Research Council | Conseil national de recherches Canada |
| `PCO` | Privy Council Office | Bureau du Conseil Privé |
| `PSPC` | Public Services and Procurement Canada | Services publics et Approvisionnement Canada |
| `SSC` | Shared Services Canada | Services Partagés Canada |
| `TBS` | Treasury Board of Canada Secretariat | Secrétariat du Conseil du Trésor du Canada |




---

#### `status` – Status / État

**Type:** `text`  
**Required:** Yes  
**Validation:** Must be one of: Not Started, In Progress, Completed. / Il doit s'agir de l'un des éléments suivants : Non commencé, En cours, Terminé.  
**Choice Set:** status (3 values)  


**Description:**  
EN: AI Strategy tracker status  
FR: Statut du tracker de la stratégie IA


##### Allowed Values (status)

| Code | Label (EN) | Label (FR) |
|------|------------|------------|
| `CO` | Completed | Réalisé |
| `IP` | In progress | En cours |
| `NS` | Not started | Non commencé |




---

#### `progress_en` – Progress Made (English) / Progrès réalisés (anglais)

**Type:** `text`  
**Required:** No  
**Validation:** Limit the number of characters, free text (maximum 1500 characters). / Limiter le nombre de caractères, libre texte (maximum 1500 caractères).  


**Description:**  
EN: Describes any progress made  
FR: Décrit les progrès réalisés


---

#### `progress_fr` – Progress Made (French) / Progrès réalisés (français)

**Type:** `text`  
**Required:** No  
**Validation:** Limit the number of characters, free text (maximum 1500 characters). / Limiter le nombre de caractères, libre texte (maximum 1500 caractères).  


**Description:**  
EN: Describes any progress made  
FR: Décrit les progrès réalisés


---




## Appendix

### Choice Sets Summary (All Resources)
| Choice Set | Field(s) | Values | Standalone Doc |
|------------|----------|--------|----------------|


### Generation Metadata

- Generated: 2025-10-12T01:23:32 (UTC)
- Source: dictionaries/aistrategy.json
- Commit: `d437fb3`
- Tool Version: simple-1

### Validation

- JSON Schema Validation: **PASSED**


### Notes

This documentation is auto-generated. Do not hand-edit; instead update the source recombinant JSON and re-run generation.