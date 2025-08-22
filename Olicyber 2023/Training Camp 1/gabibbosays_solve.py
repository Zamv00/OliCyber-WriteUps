import requests
import re

site = "http://gabibbo-says.challs.olicyber.it/"

r1 = requests.post(site, data = {"gabibbo" : "angry"}).text
print(r1)

match = re.search(r'flag\{[^\}]+\}', r1)
flag = match.group(0)
print(flag)
#flag{v0l3t3_4nCh3_l4_m14_f1rm4?}
