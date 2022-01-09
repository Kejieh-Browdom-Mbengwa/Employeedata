import csv
import pandas as pd


# def fetch_csv():
#     employee_details = pd.read_csv('input\employeedata.csv', encoding="unicode_escape")
#     return employee_details
#

userDetails = pd.read_csv('input/employeedata.csv', encoding="unicode_escape")

oldEmail = userDetails['Email'].tolist()
new_emails = []
for email in oldEmail:
    new_emails.append(email.replace("@helpinghands.cm", "@handsinhands.org"))
print(new_emails)

names = userDetails['Name'].tolist()
phone = userDetails['Phone'].tolist()

header = ['Name', 'Email', 'Phone']
my_dict = {"Name": names, "Email": new_emails, "Phone": phone}
with open('output/updatedemployeedata.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(my_dict.keys())
    writer.writerows(zip(*my_dict.values()))

