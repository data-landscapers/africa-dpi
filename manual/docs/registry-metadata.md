# Registry metadata

Metadata employed in data collection using Perplexity Deep Research.

## Population

### Status

|Field|Value|
|-|-|
|Variable Id|reg-pop-exists|
|Definition|Does the government maintain a digital population register?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially deployed; 5=Fully deployed nationwide|
|Other Metadata|A population register is a continuously updated database of all persons resident in a country, maintained by a government agency. Distinguished from a census (periodic) and CRVS (event-based). May be called National Population Register, Civil Register of Persons, or Resident Register.|
|Data Collection Guidelines|Search: "\[Country] population register", "\[Country] national population register digital", "\[Country] civil register of persons". Check national statistics office, Ministry of Interior, e-government portals. Key sources: World Bank ID4D dataset, UN Statistics Division CRVS reports, country e-government strategies.|

### Inclusivity

|Field|Value|
|-|-|
|Variable Id|reg-pop-inclusive|
|Definition|Are all non-citizens allowed to be included in the register?|
|Format|0=Unknown or n.a.; 1=None; 2=Permanent residents only; 3=Some refugees and IDPs ; 4=All included|
|Other Metadata|Non-citizens include permanent residents, refugees (UNHCR-recognised), IDPs, asylum seekers, stateless persons, and temporary residents. Assess the broadest category formally eligible for inclusion, not just those actually registered.|
|Data Collection Guidelines|Search: "\[Country] population register refugees", "\[Country] population register non-citizens", "\[Country] refugee registration system". Check UNHCR country pages, national refugee legislation, population register eligibility criteria. Note distinction between de jure eligibility and de facto practice.|

### Uptake

|Field|Value|
|-|-|
|Variable Id|reg-pop-uptake|
|Definition|What proportion of the population does the register cover?|
|Format|0=Unknown or n.a.; 1=<20%; 2=20-49%; 3=50-69%; 4=70-89%; 5=>89%|
|Other Metadata|Proportion of total resident population (citizens + eligible non-citizens) registered. Use most recent official statistics. If only citizen coverage is reported, note this in Comments and assess based on citizen coverage.|
|Data Collection Guidelines|Search: "\[Country] population register coverage", "\[Country] population register statistics". Check national statistics office, Ministry of Interior reports, World Bank ID4D data. If no population register exists (Status=1), set to 0.|

### National Id integration

|Field|Value|
|-|-|
|Variable Id|reg-pop-id|
|Definition|Is the register integrated with the national ID system?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Integration means systematic linkage via unique identifiers (e.g. national ID number used as key in population register). Assess technical integration (API/database link), not just policy intent. "Partially integrated" means linkage exists but is not universal or bidirectional.|
|Data Collection Guidelines|Search: "\[Country] population register national ID integration", "\[Country] population register linked national identity". Check e-government interoperability documents, national ID authority reports, digital transformation strategies.|

### Civil registration integration

|Field|Value|
|-|-|
|Variable Id|reg-pop-crvs|
|Definition|Is the population register integrated with the civil register?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Integration means birth/death events in the civil register automatically update the population register (additions/removals). Assess whether vital events flow in real-time or batch, and whether coverage is universal or partial.|
|Data Collection Guidelines|Search: "\[Country] population register CRVS integration", "\[Country] birth registration population register link". Check CRVS improvement plans, UNICEF CRVS country profiles, e-government interoperability documents.|

### Data exchange integration

|Field|Value|
|-|-|
|Variable Id|reg-pop-dpi|
|Definition|Is the register integrated with the government's national data exchange system?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Data exchange system refers to a government interoperability platform or data-sharing infrastructure (e.g. X-Road, GovStack, national service bus, API gateway). Assess whether the population register is connected to such a platform, not just whether data is shared ad hoc.|
|Data Collection Guidelines|Search: "\[Country] population register interoperability", "\[Country] data exchange platform", "\[Country] government service bus". Check e-government strategies, digital transformation plans, GovTech assessments. Look for X-Road, GovStack, or similar platforms.|

## Civil

### Status

|Field|Value|
|-|-|
|Variable Id|reg-cr-exists|
|Definition|Does the government maintain a digital civil register?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially deployed; 5=Fully deployed nationwide|
|Other Metadata|A civil register (CRVS) records vital events: births, deaths, marriages, divorces. Distinguished from a population register (stock) — the civil register records flows/events. May be managed by a dedicated CRVS authority, Ministry of Interior/Justice, or local authorities.|
|Data Collection Guidelines|Search: "\[Country] CRVS digital", "\[Country] civil registration system", "\[Country] birth registration digital". Key sources: UNICEF CRVS country profiles, UN-ECA CRVS Decade reports, World Bank ID4D, APAI-CRVS reports, country CRVS improvement plans.|

### Scope

|Field|Value|
|-|-|
|Variable Id|reg-cr-scope|
|Definition|Does the register cover births, deaths and marriages?|
|Format|0=Unknown or n.a.; 1=None; 2=Some; 3=All|
|Other Metadata|Assess which vital event types are captured digitally. "Some" means at least one but not all of births, deaths, and marriages are digitally registered. "All" means all three event types are captured in the digital system.|
|Data Collection Guidelines|Search: "\[Country] CRVS births deaths marriages", "\[Country] vital events registration". Check UNICEF CRVS profiles, national CRVS legislation, civil registration authority websites for which event types are digitally captured.|

### Inclusivity

|Field|Value|
|-|-|
|Variable Id|reg-cr-inclusive|
|Definition|Are all non-citizens allowed to be included in the register?|
|Format|0=Unknown or n.a.; 1=None; 2=Permanent residents only; 3=Some refugees and IDPs ; 4=All included|
|Other Metadata|Same criteria as population register inclusivity: assess whether non-citizens (permanent residents, refugees, IDPs, asylum seekers) can register vital events (births, deaths, marriages) in the system.|
|Data Collection Guidelines|Search: "\[Country] birth registration refugees", "\[Country] civil registration non-citizens". Check UNHCR country pages, UNICEF CRVS profiles, national CRVS legislation for non-citizen eligibility.|

### Uptake

|Field|Value|
|-|-|
|Variable Id|reg-cr-uptake|
|Definition|What proportion of the population does the register cover?|
|Format|0=Unknown or n.a.; 1=<20%; 2=20-49%; 3=50-69%; 4=70-89%; 5=>89%|
|Other Metadata|Use birth registration completeness as the primary proxy (most commonly reported). WHO/UNICEF/World Bank publish birth registration data. If only birth registration rates are available, use those and note in Comments.|
|Data Collection Guidelines|Search: "\[Country] birth registration rate", "\[Country] CRVS completeness". Key sources: UNICEF/WHO birth registration data, UN Statistics Division, World Bank World Development Indicators (SP.REG.BRTH.ZS), DHS/MICS surveys. Use birth registration completeness as primary proxy.|

### National Id integration

|Field|Value|
|-|-|
|Variable Id|reg-cr-id|
|Definition|Is the register integrated with the national ID system?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Integration means vital events trigger updates in the national ID system (e.g. birth registration generates a national ID number, death registration deactivates an ID). Assess technical linkage, not just policy.|
|Data Collection Guidelines|Search: "\[Country] birth registration national ID", "\[Country] CRVS identity system integration". Check whether birth registration automatically generates a national ID number, and whether death registration deactivates IDs.|

### Population register integration

|Field|Value|
|-|-|
|Variable Id|reg-cr-pop|
|Definition|Is the register integrated with the population register?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Integration means vital events in the civil register update the population register. This is the inverse of reg-pop-crvs — both should normally have the same or similar rating.|
|Data Collection Guidelines|Search: "\[Country] CRVS population register integration", "\[Country] civil registration population register linked". This is the inverse of reg-pop-crvs. Check interoperability documentation.|

### Data exchange integration

|Field|Value|
|-|-|
|Variable Id|reg-cr-dpi|
|Definition|Is the register integrated with the government's national data exchange system?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Data exchange system refers to a government interoperability platform. Assess whether the civil register is connected to such a platform for automated data sharing with other government systems.|
|Data Collection Guidelines|Search: "\[Country] CRVS interoperability", "\[Country] civil registration data exchange platform". Check e-government strategies, CRVS digitisation plans.|

## Land

### Status

|Field|Value|
|-|-|
|Variable Id|reg-land-exists|
|Definition|Does the government maintain a digital land register?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially deployed; 5=Fully deployed nationwide|
|Other Metadata|A land register (title register or deeds register) records legal ownership, rights, and encumbrances over land and property. Distinguished from a cadastral register (spatial/physical description of land parcels). May be called Land Registry, Title Registry, or Deeds Office.|
|Data Collection Guidelines|Search: "\[Country] land registration digital", "\[Country] land registry system", "\[Country] land title registration". Key sources: World Bank Doing Business/B-READY indicators (registering property), FAO land governance assessments, country land policy documents, Cadasta Foundation resources.|

### Separate cadastral register

|Field|Value|
|-|-|
|Variable Id|reg-land-cadastral|
|Definition|Does the government maintain a separate cadastral register?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially deployed; 5=Fully deployed nationwide|
|Other Metadata|A cadastral register is a spatial database of land parcel boundaries, areas, and physical descriptions, often linked to maps/GIS. Distinguished from the land/title register which records legal ownership. Some countries maintain a unified system; others have separate registers.|
|Data Collection Guidelines|Search: "\[Country] cadastral system digital", "\[Country] cadastral register GIS", "\[Country] land parcel mapping". Check land survey/mapping agencies, FAO/UN-Habitat land reports.|

### Uptake

|Field|Value|
|-|-|
|Variable Id|reg-land-uptake|
|Definition|What proportion of land ownership does the register cover?|
|Format|0=Unknown or n.a.; 1=<20%; 2=20-49%; 3=50-69%; 4=70-89%; 5=>89%|
|Other Metadata|Proportion of land parcels/ownership rights formally registered in the digital system. In many African countries, customary/communal land may not be formally registered. Note whether the figure includes or excludes customary land in Comments.|
|Data Collection Guidelines|Search: "\[Country] land registration coverage", "\[Country] percentage land titled", "\[Country] land formalization". Key sources: World Bank, FAO VGGT assessments, country land reform programmes. Note whether customary land is included.|

### Address register integration

|Field|Value|
|-|-|
|Variable Id|reg-land-address|
|Definition|Is the register integrated with the address register?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Integration means land parcels in the register are linked to the address register (e.g. a plot has a registered street address). Assess technical linkage, not just whether addresses appear in land records informally.|
|Data Collection Guidelines|Search: "\[Country] land register address integration", "\[Country] property address register linked". Check land registration authority documentation.|

### Business register integration

|Field|Value|
|-|-|
|Variable Id|reg-land-business|
|Definition|Is the register integrated with the business register?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Integration means business premises recorded in the business register are linked to land parcels in the land register. Assess technical linkage between the two systems.|
|Data Collection Guidelines|Search: "\[Country] land register business register integration". Check interoperability between land authority and companies registrar.|

### Data exchange integration

|Field|Value|
|-|-|
|Variable Id|reg-land-dpi|
|Definition|Is the register integrated with the government's national data exchange system?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Data exchange system refers to a government interoperability platform. Assess whether the land register is connected for automated data sharing.|
|Data Collection Guidelines|Search: "\[Country] land register interoperability", "\[Country] land registration data exchange". Check e-government strategies.|

## Address

### Status

|Field|Value|
|-|-|
|Variable Id|reg-address-exists|
|Definition|Does the government maintain a digital address register?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially deployed; 5=Fully deployed nationwide|
|Other Metadata|An address register is a systematic database of standardised physical addresses (street names, numbers, postal codes) for buildings and plots. Distinguished from informal addressing or GPS-based systems. May include digital addressing systems (e.g. what3words, Plus Codes) adopted officially.|
|Data Collection Guidelines|Search: "\[Country] address register", "\[Country] digital addressing system", "\[Country] national addressing system", "\[Country] street naming numbering". Check postal services, national mapping agencies, e-government portals. Note: some countries have adopted digital addressing (what3words, Plus Codes) as official systems.|

### Business uptake

|Field|Value|
|-|-|
|Variable Id|reg-address-business|
|Definition|What proportion of business properties does the register cover?|
|Format|0=Unknown or n.a.; 1=<20%; 2=20-49%; 3=50-69%; 4=70-89%; 5=>89%|
|Other Metadata|Proportion of business/commercial properties with a registered standardised address in the digital address register.|
|Data Collection Guidelines|Search: "\[Country] business address register coverage", "\[Country] commercial property addressing". If no address register exists (Status=1), set to 0.|

### Household uptake

|Field|Value|
|-|-|
|Variable Id|reg-address-house|
|Definition|What proportion of private properties does the register cover?|
|Format|0=Unknown or n.a.; 1=<20%; 2=20-49%; 3=50-69%; 4=70-89%; 5=>89%|
|Other Metadata|Proportion of residential/private properties with a registered standardised address. In many African countries, rural and informal urban areas may lack formal addresses.|
|Data Collection Guidelines|Search: "\[Country] residential address coverage", "\[Country] household addressing". Check national addressing programme statistics, postal service coverage data.|

### Land register integration

|Field|Value|
|-|-|
|Variable Id|reg-address-land|
|Definition|Is the register integrated with the land register?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Integration means addresses in the register are linked to land parcels in the land register. Assess technical linkage between the two systems.|
|Data Collection Guidelines|Search: "\[Country] address register land register integration". Check interoperability between addressing authority and land registry.|

### Data exchange integration

|Field|Value|
|-|-|
|Variable Id|reg-address-dpi|
|Definition|Is the register integrated with the government's national data exchange system?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Data exchange system refers to a government interoperability platform. Assess whether the address register is connected for automated data sharing.|
|Data Collection Guidelines|Search: "\[Country] address register interoperability", "\[Country] addressing system data exchange". Check e-government strategies.|

## Business

### Status

|Field|Value|
|-|-|
|Variable Id|reg-business-exists|
|Definition|Does the government maintain a digital business register?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially deployed; 5=Fully deployed nationwide|
|Other Metadata|A business register records formally registered businesses/companies, typically managed by a Registrar of Companies, Companies House, or equivalent. Includes company name, registration number, directors, legal form, status. May cover sole proprietors, partnerships, and corporations.|
|Data Collection Guidelines|Search: "\[Country] business registration digital", "\[Country] company registration online", "\[Country] registrar of companies". Key sources: World Bank Doing Business/B-READY (starting a business), country investment climate assessments, Companies Registry websites.|

### Uptake

|Field|Value|
|-|-|
|Variable Id|reg-business-uptake|
|Definition|What proportion of businesses does the register cover?|
|Format|0=Unknown or n.a.; 1=<20%; 2=20-49%; 3=50-69%; 4=70-89%; 5=>89%|
|Other Metadata|Proportion of businesses (formal sector) registered in the digital system. Note that informal sector businesses are typically excluded. Use total formal businesses as the denominator if available; otherwise use total registered businesses as proxy.|
|Data Collection Guidelines|Search: "\[Country] business registration rate", "\[Country] formal sector businesses registered". Check companies registrar statistics, World Bank enterprise surveys. Note that informal businesses are typically excluded.|

### Address register integration

|Field|Value|
|-|-|
|Variable Id|reg-business-address|
|Definition|Is the register integrated with the address register?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Integration means businesses in the register are linked to standardised addresses in the address register. Assess technical linkage.|
|Data Collection Guidelines|Search: "\[Country] business register address integration". Check whether business registration captures standardised addresses linked to the address register.|

### Land register integration

|Field|Value|
|-|-|
|Variable Id|reg-business-land|
|Definition|Is the register integrated with the land register?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Integration means businesses in the register are linked to land parcels (business premises) in the land register. Assess technical linkage.|
|Data Collection Guidelines|Search: "\[Country] business register land register integration". Check interoperability between companies registrar and land authority.|

### Data exchange integration

|Field|Value|
|-|-|
|Variable Id|reg-business-dpi|
|Definition|Is the register integrated with the government's national data exchange system?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Data exchange system refers to a government interoperability platform. Assess whether the business register is connected for automated data sharing.|
|Data Collection Guidelines|Search: "\[Country] business register interoperability", "\[Country] company registration data exchange". Check e-government strategies.|

## Electoral

### Status

|Field|Value|
|-|-|
|Variable Id|reg-elect-exists|
|Definition|Does the government maintain a digital electoral register?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially deployed; 5=Fully deployed nationwide|
|Other Metadata|An electoral register (voter roll) records citizens eligible to vote. Typically managed by an electoral commission or equivalent body. Assess whether the register is maintained digitally (database), not just whether paper voter lists exist.|
|Data Collection Guidelines|Search: "\[Country] electoral register digital", "\[Country] voter registration system", "\[Country] electoral commission biometric voter". Key sources: Electoral commission websites, IFES/International IDEA election profiles, ACE Electoral Knowledge Network, election observation mission reports.|

### Uptake

|Field|Value|
|-|-|
|Variable Id|reg-elect-uptake|
|Definition|What proportion of the electorate does the register cover?|
|Format|0=Unknown or n.a.; 1=<20%; 2=20-49%; 3=50-69%; 4=70-89%; 5=>89%|
|Other Metadata|Proportion of the eligible electorate (voting-age citizens) registered. Use the most recent election cycle data. Note whether the figure is from the election commission or independent estimates.|
|Data Collection Guidelines|Search: "\[Country] voter registration rate", "\[Country] registered voters percentage", "\[Country] electoral commission statistics". Check most recent election data from electoral commission, IFES, International IDEA Voter Turnout Database.|

### National Id integration

|Field|Value|
|-|-|
|Variable Id|reg-elect-id|
|Definition|Is the register integrated with the national ID system?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Integration means voter registration uses or is linked to the national ID system (e.g. national ID number as voter registration key, or biometric deduplication against the national ID database). Assess technical linkage.|
|Data Collection Guidelines|Search: "\[Country] voter registration national ID", "\[Country] electoral biometric national ID linked". Check whether voter registration requires/uses national ID, and whether biometric deduplication is linked to the national ID database.|

### Data exchange integration

|Field|Value|
|-|-|
|Variable Id|reg-elect-dpi|
|Definition|Is the register integrated with the government's national data exchange system?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Data exchange system refers to a government interoperability platform. Assess whether the electoral register is connected for automated data sharing. Note: electoral data is often kept separate for independence reasons.|
|Data Collection Guidelines|Search: "\[Country] electoral register interoperability", "\[Country] voter data exchange". Note that electoral data is often kept deliberately independent. Check e-government strategies.|

## Tax

### Status

|Field|Value|
|-|-|
|Variable Id|reg-tax-exists|
|Definition|Does the government maintain one or more tax registers?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially deployed; 5=Fully deployed nationwide|
|Other Metadata|A tax register records individual and/or business taxpayers, typically managed by a revenue authority. May include separate registers for income tax, VAT, customs, etc. Assess whether any tax register is maintained digitally.|
|Data Collection Guidelines|Search: "\[Country] tax administration digital", "\[Country] revenue authority system", "\[Country] electronic tax registration". Key sources: Revenue authority websites, IMF TADAT assessments, World Bank tax administration reports, ATAF (African Tax Administration Forum) reports.|

### Scope

|Field|Value|
|-|-|
|Variable Id|reg-tax-scope|
|Definition|Does the register manage income tax, business taxes or both?|
|Format|0=Unknown or n.a.; 1=None; 2=Income taxpayers only; 3=Business taxpayers only; 4=Both income and business taxpayers|
|Other Metadata|Assess whether the digital tax register covers individual/income taxpayers, business/corporate taxpayers, or both. "Both" means a unified or linked system covering both categories.|
|Data Collection Guidelines|Search: "\[Country] tax register individual business", "\[Country] TIN system scope". Check revenue authority website for which taxpayer types can register.|

### Income taxpayer uptake

|Field|Value|
|-|-|
|Variable Id|reg-tax-incomeuptake|
|Definition|What proportion of individual taxpayers does the register cover?|
|Format|0=Unknown or n.a.; 1=<20%; 2=20-49%; 3=50-69%; 4=70-89%; 5=>89%|
|Other Metadata|Proportion of individual/income taxpayers registered in the digital system. Denominator is the total eligible individual taxpayer base (not total population). In many African countries, the formal individual taxpayer base is small relative to population.|
|Data Collection Guidelines|Search: "\[Country] individual taxpayer registration rate", "\[Country] income tax registered proportion", "\[Country] tax-to-GDP ratio". Check revenue authority statistics, IMF Article IV reports, ATAF data.|

### Business taxpayer uptake

|Field|Value|
|-|-|
|Variable Id|reg-tax-businessuptake|
|Definition|What proportion of businesses does the register cover?|
|Format|0=Unknown or n.a.; 1=<20%; 2=20-49%; 3=50-69%; 4=70-89%; 5=>89%|
|Other Metadata|Proportion of business taxpayers registered in the digital system. Denominator is total formal businesses liable for tax. Compare with business register coverage for consistency.|
|Data Collection Guidelines|Search: "\[Country] business tax registration rate", "\[Country] VAT registered businesses proportion". Check revenue authority statistics, compare with business register data.|

### National Id integration

|Field|Value|
|-|-|
|Variable Id|reg-tax-id|
|Definition|Is the register integrated with the national ID system?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Integration means taxpayer records are linked to the national ID system (e.g. TIN linked to national ID number). Assess technical linkage, not just whether the revenue authority requires national ID for registration.|
|Data Collection Guidelines|Search: "\[Country] TIN national ID linked", "\[Country] tax registration national identity". Check whether TIN issuance requires/uses national ID number.|

### Business register integration

|Field|Value|
|-|-|
|Variable Id|reg-tax-business|
|Definition|Is the register integrated with the business register?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Integration means taxpayer records for businesses are linked to the business register (e.g. business registration number used as key in tax records). Assess technical linkage.|
|Data Collection Guidelines|Search: "\[Country] tax register business register integration", "\[Country] TIN company registration linked". Check whether business registration automatically generates a TIN or vice versa.|

### Data exchange integration

|Field|Value|
|-|-|
|Variable Id|reg-tax-dpi|
|Definition|Is the register integrated with the government's national data exchange system?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Data exchange system refers to a government interoperability platform. Assess whether the tax register is connected for automated data sharing.|
|Data Collection Guidelines|Search: "\[Country] tax system interoperability", "\[Country] revenue authority data exchange". Check e-government strategies, tax modernisation plans.|

## Social Protection

### Status

|Field|Value|
|-|-|
|Variable Id|reg-social-exists|
|Definition|Does the government maintain one or more social protection registers?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially deployed; 5=Fully deployed nationwide|
|Other Metadata|A social protection register (social registry, beneficiary registry) records beneficiaries and/or potential beneficiaries of government social protection programmes (cash transfers, food assistance, pensions, etc.). May be a unified social registry or separate programme-specific registers.|
|Data Collection Guidelines|Search: "\[Country] social registry", "\[Country] social protection register", "\[Country] beneficiary registry", "\[Country] unified beneficiary register". Key sources: World Bank Social Protection reports, ILO social protection country profiles, UNICEF social protection budgets, country social protection strategies.|

### Uptake

|Field|Value|
|-|-|
|Variable Id|reg-social-uptake|
|Definition|What proportion of the intended beneficiaries does the register cover?|
|Format|0=Unknown or n.a.; 1=<20%; 2=20-49%; 3=50-69%; 4=70-89%; 5=>89%|
|Other Metadata|Proportion of intended beneficiaries (target population for social protection) registered. Note whether the figure covers a single programme or a unified social registry. Denominator is the intended beneficiary population, not total population.|
|Data Collection Guidelines|Search: "\[Country] social registry coverage", "\[Country] social protection beneficiaries registered". Check social protection programme statistics, World Bank SP reports, country social protection strategies.|

### National Id integration

|Field|Value|
|-|-|
|Variable Id|reg-social-id|
|Definition|Is the register integrated with the national ID system?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Integration means beneficiary records are linked to the national ID system (e.g. national ID used for beneficiary identification and deduplication). Assess technical linkage.|
|Data Collection Guidelines|Search: "\[Country] social protection national ID", "\[Country] social registry identity verification". Check whether beneficiary identification uses national ID, and whether deduplication is linked to the national ID database.|

### Data exchange integration

|Field|Value|
|-|-|
|Variable Id|reg-social-dpi|
|Definition|Is the register integrated with the government's national data exchange system?|
|Format|0=Unknown or n.a.; 1=No; 2=Planned; 3=Under development; 4=Partially integrated; 5=Fully integrated nationwide|
|Other Metadata|Data exchange system refers to a government interoperability platform. Assess whether the social protection register is connected for automated data sharing.|
|Data Collection Guidelines|Search: "\[Country] social registry interoperability", "\[Country] social protection data exchange". Check e-government strategies, social protection digitisation plans.|



