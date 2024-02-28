import pandas as pd

def load_mall_data():
    mall_c = pd.read_csv("D:\TSOM\PData\Mall_Customers.csv")
    """
    \\ - Escaping the \ from its primary use
    '\n'
    '\t''
    'n'
    't'
    'D:\\nothing\\terry'
    """
    # mall_c is a data frame
    # columns - variables
    # rows - observations
    print(mall_c)
    print(type(mall_c))
    print(type(mall_c['CustomerID']))
    print(mall_c['CustomerID'])

import pandas as pd
import sqlalchemy
from sqlalchemy import text

def load_sql_data():
    engine = sqlalchemy.create_engine("mysql+pymysql://root:da12345@localhost/test1")
    conn = engine.connect()
    print(conn)
    df = pd.read_sql(text('SELECT * FROM test1.buyers'), conn)
    print(df)
    conn.close()

# load_mall_data()
# load_sql_data()

# Series
Timestamp = ['2023-08-15 10:30', '2023-08-15 14:45', '2023-08-16 09:15', '2023-08-14 09:15']
Incident_Type= ['Phishing', 'Malware Attack', 'Data Breach', 'Data Breach']
Severity = ['Low', 'High', 'Medium', 'Medium']
Affected_Users = [100, 15, 500, 100]
Description = [
    'Employees received suspicious emails with malicious links.',
    'Ransomware was executed, encrypting critical files.',
    'Sensitive customer data was accessed without authorization.',
    'Attempt to extract employee data without authorization.']

Timestamp_s = pd.Series(Timestamp)
Incident_Type_s = pd.Series(Incident_Type)
Severity_s = pd.Series(Severity)
Affected_Users_s = pd.Series(Affected_Users)
Description_s = pd.Series(Description)

print(Affected_Users)
print(Affected_Users_s)
print()
print(type(Affected_Users))
print(type(Affected_Users_s))

# List subsetting / Indexing can be used to access the data in a Series
print()
print("Series Data Access")
print("Time of the first Incident:", Timestamp_s[1])
print("Number of users affected in the last two incidents ")
print(Affected_Users_s[-2:])

Incident_Type_s2 = pd.Series(Incident_Type, index = ['I1','I2','I3','I4'])
print(Incident_Type_s2)
print(Incident_Type_s2["I2"])
print(Incident_Type_s2[["I2","I4"]])

# You can also use dictionaries to generate Series
Incident_Type_d = {'I1':'Phishing', 'I2': 'Malware Attack', 'I3': 'Data Breach', 'I4': 'Data Breach'}
Incident_Type_s3 = pd.Series(Incident_Type_d)
print(Incident_Type_s3)

print()
correction = [5, 10, 20, 5]
print("Affected Users Before Correction")
print(Affected_Users_s)
print("Affected Users After Correction")
Affected_Users_s = Affected_Users_s.add(correction)
print(Affected_Users_s)

print("Total Number of Users Affected:", Affected_Users_s.sum())
print("AVG Number of Users Affected per Incident:", Affected_Users_s.mean())