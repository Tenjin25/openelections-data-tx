import csv
import time
import requests
from bs4 import BeautifulSoup

offices = {
    4: ('President', None, [1,2,3,4,6]),
    5: ('U.S. Senate', None, [1,2,3,4,6]),
    6: ('U.S. House', 31, [1,2,3,5]),
    7: ('Railroad Commissioner', None, [1,2,3,4]),
    16: ('State Representative', 20, [1,2]),
    17: ('State Representative', 52, [1,2]),
    18: ('State Representative', 136, [1,2,3])
}

precincts = ['0119','0122','0135','0138','0140','0145','0146','0147','0149','0150','0151','0152','0160','0162','0172','0182','0185','0186','0189','0190','0197','0198','0201','0202','0204','0206','0207','0216','0218','0253','0254','0259','0263','0264','0266','0267','0273','0274','0275','0277','0278','0283','0287','0305','0309','0310','0311','0312','0314','0330','0331','0332','0333','0337','0339','0341','0342','0343','0344','0345','0368','0369','0370','0371','0379','0381','0392','0393','0394','0395','0396','0402','0403','0413','0415','0420','0423','0424','0425','0426','0427','0428','0429','0434','0436','0455','0456','0463','0480','0484','0488','0489','0490','0491']

results = []

for precinct in precincts:
    print(precinct)
    for office_num in list(offices.keys()):
        office, district, cand_nums = offices[office_num]
        for cand_num in cand_nums:
            time.sleep(0.5)
            url = f"https://apps.wilco.org/elections/results/voteinfo.aspx?r={office_num}&c={cand_num}&p={precinct}&e=764184&t=0"
            r = requests.get(url)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, features="lxml")
                candidate = soup.find('span', id='candidateLabel').find('b').text.strip()
                vote_breakdowns = soup.find('div', id='voteBreakdownDiv')
                early_voting_mail = vote_breakdowns.find('span', id='EVMail').text.replace(',','')
                early_voting_person = vote_breakdowns.find('span', id='EVPerson').text.replace(',','')
                election_day = vote_breakdowns.find('span', id='ED').text.replace(',','')
                provisional = vote_breakdowns.find('span', id='Provisional').text.replace(',','')
                votes = vote_breakdowns.find('span', id='Total').text.replace(',','')
                results.append(['Williamson', precinct, office, district, None, candidate, early_voting_mail, early_voting_person, election_day, provisional, votes])

with open("20201103__tx__general__williamson__precinct.csv", "w") as csv_outfile:
    outfile = csv.writer(csv_outfile)
    outfile.writerow(['county','precinct', 'office', 'district', 'party', 'candidate', 'mail', 'early_voting', 'election_day', 'provisional', 'votes'])
    outfile.writerows(results)
