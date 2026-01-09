import pandas as pd
import re

def transform_election_data(input_file, output_file, county_name="Harris"):
    """
    Transform election results CSV from source format to standardized format.
    
    Args:
        input_file (str): Path to input CSV file
        output_file (str): Path for output CSV file  
        county_name (str): County name to use in output (default: "Harris")
    """
    
    # Try to read the CSV file with different encodings
    encodings_to_try = ['utf-8', 'windows-1252', 'iso-8859-1', 'cp1252', 'latin1']
    df = None
    
    for encoding in encodings_to_try:
        try:
            print(f"Trying to read file with {encoding} encoding...")
            df = pd.read_csv(input_file, encoding=encoding)
            print(f"Successfully read file with {encoding} encoding")
            break
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"Error with {encoding}: {e}")
            continue
    
    if df is None:
        raise ValueError("Could not read the file with any of the attempted encodings")
    
    print(f"File read successfully. Shape: {df.shape}")
    
def transform_election_data(input_file, output_file, county_name="Harris"):
    """
    Transform election results CSV from source format to standardized format.
    
    Args:
        input_file (str): Path to input CSV file
        output_file (str): Path for output CSV file  
        county_name (str): County name to use in output (default: "Harris")
    """
    
    # Try to read the CSV file with different encodings and separators
    encodings_to_try = ['utf-8', 'windows-1252', 'iso-8859-1', 'cp1252', 'latin1']
    separators_to_try = [',', '\t', '|', ';']
    df = None
    
    for encoding in encodings_to_try:
        for separator in separators_to_try:
            try:
                print(f"Trying to read file with {encoding} encoding and '{separator}' separator...")
                df = pd.read_csv(input_file, encoding=encoding, sep=separator)
                if len(df.columns) > 10:  # Should have many columns
                    print(f"Successfully read file with {encoding} encoding and '{separator}' separator")
                    print(f"Columns found: {list(df.columns)}")
                    break
            except UnicodeDecodeError:
                continue
            except Exception as e:
                continue
        if df is not None and len(df.columns) > 10:
            break
    
    if df is None:
        raise ValueError("Could not read the file with any of the attempted encodings and separators")
    
    print(f"File read successfully. Shape: {df.shape}")
    
    # Print column names for debugging
    print("Available columns:")
    for i, col in enumerate(df.columns):
        print(f"  {i}: '{col}'")
    
    # Map column names to handle variations
    column_mapping = {}
    for col in df.columns:
        col_lower = col.lower().strip()
        col_clean = col.strip()
        
        # Precinct name mapping
        if col_clean == '#Precinct' or (col_lower.startswith('#') and 'precinct' in col_lower):
            column_mapping['precinct_name'] = col
        elif col_clean == 'Registered Voters':
            column_mapping['registered_voters'] = col
        elif col_clean == 'Ballots Cast':
            column_mapping['ballots_cast'] = col
        elif col_clean == 'Contest Title':
            column_mapping['contest_title'] = col
        elif col_clean == 'Choice Name':
            column_mapping['choice_name'] = col
        elif col_clean == 'Choice Party':
            column_mapping['choice_party'] = col
        elif col_clean == 'Total Votes':
            column_mapping['total_votes'] = col
        elif col_clean == 'Total Overvotes':
            column_mapping['total_overvotes'] = col
        elif col_clean == 'Total Undervotes':
            column_mapping['total_undervotes'] = col
        elif col_clean == 'Ballot by Mail Votes':
            column_mapping['absentee_votes'] = col
        elif col_clean == 'Ballot by Mail Overvotes':
            column_mapping['absentee_overvotes'] = col
        elif col_clean == 'Ballot by Mail Undervotes':
            column_mapping['absentee_undervotes'] = col
        elif col_clean == 'Early Voting Votes':
            column_mapping['early_votes'] = col
        elif col_clean == 'Early Voting Overvotes':
            column_mapping['early_overvotes'] = col
        elif col_clean == 'Early Voting Undervotes':
            column_mapping['early_undervotes'] = col
        elif col_clean == 'Election Day Votes':
            column_mapping['election_day_votes'] = col
        elif col_clean == 'Election Day Overvotes':
            column_mapping['election_day_overvotes'] = col
        elif col_clean == 'Election Day Undervotes':
            column_mapping['election_day_undervotes'] = col
        elif col_clean == 'EV Provisional Votes':
            column_mapping['ev_provisional_votes'] = col
        elif col_clean == 'EV Provisional Overvotes':
            column_mapping['ev_provisional_overvotes'] = col
        elif col_clean == 'EV Provisional Undervotes':
            column_mapping['ev_provisional_undervotes'] = col
        elif col_clean == 'ED Provisional Votes':
            column_mapping['ed_provisional_votes'] = col
        elif col_clean == 'ED Provisional Overvotes':
            column_mapping['ed_provisional_overvotes'] = col
        elif col_clean == 'ED Provisional Undervotes':
            column_mapping['ed_provisional_undervotes'] = col
    
    print("Column mapping:")
    for key, value in column_mapping.items():
        print(f"  {key} -> '{value}'")
    
    # Check if we have all required columns
    required_columns = ['precinct_name', 'registered_voters', 'ballots_cast', 'contest_title', 'choice_name']
    missing_columns = [col for col in required_columns if col not in column_mapping]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    # Initialize list to store transformed rows
    transformed_rows = []
    
    # Get unique precincts for voter registration data
    unique_precincts = df[[column_mapping['precinct_name'], column_mapping['registered_voters'], column_mapping['ballots_cast']]].drop_duplicates()
    
    # Add registered voters row for each precinct
    for _, precinct_data in unique_precincts.iterrows():
        transformed_rows.append({
            'county': county_name,
            'precinct': precinct_data[column_mapping['precinct_name']],
            'office': 'Registered Voters',
            'district': '',
            'party': '',
            'candidate': 'Registered Voters',
            'absentee': '',
            'early_voting': '',
            'election_day': '',
            'early_voting_provisional': '',
            'election_day_provisional': '',
            'votes': precinct_data[column_mapping['registered_voters']]
        })
        
        # Add ballots cast row for each precinct
        transformed_rows.append({
            'county': county_name,
            'precinct': precinct_data[column_mapping['precinct_name']],
            'office': 'Ballots Cast',
            'district': '',
            'party': '',
            'candidate': 'Ballots Cast',
            'absentee': '',
            'early_voting': '',
            'election_day': '',
            'early_voting_provisional': '',
            'election_day_provisional': '',
            'votes': precinct_data[column_mapping['ballots_cast']]
        })
    
    # Process each row in the original data
    for _, row in df.iterrows():
        # Skip empty choice names or zero vote candidates (except for special cases)
        choice_name = row[column_mapping['choice_name']]
        if pd.isna(choice_name) or choice_name == '':
            continue
            
        # Determine office and district
        contest_title = row[column_mapping['contest_title']]
        office = contest_title
        district = ''
        
        # Extract district information
        if 'District' in contest_title:
            district_match = re.search(r'District (\d+)', contest_title)
            if district_match:
                district = district_match.group(1)
                office = re.sub(r', District \d+', '', contest_title)
        
        # Simplify office names
        office_mapping = {
            'President / Vice President': 'President',
            'United States Senator': 'U.S. Senate',
            'United States Representative': 'U.S. House'
        }
        office = office_mapping.get(office, office)
        
        # Clean candidate name - remove running mate for president
        candidate = choice_name
        if ' / ' in candidate:
            candidate = candidate.split(' / ')[0]
        
        # Get party (handle missing party data)
        party = row[column_mapping.get('choice_party', '')] if 'choice_party' in column_mapping and pd.notna(row[column_mapping['choice_party']]) else ''
        
        # Get vote counts
        total_votes = row[column_mapping.get('total_votes', 0)] if 'total_votes' in column_mapping else 0
        absentee_votes = row[column_mapping.get('absentee_votes', 0)] if 'absentee_votes' in column_mapping else 0
        early_votes = row[column_mapping.get('early_votes', 0)] if 'early_votes' in column_mapping else 0
        election_day_votes = row[column_mapping.get('election_day_votes', 0)] if 'election_day_votes' in column_mapping else 0
        ev_provisional_votes = row[column_mapping.get('ev_provisional_votes', 0)] if 'ev_provisional_votes' in column_mapping else 0
        ed_provisional_votes = row[column_mapping.get('ed_provisional_votes', 0)] if 'ed_provisional_votes' in column_mapping else 0
        
        # Debug: Print some rows to see what's happening
        if len(transformed_rows) < 50:  # Only print first few for debugging
            print(f"Processing: {candidate} in {office}, votes: {total_votes}")
        
        # Create standard candidate row - be more permissive about including candidates
        # Include all candidates that have a name, even if votes are 0
        if candidate and candidate.strip():
            transformed_rows.append({
                'county': county_name,
                'precinct': row[column_mapping['precinct_name']],
                'office': office,
                'district': district,
                'party': party,
                'candidate': candidate,
                'absentee': absentee_votes,
                'early_voting': early_votes,
                'election_day': election_day_votes,
                'early_voting_provisional': ev_provisional_votes,
                'election_day_provisional': ed_provisional_votes,
                'votes': total_votes
            })
    
    # Add undervotes and overvotes for each office/precinct combination
    office_precinct_combinations = df.groupby([column_mapping['precinct_name'], column_mapping['contest_title']]).first().reset_index()
    
    for _, combo in office_precinct_combinations.iterrows():
        contest_title = combo[column_mapping['contest_title']]
        office = contest_title
        district = ''
        
        # Extract district information
        if 'District' in contest_title:
            district_match = re.search(r'District (\d+)', contest_title)
            if district_match:
                district = district_match.group(1)
                office = re.sub(r', District \d+', '', contest_title)
        
        # Simplify office names
        office_mapping = {
            'President / Vice President': 'President',
            'United States Senator': 'U.S. Senate',
            'United States Representative': 'U.S. House'
        }
        office = office_mapping.get(office, office)
        
        # Get vote counts for under/overvotes
        total_undervotes = combo[column_mapping.get('total_undervotes', 0)] if 'total_undervotes' in column_mapping else 0
        total_overvotes = combo[column_mapping.get('total_overvotes', 0)] if 'total_overvotes' in column_mapping else 0
        absentee_undervotes = combo[column_mapping.get('absentee_undervotes', 0)] if 'absentee_undervotes' in column_mapping else 0
        absentee_overvotes = combo[column_mapping.get('absentee_overvotes', 0)] if 'absentee_overvotes' in column_mapping else 0
        early_undervotes = combo[column_mapping.get('early_undervotes', 0)] if 'early_undervotes' in column_mapping else 0
        early_overvotes = combo[column_mapping.get('early_overvotes', 0)] if 'early_overvotes' in column_mapping else 0
        election_day_undervotes = combo[column_mapping.get('election_day_undervotes', 0)] if 'election_day_undervotes' in column_mapping else 0
        election_day_overvotes = combo[column_mapping.get('election_day_overvotes', 0)] if 'election_day_overvotes' in column_mapping else 0
        ev_provisional_undervotes = combo[column_mapping.get('ev_provisional_undervotes', 0)] if 'ev_provisional_undervotes' in column_mapping else 0
        ev_provisional_overvotes = combo[column_mapping.get('ev_provisional_overvotes', 0)] if 'ev_provisional_overvotes' in column_mapping else 0
        ed_provisional_undervotes = combo[column_mapping.get('ed_provisional_undervotes', 0)] if 'ed_provisional_undervotes' in column_mapping else 0
        ed_provisional_overvotes = combo[column_mapping.get('ed_provisional_overvotes', 0)] if 'ed_provisional_overvotes' in column_mapping else 0
        
        # Add undervotes row
        transformed_rows.append({
            'county': county_name,
            'precinct': combo[column_mapping['precinct_name']],
            'office': office,
            'district': district,
            'party': '',
            'candidate': 'Undervotes',
            'absentee': absentee_undervotes,
            'early_voting': early_undervotes,
            'election_day': election_day_undervotes,
            'early_voting_provisional': ev_provisional_undervotes,
            'election_day_provisional': ed_provisional_undervotes,
            'votes': total_undervotes
        })
        
        # Add overvotes row
        transformed_rows.append({
            'county': county_name,
            'precinct': combo[column_mapping['precinct_name']],
            'office': office,
            'district': district,
            'party': '',
            'candidate': 'Overvotes',
            'absentee': absentee_overvotes,
            'early_voting': early_overvotes,
            'election_day': election_day_overvotes,
            'early_voting_provisional': ev_provisional_overvotes,
            'election_day_provisional': ed_provisional_overvotes,
            'votes': total_overvotes
        })
    
    # Create output DataFrame
    output_df = pd.DataFrame(transformed_rows)
    
    # Sort by precinct, office, and candidate for better organization
    output_df = output_df.sort_values(['precinct', 'office', 'candidate']).reset_index(drop=True)
    
    # Save to CSV
    output_df.to_csv(output_file, index=False)
    print(f"Transformed data saved to {output_file}")
    print(f"Total rows: {len(output_df)}")
    
    return output_df

# Example usage
if __name__ == "__main__":
    # Transform the data
    # Update the file paths as needed
    input_file = "~/Downloads/harris.csv"  # Your input file
    output_file = "20241105__tx__general__harris__precinct.csv"
    
    # Run the transformation
    result_df = transform_election_data(input_file, output_file, county_name="Harris")
    
    # Display first few rows
    print("\nFirst 10 rows of transformed data:")
    print(result_df.head(10).to_string(index=False))
    
    # Show summary by office
    print("\nSummary by office:")
    print(result_df['office'].value_counts())