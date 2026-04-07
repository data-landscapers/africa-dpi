# ICT infrastructure metadata

Metadata employed in data collection using Perplexity Deep Research.

## Energy

### Electricity Access Rate

|Field|Value|
|-|-|
|Variable|ict-energy-elecaccess|
|Definition|Percentage of national population with access to electricity (grid or off-grid). This is the primary indicator of energy infrastructure availability for ICT. Based on World Bank/IEA Tracking SDG7 data, national statistical offices, or Afrobarometer surveys.|
|Format|Categorical: 0=Unknown or n.a.; 1=<25% population; 2=25-49%; 3=50-74%; 4=75-89%; 5=90%+|
|Other Metadata|Primary sources: World Bank WDI (SE.ELC.ACCS.ZS), IEA/IRENA/UNSD/World Bank SDG7 Tracking, Afrobarometer. Available for all 54 African countries. Updated annually.|
|Data Collection Guidelines|Search: World Bank data portal 'Access to electricity (% of population)', IEA SDG7 tracking database, '\[Country] electricity access rate', national energy statistics. Use most recent year available (2022-2025 preferred).|

### Urban-Rural Electrification Gap

|Field|Value|
|-|-|
|Variable|ict-energy-urbanruraldevide|
|Definition|The gap between urban and rural electricity access rates. A smaller gap indicates more equitable energy distribution, critical for ensuring ICT infrastructure can serve the whole population, not just cities.|
|Format|Categorical: 0=Unknown or n.a.; 1=Gap >60 percentage points; 2=Gap 41-60pp; 3=Gap 21-40pp; 4=Gap 10-20pp; 5=Gap <10pp|
|Other Metadata|Primary sources: World Bank WDI (urban/rural electrification rates), IEA, Afrobarometer. Urban and rural rates are separately tracked by most international databases. Difference calculated as urban rate minus rural rate.|
|Data Collection Guidelines|Search: World Bank 'Access to electricity, urban (% of urban population)' and 'Access to electricity, rural (% of rural population)' for \[Country]. Calculate the gap. Afrobarometer Round 9/10 also provides urban vs rural energy access data.|

### Grid Reliability (Power Outage Frequency)

|Field|Value|
|-|-|
|Variable|ict-energy-reliability|
|Definition|Frequency and severity of power outages experienced by businesses and households. Based on World Bank Enterprise Surveys, Afrobarometer, or national utility data. Reflects the quality of electricity supply beyond mere access — critical for running ICT equipment and data infrastructure.|
|Format|Categorical: 0=Unknown or n.a.; 1=Severe (frequent daily outages or regular load shedding); 2=Poor (weekly outages, intermittent load shedding); 3=Moderate (monthly outages, occasional disruptions); 4=Good (rare outages, <10 per year); 5=Excellent (near-continuous supply, <5 outages per year)|
|Other Metadata|Primary sources: World Bank Enterprise Surveys (infrastructure module - power outages per month), Afrobarometer energy module, national utility reliability reports, SAIDI/SAIFI indices where available. Enterprise Surveys cover most African countries.|
|Data Collection Guidelines|Search: World Bank Enterprise Surveys '\[Country]' infrastructure indicators, Afrobarometer '\[Country] electricity reliability', '\[Country] power outage frequency', national utility SAIDI/SAIFI data, '\[Country] load shedding schedule'. News reports on grid stability.|

### Renewable Energy Share of Generation

|Field|Value|
|-|-|
|Variable|ict-energy-renewableshare|
|Definition|Percentage of total electricity generation from renewable sources (hydro, solar, wind, geothermal, biomass). Indicates energy sustainability and potential for distributed power solutions relevant to ICT infrastructure in off-grid areas.|
|Format|Categorical: 0=Unknown or n.a.; 1=<10%; 2=10-24%; 3=25-49%; 4=50-74%; 5=75%+|
|Other Metadata|Primary sources: IRENA Renewable Energy Statistics, IEA electricity generation data, World Bank WDI (EG.ELC.RNEW.ZS), national energy ministry reports. Available for virtually all African countries via IRENA.|
|Data Collection Guidelines|Search: IRENA Country Profiles '\[Country]', World Bank 'Renewable electricity output (% of total)' for \[Country], IEA '\[Country] electricity generation by source', national energy ministry annual reports.|

### Electricity Affordability

|Field|Value|
|-|-|
|Variable|ict-energy-affordability|
|Definition|Affordability of electricity for residential and small business consumers, measured as cost of electricity relative to income levels. High electricity costs are a direct barrier to ICT adoption and data center viability.|
|Format|Categorical: 0=Unknown or n.a.; 1=Very Expensive (>10% of household income for basic service); 2=Expensive (6-10%); 3=Moderate (3-5%); 4=Affordable (1-2%); 5=Very Affordable (<1%)|
|Other Metadata|Primary sources: World Bank Enterprise Surveys (electricity costs), national energy regulatory authority tariff schedules, ESMAP reports, Doing Business/B-READY indicators, Alliance for Affordable Internet (cost benchmarks). Residential tariff per kWh can be compared to GNI per capita.|
|Data Collection Guidelines|Search: '\[Country] electricity tariff residential', national energy regulatory authority tariff schedules, World Bank Enterprise Surveys electricity cost data, ESMAP energy affordability reports, '\[Country] cost of electricity per kWh USD'. Compare to GNI per capita.|

### Off-Grid and Distributed Energy Policy

|Field|Value|
|-|-|
|Variable|ict-energy-offgridpolicy|
|Definition|Whether the country has established policies, regulations, and programmes supporting off-grid and distributed energy solutions (mini-grids, solar home systems). These are critical for extending ICT infrastructure to unserved areas beyond the central grid.|
|Format|Categorical: 0=Unknown or n.a.; 1=No policy framework; 2=Basic policy exists but limited implementation; 3=Active policy with some deployment; 4=Comprehensive framework with significant deployment; 5=Mature ecosystem with widespread deployment|
|Other Metadata|Primary sources: RISE (Regulatory Indicators for Sustainable Energy) - World Bank/ESMAP, GOGLA market reports, SE4All country action agendas, national rural electrification strategies. RISE covers most African countries.|
|Data Collection Guidelines|Search: RISE database (rise.esmap.org) '\[Country]' mini-grid and off-grid indicators, GOGLA '\[Country] off-grid solar market', SE4All '\[Country]', national rural electrification agency, Power Africa '\[Country]', '\[Country] mini-grid regulation'.|

## Connectivity

### Mobile Phone Penetration

|Field|Value|
|-|-|
|Variable|ict-connectivity-mobilepen|
|Definition|Unique mobile subscriber penetration rate as a percentage of the total population. Measures the proportion of individuals who subscribe to a mobile service (not SIM cards, which can be multiple per person). Mobile phones are the primary device for internet access in Africa.|
|Format|Categorical: 0=Unknown or n.a.; 1=<25%; 2=25-39%; 3=40-54%; 4=55-69%; 5=70%+|
|Other Metadata|Primary sources: GSMA Intelligence (unique subscribers), ITU World Telecommunication Indicators, national telecom regulator reports. GSMA data available for all African countries. Unique subscriber penetration more meaningful than SIM penetration.|
|Data Collection Guidelines|Search: GSMA Intelligence '\[Country] unique subscribers', GSMA Mobile Connectivity Index data download, ITU '\[Country] mobile subscriptions', national telecom regulator annual reports, DataReportal '\[Country] digital report'.|

### Smartphone Adoption

|Field|Value|
|-|-|
|Variable|ict-connectivity-smartphonepen|
|Definition|Percentage of mobile connections using smartphones (as opposed to feature phones or basic phones). Smartphones are the minimum device requirement for accessing most digital public infrastructure services, apps, and mobile internet.|
|Format|Categorical: 0=Unknown or n.a.; 1=<20%; 2=20-39%; 3=40-59%; 4=60-79%; 5=80%+|
|Other Metadata|Primary sources: GSMA Intelligence (smartphone adoption), Pew Research Center Global Attitudes surveys, national ICT household surveys. GSMA provides annual estimates for all African countries.|
|Data Collection Guidelines|Search: GSMA Intelligence '\[Country] smartphone adoption', GSMA Mobile Economy Sub-Saharan Africa report, Pew Research '\[Country] smartphone', DataReportal '\[Country]', national ICT surveys.|

### 4G/LTE Population Coverage

|Field|Value|
|-|-|
|Variable|ict-connectivity-4gcoverage|
|Definition|Percentage of the national population covered by at least one 4G/LTE mobile network signal, whether or not they subscribe to the service. 4G is the practical minimum for meaningful broadband connectivity enabling digital services.|
|Format|Categorical: 0=Unknown or n.a.; 1=<25%; 2=25-49%; 3=50-74%; 4=75-89%; 5=90%+|
|Other Metadata|Primary sources: GSMA Intelligence, ITU World Telecommunication/ICT Indicators Database, national telecom regulators, OpenSignal. Data available for all African countries via ITU and GSMA.|
|Data Collection Guidelines|Search: ITU '\[Country] 4G coverage population', GSMA Mobile Connectivity Index '\[Country]', national telecom regulator annual report, OpenSignal '\[Country]', GSMA Mobile Economy Sub-Saharan Africa.|

### Internet Usage Rate

|Field|Value|
|-|-|
|Variable|ict-connectivity-internetuse|
|Definition|Percentage of individuals who used the internet (from any location, via any device) in the last three months. This measures actual internet adoption beyond network availability, capturing the combined effect of infrastructure, affordability, digital literacy, and relevance.|
|Format|Categorical: 0=Unknown or n.a.; 1=<15%; 2=15-29%; 3=30-49%; 4=50-69%; 5=70%+|
|Other Metadata|Primary sources: ITU World Telecommunication Indicators (individuals using the internet %), World Bank WDI (IT.NET.USER.ZS), Afrobarometer, DataReportal. Available for all African countries. ITU provides annual estimates.|
|Data Collection Guidelines|Search: ITU '\[Country] individuals using the internet', World Bank 'Individuals using the Internet (% of population)' for \[Country], Afrobarometer internet use data, DataReportal '\[Country] digital report'.|

### Mobile Data Affordability

|Field|Value|
|-|-|
|Variable|ict-connectivity-dataafford|
|Definition|Affordability of mobile broadband data, measured as the cost of a basic mobile data plan (1-2GB) as a percentage of GNI per capita. The UN Broadband Commission target is below 2% of monthly GNI per capita. Affordability is the single largest barrier to internet adoption in Africa.|
|Format|Categorical: 0=Unknown or n.a.; 1=Very Expensive (>10% GNI p.c.); 2=Expensive (5-10%); 3=Moderate (2-5%); 4=Affordable (1-2%); 5=Meets UN target (<1%)|
|Other Metadata|Primary sources: ITU ICT Price Baskets, Alliance for Affordable Internet (A4AI), Cable.co.uk annual data pricing study, Research ICT Africa. ITU publishes affordability data for all African countries annually.|
|Data Collection Guidelines|Search: ITU ICT Price Baskets '\[Country]', A4AI Affordability Report, Cable.co.uk worldwide mobile data pricing '\[Country]', Research ICT Africa pricing data, '\[Country] 1GB mobile data cost USD'. Compare to GNI per capita.|

### International Internet Bandwidth

|Field|Value|
|-|-|
|Variable|ict-connectivity-intlbandwidth|
|Definition|The country's total international internet bandwidth capacity per internet user, indicating the quality and capacity of the country's connection to the global internet. Determined by submarine cable landings (for coastal states), cross-border terrestrial fibre (for landlocked states), and satellite links.|
|Format|Categorical: 0=Unknown or n.a.; 1=Very Low (<5 kbit/s per user); 2=Low (5-19 kbit/s); 3=Moderate (20-49 kbit/s); 4=Good (50-99 kbit/s); 5=Strong (100+ kbit/s per user)|
|Other Metadata|Primary sources: ITU World Telecommunication Indicators (international bandwidth per internet user), TeleGeography, national telecom regulators. ITU publishes this indicator for most African countries. Submarine cable landings data from TeleGeography Submarine Cable Map.|
|Data Collection Guidelines|Search: ITU '\[Country] international internet bandwidth', TeleGeography '\[Country] submarine cable', national telecom regulator statistics, '\[Country] international bandwidth capacity'. For landlocked states, note cross-border fibre connectivity.|

### Internet Exchange Point Presence

|Field|Value|
|-|-|
|Variable|ict-connectivity-ixp|
|Definition|Whether the country has an operational Internet Exchange Point (IXP) and its maturity. IXPs enable local internet traffic to be exchanged domestically rather than being routed internationally, reducing latency, costs, and dependence on foreign infrastructure. Critical for local digital ecosystem development.|
|Format|Categorical: 0=Unknown or n.a.; 1=No IXP; 2=IXP planned or under development; 3=Single IXP with limited participation; 4=Active IXP(s) with moderate participation; 5=Mature IXP ecosystem with broad participation|
|Other Metadata|Primary sources: Packet Clearing House (PCH) IXP directory, African IXP Association (Af-IX), PeeringDB, Internet Society IXP reports. PCH maintains a comprehensive global directory. Most data is publicly accessible.|
|Data Collection Guidelines|Search: Packet Clearing House IXP directory '\[Country]', PeeringDB '\[Country]', Af-IX member directory, Internet Society '\[Country] IXP', '\[Country] internet exchange point'. Note number of participants and traffic volumes if available.|

## Data Storage

### Commercial Data Center Presence

|Field|Value|
|-|-|
|Variable|ict-storage-dcpresence|
|Definition|The presence and tier quality of commercial/colocation data center facilities operating in the country. Commercial data centers provide the physical infrastructure for hosting cloud services, content delivery, and enterprise applications domestically.|
|Format|Categorical: 0=Unknown or n.a.; 1=No commercial data centers; 2=Small-scale facilities only (Tier I-II); 3=At least one Tier III facility; 4=Multiple Tier III facilities or at least one Tier IV; 5=Mature data center market with multiple operators and hyperscale presence|
|Other Metadata|Primary sources: Cloudscene data center directory, Data Center Map, Xalam Analytics, Africa Data Centres reports, operator websites (Teraco, Equinix, Raxio, PAIX, MainOne, Liquid). Industry is well-documented due to investment interest.|
|Data Collection Guidelines|Search: Cloudscene '\[Country] data centers', Data Center Map '\[Country]', '\[Country] colocation data center', Xalam Analytics Africa data center report, Africa Data Centres '\[Country]', Raxio '\[Country]'. Note tier levels and major operators.|

### Government Data Center / Cloud Strategy

|Field|Value|
|-|-|
|Variable|ict-storage-govcloud|
|Definition|Whether the government has established dedicated data center infrastructure and/or a government cloud (G-Cloud) strategy for hosting e-government services and public sector data domestically. Critical for data sovereignty and e-government service delivery.|
|Format|Categorical: 0=Unknown or n.a.; 1=No government data center or cloud strategy; 2=Government data center planned or under construction; 3=Basic government data center operational; 4=National data center operational with cloud strategy adopted; 5=Mature government cloud/data center ecosystem with active migration|
|Other Metadata|Primary sources: National ICT/digital transformation strategies, e-government agency websites, ministry of ICT reports, World Bank Digital Development country diagnostics, ITU national cybersecurity and ICT reports.|
|Data Collection Guidelines|Search: '\[Country] national data center', '\[Country] government cloud strategy', '\[Country] e-government data center', ministry of ICT/digital economy reports, World Bank '\[Country] digital development', UN e-Government Survey country profile.|

### Data Localisation Requirements

|Field|Value|
|-|-|
|Variable|ict-storage-datalocalisation|
|Definition|Whether the country has enacted legal or regulatory requirements mandating that certain categories of data (personal data, government data, financial data, or critical infrastructure data) be stored within national borders. Central to data sovereignty debates in Africa.|
|Format|Categorical: 0=Unknown or n.a.; 1=No data localisation requirements; 2=Proposed or draft legislation; 3=Sectoral requirements only (e.g., financial or telecoms data); 4=Comprehensive requirements for personal data or broad categories; 5=Strict requirements covering multiple data types with enforcement|
|Other Metadata|Primary sources: UNCTAD Data Protection and Privacy Legislation tracker, Data Protection Africa portal, national data protection authority websites, DLA Piper Global Data Protection Laws database, AU Convention on Cyber Security ratification status.|
|Data Collection Guidelines|Search: UNCTAD '\[Country] data protection legislation', DLA Piper '\[Country] data protection', Data Protection Africa '\[Country]', '\[Country] data localisation law', '\[Country] data residency requirements', national data protection authority website.|

### Data Protection Legislation

|Field|Value|
|-|-|
|Variable|ict-storage-dataprotection|
|Definition|Whether the country has enacted comprehensive data protection and privacy legislation. A foundational legal requirement for building trust in digital public infrastructure and for enabling secure cross-border data flows under frameworks like the AU Convention on Cyber Security and Personal Data Protection.|
|Format|Categorical: 0=Unknown or n.a.; 1=No legislation; 2=Draft legislation or partial provisions in other laws; 3=Legislation enacted but no enforcement authority; 4=Legislation enacted with Data Protection Authority established; 5=Mature framework with active enforcement and regional alignment|
|Other Metadata|Primary sources: UNCTAD Cyberlaw Tracker (data protection section), Data Protection Africa, African Union Convention ratification tracker, national gazette/legal databases. UNCTAD covers all African countries.|
|Data Collection Guidelines|Search: UNCTAD Cyberlaw Tracker '\[Country]', Data Protection Africa '\[Country]', '\[Country] data protection act', '\[Country] data protection authority', AU Convention on Cyber Security ratification status, DLA Piper data protection laws of the world.|

### Cloud Services Availability

|Field|Value|
|-|-|
|Variable|ict-storage-cloudadoption|
|Definition|The availability and presence of major cloud service providers (hyperscale and regional) operating in or serving the country with local or near-local infrastructure. Cloud availability determines access to scalable computing resources for government, business, and startups.|
|Format|Categorical: 0=Unknown or n.a.; 1=No local or regional cloud presence; 2=Served remotely from distant regions only (>100ms latency); 3=Regional cloud availability zone nearby (same sub-region); 4=At least one major provider with local presence or edge node; 5=Multiple hyperscale providers with local availability zones|
|Other Metadata|Primary sources: AWS, Microsoft Azure, Google Cloud, Huawei Cloud, Oracle Cloud region availability maps, local cloud provider directories. Hyperscale expansion into Africa is well-documented in trade press.|
|Data Collection Guidelines|Search: AWS Global Infrastructure map Africa, Microsoft Azure regions Africa, Google Cloud regions Africa, '\[Country] cloud data center', '\[Country] cloud services provider', Huawei Cloud Africa, Oracle Cloud Africa. Note nearest availability zone and latency estimates.|

### National Cybersecurity Readiness

|Field|Value|
|-|-|
|Variable|ict-storage-cybersecurity|
|Definition|The country's overall cybersecurity preparedness, based on the ITU Global Cybersecurity Index (GCI). Covers legal measures, technical measures, organisational measures, capacity development, and cooperation. Essential for trust in stored data and digital services.|
|Format|Categorical: 0=Unknown or n.a.; 1=GCI score <20 (Building); 2=GCI score 20-39 (Evolving); 3=GCI score 40-59 (Establishing); 4=GCI score 60-79 (Advancing); 5=GCI score 80+ (Role-modelling)|
|Other Metadata|Primary sources: ITU Global Cybersecurity Index (published biennially, most recent 2024). Covers all African countries. Score is 0-100 across 5 pillars: legal, technical, organisational, capacity development, cooperation.|
|Data Collection Guidelines|Search: ITU Global Cybersecurity Index '\[Country]', GCI 2024 country profile, '\[Country] cybersecurity readiness score'. The ITU GCI database at itu.int/en/ITU-D/Cybersecurity/Pages/global-cybersecurity-index.aspx provides country scores.|

## Technical Capacity

### Basic Digital Literacy

|Field|Value|
|-|-|
|Variable|ict-capacity-digitalliteracy|
|Definition|The proportion of the population with basic digital skills (ability to use a computer, smartphone, or the internet for simple tasks such as sending messages, finding information, or using apps). Based on ITU household survey data, Afrobarometer, or national ICT surveys.|
|Format|Categorical: 0=Unknown or n.a.; 1=<10% of population; 2=10-24%; 3=25-39%; 4=40-59%; 5=60%+|
|Other Metadata|Primary sources: ITU household ICT survey indicators (basic digital skills), Afrobarometer internet/ICT literacy questions, UNESCO UIS ICT in Education data, national digital economy assessments. ITU publishes estimates for most countries.|
|Data Collection Guidelines|Search: ITU '\[Country] ICT skills', ITU household ICT survey data, Afrobarometer '\[Country] digital literacy', UNESCO UIS '\[Country] ICT skills', '\[Country] digital literacy survey', World Bank Digital Development diagnostic.|

### Tertiary ICT/STEM Education

|Field|Value|
|-|-|
|Variable|ict-capacity-tertiaryict|
|Definition|The scale and quality of tertiary-level ICT and STEM education programmes available in the country, based on the number and quality of institutions offering ICT degrees, computer science programmes, and engineering courses relative to the population.|
|Format|Categorical: 0=Unknown or n.a.; 1=Very limited (<2 institutions with ICT programmes); 2=Limited (few institutions, low enrolment); 3=Moderate (several institutions, growing enrolment); 4=Good (established institutions with diverse ICT programmes); 5=Strong (multiple quality institutions, high enrolment, regional reputation)|
|Other Metadata|Primary sources: UNESCO UIS education statistics (STEM graduates), QS World University Rankings by subject (Computer Science), national higher education authorities, ACM/IEEE accreditation records. Proxy: STEM graduates as % of total graduates from UNESCO.|
|Data Collection Guidelines|Search: UNESCO UIS '\[Country] STEM graduates', QS Rankings '\[Country] computer science', '\[Country] universities ICT programmes', '\[Country] computer science degree', national higher education council, Times Higher Education '\[Country]'.|

### Developer and Tech Community

|Field|Value|
|-|-|
|Variable|ict-capacity-devcommunity|
|Definition|The size and vibrancy of the local software developer and technology professional community. Measured through proxies such as GitHub activity, Stack Overflow representation, local tech meetup groups, and developer surveys. Indicates the country's capacity to build and maintain digital systems locally.|
|Format|Categorical: 0=Unknown or n.a.; 1=Negligible (very few active developers); 2=Emerging (small but growing community, <1,000 active developers); 3=Developing (active community, local meetups, 1,000-10,000 developers); 4=Established (vibrant community, multiple events, 10,000-50,000 developers); 5=Mature (large community, international visibility, 50,000+ developers)|
|Other Metadata|Primary sources: GitHub Octoverse (developer geography), Stack Overflow Developer Survey, Google Developer Groups directory, AfriLabs member hubs by country, Andela/developer training programme presence. Approximate based on multiple signals.|
|Data Collection Guidelines|Search: GitHub '\[Country] developers', Google Developer Groups '\[Country]', Stack Overflow '\[Country]', '\[Country] tech community', '\[Country] software developers', AfriLabs '\[Country]', '\[Country] coding bootcamp'.|

### Gender Gap in ICT Access

|Field|Value|
|-|-|
|Variable|ict-capacity-gendergap|
|Definition|The gap between men and women in mobile internet usage or internet access. Based on the GSMA Mobile Gender Gap data or ITU gender-disaggregated ICT statistics. A smaller gap indicates more equitable access to digital opportunities.|
|Format|Categorical: 0=Unknown or n.a.; 1=Very large gap (>40% fewer women online); 2=Large gap (30-40% fewer); 3=Moderate gap (20-29% fewer); 4=Small gap (10-19% fewer); 5=Near parity (<10% gap)|
|Other Metadata|Primary sources: GSMA Mobile Gender Gap Report (annual), ITU gender-disaggregated ICT data, Afrobarometer gender analysis, EQUALS Global Partnership. GSMA publishes gender gap data for most African countries.|
|Data Collection Guidelines|Search: GSMA Mobile Gender Gap Report '\[Country]', GSMA Connected Women '\[Country]', ITU '\[Country] gender internet', Afrobarometer '\[Country] gender digital', '\[Country] women internet access'. The gender gap is usually expressed as a percentage difference.|

### E-Government Development

|Field|Value|
|-|-|
|Variable|ict-capacity-egovreadiness|
|Definition|The country's e-government development level based on the UN E-Government Development Index (EGDI). This composite index measures online service delivery, telecommunications infrastructure, and human capital. Indicates the government's capacity to deliver digital public services.|
|Format|Categorical: 0=Unknown or n.a.; 1=EGDI <0.25 (Low); 2=EGDI 0.25-0.49 (Middle); 3=EGDI 0.50-0.64 (High); 4=EGDI 0.65-0.79 (Very High); 5=EGDI 0.80+ (Very High)|
|Other Metadata|Primary sources: UN E-Government Survey (published biennially, most recent 2024). Covers all UN member states including all 54 African countries. EGDI ranges 0 to 1.|
|Data Collection Guidelines|Search: UN E-Government Survey 2024 '\[Country]', UN DESA E-Government Development Index '\[Country]', publicadministration.un.org country data. The UN publishes individual country profiles with EGDI scores.|

## Innovation

### Tech Startup Ecosystem

|Field|Value|
|-|-|
|Variable|ict-innovation-startupecosystem|
|Definition|The maturity of the country's technology startup ecosystem, based on the number of tech startups, venture capital activity, accelerators/incubators, and the presence of a supportive ecosystem. Africa's startup scene is well-documented by trackers like Partech, Disrupt Africa, and Briter Bridges.|
|Format|Categorical: 0=Unknown or n.a.; 1=Nascent (very few tech startups, no visible VC activity); 2=Emerging (some startups, limited funding, 1-2 hubs); 3=Developing (growing startup base, regular funding rounds, several hubs); 4=Established (significant startup activity, $50M+ annual VC, multiple hubs and accelerators); 5=Leading (major ecosystem, $200M+ annual VC, international recognition)|
|Other Metadata|Primary sources: Africa: The Big Deal (tracks every disclosed funding round), Partech Africa Tech Venture Capital Report, Disrupt Africa funding report, Briter Bridges ecosystem maps, GSMA DNSI tech startup indicators. Well-documented sector.|
|Data Collection Guidelines|Search: Africa: The Big Deal '\[Country]' funding data, Partech Africa '\[Country]', Disrupt Africa '\[Country]', '\[Country] tech startup ecosystem', '\[Country] venture capital tech', Briter Bridges '\[Country]'. Note total VC funding and major startups.|

### Technology and Innovation Hubs

|Field|Value|
|-|-|
|Variable|ict-innovation-techhubs|
|Definition|The number and activity level of technology hubs, incubators, accelerators, and co-working spaces focused on technology and innovation. These provide physical infrastructure and support for tech entrepreneurship and skills development.|
|Format|Categorical: 0=Unknown or n.a.; 1=None identified; 2=1-2 hubs with limited activity; 3=3-9 hubs with regular activity; 4=10-24 hubs with diverse focus areas; 5=25+ hubs with a vibrant, mature ecosystem|
|Other Metadata|Primary sources: AfriLabs network directory (largest pan-African hub network), Briter Bridges innovation map, GSMA Ecosystem Accelerator, national ICT authority directories. AfriLabs has mapped over 400 hubs across Africa.|
|Data Collection Guidelines|Search: AfriLabs directory '\[Country]', Briter Bridges innovation map '\[Country]', '\[Country] tech hubs', '\[Country] innovation hubs incubators', GSMA Ecosystem Accelerator '\[Country]', i-Hub/CcHub/other known hub networks.|

### Global Innovation Index Ranking

|Field|Value|
|-|-|
|Variable|ict-innovation-gii|
|Definition|The country's performance on the WIPO Global Innovation Index (GII), which measures innovation capabilities across institutions, human capital, infrastructure, market sophistication, business sophistication, knowledge outputs, and creative outputs. Provides a composite view of the national innovation ecosystem.|
|Format|Categorical: 0=Unknown or n.a. (not included in GII); 1=GII rank 121+ or bottom quartile; 2=GII rank 101-120; 3=GII rank 81-100; 4=GII rank 61-80; 5=GII rank 1-60|
|Other Metadata|Primary sources: WIPO Global Innovation Index (published annually). GII 2024 covers 133 economies including most African countries. Individual country profiles available on WIPO website with detailed sub-indicator breakdowns.|
|Data Collection Guidelines|Search: WIPO Global Innovation Index 2024 '\[Country]', GII 2024 country profile, wipo.int Global Innovation Index rankings. Note overall rank, sub-index ranks for innovation inputs and outputs, and year-on-year change.|



