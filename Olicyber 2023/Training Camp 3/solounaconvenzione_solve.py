import requests
import re

site = "http://convenzione.challs.olicyber.it/"

r = requests.request("FLAG", site).headers
match = re.search(r'flag\{[^\}]+\}', str(r))
flag = match.group(0)
print(flag)

#flag{SPL4SH!_duuu_duu_duddurudduru_dururu}