# Case institution & stakeholder metadata

Variable definitions and collection guidance for case institution and stakeholder.

## Basic Information

### Institution_ID

| Field | Value |
|---|---|
| Variable ID | INST_001 |
| Definition | Unique identifier for the institution |
| Format | Text |
| Data Collection Guidance | Auto-generated. Format: [ISO country code][3-digit sequence]. Start at 001 for each country. |

### Country

| Field | Value |
|---|---|
| Variable ID | INST_002 |
| Definition | Country where institution is based |
| Format | Text |
| Data Collection Guidance | Use ISO 3166-1 alpha-2 codes only (ZA, KE, NG, etc.). For pan-African institutions, use country of headquarters. |

### Institution_Name

| Field | Value |
|---|---|
| Variable ID | INST_003 |
| Definition | Official name of the institution |
| Format | Text |
| Data Collection Guidance | Search official websites, company registries, NGO databases. Example: 'Central Bank of Kenya (CBK)'. Use English name if multiple languages available. |

### Institution_Type

| Field | Value |
|---|---|
| Variable ID | INST_004 |
| Definition | Primary institutional category |
| Format | Categorical: Government \| Private Sector \| Civil Society/NGO \| Media \| Academic/Research \| International Organization \| Hybrid/Multi-Sector |
| Data Collection Guidance | Determine based on legal status, funding, governance. Government = state-owned/controlled; Private = commercial entity; Civil Society = non-profit advocacy/service; Media = journalism focus; Academic = research/teaching; International = multilateral/foreign; Hybrid = multiple types. |

### Institution_Subtype

| Field | Value |
|---|---|
| Variable ID | INST_005 |
| Definition | More specific institutional classification |
| Format | Text |
| Data Collection Guidance | Examples: Ministry, Regulatory Agency, Central Bank, State-Owned Enterprise, Bank, Telco, Fintech, Payment Provider, Advocacy NGO, Think Tank, News Outlet, University, UN Agency. Use consistent terminology. |

## DPI Mandate & Role

### DPI_Mandate

| Field | Value |
|---|---|
| Variable ID | INST_006 |
| Definition | Whether institution has explicit DPI mandate in legislation/policy |
| Format | Categorical: Yes \| No \| Unclear |
| Data Collection Guidance | Search enabling laws, regulations, strategic plans for explicit mention of digital identity, digital payments, data exchange, or digital infrastructure responsibilities. Yes = clear mandate; No = no formal mandate; Unclear = ambiguous or emerging mandate. |

### DPI_Role

| Field | Value |
|---|---|
| Variable ID | INST_007 |
| Definition | Primary functional roles in DPI ecosystem |
| Format | Categorical : Policy Maker \| Regulator \| Implementer \| System Integrator \| Service Provider \| Funding Source \| Advocacy/Watchdog \| Research/Advisory \| Capacity Builder \| User Representative \| Technical Standards Setter \| Unknown |
| Data Collection Guidance | Review institutional functions, project portfolios, press releases, partnerships. Select ALL applicable roles. Separate with semicolon (;). Examples: 'Policy Maker;Regulator' or 'Service Provider;System Integrator'. |

### DPI_Focus_Areas

| Field | Value |
|---|---|
| Variable ID | INST_008 |
| Definition | Specific DPI domains where institution is active |
| Format | Categorical : Digital Identity \| Digital Payments \| Data Sharing/Exchange \| Connectivity Infrastructure \| Cybersecurity \| Data Protection/Privacy \| Digital Skills/Literacy \| Interoperability Standards \| Digital Public Services \| Other |
| Data Collection Guidance | Search reports, project descriptions, news articles about DPI work. Select ALL applicable areas. Separate with semicolon (;). Include 'Other' if significant work doesn't fit categories. |

### Legal_Authority

| Field | Value |
|---|---|
| Variable ID | INST_009 |
| Definition | Type of legal authority held by institution |
| Format | Categorical: Legislative Authority \| Regulatory Authority \| Policy Development Authority \| Operational Authority \| Advisory/Consultative \| Commercial/Market-Based \| None/Limited \| Unclear |
| Data Collection Guidance | Check enabling legislation, regulatory powers, licensing authority. Legislative = law-making power; Regulatory = rule-making/enforcement; Policy Development = strategy/guidance; Operational = implementation; Advisory = consultation only; Commercial = market participation; None/Limited = no formal authority. |

## Contact & Digital Presence

### Website_URL

| Field | Value |
|---|---|
| Variable ID | INST_010 |
| Definition | Official institutional website |
| Format | Text (URL) |
| Data Collection Guidance | Search Google for official website, verify authenticity. Use 'None' if no website exists, 'Unknown' if cannot be determined. Include protocol (https:// or http://). |

### Contact_Email

| Field | Value |
|---|---|
| Variable ID | INST_011 |
| Definition | General institutional contact email |
| Format | Text (Email) |
| Data Collection Guidance | Find on website contact page. Use general/info email, not personal addresses. Use 'None' if not publicly available. |

### Physical_Location

| Field | Value |
|---|---|
| Variable ID | INST_012 |
| Definition | City and country of headquarters |
| Format | Text |
| Data Collection Guidance | Find on website or company registry. Format: 'Nairobi, Kenya' or 'Cape Town, South Africa'. Use headquarters if multiple offices. |

## Influence Assessment

### Power_Level

| Field | Value |
|---|---|
| Variable ID | INST_013 |
| Definition | Overall ability to influence DPI outcomes |
| Format | Categorical : Very High \| High \| Medium \| Low \| Very Low |
| Data Collection Guidance | Consider authority, resources, network, expertise, track record. Very High = can veto/independently decide (minister, regulator); High = strong influence (director, influential advocate); Medium = moderate influence (program manager); Low = limited influence; Very Low = minimal influence. |

### Legitimacy

| Field | Value |
|---|---|
| Variable ID | INST_014 |
| Definition | Recognized right to be involved in DPI decisions |
| Format | Categorical : Very High \| High \| Medium \| Low \| Very Low |
| Data Collection Guidance | Assess formal mandate and recognized role. Very High = clear legal/constitutional mandate; High = strong regulatory/policy mandate; Medium = recognized stakeholder; Low = informal role; Very Low = limited/disputed legitimacy. |

### Decision_Authority

| Field | Value |
|---|---|
| Variable ID | INST_015 |
| Definition | Level of decision-making power in DPI domain |
| Format | Categorical : Full Authority \| Significant Authority \| Moderate Authority \| Limited Authority \| No Authority |
| Data Collection Guidance | Check governance documents, decision processes. Full = final decision-maker; Significant = most decisions within domain; Moderate = shared decision-making; Limited = advisory role; No Authority = observer/external. |

### Resource_Control

| Field | Value |
|---|---|
| Variable ID | INST_016 |
| Definition | Control over financial/technical resources for DPI |
| Format | Categorical : Full Control \| Significant Control \| Moderate Control \| Limited Control \| No Control |
| Data Collection Guidance | Check budget documents, funding announcements. Full = controls budget/resources; Significant = substantial allocation power; Moderate = some resource influence; Limited = minimal access; No Control = dependent on others. |

### Network_Strength

| Field | Value |
|---|---|
| Variable ID | INST_017 |
| Definition | Connectivity to other key DPI stakeholders |
| Format | Categorical : Very Strong \| Strong \| Moderate \| Weak \| Very Weak |
| Data Collection Guidance | Check forum participation, partnerships, board memberships, MOUs. Very Strong = central hub; Strong = well-connected to key actors; Moderate = connected to some actors; Weak = limited connections; Very Weak = isolated. |

### Technical_Expertise

| Field | Value |
|---|---|
| Variable ID | INST_018 |
| Definition | Level of technical knowledge in DPI domains |
| Format | Categorical : Expert \| Advanced \| Intermediate \| Basic \| Non-technical |
| Data Collection Guidance | Check publications, presentations, qualifications of staff, technical outputs. Expert = recognized technical authority; Advanced = strong technical knowledge; Intermediate = moderate understanding; Basic = limited knowledge; Non-technical = no technical expertise. |

## Engagement

### Interest_Level

| Field | Value |
|---|---|
| Variable ID | INST_019 |
| Definition | Degree of interest/priority given to DPI work |
| Format | Categorical : Very High \| High \| Medium \| Low \| Very Low |
| Data Collection Guidance | Check speeches, publications, project allocations, public statements. Very High = priority focus; High = significant interest; Medium = moderate interest; Low = peripheral interest; Very Low = minimal/no interest. |

### Current_Engagement

| Field | Value |
|---|---|
| Variable ID | INST_020 |
| Definition | Current level of active participation in DPI |
| Format | Categorical : Leading \| Active \| Involved \| Monitoring \| Inactive \| Unknown |
| Data Collection Guidance | Check recent activities, meeting minutes, project documents. Leading = actively driving initiatives; Active = regularly participating; Involved = occasionally participating; Monitoring = observing only; Inactive = no recent participation; Unknown = unclear. |

### DPI_Advocacy

| Field | Value |
|---|---|
| Variable ID | INST_021 |
| Definition | Public advocacy stance on DPI development |
| Format | Categorical : Strong Advocate \| Moderate Advocate \| Neutral \| Moderate Critic \| Strong Critic \| Unknown |
| Data Collection Guidance | Review public statements, policy positions, campaigns. Strong Advocate = actively promotes DPI; Moderate Advocate = generally supportive; Neutral = no clear position; Moderate Critic = raises concerns; Strong Critic = opposes DPI; Unknown = unclear. |

### Collaboration_Type

| Field | Value |
|---|---|
| Variable ID | INST_022 |
| Definition | Types of collaborative relationships with other stakeholders |
| Format | Categorical : Public-Private Partnership \| Co-governance \| Service Delivery Partnership \| Funding Relationship \| Research Collaboration \| Technical Advisory \| Regulator-Regulatee \| Multi-stakeholder Forum \| Informal Network \| None |
| Data Collection Guidance | Identify formal/informal collaboration mechanisms. Select ALL applicable. Separate with semicolon (;). Check partnership agreements, MOUs, forum participation, joint projects. |

### Engagement_Barriers

| Field | Value |
|---|---|
| Variable ID | INST_023 |
| Definition | Identified barriers to effective engagement |
| Format | Text |
| Data Collection Guidance | Document challenges from reports, interviews, news articles. Examples: funding constraints, technical capacity gaps, political interference, coordination failures, data access issues, regulatory uncertainty. Use 'None identified' if no barriers found. |

## Positioning

### Policy_Position

| Field | Value |
|---|---|
| Variable ID | INST_024 |
| Definition | Overall policy stance on DPI development approach |
| Format | Categorical : Strongly Supportive \| Supportive \| Neutral/Balanced \| Supportive (privacy concerns \| Supportive (equity concerns \| Supportive (governance concerns \| Critical \| Strongly Critical \| Unknown |
| Data Collection Guidance | Synthesize from policy documents, public statements, advocacy positions. Note specific concerns in parentheses (privacy, equity, governance) if generally supportive but with reservations. |

## Activity Tracking

### Recent_Activity

| Field | Value |
|---|---|
| Variable ID | INST_025 |
| Definition | Recent DPI-related activities, projects, statements (last 12-24 months) |
| Format | Text |
| Data Collection Guidance | Document recent activities with brief description and date/timeframe. Format: 'Activity description - Month Year; Another activity - Month Year'. Check press releases, annual reports, news coverage, project announcements. |

## Funding

### Funding_Source

| Field | Value |
|---|---|
| Variable ID | INST_026 |
| Definition | Primary sources of institutional funding |
| Format | Categorical : Government Budget \| Private Sector \| Donor/Development Partner \| Membership Fees \| Revenue Generation \| Mixed Sources \| Unknown |
| Data Collection Guidance | Check annual reports, financial statements, about pages. Select ALL significant sources (>10% of budget). Separate with semicolon (;). Mixed Sources = diverse funding without clear dominance. |

## Participation

### Multi_Stakeholder_Forums

| Field | Value |
|---|---|
| Variable ID | INST_027 |
| Definition | Participation in multi-stakeholder DPI forums/processes |
| Format | Categorical : Active Participant \| Occasional Participant \| Involved \| Not Participating \| Unknown |
| Data Collection Guidance | Check participation in national DPI forums, working groups, consultations, regional forums. Active = regular participation with substantive input; Occasional = attends but limited input; Involved = observes or minimal participation; Not Participating = absent from multi-stakeholder processes. |

## Data Provenance

### Data_Source

| Field | Value |
|---|---|
| Variable ID | INST_028 |
| Definition | Sources consulted for institutional data |
| Format | Text |
| Data Collection Guidance | Document ALL sources used. Format: 'Source description \| URL \| YYYY-MM-DD'. Separate multiple sources with semicolon (;). Example: 'Institution website \| https://example.org \| 2026-03-09; Annual report \| https://example.org/report.pdf \| 2025-12-31'. |

### Data_Collection_Date

| Field | Value |
|---|---|
| Variable ID | INST_029 |
| Definition | Date when data was collected |
| Format | Date |
| Data Collection Guidance | Use ISO 8601 format (YYYY-MM-DD). Record date when data collection was completed for this institution. |

### Data_Collector

| Field | Value |
|---|---|
| Variable ID | INST_030 |
| Definition | Person/team who collected the data |
| Format | Text |
| Data Collection Guidance | Record researcher name or initials for quality control and follow-up. Use consistent format within dataset. |
