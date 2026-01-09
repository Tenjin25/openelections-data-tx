#!/usr/bin/env python3
"""
Calhoun County PDF Election Data Extractor using pdfplumber
"""

import sys
import csv
import re
from typing import List, Dict

try:
    import pdfplumber
except ImportError:
    print("Please install pdfplumber: pip install pdfplumber")
    sys.exit(1)

def extract_text_with_layout(pdf_path: str) -> str:
    """Extract text from PDF preserving layout using pdfplumber."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def normalize_office_name(office: str) -> str:
    """Normalize office names according to specifications."""
    office = office.strip()
    
    # Handle various President formats
    if "President/Vice President" in office or "President and Vice President" in office:
        return "President"
    elif "US Senator" in office or "U.S. Senator" in office:
        return "U.S. Senate"
    elif "US Representative" in office or "U.S. Representative" in office:
        return "U.S. House"
    elif "State Representative" in office:
        return "State Representative"
    elif "Railroad Commissioner" in office:
        return "Railroad Commissioner"
    elif "Justice, Supreme Court" in office:
        return office
    elif "Judge," in office or "Justice," in office or "Presiding Judge" in office:
        return office
    elif "Member, State BoE" in office:
        return "State Board of Education"
    elif "Dist Attorney" in office or "District Attorney" in office:
        return "District Attorney"
    elif "County" in office:
        return office
    elif "Sheriff" in office:
        return "Sheriff"
    elif "Constable" in office:
        return office
    elif "Board of Trustees" in office:
        return office
    elif "Chief Justice" in office:
        return office
    
    return office

def parse_election_data(text: str, county: str) -> List[Dict]:
    """Parse election data from PDF text with preserved layout."""
    data = []
    lines = text.split('\n')
    
    current_precinct = None
    current_office = None
    district = ""
    precinct_stats_added = set()
    
    print(f"Processing {len(lines)} lines of text...")
    
    for i, line in enumerate(lines):
        try:
            original_line = line
            line = line.strip()
            if not line:
                continue
            
            # Check for precinct headers - updated for Calhoun County format
            if re.match(r'^PCT\.\d+$', line):
                current_precinct = line
                print(f"Found precinct: {current_precinct}")
                precinct_stats_added.clear()  # Reset stats tracking for new precinct
                continue
            
            # Skip if no current precinct
            if current_precinct is None:
                continue
            
            # Check for statistics section
            if line == "Statistics" or ("TOTAL" in line and "Absentee" in line and "Early" in line):
                continue
                
            # Parse registered voters - format: "Registered Voters - Total 1,607"
            if "Registered Voters - Total" in line:
                match = re.search(r'Registered Voters - Total\s+([\d,]+)', line)
                if match and f"{current_precinct}_registered" not in precinct_stats_added:
                    registered_voters = int(match.group(1).replace(',', ''))
                    data.append({
                        'county': county,
                        'precinct': current_precinct,
                        'office': 'Registered Voters',
                        'district': '',
                        'party': '',
                        'candidate': '',
                        'votes': registered_voters,
                        'absentee': '',
                        'early_voting': '',
                        'election_day': ''
                    })
                    precinct_stats_added.add(f"{current_precinct}_registered")
                    print(f"Added registered voters: {registered_voters}")
                continue
            
            # Parse ballots cast - format: "Ballots Cast - Total 730 25 600 105"
            if "Ballots Cast - Total" in line:
                match = re.search(r'Ballots Cast - Total\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)', line)
                if match and f"{current_precinct}_ballots" not in precinct_stats_added:
                    total_ballots = int(match.group(1).replace(',', ''))
                    absentee = int(match.group(2).replace(',', ''))
                    early = int(match.group(3).replace(',', ''))
                    election_day = int(match.group(4).replace(',', ''))
                    
                    data.append({
                        'county': county,
                        'precinct': current_precinct,
                        'office': 'Ballots Cast',
                        'district': '',
                        'party': '',
                        'candidate': '',
                        'votes': total_ballots,
                        'absentee': absentee,
                        'early_voting': early,
                        'election_day': election_day
                    })
                    precinct_stats_added.add(f"{current_precinct}_ballots")
                    print(f"Added ballots cast: {total_ballots}")
                continue
            
            # Parse blank ballots - format: "Ballots Cast - Blank 1 0 1 0"
            if "Ballots Cast - Blank" in line:
                match = re.search(r'Ballots Cast - Blank\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)', line)
                if match and f"{current_precinct}_blank" not in precinct_stats_added:
                    total_blank = int(match.group(1).replace(',', ''))
                    absentee_blank = int(match.group(2).replace(',', ''))
                    early_blank = int(match.group(3).replace(',', ''))
                    election_day_blank = int(match.group(4).replace(',', ''))
                    
                    data.append({
                        'county': county,
                        'precinct': current_precinct,
                        'office': 'Ballots Cast - Blank',
                        'district': '',
                        'party': '',
                        'candidate': '',
                        'votes': total_blank,
                        'absentee': absentee_blank,
                        'early_voting': early_blank,
                        'election_day': election_day_blank
                    })
                    precinct_stats_added.add(f"{current_precinct}_blank")
                    print(f"Added blank ballots: {total_blank}")
                continue
            
            # Parse overvotes - format: "Overvotes 0 0 0 0"
            if line.startswith("Overvotes") and current_office:
                match = re.search(r'Overvotes\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)', line)
                if match:
                    total_over = int(match.group(1).replace(',', ''))
                    absentee_over = int(match.group(2).replace(',', ''))
                    early_over = int(match.group(3).replace(',', ''))
                    election_day_over = int(match.group(4).replace(',', ''))
                    
                    data.append({
                        'county': county,
                        'precinct': current_precinct,
                        'office': normalize_office_name(current_office),
                        'district': district,
                        'party': '',
                        'candidate': 'Over Votes',
                        'votes': total_over,
                        'absentee': absentee_over,
                        'early_voting': early_over,
                        'election_day': election_day_over
                    })
                    print(f"Added overvotes for {current_office}: {total_over}")
                continue
            
            # Parse undervotes - format: "Undervotes 1 0 1 0"  
            if line.startswith("Undervotes") and current_office:
                match = re.search(r'Undervotes\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)', line)
                if match:
                    total_under = int(match.group(1).replace(',', ''))
                    absentee_under = int(match.group(2).replace(',', ''))
                    early_under = int(match.group(3).replace(',', ''))
                    election_day_under = int(match.group(4).replace(',', ''))
                    
                    data.append({
                        'county': county,
                        'precinct': current_precinct,
                        'office': normalize_office_name(current_office),
                        'district': district,
                        'party': '',
                        'candidate': 'Under Votes',
                        'votes': total_under,
                        'absentee': absentee_under,
                        'early_voting': early_under,
                        'election_day': election_day_under
                    })
                    print(f"Added undervotes for {current_office}: {total_under}")
                continue
            
            # Check for office headers
            office_indicators = [
                "President/Vice President", "US Senator", "U.S. Senator",
                "US Representative", "U.S. Representative", "Railroad Commissioner",
                "Justice, Supreme Court", "Justice,", "Judge,", "Presiding Judge",
                "Member, State BoE", "State Representative", "Dist Attorney",
                "County Attorney", "County Commissioner", "County Clerk", "County Tax",
                "Sheriff", "Constable", "Board of Trustees", "Chief Justice"
            ]
            
            for indicator in office_indicators:
                if indicator in line:
                    current_office = line
                    district = ""
                    
                    # Extract district number if present
                    district_match = re.search(r'Dist\s+(\d+)', line)
                    if district_match:
                        district = district_match.group(1)
                    elif re.search(r'Place\s+(\d+)', line):
                        place_match = re.search(r'Place\s+(\d+)', line)
                        if place_match:
                            district = place_match.group(1)
                    elif re.search(r'Pct\s+(\d+)', line):
                        pct_match = re.search(r'Pct\s+(\d+)', line)
                        if pct_match:
                            district = pct_match.group(1)
                    elif re.search(r'Pl\s+(\d+)', line):
                        pl_match = re.search(r'Pl\s+(\d+)', line)
                        if pl_match:
                            district = pl_match.group(1)
                    
                    print(f"Found office: {current_office}")
                    break
            
            if current_office is None:
                continue
            
            # Skip header and summary lines
            skip_terms = [
                'Vote For', 'TOTAL', 'Absentee', 'Early', 'Election',
                'Voting', 'Day', 'Total Votes Cast', 'Write-In Totals',
                'Not Assigned', 'Contest Totals', 'Write-In:', 'VOTE %'
            ]
            
            if any(skip_term in line for skip_term in skip_terms):
                continue
            
            # Parse candidate lines - updated pattern for Calhoun County format with percentages
            # Format: "REP Donald J. Trump/JD Vance 333 54.77% 3 226 104"
            candidate_pattern = r'^(REP|DEM|LIB|GRN|IND)\s+(.+?)\s+(\d+)\s+[\d.]+%\s+(\d+)\s+(\d+)\s+(\d+)$'
            candidate_match = re.match(candidate_pattern, line)
            
            if candidate_match:
                party = candidate_match.group(1).strip()
                candidate_name = candidate_match.group(2).strip()
                total = int(candidate_match.group(3))
                absentee = int(candidate_match.group(4))
                early = int(candidate_match.group(5))
                election_day = int(candidate_match.group(6))
                
                # Skip certain write-ins with actual names
                if candidate_name.startswith('Write-In:'):
                    continue
                
                data.append({
                    'county': county,
                    'precinct': current_precinct,
                    'office': normalize_office_name(current_office),
                    'district': district,
                    'party': party,
                    'candidate': candidate_name,
                    'votes': total,
                    'absentee': absentee,
                    'early_voting': early,
                    'election_day': election_day
                })
                print(f"Added candidate: {candidate_name} ({party}) - {total} votes")
                continue
                    
        except Exception as e:
            print(f"Error processing line {i}: {original_line[:50]}... - {e}")
            continue
    
    print(f"Total records extracted: {len(data)}")
    return data

def main():
    if len(sys.argv) != 4:
        print("Usage: python calhoun_county_parser.py <input_pdf> <county_name> <output_csv>")
        sys.exit(1)
    
    input_pdf = sys.argv[1]
    county_name = sys.argv[2]
    output_csv = sys.argv[3]
    
    try:
        print(f"Extracting text from {input_pdf}...")
        text = extract_text_with_layout(input_pdf)
        
        print(f"Parsing election data for {county_name}...")
        data = parse_election_data(text, county_name)
        
        if not data:
            print("No data extracted. Check the debug output above.")
            return
        
        print(f"Writing {len(data)} records to {output_csv}...")
        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['county', 'precinct', 'office', 'district', 'party', 'candidate', 'votes', 'absentee', 'early_voting', 'election_day']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        
        print(f"Success! Created {output_csv}")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()