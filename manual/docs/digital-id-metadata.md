# Digital ID metadata

Metadata employed in data collection using Perplexity Deep Research.

## System

### Digital ID System Exists

|Field|Value|
|-|-|
|Variable|id-system-didexists|
|Definition|Whether the country has established or is actively developing a national digital identity system, including foundational ID systems that enable authentication across multiple services. Fully deployed means operational nationwide and accepting new registrations.|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Planning; 3=Under development; 4=Partially deployed; 5=Fully deployed nationwide|
|Other Metadata|Provide details in Comments. Specify: system name, managing authority, year launched or planned, and credential type (card, mobile, number).|
|Data Collection Guidelines|Sources: Government websites, ID authority websites, World Bank ID4D dataset, DPI Map, official legislation. Check for claims of digital or electronic ID publicly displayed in official sources. Verify implementation status through operational websites or evidence of system usage.|

### Biometric Data Collection

|Field|Value|
|-|-|
|Variable|id-system-biocollect|
|Definition|Whether the system collects biometric data and which modalities are collected (fingerprints, facial image, iris scans)|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Fingerprints only; 3=Facial/Iris|
|Other Metadata|Provide details in Comments. Specify: modalities collected (fingerprints, facial, iris), number of fingerprints (2 or 10), and whether biometrics are stored centrally or on the credential.|
|Data Collection Guidelines|Sources: ID authority technical documentation, registration process descriptions, ID4D dataset. Specify number of fingerprints collected (typically 2 or 10), whether facial image captured, and iris scan usage.|

### System Interoperability

|Field|Value|
|-|-|
|Variable|id-system-sysinterop|
|Definition|Whether the digital ID system is designed to be interoperable across government agencies and with other systems through APIs or data exchange protocols|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Yes|
|Other Metadata|Provide details in Comments. Specify: which agencies are connected, whether APIs are documented publicly, and any interoperability framework in place.|
|Data Collection Guidelines|Sources: DPI Map, technical architecture documentation, e-government interoperability frameworks. Check for API availability, data exchange agreements, and cross-agency usage evidence.|

### Electronic Database

|Field|Value|
|-|-|
|Variable|id-system-dbelectronic|
|Definition|Whether identity records are stored in electronic/digital format versus paper-based records|
|Format|Categorical: 0=Unknown or n.a.; 1=Paper only; 2=Mix of paper and digital; 3=Digital|
|Other Metadata|Provide details in Comments. Specify: estimated proportion of records digitized and any ongoing digitization programs.|
|Data Collection Guidelines|Sources: ID authority technical reports, system documentation. Assess extent of digitization - fully electronic, hybrid, or primarily paper-based.|

## Ownership

### Maintenance

|Field|Value|
|-|-|
|Variable|id-ownership-maintenance|
|Definition|Whether the system and the production of credentials can be managed, maintained and developed by in-country technical staff (as opposed to foreign vendors)|
|Format|Categorical: 0=Unknown or n.a.; 1=Foreign vendors dominate;2=Partial in-country capacity; 3=All in-country|
|Other Metadata|Provide details in Comments. Specify: identity of primary vendor, contract arrangements, and any capacity-building or technology transfer programs.|
|Data Collection Guidelines|Sources: ID authority procurement records, World Bank project documents, vendor announcements, news reports on system contracts. Check for technology transfer agreements, local training programs, and vendor dependency risks. Search for "\[country] national ID system vendor" and "\[country] ID authority technical capacity."|

## Governance

### Legal Framework

|Field|Value|
|-|-|
|Variable|id-governance-legframework|
|Definition|Whether formal legislation (act, law, regulation) governs digital identity including identification acts, digital ID laws, or equivalent legislation|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Yes|
|Other Metadata|Provide details in Comments. Cite specific legislation by name, year, and section where possible.|
|Data Collection Guidelines|Sources: National legal databases, parliament/legislature websites, ID authority legal pages. Record specific acts: ID Act, Civil Registration Act, Digital ID Regulation. Cite official legal references.|

### Digital ID Specific Regulation

|Field|Value|
|-|-|
|Variable|id-governance-digidreg|
|Definition|Whether specific regulation or policy addresses digital ID beyond general identification legislation|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Yes|
|Other Metadata|Provide details in Comments. Distinguish from general ID legislation. Cite specific regulation name and date.|
|Data Collection Guidelines|Sources: Legal databases, government gazettes, ID authority policy documents. Distinguish from general ID legislation - look for explicit digital ID policies, data protection rules specific to digital ID.|

### Data Protection Act

|Field|Value|
|-|-|
|Variable|id-governance-dpaexists|
|Definition|Whether national data protection legislation exists and covers personal data linked to the ID system|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Yes|
|Other Metadata|Provide details in Comments. Cite specific DPA name and year. Note whether biometric data is explicitly covered.|
|Data Collection Guidelines|Sources: DLA Piper Data Protection Laws, UNCTAD Data Protection Tracker, national legal databases. Check if DPA explicitly covers biometric data and ID systems.|

### Data Protection Authority Oversight

|Field|Value|
|-|-|
|Variable|id-governance-dpaoversight|
|Definition|Whether a Data Protection Authority or similar body regulates ID data collection and sharing by the ID system|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Yes|
|Other Metadata|Provide details in Comments. Name the DPA authority. Distinguish between existence and active enforcement of oversight.|
|Data Collection Guidelines|Sources: Data protection authority websites, regulatory frameworks. Verify active oversight role, not just existence. Check for ID system-specific mandates or compliance requirements.|

### Legal Proof Status

|Field|Value|
|-|-|
|Variable|id-governance-legalproof|
|Definition|Whether the digital ID credential serves as legal proof of an individual's identity as codified in law|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Yes|
|Other Metadata|Provide details in Comments. Cite specific legal provision. Note any limitations (e.g., accepted for some purposes but not others).|
|Data Collection Guidelines|Sources: Identity legislation, digital ID regulations. Check specific legal provisions stating digital ID has same legal validity as traditional ID. Note any limitations.|

### Civil Registration Integration

|Field|Value|
|-|-|
|Variable|id-governance-crvs|
|Definition|Whether the civil registration and digital ID systems are integrated|
|Format|Categorical: 0=Unknown or n.a.; 1=No integration; 2=Partial integration; 3=Full integration|
|Other Metadata|Provide details in Comments. Specify: direction of integration (CRVS feeds ID, ID feeds CRVS, or bidirectional), technical mechanism, and any ongoing integration projects.|
|Data Collection Guidelines|Sources: Civil registration authority websites, UNICEF CRVS reports, ID4D dataset, AU APAI-CRVS initiative documentation. Check for shared databases, automatic birth-to-ID registration pipelines, and data exchange protocols between civil registration and ID authorities.|

### Judicial Oversight

|Field|Value|
|-|-|
|Variable|id-governance-courtoversight|
|Definition|Whether the ID authority and system are subject to general oversight of the courts and judicial review|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Yes, but not specific to ID; 3=Yes, with ID-specific judicial mechanisms|
|Other Metadata|Provide details in Comments. Cite constitutional provisions or administrative law enabling judicial review of ID decisions.|
|Data Collection Guidelines|Sources: Constitutional provisions, administrative law, judicial review mechanisms. Check if ID-related disputes can be taken to court and if court can review ID authority decisions.|

### Data Sharing Rules

|Field|Value|
|-|-|
|Variable|id-governance-datasharingrules|
|Definition|Whether procedural rules for collection, storage, and sharing of ID-related personal data are publicly available and established|
|Format|Categorical: 0=Unknown or n.a.; 1=Not available; 2=Partially available; 3=Fully available|
|Other Metadata|Provide details in Comments. Specify: whether rules are published online, whether consent mechanisms exist, and whether data-sharing agreements are publicly documented.|
|Data Collection Guidelines|Sources: ID regulations, privacy policies, data sharing agreements. Check for explicit data sharing frameworks, consent mechanisms, and documentation of data flows.|

## Finance

### Ministry of Finance Oversight

|Field|Value|
|-|-|
|Variable|id-finance-oversight|
|Definition|Whether the Ministry of Finance has oversight of the financing and development of the digital ID system|
|Format|Categorical: 0=Unknown or n.a.; 1=No oversight; 2=Partial oversight; 3=Full oversight|
|Other Metadata|Provide details in Comments. Specify: which ministry oversees budget allocation and whether the ID authority has a dedicated budget line.|
|Data Collection Guidelines|Sources: National budget documents, medium-term expenditure frameworks, ID authority annual reports, World Bank or donor project appraisal documents. Check whether ID system has dedicated budget line under MoF. Search for "\[country] national ID budget" and "\[country] ID system funding."|

### Sustainability

|Field|Value|
|-|-|
|Variable|id-finance-sustainability|
|Definition|Whether the ongoing management, maintenance and development of the ID system can be funded by sustainable domestic resources|
|Format|Categorical: 0=Unknown or n.a.; 1=Primarily dependent on external funding; 2=Mixed domestic/external; 3=Primarily domestic funding|
|Other Metadata|Provide details in Comments. Identify major external funders (e.g., World Bank, EU) and any sustainability plan. Note ratio of domestic vs external funding if available.|
|Data Collection Guidelines|Sources: World Bank ID4D project documents, donor coordination reports, ID authority financial statements, government budget documents. Check for donor dependency by searching "\[country] digital ID World Bank funding" and "\[country] ID system donor support." Note ratio of domestic vs external funding if available.|

## Inclusivity

### Population Coverage

|Field|Value|
|-|-|
|Variable|id-inclusivity-popcoverage|
|Definition|Percentage of eligible population that has been issued or registered with digital ID credentials|
|Format|Categorical: 0=Unknown or n.a.; 1=<20%; 2=20-49%;3=50-69%; 4=70-89%; 5=>89%|
|Other Metadata|Provide details in Comments. Distinguish between enrolled and issued. Note eligible population definition (e.g., citizens 16+, all residents). Cite source and year of data.|
|Data Collection Guidelines|Sources: ID authority reports, national statistics, World Bank ID4D, DPI Map. Report both enrolled and issued percentages separately if available. Note eligible population definition (e.g., citizens 16+).|

### Enrollment Eligibility Age

|Field|Value|
|-|-|
|Variable|id-inclusivity-enrolleligible|
|Definition|Age in years at which an individual becomes eligible to register for digital ID|
|Format|Categorical: 0=Unknown or n.a.; 1=>17; 2=10-17; 3=6-10; 4=1-5; 5=<1|
|Other Metadata|Provide details in Comments. Distinguish between registration age and credential issuance age if different. Note any birth registration linkage.|
|Data Collection Guidelines|Sources: ID legislation, registration policies, ID4D dataset. Note if enrollment at birth vs at specific age. Check for different ages for registration vs credential issuance.|

### Enrollment Mandatory Status

|Field|Value|
|-|-|
|Variable|id-inclusivity-enrollmandatory|
|Definition|Whether registration for digital ID is mandatory, optional, or mandatory for specific groups|
|Format|Categorical: 0=Unknown or n.a.; 1=Optional; 2=Mandatory for some; 3=Mandatory for all|
|Other Metadata|Provide details in Comments. Note penalties for non-compliance. Distinguish mandatory registration from mandatory credential possession.|
|Data Collection Guidelines|Sources: ID legislation, registration requirements. Check penalties for non-compliance. Note if mandatory registration differs from mandatory credential possession.|

### Non-National Eligibility

|Field|Value|
|-|-|
|Variable|id-inclusivity-nonnateligible|
|Definition|Whether non-nationals including refugees, asylum seekers, and permanent residents are eligible to register|
|Format|Categorical: 0=Unknown or n.a.; 1=None; 2=Some; 3=All|
|Other Metadata|Provide details in Comments. Specify which categories are eligible (refugees, asylum seekers, permanent residents, temporary workers). Cite UNHCR or immigration policy sources.|
|Data Collection Guidelines|Sources: ID legislation, immigration policies, UNHCR reports. Check specific provisions for different non-national categories. Note any conditional eligibility.|

### Cost of Credential

|Field|Value|
|-|-|
|Variable|id-inclusivity-cost|
|Definition|Whether credentials are issued free of charge|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Yes|
|Other Metadata|Provide details in Comments. Record fee amount in local currency and USD equivalent. Note any fee waivers or subsidies for vulnerable groups.|
|Data Collection Guidelines|Sources: ID authority fee schedules, government gazettes, ID4D dataset. Record local currency and USD equivalent. Note fee waivers or subsidies for vulnerable groups.|

## Functionality

### Digital Authentication Function

|Field|Value|
|-|-|
|Variable|id-functionality-authdigital|
|Definition|Whether the system enables individuals to authenticate themselves or their documents digitally through electronic verification|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Yes|
|Other Metadata|Provide details in Comments. Specify authentication methods: biometric matching, PIN/OTP, QR code, online verification portal.|
|Data Collection Guidelines|Sources: DPI Map, ID authority technical documentation, service descriptions. Check for explicit authentication capabilities: biometric matching, credential verification, API-based authentication.|

### Government Portal Authentication

|Field|Value|
|-|-|
|Variable|id-functionality-authgovtportal|
|Definition|Whether authentication is possible through a centralized government portal or digital gateway|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Yes|
|Other Metadata|Provide details in Comments. Name the portal and describe the scope of services accessible through it.|
|Data Collection Guidelines|Sources: E-government portals, single sign-on systems. Check for integrated digital ID authentication across government services (e.g., Ghana.gov, MyMzansi, Diia).|

### KYC Enablement

|Field|Value|
|-|-|
|Variable|id-functionality-kycenable|
|Definition|Whether the system enables Know Your Customer (KYC) packet collection for service provision, particularly financial services|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Yes|
|Other Metadata|Provide details in Comments. Specify: which sectors use eKYC, whether API-based or manual, and the regulatory basis.|
|Data Collection Guidelines|Sources: Financial sector regulations, ID authority partnerships with banks. Check for electronic KYC verification allowing service providers to access verified identity data.|

### Individual Data Access

|Field|Value|
|-|-|
|Variable|id-functionality-dataview|
|Definition|Whether individuals can view their data held in the ID database and see how it has been accessed|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Yes|
|Other Metadata|Provide details in Comments. Describe mechanism: self-service portal, mobile app, or formal request procedure.|
|Data Collection Guidelines|Sources: ID authority privacy policies, data subject rights documentation. Check for self-service portals, mobile apps, or formal request procedures for data access.|

## Uptake

### Banking/Financial Services Use

|Field|Value|
|-|-|
|Variable|id-uptake-bankuse|
|Definition|Whether credential is accepted or mandatory for opening bank accounts and accessing financial services|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Accepted but not mandatory; 3=Mandatory|
|Other Metadata|Provide details in Comments. Cite regulatory basis (central bank KYC requirements). Note whether digital verification or physical credential is required.|
|Data Collection Guidelines|Sources: Central bank regulations, KYC requirements, financial inclusion policies. Check if digital ID satisfies KYC requirements and is accepted by banks.|

### SIM Card Registration Use

|Field|Value|
|-|-|
|Variable|id-uptake-simreguse|
|Definition|Whether credential is accepted or mandatory for SIM card activation and mobile service registration|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Accepted but not mandatory; 3=Mandatory|
|Other Metadata|Provide details in Comments. Cite telecom regulation. Note whether biometric verification is required for SIM registration.|
|Data Collection Guidelines|Sources: Telecom regulations, SIM registration policies, mobile operator requirements. Note if digital ID meets SIM registration requirements.|

### Social Services Use

|Field|Value|
|-|-|
|Variable|id-uptake-socialservicesuse|
|Definition|Whether credential is accepted or mandatory for registering for social assistance programs and accessing social services|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Accepted but not mandatory; 3=Mandatory|
|Other Metadata|Provide details in Comments. Specify which programs require ID (cash transfers, pensions, subsidies).|
|Data Collection Guidelines|Sources: Social protection policies, program registration requirements. Check integration with cash transfer programs, pensions, subsidies.|

### Healthcare Access Use

|Field|Value|
|-|-|
|Variable|id-uptake-healthuse|
|Definition|Whether credential is accepted or mandatory for accessing public healthcare services|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Accepted but not mandatory; 3=Mandatory|
|Other Metadata|Provide details in Comments. Specify whether ID is required for registration, insurance enrollment, or service delivery.|
|Data Collection Guidelines|Sources: Health ministry policies, patient registration systems, health information systems. Check for ID-health system integration.|

### Cross-Border Recognition

|Field|Value|
|-|-|
|Variable|id-uptake-crossborder|
|Definition|Whether the digital ID is recognized or interoperable across borders through regional agreements or travel documents|
|Format|Categorical: 0=Unknown or n.a.; 2=Recognized in some regional contexts (e.g., ECOWAS travel); 3=Formally interoperable across borders|
|Other Metadata|Provide details in Comments. Specify regional framework (ECOWAS, EAC, SADC). Note whether credential is accepted as a travel document.|
|Data Collection Guidelines|Sources: Regional integration frameworks (e.g., ECOWAS, EAC), travel document policies. Check for regional ID initiatives, border management systems integration.|

## Credibility

### Security Reviews

|Field|Value|
|-|-|
|Variable|id-credibility-securityreview|
|Definition|Whether ID system undergoes regular security audits, penetration testing, or vulnerability assessments|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Yes|
|Other Metadata|Provide details in Comments. Note whether audits are publicly reported. Distinguish between internal reviews and independent third-party assessments.|
|Data Collection Guidelines|Sources: Security reports, audit reports (often confidential). Check for regular security assessments, cyber resilience reviews, and vulnerability management.|



