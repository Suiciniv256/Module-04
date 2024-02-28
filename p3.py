python
import re
import pandas as pd


with open('ServiceWebSite.html', 'r') as f:
    html_str = f.read()

phone_regex = r'\(\d{3}\) \d{3}-\d{4}'
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
name_regex = r'<td>([A-Za-z ]+)</td>'


phone_numbers = re.findall(phone_regex, html_str)
emails = re.findall(email_regex, html_str)
names = re.findall(name_regex, html_str)


df = pd.DataFrame({'Name': names, 'Phone': phone_numbers, 'Email': emails})

print(df)