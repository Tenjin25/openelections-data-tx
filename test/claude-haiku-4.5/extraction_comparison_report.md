# PDF Extraction Comparison Report

## Overview
We extracted election results from 8 county PDFs using Anthropic's Claude 4.5 Haiku model and compared them against the reference data in 2024/counties/.

## Summary

| County | Precincts | Votes Checked | Vote Accuracy | Precinct Errors |
|--------|-----------|---------------|---------------|----------------|
| Cottle | 4 | 106 | 64.2% | 0 |
| Foard | 4 | 146 | 84.9% | 0 |
| Jones | 4 | 240 | 68.3% | 0 |
| Limestone | 21 | 870 | 99.9% | 0 |
| Lynn | 8 | 376 | 71.5% | 0 |
| Panola | 19 | 364 | 16.2% | 0 |
| San Saba | 6 | 72 | 91.7% | 0 |
| Scurry | 11 | 321 | 100.0% | 0 |

**Overall: 2,495 votes checked, 77.8% accuracy, 0 precinct name errors**

## County Details

### Cottle County

4 precincts, 106 votes checked across 17 races.

✗ **Vote accuracy: 64.2%** - 38 errors found:

- Precinct 101, Justice, Supreme Court, Jimmy Blacklock: Reference=168, Extracted=MISSING
- Precinct 101, Justice, Supreme Court, DaSean Jones: Reference=15, Extracted=MISSING
- Precinct 101, Justice, Supreme Court, John Devine: Reference=169, Extracted=MISSING
- Precinct 101, Justice, Supreme Court, Christine Vinh Weems: Reference=16, Extracted=MISSING
- Precinct 101, Justice, Supreme Court, Jane Bland: Reference=164, Extracted=MISSING
- Precinct 101, Justice, Supreme Court, Bonnie Lee Goldstein: Reference=16, Extracted=MISSING
- Precinct 101, Justice, Supreme Court, J. David Roberson: Reference=6, Extracted=MISSING
- Precinct 101, State Representative, James B Frank: Reference=169, Extracted=MISSING
- Precinct 101, State Representative, Walter Coppage: Reference=15, Extracted=MISSING
- Precinct 101, County Commissioner, Arty Roy Tucker: Reference=173, Extracted=MISSING

...and 28 more errors

✓ **All precinct names correct**

### Foard County

4 precincts, 146 votes checked across 20 races.

✗ **Vote accuracy: 84.9%** - 22 errors found:

- Precinct 101, Member, State Board of Education, Over Votes: Reference=0, Extracted=MISSING
- Precinct 101, Member, State Board of Education, Under Votes: Reference=12, Extracted=MISSING
- Precinct 101, State Representative, Over Votes: Reference=0, Extracted=MISSING
- Precinct 101, State Representative, Under Votes: Reference=10, Extracted=MISSING
- Precinct 101, County Commissioner, Matthew Tamplen: Reference=102, Extracted=MISSING
- Precinct 101, County Commissioner, Over Votes: Reference=0, Extracted=MISSING
- Precinct 101, County Commissioner, Under Votes: Reference=19, Extracted=MISSING
- Precinct 201, Member, State Board of Education, Over Votes: Reference=0, Extracted=MISSING
- Precinct 201, Member, State Board of Education, Under Votes: Reference=23, Extracted=MISSING
- Precinct 201, State Representative, Over Votes: Reference=0, Extracted=MISSING

...and 12 more errors

✓ **All precinct names correct**

### Jones County

4 precincts, 240 votes checked across 23 races.

✗ **Vote accuracy: 68.3%** - 76 errors found:

- Precinct 1, Justice, Supreme Court, Jimmy Blacklock: Reference=949, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, DaSean Jones: Reference=203, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, Under Votes: Reference=62, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, John Devine: Reference=946, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, Christine Vinh Weems: Reference=207, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, Under Votes: Reference=61, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, Jane Bland: Reference=929, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, Bonnie Lee Goldstein: Reference=200, Extracted=MISSING

...and 66 more errors

✓ **All precinct names correct**

### Limestone County

21 precincts, 870 votes checked across 19 races.

✗ **Vote accuracy: 99.9%** - 1 errors found:

- Precinct 401, Railroad Commissioner, Hawk, Dunlap: Reference=9, Extracted=MISSING

✓ **All precinct names correct**

### Lynn County

8 precincts, 376 votes checked across 19 races.

✗ **Vote accuracy: 71.5%** - 107 errors found:

- Precinct 1, Justice, Supreme Court, Jimmy Blacklock: Reference=224, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, DaSean Jones: Reference=84, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, Under Votes: Reference=33, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, John Devine: Reference=224, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, Christine Vinh Weems: Reference=85, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, Under Votes: Reference=32, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, Jane Bland: Reference=222, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, Bonnie Lee Goldstein: Reference=78, Extracted=MISSING

...and 97 more errors

✓ **All precinct names correct**

### Panola County

19 precincts, 364 votes checked across 20 races.

✗ **Vote accuracy: 16.2%** - 305 errors found:

- 7, Registered Voters, : Reference=898, Extracted=858
- 1, President, Kamala D. Harris: Reference=233, Extracted=227
- 1, President, Chase Oliver: Reference=4, Extracted=10
- 1, President, Shiva Ayyadurai: Reference=0, Extracted=MISSING
- 1, President, Jessie Cuellar: Reference=0, Extracted=MISSING
- 1, President, Claudia De La Cruz: Reference=0, Extracted=MISSING
- 1, President, Cherunda Fox: Reference=0, Extracted=MISSING
- 1, President, Peter Sonski: Reference=0, Extracted=MISSING
- 1, President, Cornel West: Reference=0, Extracted=MISSING
- 2, President, Kamala D. Harris: Reference=293, Extracted=287

...and 295 more errors

✓ **All precinct names correct**

### San Saba County

6 precincts, 72 votes checked across 26 races.

✗ **Vote accuracy: 91.7%** - 6 errors found:

- Precinct 1, Railroad Commissioner, Write-ins: Reference=0, Extracted=MISSING
- Precinct 2A, Railroad Commissioner, Write-ins: Reference=0, Extracted=MISSING
- Precinct 2B, Railroad Commissioner, Write-ins: Reference=0, Extracted=MISSING
- Precinct 3A, Railroad Commissioner, Write-ins: Reference=0, Extracted=MISSING
- Precinct 3B, Railroad Commissioner, Write-ins: Reference=0, Extracted=MISSING
- Precinct 4, Railroad Commissioner, Write-ins: Reference=0, Extracted=MISSING

✓ **All precinct names correct**

### Scurry County

11 precincts, 321 votes checked across 31 races.

✓ **Vote accuracy: 100%** - All vote counts matched perfectly.

✓ **All precinct names correct**

## Conclusion

The tool achieved 77.8% accuracy overall. All precinct names were extracted correctly.
