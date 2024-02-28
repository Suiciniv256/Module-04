# Fun Activity : Brute Force Attack for Pins
import random

def demonstrate_pin_based_brute(correct_pin):
    print()
    print("####### Initiating Brute Force #######")

    hit = False
    generated_pins = []
    counter = 1

    while not(hit):
        n1 = str(random.randint(0,9))
        n2 = str(random.randint(0, 9))
        n3 = str(random.randint(0, 9))

        pin = n1+n2+n3

        if(pin not in generated_pins):
            generated_pins.append(pin)
            if(pin == correct_pin):
                hit = True
                print("Attempt", counter ,": Attack Successful with Pin:", pin)

            else:
                print("Attempt", counter ,": Attack Unsuccessful with Pin:", pin)

            counter += 1

# demonstrate_pin_based_brute("764")

import pandas as pd

Timestamp = ['2023-08-15 10:30', '2023-08-15 14:45', '2023-08-16 09:15', '2023-08-14 09:15']
Incident_Type= ['Phishing', 'Malware Attack', 'Data Breach', 'Data Breach']
Severity = ['Low', 'High', 'Medium', 'Medium']
Affected_Users = [100, 15, 500, 100]
Description = [
    'Employees received suspicious emails with malicious links.',
    'Ransomware was executed, encrypting critical files.',
    'Sensitive customer data was accessed without authorization.',
    'Attempt to extract employee data without authorization.']

attacks_df = pd.DataFrame(Timestamp)
# Set options to display all rows and columns
pd.set_option('display.max_rows', None)    # Display all rows
pd.set_option('display.max_columns', None) # Display all columns


attacks_df = pd.DataFrame({"Timestamp" : Timestamp,
                           "Incident_Type": Incident_Type,
                           "Severity" : Severity,
                           "Affected_Users" : Affected_Users,
                           "Description": Description})

# Columns
print(attacks_df)
print()
print(attacks_df.Severity)
print()
print(attacks_df["Severity"])
print()
print(attacks_df[["Severity"]])
print()
print(attacks_df[["Severity", "Timestamp", "Incident_Type"]])

# Rows and Columns
print()
print(attacks_df.loc[0])
print(attacks_df.loc[2])
print()

print(attacks_df)
print(attacks_df.iloc[2])
print(attacks_df.iloc[1:4])
print(attacks_df.iloc[-1])

print()
# Rows and Columns
print("the data of the first observation for Severity, Timestamp, Incident_Type")
print(attacks_df[["Severity", "Timestamp", "Incident_Type"]].loc[0])
print("the data of the first and second observation for Severity, Timestamp, Incident_Type")
print(attacks_df[["Severity", "Timestamp", "Incident_Type"]][:2])

print(attacks_df.Severity[0])
print()

print(attacks_df[attacks_df.Severity == 'High'])

# Ex 1.

broadband = pd.read_csv("D:\\TSOM\\PData\\broadband.csv")
print(broadband)
print("First 6 Obs.")
print(broadband.head())

print("Last 6 Obs.")
print(broadband.tail())

print("Summaries")
print(broadband.describe())

list_6 = ["A","B","C","D","E","F"]

print(":".join(list_6))