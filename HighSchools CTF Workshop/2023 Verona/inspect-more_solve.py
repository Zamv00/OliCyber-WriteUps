import requests
import re

site = "http://inspect-more.challs.olicyber.it/"

r = requests.post(f"{site}/validate_result", json = {"result":"0.0776"}).text #source code
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{was_the_qu3sti0n_t00_easy?}