import pandas as pd
import re

def extract_district(office):
    match = re.search(r'Dist(?:rict)?\s*(\d+)', office, re.IGNORECASE)
    return match.group(1) if match else ""

def normalize_office_name(raw_office):
    """Standardize office names like 'United States Representative, District 6'."""
    cleaned = raw_office.replace("(Vote For 1)", "").strip()

    if re.search(r"united states senator", cleaned, re.IGNORECASE):
        return "U.S. Senate", ""
    if re.search(r"united states representative", cleaned, re.IGNORECASE):
        return "U.S. House", extract_district(cleaned)
    if re.search(r"president/?vice president", cleaned, re.IGNORECASE):
        return "President", ""

    return re.sub(r",?\s*District\s*\d+", "", cleaned), extract_district(cleaned)

def parse_registered_voters_sheet(sheet_df, county):
    sheet_df.columns = sheet_df.columns.str.strip()
    rows = []

    for _, row in sheet_df.iterrows():
        precinct = str(row.iloc[0]).strip()
        if precinct == "Total:" or not precinct.lower().startswith("precinct"):
            continue

        rows.append({
            "county": county,
            "precinct": precinct,
            "office": "Registered Voters",
            "district": "",
            "party": "",
            "candidate": "",
            "absentee": "",
            "early_voting": "",
            "election_day": "",
            "votes": row.get("Registered Voters", "")
        })

        rows.append({
            "county": county,
            "precinct": precinct,
            "office": "Ballots Cast",
            "district": "",
            "party": "",
            "candidate": "",
            "absentee": row.get("Absentee", ""),
            "early_voting": row.get("Early Voting", ""),
            "election_day": row.get("Election Day", ""),
            "votes": row.get("Ballots Cast", "")
        })

    return rows

def parse_candidate_sheet(sheet_df, raw_office, county):
    sheet_df = sheet_df.dropna(how="all").reset_index(drop=True)
    if sheet_df.shape[0] < 4:
        return []

    candidate_names = sheet_df.iloc[1]
    data_rows = sheet_df.iloc[2:]

    candidate_blocks = []
    for col_start in range(2, len(candidate_names), 4):
        candidate = candidate_names[col_start]
        if pd.isna(candidate):
            continue
        candidate_blocks.append((candidate.strip(), col_start))

    office, district = normalize_office_name(raw_office)

    parsed_rows = []
    for _, row in data_rows.iterrows():
        precinct = str(row.iloc[0]).strip()
        if precinct == "Total:" or not precinct.lower().startswith("precinct"):
            continue

        for candidate, start_col in candidate_blocks:
            vote_absentee = row.iloc[start_col]
            vote_early = row.iloc[start_col + 1]
            vote_election = row.iloc[start_col + 2]
            total_votes = row.iloc[start_col + 3]

            if " " in candidate:
                parts = candidate.split(" ", 1)
                party_abbr = parts[0].strip() if len(parts[0]) <= 5 else ""
                name_part = parts[1].strip() if len(parts) > 1 else candidate
            else:
                party_abbr = ""
                name_part = candidate

            parsed_rows.append({
                "county": county,
                "precinct": precinct,
                "office": office,
                "district": district,
                "party": party_abbr,
                "candidate": name_part,
                "absentee": vote_absentee,
                "early_voting": vote_early,
                "election_day": vote_election,
                "votes": total_votes
            })

    return parsed_rows

def main(input_file, county, output_file):
    xlsx = pd.ExcelFile(input_file)

    # Load Table of Contents
    toc_df = pd.read_excel(xlsx, sheet_name="Table of Contents")
    toc_clean = toc_df.iloc[4:].dropna(subset=["Unnamed: 0", "Unnamed: 1"])
    toc_clean.columns = ["page", "office"]
    toc_clean["page"] = toc_clean["page"].astype(str).str.strip()
    toc_clean["office"] = toc_clean["office"].astype(str).str.strip()

    all_rows = []

    # Registered Voters sheet
    if "Registered Voters" in xlsx.sheet_names:
        reg_df = pd.read_excel(xlsx, sheet_name="Registered Voters").dropna(how="all")
        all_rows.extend(parse_registered_voters_sheet(reg_df, county))

    # All other sheets
    for _, row in toc_clean.iterrows():
        page = str(row["page"])
        raw_office = row["office"]

        if page in xlsx.sheet_names:
            df = pd.read_excel(xlsx, sheet_name=page, header=None)
            all_rows.extend(parse_candidate_sheet(df, raw_office, county))

    df = pd.DataFrame(all_rows)
    df.to_csv(output_file, index=False)
    print(f"✅ Results saved to {output_file}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python parse_precinct_results.py input.xlsx COUNTY_NAME output.csv")
    else:
        input_file = sys.argv[1]
        county = sys.argv[2]
        output_file = sys.argv[3]
        main(input_file, county, output_file)
