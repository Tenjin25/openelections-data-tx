import pdfplumber
import csv
import re
from typing import List, Dict, Optional

def clean_text(text: str) -> str:
    """Clean and normalize text"""
    if not text:
        return ""
    return text.strip().replace('\n', ' ').replace('  ', ' ')

def parse_precinct_from_line(line: str) -> Optional[str]:
    """Extract precinct number from a line"""
    # Look for patterns like "1001-5001", "1002", etc.
    match = re.search(r'\b(\d{4}(?:-\d{4})?)\b', line)
    return match.group(1) if match else None

def normalize_office_name(office: str) -> str:
    """Normalize office names according to specifications"""
    office_mapping = {
        'President/Vice-President': 'President',
        'US Senator': 'U.S. Senate', 
        'US Representative': 'U.S. House',
        'State Representative': 'State Representative'
    }
    
    for key, value in office_mapping.items():
        if key.lower() in office.lower():
            return value
    
    return office

def parse_candidate_info(text: str) -> tuple:
    """Parse candidate name and party from text like 'REP Donald J. Trump/JD Vance'"""
    text = clean_text(text)
    
    # Handle write-ins
    if 'write-in' in text.lower():
        if any(skip_term in text.lower() for skip_term in ['total', 'not assigned', 'uncertified']):
            return None, None, True  # Skip this entry
        return 'Write-ins', '', False
    
    # Handle over/under votes
    if 'overvotes' in text.lower():
        return 'Over Votes', '', False
    if 'undervotes' in text.lower():
        return 'Under Votes', '', False
    
    # Parse party and candidate
    party_match = re.match(r'^(REP|DEM|LIB|GRN)\s+(.+)', text)
    if party_match:
        party = party_match.group(1)
        candidate = party_match.group(2).strip()
        return candidate, party, False
    
    return text, '', False

def should_skip_row(text: str) -> bool:
    """Check if a row should be skipped based on content"""
    skip_terms = [
        'total votes cast',
        'not assigned', 
        'rejected write-in votes',
        'unresolved write-in votes',
        'contest total',
        'contest totals'
    ]
    
    text_lower = text.lower()
    return any(term in text_lower for term in skip_terms)

def extract_district_from_office(office: str) -> tuple:
    """Extract district number from office name"""
    # Look for patterns like "Dist. 6", "District 10", "Pct. 1", etc.
    dist_match = re.search(r'(?:Dist\.?\s*|District\s*|Pct\.?\s*)(\d+)', office, re.IGNORECASE)
    if dist_match:
        district = dist_match.group(1)
        # Remove district info from office name
        office_clean = re.sub(r',?\s*(?:Dist\.?\s*|District\s*|Pct\.?\s*)\d+', '', office, flags=re.IGNORECASE).strip()
        return office_clean, district
    
    return office, ''

def parse_pdf_to_csv(pdf_path: str, output_path: str):
    """Main function to parse the PDF and create CSV"""
    
    results = []
    
    with pdfplumber.open(pdf_path) as pdf:
        current_office = ""
        current_district = ""
        
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
                
            lines = text.split('\n')
            
            for i, line in enumerate(lines):
                line = clean_text(line)
                if not line:
                    continue
                
                # Check for office headers
                if any(office_term in line for office_term in [
                    'President/Vice-President',
                    'US Senator', 
                    'US Representative',
                    'State Representative',
                    'Railroad Commissioner',
                    'Justice, Supreme Court',
                    'Judge, Court of Criminal Appeals',
                    'County', 'Sheriff', 'Constable'
                ]):
                    current_office = normalize_office_name(line)
                    current_office, current_district = extract_district_from_office(current_office)
                    continue
                
                # Skip headers and non-data lines
                if should_skip_row(line):
                    continue
                
                # Look for precinct data lines
                precinct = parse_precinct_from_line(line)
                if not precinct:
                    continue
                
                # Split the line to extract vote data
                parts = line.split()
                if len(parts) < 2:
                    continue
                
                # Find vote numbers (last few numbers in the line)
                vote_numbers = []
                candidate_parts = []
                
                for part in reversed(parts):
                    if part.replace(',', '').isdigit():
                        vote_numbers.insert(0, int(part.replace(',', '')))
                    else:
                        candidate_parts = parts[:parts.index(part)+1]
                        break
                
                if not vote_numbers:
                    continue
                
                # Get the main vote count (usually the first number)
                votes = vote_numbers[0] if vote_numbers else 0
                
                # Parse candidate info
                candidate_text = ' '.join(candidate_parts[1:])  # Skip precinct number
                candidate, party, should_skip = parse_candidate_info(candidate_text)
                
                if should_skip:
                    continue
                
                # Add to results
                results.append({
                    'county': 'Ellis',
                    'precinct': precinct,
                    'office': f'"{current_office}"',
                    'district': current_district,
                    'party': party,
                    'candidate': f'"{candidate}"',
                    'votes': votes,
                    'absentee': '',
                    'early_voting': '',
                    'election_day': ''
                })
    
    # Write to CSV
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['county', 'precinct', 'office', 'district', 'party', 'candidate', 'votes', 'absentee', 'early_voting', 'election_day']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    
    print(f"Parsed {len(results)} records to {output_path}")

if __name__ == "__main__":
    # Usage
    pdf_path = "/Users/dwillis/code/openelections-sources-tx/2024/general/2024 Ellis County, TX precinct-level results.pdf"  # Update with actual path
    output_path = "20241105__tx__general__ellis__precinct.csv"
    
    parse_pdf_to_csv(pdf_path, output_path)