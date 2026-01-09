#!/usr/bin/env python3
"""
Trace all potential precincts in the PDF to see what we're missing
"""

import sys
import re

try:
    import pdfplumber
except ImportError:
    print("Please install pdfplumber: pip install pdfplumber")
    sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python trace_all_precincts.py <input_pdf>")
        sys.exit(1)
    
    input_pdf = sys.argv[1]
    
    with pdfplumber.open(input_pdf) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    
    lines = text.split('\n')
    
    print("All lines starting with 1 digit and containing 'registered voters':")
    print("=" * 80)
    
    # Find all potential precinct lines
    precinct_lines = []
    for i, line in enumerate(lines):
        if re.match(r'^\d{1}', line.strip()) and 'registered voters' in line.lower():
            precinct_lines.append((i, line.strip()))
    
    print(f"Found {len(precinct_lines)} potential precinct lines:")
    
    # Group by precinct number to see unique precincts
    precinct_numbers = set()
    for i, line in precinct_lines:
        # Extract the 3-digit precinct number
        match = re.match(r'^(\d{3})', line)
        if match:
            precinct_num = match.group(1)
            precinct_numbers.add(precinct_num)
            print(f"Line {i}: {line}")
    
    print(f"\nUnique precinct numbers found: {sorted(precinct_numbers)}")
    print(f"Total unique precincts: {len(precinct_numbers)}")
    
    # Test our current regex on each line
    print(f"\n" + "=" * 80)
    print("Testing current regex pattern on each line:")
    print("=" * 80)
    
    current_pattern = r'^(\d{3}(?:\s*-\s*\w+)?)\s+(\d+)\s+of\s+(\d+)\s+registered\s+voters'
    
    matched_precincts = set()
    failed_lines = []
    
    for i, line in precinct_lines:
        match = re.search(current_pattern, line)
        if match:
            precinct = re.sub(r'\s*-\s*\w+$', '', match.group(1).strip())
            matched_precincts.add(precinct)
            print(f"✓ Line {i}: {line}")
            print(f"   Precinct: {precinct}, Ballots: {match.group(2)}, Registered: {match.group(3)}")
        else:
            failed_lines.append((i, line))
            print(f"✗ Line {i}: {line}")
    
    print(f"\nCurrent regex matched {len(matched_precincts)} precincts: {sorted(matched_precincts)}")
    
    if failed_lines:
        print(f"\nFailed to match {len(failed_lines)} lines:")
        for i, line in failed_lines:
            print(f"  Line {i}: {line}")
        
        print(f"\nAnalyzing failed lines to understand the pattern...")
        for i, line in failed_lines[:5]:  # Show first 5 failures
            print(f"\nLine {i}: {line}")
            # Try to break down the line
            parts = line.split()
            print(f"  Parts: {parts}")

if __name__ == "__main__":
    main()