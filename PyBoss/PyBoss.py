import os
import csv
from datetime import datetime

csvpath = os.path.join("employee_data.csv")

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

empID = []
name = []
firstname = []
lastname = []
date = ""
DOB = []
SSN = []
state = []

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        empID.append(row[0])
        name = row[1].split()
        firstname.append(name[0])
        lastname.append(name[1])
        d = datetime.strptime(row[2],'%Y-%m-%d')
        date = d.strftime('%m/%d/%Y')
        DOB.append(date)
        SSN.append(f"***-**{row[3][6:]}")
        state.append(us_state_abbrev[row[4]])

headers = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
newfiledata = zip(empID, firstname, lastname, DOB, SSN, state)

output_path = os.path.join("new_employee_data.csv")

with open(output_path, "w", newline="") as datafile:
    writer = csv.writer(datafile, delimiter=",")

    writer.writerow(headers)
    writer.writerows(newfiledata)


