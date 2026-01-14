import requests
import re
site = "http://web-04.challs.olicyber.it/users"
req = requests.get(site, headers={"accept" : "application/xml"}).text
match = re.search(r'flag\{[^\}]+\}', req)
flag = match.group(0)
print(flag)

#flag{54m3_7hing_diff3r3n7_7hing}