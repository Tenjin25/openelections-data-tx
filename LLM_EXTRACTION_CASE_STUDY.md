# Testing LLM Models for Texas Precinct Data Extraction

Testing whether large language models could accurately extract precinct-level election results from PDF files without manual data entry or traditional OCR software.

## The Challenge

Texas has 254 counties, each producing precinct-level election results in different formats. Many counties provide results only as image PDFs, which require either manual data entry or optical character recognition to convert into usable CSV files. Both approaches have problems: data entry is expensive and error-prone, while commercial OCR software struggles with marked-up documents, multi-column layouts, and inconsistent formatting.

We tested four LLM models on eight Texas counties from the 2024 general election to measure extraction accuracy and identify common failure patterns.

## Test Design

We selected eight counties that represented different PDF styles and complexity levels:

- **Cottle County**: 4 precincts, simple layout
- **Foard County**: 4 precincts, includes Over/Under votes
- **Jones County**: 4 precincts, multiple judicial races
- **Limestone County**: 21 precincts, two-column layout with dotted leaders
- **Lynn County**: 8 precincts, standard format
- **Panola County**: 19 precincts, many minor party candidates
- **San Saba County**: 6 precincts with split precincts (2A, 2B, etc.)
- **Scurry County**: 11 precincts, clean format

These eight counties represent about 3% of Texas's 254 counties but offered different challenges in formatting and complexity.

The extraction tool used Python's `llm` library to send PDFs to each model with a prompt containing:
- The target CSV column structure (county, precinct, office, district, party, candidate, votes, absentee, early_voting, election_day)
- Specific formatting rules for office names (e.g., "Justice, Supreme Court" not "Supreme Court Justice")
- 40+ example rows showing proper formatting
- Instructions to include all candidates, even those with 0 votes
- Maximum token limit of 32,000 to prevent truncation

A comparison script validated the extracted data against reference files that had been manually verified, checking vote counts, candidate names, office names, and precinct identifiers.

## Models Tested

We tested four models:

1. **Claude Haiku 4.5** (Anthropic) - Fast, lower cost
2. **Claude Sonnet 4.5** (Anthropic) - Slower, higher capability
3. **Gemini 3 Flash** (Google) - Fast, efficient
4. **Gemini 2.5 Pro** (Google) - Most capable

## Results

### Overall Accuracy

| Model | Votes Checked | Accuracy | Total Rows Generated | Reference Rows |
|-------|---------------|----------|---------------------|----------------|
| Gemini 2.5 Pro | 1,512 | 82.5% | 3,131 | 3,936 |
| Claude Haiku 4.5 | 2,495 | 77.8% | 3,697 | 3,936 |
| Gemini 3 Flash | 2,049 | 70.5% | 3,131 | 3,936 |
| Claude Sonnet 4.5 | 1,445 | 60.8% | 3,331 | 3,936 |

All models correctly identified precinct names with zero precinct naming errors across 2,495 total vote records.

### Performance by County

**Perfect or Near-Perfect Extraction (95-100% accuracy)**

- **Scurry County**: Claude Haiku achieved 100% accuracy across all 11 precincts and 321 votes checked. Gemini 2.5 Pro and Gemini 3 Flash also scored 100%.
- **Limestone County**: Claude Haiku achieved 99.9% accuracy (1 error in 870 votes). Gemini 2.5 Pro scored 99.7%, both near-perfect on this 21-precinct county with a challenging two-column layout.
- **Cottle County**: Gemini 2.5 Pro and Gemini 3 Flash both achieved 100% accuracy.
- **San Saba County**: Gemini 2.5 Pro and Gemini 3 Flash both achieved 100% accuracy. Claude Haiku scored 91.7%, missing only write-in candidates with 0 votes.

**Moderate Accuracy (70-90%)**

- **Foard County**: Claude Haiku achieved 84.9% accuracy. Main errors were missing "Over Votes" and "Under Votes" rows.

**Lower Accuracy (below 70%)**

Models struggled with three counties:

- **Jones, Lynn, Foard**: Missing Supreme Court justice races and Over/Under vote rows
- **Panola**: Claude Haiku scored only 16.2% due to incorrect vote counts and missing minor party candidates with 0 votes

### Common Error Patterns

1. **Missing Over/Under Votes**: All models frequently omitted "Over Votes" and "Under Votes" rows, which typically show 0 and small numbers respectively.

2. **Missing Zero-Vote Candidates**: Models often skipped candidates who received 0 votes, particularly minor party candidates. Panola County had six candidates (Shiva Ayyadurai, Jessie Cuellar, Claudia De La Cruz, Cherunda Fox, Peter Sonski, Cornel West) who received 0 votes and were omitted by Claude Haiku.

3. **Incomplete Extraction**: Claude Sonnet and Gemini models generated fewer total rows (3,131-3,331) compared to the reference (3,936), suggesting they missed entire races or candidates.

4. **Vote Count Errors**: Panola County showed systematic vote count errors with Claude Haiku, such as reading 233 votes as 227, suggesting either PDF quality issues or OCR errors.

5. **Missing Judicial Races**: Jones, Lynn, and Cottle counties showed missing Supreme Court justice races, which may indicate the models stopped extracting before reaching those races in the PDF.

## Technical Details

The extraction script (`pdf_extractor.py`) uses a 32,000 token limit, which was necessary to prevent truncation of results. Initial testing with default token limits resulted in incomplete extractions that stopped after 10-15 precincts.

The prompt engineering required specific formatting rules because Texas uses commas in office names ("Justice, Supreme Court") and has complex district designations ("Place 2", "Pl 6", "Pct 1"). Without explicit examples, models would format these incorrectly.

The comparison script (`compare_extraction.py`) normalizes precinct names (treating "Precinct 101" and "101" as identical) and uses substring matching for candidate names (so "Donald J. Trump" matches "Donald J. Trump/JD Vance"). This accommodation was necessary because some PDFs include running mates while others don't.

## Validation Process

The comparison process sampled vote counts rather than checking every value. It selected a subset of races and candidates to verify, which explains why "votes checked" is lower than total rows. This sampling approach catches systematic errors while being computationally efficient.

The validation identified errors in three categories:
- **Vote mismatches**: Extracted vote count differs from reference
- **Missing candidates**: Candidate appears in reference but not extraction
- **Precinct name errors**: Precinct identifier doesn't match (0 errors across all tests)

## Conclusions

LLM-based extraction works well for clean, well-formatted PDFs. Gemini 2.5 Pro achieved the highest accuracy (82.5%), while Claude Haiku 4.5 checked the most votes (2,495) with 77.8% accuracy.

The main limitations are:

1. **Zero-value rows**: Models need explicit instructions to include rows with 0 votes
2. **Completeness**: Models may not extract all races, particularly those later in the document
3. **Vote accuracy**: Some PDFs produce systematic OCR errors that may indicate scan quality issues

For production use, this suggests:
- Use Gemini 2.5 Pro or Claude Haiku 4.5 as the primary extraction model
- Implement automated validation against county-level totals to catch missing races
- Add explicit checks for expected race counts and candidate counts
- Consider extracting twice with different models and comparing results for critical data

The 77-82% accuracy achieved on diverse county formats suggests LLM extraction is viable for the majority of Texas counties, though manual review remains necessary for counties with unusual formats or poor PDF quality.
