# Case individual stakeholder metadata

Variable definitions and collection guidance for case individual stakeholder.

## Linkage

### Individual_ID

| Field | Value |
|---|---|
| Variable ID | IND_001 |
| Definition | Unique identifier for the individual |
| Format | Text |
| Data Collection Guidance | Auto-generated. Format: [ISO country code]I[3-digit sequence]. The 'I' distinguishes individuals from institutions. Start at 001 for each country. Use country where individual is primarily based/active. |

### Institution_ID

| Field | Value |
|---|---|
| Variable ID | IND_002 |
| Definition | Links individual to their primary institution (if applicable) |
| Format | Text (Foreign Key - Optional) |
| Data Collection Guidance | OPTIONAL. If individual works for mapped institution, use exact Institution_ID (e.g., ZA001). If independent (journalist, consultant, retired), use 'Independent'. If works for non-mapped institution (e.g., minor university, African Union, foreign org), use 'Non-Mapped Institution' and specify in Institution_Name_If_Not_Mapped. |

### Institution_Name_If_Not_Mapped

| Field | Value |
|---|---|
| Variable ID | IND_003 |
| Definition | Name of institution if individual is affiliated but institution not in main dataset |
| Format | Text |
| Data Collection Guidance | Fill ONLY if Institution_ID = 'Non-Mapped Institution'. Examples: 'African Union Commission', 'University of Lagos', 'Independent Consultant', 'Freelance Journalist'. Leave blank if Institution_ID links to mapped institution or if truly independent. |

## Basic Information

### Individual_Name

| Field | Value |
|---|---|
| Variable ID | IND_004 |
| Definition | Full name of the individual |
| Format | Text |
| Data Collection Guidance | Search leadership pages, LinkedIn, news articles, conference speakers, publications. Use format 'FirstName LastName'. Add [Partial] if only surname known: 'Unknown [Partial] Surname'. Verify spelling across multiple sources. |

### Job_Title

| Field | Value |
|---|---|
| Variable ID | IND_005 |
| Definition | Current official job title/position or professional designation |
| Format | Text |
| Data Collection Guidance | For institutional roles: use exact title from website/LinkedIn (e.g., 'Chief Executive Officer', 'Director of Digital Identity'). For independent: use professional descriptor (e.g., 'Independent Digital Policy Consultant', 'Investigative Journalist specializing in tech policy', 'Emeritus Professor of Computer Science', 'Senior Research Fellow'). Verify current position. |

### Role_Category

| Field | Value |
|---|---|
| Variable ID | IND_006 |
| Definition | Standardized role category for analysis |
| Format | Categorical: Senior Leadership C-suite/Director \| Technical Lead \| Policy/Strategy Lead \| Operational Manager \| Program Manager \| Advocacy/Communications Lead \| Research Lead \| Legal/Compliance Lead \| Independent Expert/Consultant \| Journalist/Media \| Other |
| Data Collection Guidance | Categorize based on title and primary role. Senior Leadership = CEO, Executive Director, Minister, Director-General, VP; Technical Lead = CTO, Head of Engineering, Technical Director; Policy/Strategy = Chief Policy Officer, Head of Strategy; Independent Expert/Consultant = consultants, advisors not employed by mapped institution; Journalist/Media = journalists, editors, media analysts; Research Lead = Research Director, Principal Investigator, Professor. |

## Tenure

### Tenure_Start

| Field | Value |
|---|---|
| Variable ID | IND_007 |
| Definition | Start date in current position or independent practice |
| Format | Date (Partial) |
| Data Collection Guidance | Search LinkedIn, institution announcements, news archives. For independent consultants: when they started independent practice. For journalists: when they began covering DPI/digital policy. Use YYYY-MM if exact month known, YYYY if only year. Add ~ prefix for approximate dates (~2023). Use 'Unknown' if cannot be determined. |

### Years_In_Role

| Field | Value |
|---|---|
| Variable ID | IND_009 |
| Definition | Approximate years in current role or practice area |
| Format | Numeric |
| Data Collection Guidance | Calculate from Tenure_Start to present (or Tenure_End if departed). For independent experts: years focusing on DPI domain. Round to 1 decimal place. Use 'Unknown' if tenure dates unavailable. |

## DPI Experience

### DPI_Focus_Areas

| Field | Value |
|---|---|
| Variable ID | IND_010 |
| Definition | Individual's specific DPI domains of work/expertise |
| Format | Categorical: (Multiple) Digital Identity \| Digital Payments \| Data Sharing/Exchange \| Connectivity Infrastructure \| Cybersecurity \| Data Protection/Privacy \| Digital Skills/Literacy \| Interoperability Standards \| Digital Public Services \| Other |
| Data Collection Guidance | May differ from institutional focus. Check individual's project portfolio, publications, speeches, LinkedIn profile, articles written, research conducted. Select ALL areas where individual has demonstrated expertise/leadership. Separate with semicolon (;). |

### Previous_DPI_Role

| Field | Value |
|---|---|
| Variable ID | IND_011 |
| Definition | Previous relevant position in DPI ecosystem |
| Format | Text |
| Data Collection Guidance | Document most recent/relevant previous DPI role. Format: 'Job Title, Institution Name, YYYY-YYYY'. Example: 'Director of Payments, Central Bank, 2018-2022' or 'Senior Correspondent, Tech News Africa, 2015-2020'. Use LinkedIn, CVs, biographical profiles. |

## Expertise

### Technical_Expertise

| Field | Value |
|---|---|
| Variable ID | IND_012 |
| Definition | Level of individual's technical knowledge in DPI |
| Format | Categorical: Expert \| Advanced \| Intermediate \| Basic \| Non-technical \| Unknown |
| Data Collection Guidance | Check publications, presentations, qualifications, technical outputs. Expert = recognized technical authority, advanced degree/certification; Advanced = strong technical knowledge, can lead technical projects; Intermediate = moderate understanding; Basic = limited knowledge; Non-technical = policy/management/journalism focus without technical background. |

### Educational_Background

| Field | Value |
|---|---|
| Variable ID | IND_013 |
| Definition | Highest relevant degree and field |
| Format | Text |
| Data Collection Guidance | Search LinkedIn, bios, conference profiles. Format: 'PhD in Computer Science, MIT' or 'MBA, University of Cape Town'. Focus on highest/most relevant degree. Use 'Unknown' if not found. |

## Influence

### Decision_Authority

| Field | Value |
|---|---|
| Variable ID | IND_015 |
| Definition | Individual's decision-making power in DPI matters |
| Format | Categorical: Full Authority \| Significant Authority \| Moderate Authority \| Limited Authority \| No Authority \| Unknown |
| Data Collection Guidance | Assess from job title, organizational structure, decision documents. Full = can make final decisions (CEO, Minister); Significant = substantial decision power (Director); Moderate = shared decision-making (Manager); Limited = advisory role; No Authority = implementation only. For independent experts/journalists: typically 'Limited Authority' or 'No Authority' unless serving in advisory capacity to decision-makers. |

### Budget_Authority

| Field | Value |
|---|---|
| Variable ID | IND_016 |
| Definition | Whether individual controls DPI-related budget |
| Format | Categorical: Yes - Full \| Yes - Partial \| No \| Unknown |
| Data Collection Guidance | Check if individual has budget allocation/approval powers for DPI projects. Full = complete budget control; Partial = shared or limited budget authority; No = no budget control (typical for independent consultants, journalists, academics without grant management); Unknown = unclear. |

### Network_Position

| Field | Value |
|---|---|
| Variable ID | IND_017 |
| Definition | Position within DPI stakeholder networks |
| Format | Categorical: Central Hub \| Well-Connected \| Moderately Connected \| Peripheral \| Isolated \| Unknown |
| Data Collection Guidance | Assess from forum participation, board memberships, speaking engagements, co-authorships, partnerships, media citations. Central Hub = key connector across sectors, frequently referenced; Well-Connected = strong networks across multiple stakeholder types; Moderately Connected = some connections, mainly within sector; Peripheral = limited networks; Isolated = few connections. Independent experts/journalists with high visibility can be 'Central Hub' or 'Well-Connected'. |

### Influence_Type

| Field | Value |
|---|---|
| Variable ID | IND_018 |
| Definition | Primary mechanism through which individual exerts influence |
| Format | Categorical: (Multiple) Formal Authority \| Technical Expertise \| Thought Leadership \| Media Influence \| Network Position \| Research/Evidence \| Advocacy/Activism \| Funding Control \| Implementation Capacity \| Other |
| Data Collection Guidance | Select ALL applicable influence mechanisms. Formal Authority = official position power; Technical Expertise = recognized expert status; Thought Leadership = shapes discourse through ideas; Media Influence = shapes public opinion through journalism/commentary; Network Position = connector/broker role; Research/Evidence = influences through credible research; Advocacy = campaigns and mobilization; Funding Control = resource allocation power; Implementation = makes things happen. Separate with semicolon (;). |

## Engagement

### Public_Visibility

| Field | Value |
|---|---|
| Variable ID | IND_019 |
| Definition | Level of public visibility in DPI discussions |
| Format | Categorical: Very High \| High \| Medium \| Low \| Very Low \| Unknown |
| Data Collection Guidance | Assess from media presence, speaking engagements, social media, publications. Very High = regular media presence, keynote speaker, high social media following; High = frequent public commentary; Medium = occasional visibility; Low = rare public presence; Very Low = behind-the-scenes only. Independent journalists/analysts often have 'High' or 'Very High' visibility. |

### Publications_Output

| Field | Value |
|---|---|
| Variable ID | IND_020 |
| Definition | Recent publications on DPI topics |
| Format | Text |
| Data Collection Guidance | Document recent (last 3 years) publications, reports, papers, articles on DPI. Format: 'Title, YYYY'. Include: research papers, reports, policy briefs, op-eds, investigative journalism pieces, blog posts (if influential). Separate multiple with semicolon (;). Include links if available. Use 'None found' if no publications. |

### Speaking_Engagements

| Field | Value |
|---|---|
| Variable ID | IND_021 |
| Definition | Recent conference/event speaking engagements |
| Format | Text |
| Data Collection Guidance | Document recent (last 2 years) speaking at conferences, panels, webinars on DPI. Format: 'Event Name, YYYY-MM' or 'Event Name, YYYY'. Separate multiple with semicolon (;). Check conference programs, LinkedIn, YouTube. Use 'None found' if not available. |

## Data Provenance

### Data_Source

| Field | Value |
|---|---|
| Variable ID | IND_025 |
| Definition | Sources consulted for individual data |
| Format | Text |
| Data Collection Guidance | Document ALL sources used. Format: 'Source description \| URL \| YYYY-MM-DD'. Separate multiple sources with semicolon (;). Example: 'LinkedIn profile \| https://linkedin.com/in/name \| 2026-03-09; Personal website \| https://example.com \| 2026-03-09; News byline \| https://news.com/author/name \| 2026-03-05'. |

### Data_Collection_Date

| Field | Value |
|---|---|
| Variable ID | IND_026 |
| Definition | Date when data was collected |
| Format | Date |
| Data Collection Guidance | Use ISO 8601 format (YYYY-MM-DD). Record date when data collection was completed for this individual. |

### Data_Collector

| Field | Value |
|---|---|
| Variable ID | IND_027 |
| Definition | Person/team who collected the data |
| Format | Text |
| Data Collection Guidance | Record researcher name or initials for quality control and follow-up. Use consistent format within dataset. |
