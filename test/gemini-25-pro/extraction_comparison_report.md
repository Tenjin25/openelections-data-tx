# PDF Extraction Comparison Report

## Overview
We extracted election results from 8 county PDFs using Google's Gemini 2.5 Pro model and compared them against the reference data in 2024/counties/.

## Summary

| County | Precincts | Votes Checked | Vote Accuracy | Precinct Errors |
|--------|-----------|---------------|---------------|----------------|
| Cottle | 4 | 42 | 100.0% | 0 |
| Foard | 4 | 134 | 44.8% | 0 |
| Jones | 4 | 148 | 53.4% | 0 |
| Limestone | 21 | 387 | 99.7% | 0 |
| Lynn | 8 | 168 | 51.2% | 0 |
| Panola | 19 | 381 | 89.8% | 0 |
| San Saba | 6 | 72 | 100.0% | 0 |
| Scurry | 11 | 180 | 100.0% | 0 |

**Overall: 1,512 votes checked, 82.5% accuracy, 0 precinct name errors**

## County Details

### Cottle County

4 precincts, 42 votes checked across 17 races.

✓ **Vote accuracy: 100%** - All vote counts matched perfectly.

✓ **All precinct names correct**

### Foard County

4 precincts, 134 votes checked across 20 races.

✗ **Vote accuracy: 44.8%** - 74 errors found:

- Precinct 101, Railroad Commissioner, Over Votes: Reference=0, Extracted=MISSING
- Precinct 101, Railroad Commissioner, Under Votes: Reference=14, Extracted=MISSING
- Precinct 101, Presiding Judge, Court of Criminal Appeals, Over Votes: Reference=0, Extracted=MISSING
- Precinct 101, Presiding Judge, Court of Criminal Appeals, Under Votes: Reference=11, Extracted=MISSING
- Precinct 101, Member, State Board of Education, Over Votes: Reference=0, Extracted=MISSING
- Precinct 101, Member, State Board of Education, Under Votes: Reference=12, Extracted=MISSING
- Precinct 101, State Representative, Over Votes: Reference=0, Extracted=MISSING
- Precinct 101, State Representative, Under Votes: Reference=10, Extracted=MISSING
- Precinct 101, District Attorney, Jon Whitsitt: Reference=94, Extracted=MISSING
- Precinct 101, District Attorney, Over Votes: Reference=0, Extracted=MISSING

...and 64 more errors

✓ **All precinct names correct**

### Jones County

4 precincts, 148 votes checked across 23 races.

✗ **Vote accuracy: 53.4%** - 69 errors found:

- Precinct 1, President, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, President, Under Votes: Reference=8, Extracted=MISSING
- Precinct 1, Railroad Commissioner, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, Railroad Commissioner, Under Votes: Reference=61, Extracted=MISSING
- Precinct 1, State Representative, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, State Representative, Under Votes: Reference=60, Extracted=MISSING
- Precinct 1, County Attorney, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, County Attorney, Under Votes: Reference=214, Extracted=MISSING
- Precinct 1, Sheriff, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, Sheriff, Under Votes: Reference=213, Extracted=MISSING

...and 59 more errors

✓ **All precinct names correct**

### Limestone County

21 precincts, 387 votes checked across 19 races.

✗ **Vote accuracy: 99.7%** - 1 errors found:

- Precinct 401, Railroad Commissioner, Hawk, Dunlap: Reference=9, Extracted=MISSING

✓ **All precinct names correct**

### Lynn County

8 precincts, 168 votes checked across 19 races.

✗ **Vote accuracy: 51.2%** - 82 errors found:

- Precinct 1, Railroad Commissioner, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, Railroad Commissioner, Under Votes: Reference=25, Extracted=MISSING
- Precinct 1, State Representative, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, State Representative, Under Votes: Reference=74, Extracted=MISSING
- Precinct 1, County Attorney, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, County Attorney, Under Votes: Reference=56, Extracted=MISSING
- Precinct 1, Sheriff, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, Sheriff, Under Votes: Reference=59, Extracted=MISSING
- Precinct 1, County Tax Assessor-Collector, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, County Tax Assessor-Collector, Under Votes: Reference=59, Extracted=MISSING

...and 72 more errors

✓ **All precinct names correct**

### Panola County

19 precincts, 381 votes checked across 20 races.

✗ **Vote accuracy: 89.8%** - 39 errors found:

- 7, President, Peter Sonski: Reference=0, Extracted=2
- 18, President, Jill Stein: Reference=0, Extracted=1
- 27, President, Jill Stein: Reference=0, Extracted=1
- 28, President, Jill Stein: Reference=4, Extracted=1
- 28, President, Peter Sonski: Reference=2, Extracted=0
- 5, Railroad Commissioner, Eddie Espinoza: Reference=2, Extracted=0
- 7, Railroad Commissioner, Eddie Espinoza: Reference=5, Extracted=0
- 9, Railroad Commissioner, Eddie Espinoza: Reference=6, Extracted=0
- 10, Railroad Commissioner, Eddie Espinoza: Reference=1, Extracted=0
- 13, Railroad Commissioner, Eddie Espinoza: Reference=3, Extracted=1

...and 29 more errors

✓ **All precinct names correct**

### San Saba County

6 precincts, 72 votes checked across 26 races.

✓ **Vote accuracy: 100%** - All vote counts matched perfectly.

✓ **All precinct names correct**

### Scurry County

11 precincts, 180 votes checked across 31 races.

✓ **Vote accuracy: 100%** - All vote counts matched perfectly.

✓ **All precinct names correct**

## Conclusion

The tool achieved 82.5% accuracy overall. All precinct names were extracted correctly.
