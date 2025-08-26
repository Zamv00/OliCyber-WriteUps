import requests
import re

site = "http://trova-le-soluzioni.challs.olicyber.it"

r = requests.get(f"{site}/soluzioni-2023-2024/soluzioni/20231204.txt").text

match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{Non_ho_voglia_di_studiar3}