import argparse
import csv
import llm


def extract_results_with_llm(pdf_path, county, model_name):
    """Use LLM to extract election results from PDF using OCR."""
    
    prompt = f"""You are extracting election results from a PDF. The data should be formatted as CSV with these columns:
county,precinct,office,district,party,candidate,votes,absentee,early_voting,election_day

The county is: {county}

CRITICAL FORMATTING RULES:
1. Office names must use commas in specific formats:
   - "Justice, Supreme Court" (NOT "Justice Supreme Court" or "Supreme Court")
   - "Judge, Court of Criminal Appeals" (NOT "Judge Court of Criminal Appeals")
   - "Presiding Judge, Court of Criminal Appeals"
   - "Member, State Board of Education"
   - "Chief Justice, 10th Court of Appeals District"
   - "District Judge, 77th Judicial District"
2. District values go in the district column:
   - Supreme Court: "Place 2", "Place 4", "Pl 6"
   - Court of Criminal Appeals: "Pl 7", "Pl 8"
   - State Board of Education: just the number like "10"
   - State Representative: just the number like "13"
   - U.S. House: just the number like "17"
   - County Commissioner: "Pct 1", "Pct 2", etc.
   - Constable: "Precinct 1", "Precinct 2", etc.
3. Candidate names must be exact - check spelling carefully (e.g., "Angelia" vs "Angela", "Janes" vs "Jones")
4. Include rows with 0 votes - do not skip them
5. Write-ins should have empty party field and candidate must be "Write-ins" (plural)
6. Registered Voters and Ballots Cast have empty party and candidate fields
7. Double-quote values with commas in them

Example format:
county,precinct,office,district,party,candidate,votes,absentee,early_voting,election_day
Scurry,Precinct 5,Registered Voters,,,,98,,,
Scurry,Precinct 5,Ballots Cast,,,,73,0,65,8
Scurry,Precinct 5,President,,REP,Donald J. Trump,60,0,54,6
Scurry,Precinct 5,President,,DEM,Kamala D. Harris,13,0,11,2
Scurry,Precinct 5,President,,LIB,Chase Oliver,0,0,0,0
Scurry,Precinct 5,President,,GRN,Jill Stein,0,0,0,0
Scurry,Precinct 5,President,,,Write-ins,0,0,0,0
Scurry,Precinct 5,U.S. Senate,,REP,Ted Cruz,57,0,51,6
Scurry,Precinct 5,U.S. Senate,,DEM,Colin Allred,14,0,12,2
Scurry,Precinct 5,U.S. Senate,,LIB,Ted Brown,0,0,0,0
Scurry,Precinct 5,U.S. Senate,,,Write-ins,0,0,0,0
Scurry,Precinct 5,U.S. House,19,REP,Jodey C. Arrington,62,0,55,7
Scurry,Precinct 5,U.S. House,19,LIB,Bernard Johnson,3,0,2,1
Scurry,Precinct 5,U.S. House,19,IND,Nathan Lewis,3,0,3,0

Extract ALL precinct-level results from the PDF following this exact format. Process every page of the PDF.
Return ONLY the CSV data, no explanations or header row.

Return the CSV data:"""

    model = llm.get_model(model_name)
    
    # Attach the PDF for the model to read
    # Set very high max_tokens to ensure we get all results
    response = model.prompt(
        prompt,
        attachments=[llm.Attachment(path=pdf_path)],
        system="You are a precise data extraction assistant. Extract all data from the document completely.",
        max_tokens=48000
    )
    return response.text()


def parse_and_write_csv(llm_output, output_file):
    """Parse LLM output and write to CSV file."""
    lines = llm_output.strip().split('\n')
    
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(['county', 'precinct', 'office', 'district', 'party', 'candidate', 'votes','absentee','early_voting','election_day'])
        
        # Write data lines
        for i, line in enumerate(lines):
            if line.strip():
                # Parse the CSV line
                reader = csv.reader([line])
                for row in reader:
                    # Skip header row if LLM included it (first line starting with "county")
                    if i == 0 and len(row) > 0 and row[0].lower() == 'county':
                        continue
                    writer.writerow(row)


def main():
    parser = argparse.ArgumentParser(
        description='Extract precinct-level election results from PDF using LLM OCR'
    )
    parser.add_argument('pdf_path', help='Path to the PDF file')
    parser.add_argument('county', help='County name')
    parser.add_argument('output_file', help='Output CSV filename')
    parser.add_argument('-m', '--model', default='gpt-4o', 
                       help='LLM model to use (default: gpt-4o)')
    
    args = parser.parse_args()
    
    print(f"Processing {args.pdf_path} with {args.model}...")
    results = extract_results_with_llm(args.pdf_path, args.county, args.model)
    
    print(f"Writing results to {args.output_file}...")
    parse_and_write_csv(results, args.output_file)
    
    print("Done!")


if __name__ == '__main__':
    main()
