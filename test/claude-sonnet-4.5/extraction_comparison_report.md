# PDF Extraction Comparison Report

## Overview
We extracted election results from 8 county PDFs using Anthropic's Claude 4.5 Sonnet model and compared them against the reference data in 2024/counties/.

## Summary

| County | Precincts | Votes Checked | Vote Accuracy | Precinct Errors |
|--------|-----------|---------------|---------------|----------------|
| Cottle | 4 | 50 | 84.0% | 0 |
| Foard | 4 | 98 | 40.8% | 0 |
| Jones | 4 | 120 | 45.0% | 0 |
| Limestone | 21 | 387 | 94.3% | 0 |
| Lynn | 8 | 182 | 47.3% | 0 |
| Panola | 19 | 363 | 28.7% | 0 |
| San Saba | 6 | 72 | 100.0% | 0 |
| Scurry | 11 | 173 | 67.1% | 0 |

**Overall: 1,445 votes checked, 60.8% accuracy, 0 precinct name errors**

## County Details

### Cottle County

4 precincts, 50 votes checked across 17 races.

✗ **Vote accuracy: 84.0%** - 8 errors found:

- Precinct 101, Dist Judge, Jennifer A. Habert: Reference=167, Extracted=MISSING
- Precinct 101, Dist Attorney, Hunter Brooks: Reference=165, Extracted=MISSING
- Precinct 201, Dist Judge, Jennifer A. Habert: Reference=158, Extracted=MISSING
- Precinct 201, Dist Attorney, Hunter Brooks: Reference=148, Extracted=MISSING
- Precinct 301, Dist Judge, Jennifer A. Habert: Reference=105, Extracted=MISSING
- Precinct 301, Dist Attorney, Hunter Brooks: Reference=99, Extracted=MISSING
- Precinct 401, Dist Judge, Jennifer A. Habert: Reference=109, Extracted=MISSING
- Precinct 401, Dist Attorney, Hunter Brooks: Reference=107, Extracted=MISSING

✓ **All precinct names correct**

### Foard County

4 precincts, 98 votes checked across 20 races.

✗ **Vote accuracy: 40.8%** - 58 errors found:

- Precinct 101, Railroad Commissioner, Over Votes: Reference=0, Extracted=MISSING
- Precinct 101, Railroad Commissioner, Under Votes: Reference=14, Extracted=MISSING
- Precinct 101, State Representative, Over Votes: Reference=0, Extracted=MISSING
- Precinct 101, State Representative, Under Votes: Reference=10, Extracted=MISSING
- Precinct 101, District Attorney, Jon Whitsitt: Reference=94, Extracted=MISSING
- Precinct 101, District Attorney, Over Votes: Reference=0, Extracted=MISSING
- Precinct 101, District Attorney, Under Votes: Reference=27, Extracted=MISSING
- Precinct 101, County Attorney, Over Votes: Reference=0, Extracted=MISSING
- Precinct 101, County Attorney, Under Votes: Reference=19, Extracted=MISSING
- Precinct 101, Sheriff / County Tax Assessor-Collector, Over Votes: Reference=0, Extracted=MISSING

...and 48 more errors

✓ **All precinct names correct**

### Jones County

4 precincts, 120 votes checked across 23 races.

✗ **Vote accuracy: 45.0%** - 66 errors found:

- Precinct 1, Railroad Commissioner, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, Railroad Commissioner, Under Votes: Reference=61, Extracted=MISSING
- Precinct 1, State Representative, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, State Representative, Under Votes: Reference=60, Extracted=MISSING
- Precinct 1, County Attorney, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, County Attorney, Under Votes: Reference=214, Extracted=MISSING
- Precinct 1, Sheriff, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, Sheriff, Under Votes: Reference=213, Extracted=MISSING
- Precinct 1, County Tax Assessor-Collector, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, County Tax Assessor-Collector, Under Votes: Reference=215, Extracted=MISSING

...and 56 more errors

✓ **All precinct names correct**

### Limestone County

21 precincts, 387 votes checked across 19 races.

✗ **Vote accuracy: 94.3%** - 22 errors found:

- Precinct 101, Constable, Scott Smith: Reference=937, Extracted=MISSING
- Precinct 102, Constable, Scott Smith: Reference=438, Extracted=MISSING
- Precinct 103, Constable, Scott Smith: Reference=466, Extracted=MISSING
- Precinct 104, Constable, Scott Smith: Reference=531, Extracted=MISSING
- Precinct 201, Constable, Michael Carter: Reference=236, Extracted=MISSING
- Precinct 202, Constable, Michael Carter: Reference=241, Extracted=MISSING
- Precinct 203, Constable, Michael Carter: Reference=58, Extracted=MISSING
- Precinct 204, Constable, Michael Carter: Reference=311, Extracted=MISSING
- Precinct 205, Constable, Michael Carter: Reference=263, Extracted=MISSING
- Precinct 206, Constable, Michael Carter: Reference=266, Extracted=MISSING

...and 12 more errors

✓ **All precinct names correct**

### Lynn County

8 precincts, 182 votes checked across 19 races.

✗ **Vote accuracy: 47.3%** - 96 errors found:

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

...and 86 more errors

✓ **All precinct names correct**

### Panola County

19 precincts, 363 votes checked across 20 races.

✗ **Vote accuracy: 28.7%** - 259 errors found:

- 1, President, Donald J. Trump: Reference=1021, Extracted=787
- 1, President, Kamala D. Harris: Reference=233, Extracted=230
- 1, President, Chase Oliver: Reference=4, Extracted=0
- 1, President, Jill Stein: Reference=4, Extracted=0
- 1, President, Shiva Ayyadurai: Reference=0, Extracted=MISSING
- 1, President, Jessie Cuellar: Reference=0, Extracted=MISSING
- 1, President, Claudia De La Cruz: Reference=0, Extracted=MISSING
- 1, President, Cherunda Fox: Reference=0, Extracted=MISSING
- 1, President, Peter Sonski: Reference=0, Extracted=MISSING
- 1, President, Cornel West: Reference=0, Extracted=MISSING

...and 249 more errors

✓ **All precinct names correct**

### San Saba County

6 precincts, 72 votes checked across 26 races.

✓ **Vote accuracy: 100%** - All vote counts matched perfectly.

✓ **All precinct names correct**

### Scurry County

11 precincts, 173 votes checked across 31 races.

✗ **Vote accuracy: 67.1%** - 57 errors found:

- Precinct 5, Railroad Commissioner, Write-ins: Reference=0, Extracted=MISSING
- Precinct 6, Railroad Commissioner, Write-ins: Reference=0, Extracted=MISSING
- Precinct 7, Railroad Commissioner, Write-ins: Reference=1, Extracted=MISSING
- Precinct 8, Railroad Commissioner, Write-ins: Reference=0, Extracted=MISSING
- Precinct 9, Railroad Commissioner, Write-ins: Reference=0, Extracted=MISSING
- Precinct 9, Board of Trustee Ira ISD, Rance Dunn: Reference=235, Extracted=MISSING
- Precinct 9, Board of Trustee Ira ISD, Justin Taylor: Reference=94, Extracted=MISSING
- Precinct 9, Board of Trustee Ira ISD, David Kirk: Reference=136, Extracted=MISSING
- Precinct 9, Board of Trustee Ira ISD, J.J. Caswell: Reference=141, Extracted=MISSING
- Precinct 9, Board of Trustee Ira ISD, Russell Wall: Reference=169, Extracted=MISSING

...and 47 more errors

✓ **All precinct names correct**

## Conclusion

The tool achieved 60.8% accuracy overall. All precinct names were extracted correctly.
