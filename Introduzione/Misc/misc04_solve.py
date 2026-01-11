import requests
import re

site = "http://sito.challs.olicyber.it/"
r = requests.get(site).text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{h41_4p3rt0_un_s1t0_w3b}