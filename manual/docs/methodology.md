# Data collection methodology

Is it possible to collect reasonably accurate, comparable data for 54 countries on a limited budget? This was the challenge taken on for this exercise.

Using the methodology outlined below data for all 54 African countries has been collected for:  
- ICT Infrastructure  
- Data Exchange  
- Digital Identity  
- Digital Payments  
- Registries  

## The changing technology landscape.

The use of AI-powered search engines combined with Large Language Model (LLM) analysis is a new, fast-moving discipline that internet-based desk research can no longer ignore. There have been very legitimate concerns about 'hallucinations' as well as the difficulty in producing replicable results. These are, however not insurmountable.

<a href="https://www.perplexity.ai/help-center/en/articles/10352155-what-is-perplexity" target="_blank" rel="noopener noreferrer">Perplexity</a> was chosen as the engine to conduct this research. Unlike its better known competitors such as ChatGPT it isn't itself a LLM. It is an AI-powered, real-time search engine that, properly managed, produces well-cited, verifiable results.

Working in this field requires the mastery of two elements. Firstly one needs to master prompt engineering. This is the art and science of structuring, designing, and refining inputs (prompts) to guide Large Language Models (LLMs) to produce accurate, relevant, and high-quality outputs. Perplexity's own guidance recommends that every effective prompt contain four core elements: a clear unambiguous instruction (what you want done), context (background that helps Perplexity understand the task), relevant keywords (to focus the search on the right details), and a specified output format. 

Secondly, one needs to understand the sweet spot between depth and breadth: the broader the query the shallower the investigation. For this research it became clear that prompting for a single topic (eg digital identity) in a single country with a narrowly defined set of target outputs was the most effective approach. Manually running 54 queries, each taking approximately 10 minutes, is a challenge.

In February 2026 <a href="https://www.perplexity.ai/hub/blog/introducing-perplexity-computer" target="_blank" rel="noopener noreferrer">Perplexity Computer</a> was launched. It operates as an orchestration layer sitting above multiple foundation models. When you submit a query, the system does not send it directly to a single model. Instead, a meta-router analyses the request, classifies it by type and complexity, and dispatches it to the model or combination of models most likely to produce an accurate, well-grounded response.

The orchestration layer manages three core functions. First, it performs task classification, determining whether a query requires web search, document analysis, code generation, mathematical reasoning, or creative writing. Second, it handles model selection, matching the classified task to the model with the strongest performance benchmarks for that category. Third, it manages result synthesis, combining outputs from multiple sub-agents when a complex query requires different types of processing at different stages.

This meant a single continental query could be distributed simultaneously to 54 independent agents, and once the search results were in, Claude Opus 4.6 was deployed to distil them into the required structured output.

## A standardised approach

In this fast-moving environment it is impossible to be prescriptive about a precise methodology that will be suitable in six-month's time. Suffice to say there are two essential elements:

- Well constructed metadata. (See the navigation bar for the metadata deployed)
- Clear instructions (See below for an example)


## Example of instructions
Similar instructions were issued for all five of the data collection processes which used Perplexity 

**Purpose**

This task is part of the data collection exercise for mapping progress with digital public infrastructures in Africa. The aim of this task is to collect comparable indicators on registries for all 54 African countries.

**Approach**

The overriding priority is to produce comprehensive, accurate and comparable evidence. The most appropriate model should be selected to achieve the best results. The results will be fed into a dashboard where the data will be represented on a heatmap of Africa. It is therefore critical that the calculation of the values specified in metadata.csv are followed consistently.

**Task**

1. For each country in countries.csv use the content of registry-metadata.csv to collect data on 44 variables and produce an output defined in the Output section below.
2. If no credible evidence is found after thorough searching, set Value to 0, Year to blank, and Comments to a brief explanation of what was searched and why no evidence was found.
3. Validate each file to ensure that it contains 44 data rows and that the Variable Id matches that in registry-metadata.csv.
4. Output a validation.csv file containing details of errors detected.
5. Once complete consolidate all countries - excluding those that failed validation - into a single file africa-registries.csv maintaining the same column formats.


**Inputs**

Three files are attached:

- registry-instructions.md (these instructions)
- registry-metadata.csv (defining the data to be collected as well as data collection and data formatting guidelines)
- countries.csv (a list of countries to be processed)

**Output**

Each country's data should be output to a csv file named \[country].csv (Where country is the name in lower case with hyphens in the place of spaces)

All CSV files must be encoded as UTF-8 with BOM (byte order mark) to ensure correct rendering of non-ASCII characters (e.g. French, Portuguese) in Excel.

The file should contain the following columns

- Country (ISO-3 country code)
- Chapter (from registry-metadata.csv)
- Section (from registry-metadata.csv)
- Variable Name (from registry-metadata.csv)
- Value (The value calculated. Value must be an integer matching the scale in the Format column. NB that the value "0" is used to represent "Unknown" or Not available/NA throughout the dataset)
- Year (Year should reflect the most recent year for which the evidence applies. If the value is 0, leave Year blank. If evidence spans multiple years, use the most recent.)
- Comments (Comments must include the specific evidence that justifies the numeric value chosen. For values above 1, cite the system name, programme, policy document, etc that demonstrates the capability exists.)
- Variable Id (from metadata.csv)
- Sort (from registry-metadata.csv)
- Source urls (Source urls must contain at least one valid URL for any Value that is not 0. Multiple URLs should be semicolon-delimited with no spaces.)