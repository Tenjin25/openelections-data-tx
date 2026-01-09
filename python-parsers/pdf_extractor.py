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

Example format:
county,precinct,office,district,party,candidate,votes,absentee,early_voting,election_day
Panola,1,Registered Voters,,,,1972,,,
Panola,2,Registered Voters,,,,2332,,,
Panola,3,Registered Voters,,,,1453,,,
Panola,5,Registered Voters,,,,505,,,
Panola,7,Registered Voters,,,,898,,,
Panola,8,Registered Voters,,,,282,,,
Panola,9,Registered Voters,,,,788,,,
Panola,10,Registered Voters,,,,368,,,
Panola,12,Registered Voters,,,,439,,,
Panola,13,Registered Voters,,,,363,,,
Panola,14,Registered Voters,,,,508,,,
Panola,18,Registered Voters,,,,2240,,,
Panola,19,Registered Voters,,,,380,,,
Panola,20,Registered Voters,,,,360,,,
Panola,22,Registered Voters,,,,465,,,
Panola,26,Registered Voters,,,,177,,,
Panola,27,Registered Voters,,,,1504,,,
Panola,28,Registered Voters,,,,2518,,,
Panola,29,Registered Voters,,,,365,,,
Panola,1,Ballots Cast,,,,1264,56,954,254
Panola,2,Ballots Cast,,,,1489,50,1132,307
Panola,3,Ballots Cast,,,,986,19,639,328
Panola,5,Ballots Cast,,,,390,6,227,157
Panola,7,Ballots Cast,,,,590,12,280,298
Panola,8,Ballots Cast,,,,181,1,93,87
Panola,9,Ballots Cast,,,,497,17,190,290
Panola,10,Ballots Cast,,,,229,7,134,88
Panola,12,Ballots Cast,,,,339,16,178,145
Panola,13,Ballots Cast,,,,230,8,124,98
Panola,14,Ballots Cast,,,,348,5,215,128
Panola,18,Ballots Cast,,,,1556,52,1063,441
Panola,19,Ballots Cast,,,,263,6,128,129
Panola,20,Ballots Cast,,,,266,2,174,90
Panola,22,Ballots Cast,,,,256,8,102,146
Panola,26,Ballots Cast,,,,127,2,60,65
Panola,27,Ballots Cast,,,,777,27,535,215
Panola,28,Ballots Cast,,,,1474,49,1117,308
Panola,29,Ballots Cast,,,,238,3,104,131
Panola,1,President,,REP,Donald J. Trump,1021,39,787,195
Panola,2,President,,REP,Donald J. Trump,1182,35,937,210
Panola,3,President,,REP,Donald J. Trump,816,16,545,255
Panola,5,President,,REP,Donald J. Trump,368,4,220,144
Panola,7,President,,REP,Donald J. Trump,495,8,249,238
Panola,8,President,,REP,Donald J. Trump,154,0,80,74

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
#        max_tokens=32000
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
