import requests
import re


site = "http://no-robots.challs.olicyber.it"

r = requests.get("http://no-robots.challs.olicyber.it/I77p0mhKjr.html").text

match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)
#flag{Gu355_y0u_f0und_7h3_r0b075}
