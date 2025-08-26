import requests
import re

site = "http://change-me.challs.olicyber.it/"

r = requests.post(site).text #app.py
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

# flag{changing_m3th0ds_sometimes_helps}