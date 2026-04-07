# Digital payment metadata

Metadata employed in data collection using Perplexity Deep Research.

## System

### Digital Payment System Exists

|Field|Value|
|-|-|
|Variable|pay-system-dpayexists|
|Definition|Whether the country has established or is actively developing an instant/real-time payment system (IPS/RTP) that enables digital payments with near-instant settlement (typically within seconds), available 24/7/365. This includes both bank-led and mobile money interoperability systems.|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially deployed; 5=Fully deployed nationwide|
|Old Format|Categorical: "Yes - Operational", "Yes - In Development", "No", "Unknown"|
|Other Metadata|If "In Development", note expected launch date if available. Include year of launch for operational systems.|
|Data Collection Guidelines|Search: "\[Country] instant payment system", "\[Country] real-time payment", "\[Country] digital payment infrastructure", central bank payment systems reports. Check SIIPS Report (AfricaNenda Foundation), World Bank payment systems database, central bank websites.|

## Governance

### Central Bank Involvement in Governance

|Field|Value|
|-|-|
|Variable|pay-governance-cbgovernance|
|Definition|Whether and how the central bank participates in payment system governance beyond its regulatory oversight role, including board representation, operational management, technical standard-setting, or direct system operation.|
|Format|Categorical: 0=Unknown or n.a.; 1=No Direct Role; 2=Regulatory Only; 3=Advisory Role; 4=Board Representation; 5=Direct Operation|
|Old Format|Categorical: "Direct Operation", "Board Representation", "Advisory Role", "Regulatory Only", "No Direct Role", "Unknown"|
|Other Metadata|Direct Operation: CB operates the system. Board Representation: CB has board seats in operator entity. Advisory: CB provides guidance but no formal control. Regulatory Only: CB regulates but doesn't govern operations.|
|Data Collection Guidelines|Search: "\[Country] central bank payment system role", "\[Country] central bank payment governance", payment system board composition, central bank organizational structure, payment system governance frameworks, CB strategic documents.|

### Pro-Poor Governance Mechanisms

|Field|Value|
|-|-|
|Variable|pay-governance-propoorgovernance|
|Definition|Whether payment system governance explicitly includes mechanisms to ensure inclusivity and represent interests of vulnerable populations, including provisions for input from all participant types, consumer representatives, small providers, or explicit financial inclusion mandates in governance documents.|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Partial; 3=Yes|
|Old Format|Categorical: "Yes - Explicit Mechanisms", "Partial - Informal Consideration", "No", "Unknown"|
|Other Metadata|Explicit mechanisms: Consumer advisory boards, small PSP representation, inclusion mandate in charter, affordability requirements. Describe specific mechanisms if present (e.g., "SME PSP reserved board seat", "Annual inclusion reporting requirement").|
|Data Collection Guidelines|Search: "\[Country] payment system financial inclusion governance", "\[Country] payment consumer representation", scheme rules on inclusion, governance charters, stakeholder consultation frameworks, financial inclusion strategies linked to payment systems.|

### Scheme Rules Publicly Available

|Field|Value|
|-|-|
|Variable|pay-governance-schemerulesavail|
|Definition|Whether the scheme rules governing payment system participation, pricing structure, technical requirements, security standards, and conduct are publicly accessible via website, public repository, or on request. Transparency indicator.|
|Format|Categorical: 0=Unknown or n.a.; 1=No - Confidential; 2=Partial - On Request; 3=Yes - Fully Public|
|Old Format|Categorical: "Yes - Fully Public", "Partial - On Request", "No - Confidential", "Unknown"|
|Other Metadata|Fully Public: Rules downloadable online without registration. On Request: Available to interested parties who request. Confidential: Only available to participants. Note URL if publicly available. Comment on language availability.|
|Data Collection Guidelines|Search: "\[Country] payment system scheme rules", "\[Country] payment system rulebook", payment system operator website documentation sections, participant handbooks, regulatory filings, request access if "on request" model noted.|

### Data Privacy Legislation Coverage

|Field|Value|
|-|-|
|Variable|pay-governance-dataprivacylaw|
|Definition|Whether national data protection or privacy legislation exists and explicitly covers payment transaction data, including provisions on data collection, storage, sharing, retention, and user rights over their payment data.|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=General Data Protection Legislation; 3=Specific Payment Data Provisions|
|Old Format|Categorical: "Yes - Specific Payment Data Provisions", "Yes - General Data Protection (includes payments)", "No Specific Legislation", "Unknown"|
|Other Metadata|Cite legislation name and year (e.g., "Data Protection Act 2020"). Note if modeled on GDPR, AU Data Protection Convention. Comment on applicability to mobile money vs bank payments if different.|
|Data Collection Guidelines|Search: "\[Country] data protection act", "\[Country] privacy law payment data", "\[Country] data protection authority", legislative databases, AU Convention on Cyber Security and Personal Data Protection ratification status, DPA websites.|

### Data Breach Notification Requirements

|Field|Value|
|-|-|
|Variable|pay-governance-databreachnotif|
|Definition|Whether legal or regulatory requirements obligate payment service providers to notify users, regulators, and/or data protection authorities about payment data breaches, cybersecurity incidents, or unauthorized access within specified timeframes.|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Discretionary; 3=Mandatory|
|Old Format|Categorical: "Yes - Mandatory with Timeline", "Yes - Discretionary", "No Requirement", "Unknown"|
|Other Metadata|If mandatory, note notification timeline (e.g., "within 72 hours"). Specify who must be notified (users, regulator, DPA). Cite regulation imposing requirement. Note enforcement mechanisms/penalties if available.|
|Data Collection Guidelines|Search: "\[Country] data breach notification", "\[Country] payment security incident reporting", data protection regulations, central bank cybersecurity directives, telecommunications security regulations, incident response frameworks.|

### Consumer Protection Framework for Payments

|Field|Value|
|-|-|
|Variable|pay-governance-consumerprotectlaw|
|Definition|Whether consumer protection legislation or regulations specifically address digital payment services, covering disclosure requirements, liability allocation for unauthorized transactions, error resolution procedures, and user rights.|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Partial; 3=Yes|
|Old Format|Categorical: "Yes - Comprehensive Framework", "Partial - Limited Provisions", "No Specific Framework", "Unknown"|
|Other Metadata|Comprehensive: Dedicated payment consumer protection rules (disclosure, liability limits, dispute resolution, transparency). Partial: General consumer law applies without payment-specific provisions. Cite key regulation.|
|Data Collection Guidelines|Search: "\[Country] payment consumer protection", "\[Country] digital payment user rights", "\[Country] payment error resolution regulation", consumer protection laws, central bank consumer protection directives, scheme rules on consumer protection.|

### Public Performance Reporting

|Field|Value|
|-|-|
|Variable|pay-governance-performancereporting|
|Definition|Whether payment system operators or regulators regularly publish performance metrics and statistics on system usage, transaction volumes/values, participant numbers, uptime, and other operational indicators.|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Ad Hoc; 3=Annual; 4=Monthly/Quarterly|
|Old Format|Categorical: "Yes - Regular (Monthly/Quarterly)", "Yes - Annual Only", "Ad Hoc", "No Public Reporting", "Unknown"|
|Other Metadata|Specify reporting frequency and format (e.g., "Quarterly dashboard", "Annual report"). Note what metrics are disclosed (transaction volume, value, participant count, uptime, etc.). Provide URL if available.|
|Data Collection Guidelines|Search: "\[Country] payment system statistics", "\[Country] payment system annual report", payment system operator website, central bank payment statistics publications, financial stability reports, quarterly bulletins.|

## Functionality

### Person-to-Person (P2P) Payments

|Field|Value|
|-|-|
|Variable|pay-functionality-usecasep2p|
|Definition|Whether the instant payment system supports direct person-to-person transfer of funds between individuals for informal transactions, remittances, and interpersonal value transfers.|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Yes|
|Old Format|Categorical: "Yes", "No", "Unknown"|
|Other Metadata|If Yes, note typical use cases (family support, informal trade, bill splitting, etc.). Comment on usage volume/share if available. Note if P2P is primary use case of system.|
|Data Collection Guidelines|Search: "\[Country] P2P payments", "\[Country] person to person transfer", payment system use case documentation, scheme rules on transaction types, user guides, transaction statistics by type if disclosed.|

### Person-to-Business (P2B) Merchant Payments

|Field|Value|
|-|-|
|Variable|pay-functionality-usecasep2b|
|Definition|Whether the system enables consumer payments to merchants and businesses for goods and services, including retail purchases, bill payments, e-commerce, and subscription services.|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Yes|
|Old Format|Categorical: "Yes", "No", "Unknown"|
|Other Metadata|If Yes, note payment methods (QR code, POS, online checkout, in-app). Comment on merchant adoption rate if available. Distinguish between formal large merchants and informal micro-merchants. Note bill payment service integration.|
|Data Collection Guidelines|Search: "\[Country] merchant payments", "\[Country] QR code merchant", "\[Country] POS acceptance", scheme rules on merchant payments, merchant payment solutions, e-commerce payment integration, bill payment platforms.|

### Government-to-Person (G2P) Payments

|Field|Value|
|-|-|
|Variable|pay-functionality-usecaseg2p|
|Definition|Whether the instant payment system is used or can be used for government disbursements to citizens, including social transfers, welfare payments, salaries, pensions, subsidies, grants, and emergency assistance.|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Limited Use; 3=Yes - Active Use|
|Old Format|Categorical: "Yes - Active Use", "Yes - Capable but Limited Use", "No", "Unknown"|
|Other Metadata|Active Use: Government actively disburses via system. Capable: System supports but limited adoption. If active, note main G2P programs using system (pensions, social transfers, civil service salaries). Estimate percentage of G2P digitized if available.|
|Data Collection Guidelines|Search: "\[Country] government digital payments", "\[Country] G2P payments", "\[Country] social transfer digitization", government treasury/payment modernization, social protection program documentation, civil service payroll systems, COVID relief digital payments.|

### Person-to-Government (P2G) Payments

|Field|Value|
|-|-|
|Variable|pay-functionality-usecasep2g|
|Definition|Whether the system enables citizen payments to government for taxes, fees, licenses, fines, utility bills, and other government service charges.|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Limited Use; 3=Yes - Active Use|
|Old Format|Categorical: "Yes - Active Use", "Yes - Capable but Limited Use", "No", "Unknown"|
|Other Metadata|Active Use: Government widely accepts payments via system. Capable: System supports but limited use. If active, note which revenue types accepted (taxes, fees, fines, utilities). Note if integrated with e-government platforms. Comment on convenience compared to alternatives.|
|Data Collection Guidelines|Search: "\[Country] P2G payments", "\[Country] pay taxes digitally", "\[Country] government revenue collection digital", tax authority payment options, government service portals, revenue authority digitization, utility payment options.|

### Business-to-Business (B2B) Payments

|Field|Value|
|-|-|
|Variable|pay-functionality-usecaseb2b|
|Definition|Whether the instant payment system supports business payments to suppliers, vendors, contractors, and other businesses for commercial transactions, procurement, and supply chain payments.|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Yes|
|Old Format|Categorical: "Yes", "No", "Unknown"|
|Other Metadata|If Yes, note if B2B is common use case or limited. Comment on suitability for SME vs large enterprise payments. Note transaction limit implications for B2B. Mention integration with invoicing/accounting systems if available.|
|Data Collection Guidelines|Search: "\[Country] B2B instant payments", "\[Country] supplier payments digital", scheme rules on business accounts, transaction limits for B2B, SME payment use cases, payment system B2B features, trade finance integration.|

### Cross-Border Payment Functionality

|Field|Value|
|-|-|
|Variable|pay-functionality-usecasecrossborder|
|Definition|Whether the instant payment system enables or plans to enable instant payments across national borders to other countries or regional payment systems, supporting remittances, trade, and regional integration.|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially functional; 5=Fully functional|
|Old Format|Categorical: "Yes - Operational", "Yes - In Development", "Planned", "No", "Unknown"|
|Other Metadata|If operational, list connected countries/systems. Note if bilateral or regional (e.g., PAPSS, WAEMU). Specify if all cross-border or limited corridors. Comment on cost and speed vs traditional remittance. Note currency conversion arrangements (local currency settlement).|
|Data Collection Guidelines|Search: "\[Country] cross-border instant payments", "\[Country] PAPSS integration", "\[Country] regional payment linkage", PAPSS participant lists, bilateral payment agreements, regional economic community payment integration, remittance corridor digitization.|

### Revenue Collection

|Field|Value|
|-|-|
|Variable|pay-functionality-revenue|
|Definition|Whether government taxes, customs duties, and other revenue can be paid using the instant digital payment system, indicating integration of payment infrastructure with tax administration systems.|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Partial; 3=Yes|
|Old Format|Categorical: "Yes - Comprehensive", "Partial - Limited Tax Types", "No", "Unknown"|
|Other Metadata|Comprehensive: All or most taxes payable digitally. Partial: Only certain taxes or fees. Specify which tax types if partial (income tax, VAT, customs, property tax). Note if real-time posting to government accounts. Comment on taxpayer convenience.|
|Data Collection Guidelines|Search: "\[Country] digital tax payment", "\[Country] pay taxes online", "\[Country] revenue authority digital payments", tax authority websites payment options, customs digital payment, e-government payment integration, revenue modernization initiatives.|

### Tax Portal

|Field|Value|
|-|-|
|Variable|pay-functionality-taxportal|
|Definition|Whether an official government web portal or mobile application exists where taxpayers can file tax returns and pay taxes online with direct e-payment capability linked to instant payment system.|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Yes|
|Old Format|Categorical: "Yes" or "No". If Yes, add year of earliest rollout in format: "Yes (YYYY)" or "Yes (YYYY-MM)"|
|Other Metadata|If Yes, provide portal URL and name. Note supported tax types (income, corporate, VAT, etc.). Specify if portal includes filing + payment or payment only. Comment on payment method integration (direct debit, instant payment, card). Note user adoption if available.|
|Data Collection Guidelines|Search: "\[Country] tax e-filing portal", "\[Country] online tax payment", "\[Country] revenue authority e-services", tax authority official websites, e-government portals, digital services for taxpayers, press releases on tax portal launches.|

## Uptake

### Active Digital Payment Users

|Field|Value|
|-|-|
|Variable|pay-uptake-activeusers|
|Definition|Percentage of the adult population (15+ years) who have made at least one digital payment transaction through the instant payment system in the past 90 days, indicating active usage rather than just account ownership.|
|Format|Categorical: 0=Unknown or n.a.; 1=<20%; 2=20-49%; 3=50-69%; 4=70-89%; 5=>89%|
|Old Format|Text: "N users (Date)" or "X% of adults (Date)" or both. Use "Not Available" if unreported.|
|Other Metadata|Specify measurement period (typically 90 days active). Note if count includes mobile money, bank accounts, or both. Distinguish registered accounts vs active users. Provide denominator (total adult population) if percentage. Source data (survey, system operator, regulator).|
|Data Collection Guidelines|Search: "\[Country] active digital payment users", "\[Country] mobile money active users", Global Findex data, GSMA mobile money state of industry reports, payment system statistics, financial inclusion surveys, central bank household surveys.|

### Government Payment Digitization

|Field|Value|
|-|-|
|Variable|pay-uptake-govtadoption|
|Definition|Percentage of government payments (G2P disbursements including salaries, pensions, social transfers) made through instant digital payment system rather than cash or check, reflecting government adoption and modernization.|
|Format|Categorical: 0=Unknown or n.a.; 1=<20%; 2=20-49%; 3=50-69%; 4=70-89%; 5=>89%|
|Old Format|Text: "X% of G2P digitized (Date)" or descriptive text. Use "Not Available" if unreported.|
|Other Metadata|Specify which G2P types included (all, social transfers only, salaries, pensions). Note if percentage by value or volume. Distinguish instant payment system vs other digital (e.g., older bank transfer). Mention major programs fully digitized. Source data (treasury, social protection ministry, central bank).|
|Data Collection Guidelines|Search: "\[Country] G2P digitization", "\[Country] government payment modernization", "\[Country] digital social transfers", treasury reports, social protection program evaluations, World Bank G2P data, IMF financial management assessments, government digital transformation strategies.|

## Credibility

### Independent Audits and Reviews

|Field|Value|
|-|-|
|Variable|pay-credibility-auditsandreviews|
|Definition|Whether independent external audits of payment system security, operations, financial controls, and compliance are conducted by third-party auditors, and whether audit results or summaries are made public.|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Private Audits; 3=Public Audits|
|Old Format|Categorical: "Yes - Public Results", "Yes - Private Audits", "No", "Unknown"|
|Other Metadata|Public Results: Audit findings disclosed. Private: Audits conducted but not public. Specify audit types (financial, security, operational, compliance). Note audit frequency (annual, biennial). Name auditor type (Big 4, local firm, government auditor). Mention audit standards used (IFRS, ISA, ISAE).|
|Data Collection Guidelines|Search: "\[Country] payment system audit", "\[Country] payment operator financial statements", payment system operator annual reports with auditor opinion, regulatory audit requirements, security audit reports, external assessment reports, company filings with audited financials.|

## Social Equity

### Accessibility for Persons with Disabilities

|Field|Value|
|-|-|
|Variable|pay-socialequity-disabilityaccess|
|Definition|Whether digital payment systems and access points (apps, USSD, agents) are designed to accommodate persons with disabilities (visual, hearing, mobility, cognitive impairments), and disability-disaggregated coverage rates if data available.|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Partial; 3=Yes|
|Old Format|Categorical: "Yes - Accessible Design", "Partial - Some Accommodations", "No - Not Accessible", "Unknown". If data available, add: "Coverage: X% of persons with disabilities (Date)"|
|Other Metadata|Yes: Assistive technology compatible, accessible design. Partial: Some features. Describe accommodations: screen reader support, voice interface, tactile/audio ATMs, agent assistance, simplified UI. Cite disability inclusion policy. Note if usage data by disability status collected.|
|Data Collection Guidelines|Search: "\[Country] payment accessibility disability", "\[Country] financial inclusion disability", accessibility features in payment apps, disability rights legislation applied to financial services, financial inclusion surveys with disability module, assistive technology compatibility, agent services for persons with disabilities.|

### Refugee and Migrant Access

|Field|Value|
|-|-|
|Variable|pay-socialequity-refugeemigrantaccess|
|Definition|Whether refugees, asylum seekers, internally displaced persons, migrants, and stateless persons can legally access and open digital payment accounts, and practical barriers or enablers for these populations.|
|Format|Categorical: 0=Unknown or n.a.; 1=No; 2=Partial; 3=Yes|
|Old Format|Categorical: "Yes - Full Access", "Partial - With Documentation", "No - Excluded", "Unknown"|
|Other Metadata|Full Access: Refugee ID accepted for account opening. Partial: Some documentation pathways exist. Excluded: National ID required, refugees excluded. Describe documentation accepted (refugee ID, asylum papers). Note regulatory barriers (AML/KYC requirements). Cite refugee financial inclusion policies.|
|Data Collection Guidelines|Search: "\[Country] refugee financial inclusion", "\[Country] migrants mobile money access", "\[Country] KYC refugee", refugee affairs regulations, UNHCR financial inclusion programs, humanitarian cash transfer programs, KYC requirements for non-nationals, refugee documentation accepted by PSPs, displacement-affected financial access studies.|



