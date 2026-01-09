# PDF Extraction Comparison Report

## Overview
We extracted election results from 8 county PDFs using Google's Gemini 3 Flash model and compared them against the reference data in 2024/counties/.

## Summary

| County | Precincts | Votes Checked | Vote Accuracy | Precinct Errors |
|--------|-----------|---------------|---------------|----------------|
| Cottle | 4 | 66 | 100.0% | 0 |
| Foard | 4 | 122 | 45.9% | 0 |
| Jones | 4 | 136 | 55.1% | 0 |
| Limestone | 21 | 744 | 88.4% | 0 |
| Lynn | 8 | 328 | 38.4% | 0 |
| Panola | 19 | 380 | 50.3% | 0 |
| San Saba | 6 | 108 | 100.0% | 0 |
| Scurry | 11 | 165 | 100.0% | 0 |

**Overall: 2,049 votes checked, 70.5% accuracy, 0 precinct name errors**

## County Details

### Cottle County

4 precincts, 66 votes checked across 17 races.

✓ **Vote accuracy: 100%** - All vote counts matched perfectly.

✓ **All precinct names correct**

### Foard County

4 precincts, 122 votes checked across 20 races.

✗ **Vote accuracy: 45.9%** - 66 errors found:

- Precinct 101, President, Over Votes: Reference=0, Extracted=MISSING
- Precinct 101, President, Under Votes: Reference=2, Extracted=MISSING
- Precinct 101, Railroad Commissioner, Over Votes: Reference=0, Extracted=MISSING
- Precinct 101, Railroad Commissioner, Under Votes: Reference=14, Extracted=MISSING
- Precinct 101, State Representative, Over Votes: Reference=0, Extracted=MISSING
- Precinct 101, State Representative, Under Votes: Reference=10, Extracted=MISSING
- Precinct 101, District Attorney, Jon Whitsitt: Reference=94, Extracted=MISSING
- Precinct 101, District Attorney, Over Votes: Reference=0, Extracted=MISSING
- Precinct 101, District Attorney, Under Votes: Reference=27, Extracted=MISSING
- Precinct 101, County Attorney, Over Votes: Reference=0, Extracted=MISSING

...and 56 more errors

✓ **All precinct names correct**

### Jones County

4 precincts, 136 votes checked across 23 races.

✗ **Vote accuracy: 55.1%** - 61 errors found:

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

...and 51 more errors

✓ **All precinct names correct**

### Limestone County

21 precincts, 744 votes checked across 19 races.

✗ **Vote accuracy: 88.4%** - 86 errors found:

- Precinct 101, President, Donald J. Trump/JD Vance: Reference=879, Extracted=MISSING
- Precinct 101, President, Kamala D. Harris/Tim Walz: Reference=271, Extracted=MISSING
- Precinct 101, President, Chase Oliver/Mike ter Maat: Reference=1, Extracted=MISSING
- Precinct 101, President, Jill Stein/Rudolph Ware: Reference=4, Extracted=MISSING
- Precinct 102, President, Donald J. Trump/JD Vance: Reference=454, Extracted=MISSING
- Precinct 102, President, Kamala D. Harris/Tim Walz: Reference=42, Extracted=MISSING
- Precinct 102, President, Chase Oliver/Mike ter Maat: Reference=3, Extracted=MISSING
- Precinct 102, President, Jill Stein/Rudolph Ware: Reference=0, Extracted=MISSING
- Precinct 102, Railroad Commissioner, Write-ins: Reference=0, Extracted=MISSING
- Precinct 103, President, Donald J. Trump/JD Vance: Reference=471, Extracted=MISSING

...and 76 more errors

✓ **All precinct names correct**

### Lynn County

8 precincts, 328 votes checked across 19 races.

✗ **Vote accuracy: 38.4%** - 202 errors found:

- Precinct 1, President, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, President, Under Votes: Reference=0, Extracted=MISSING
- Precinct 1, Railroad Commissioner, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, Railroad Commissioner, Under Votes: Reference=25, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, Jimmy Blacklock: Reference=224, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, DaSean Jones: Reference=84, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, Over Votes: Reference=0, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, Under Votes: Reference=33, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, John Devine: Reference=224, Extracted=MISSING
- Precinct 1, Justice, Supreme Court, Christine Vinh Weems: Reference=85, Extracted=MISSING

...and 192 more errors

✓ **All precinct names correct**

### Panola County

19 precincts, 380 votes checked across 20 races.

✗ **Vote accuracy: 50.3%** - 189 errors found:

- 1, President, Jill Stein: Reference=4, Extracted=2
- 1, President, Shiva Ayyadurai: Reference=0, Extracted=MISSING
- 1, President, Jessie Cuellar: Reference=0, Extracted=MISSING
- 1, President, Claudia De La Cruz: Reference=0, Extracted=MISSING
- 1, President, Cherunda Fox: Reference=0, Extracted=MISSING
- 1, President, Peter Sonski: Reference=0, Extracted=MISSING
- 1, President, Cornel West: Reference=0, Extracted=MISSING
- 2, President, Jill Stein: Reference=1, Extracted=0
- 2, President, Shiva Ayyadurai: Reference=0, Extracted=MISSING
- 2, President, Jessie Cuellar: Reference=0, Extracted=MISSING

...and 179 more errors

✓ **All precinct names correct**

### San Saba County

6 precincts, 108 votes checked across 26 races.

✓ **Vote accuracy: 100%** - All vote counts matched perfectly.

✓ **All precinct names correct**

### Scurry County

11 precincts, 165 votes checked across 31 races.

✓ **Vote accuracy: 100%** - All vote counts matched perfectly.

✓ **All precinct names correct**

## Conclusion

The tool achieved 70.5% accuracy overall. All precinct names were extracted correctly.
