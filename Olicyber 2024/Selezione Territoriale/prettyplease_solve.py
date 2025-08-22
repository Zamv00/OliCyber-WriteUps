import requests
import re

site = "http://prettyplease.challs.olicyber.it/"

r = requests.post(site, data = {"how" : "pretty please"}).text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{how_d1d_y0u_h4ck_m3?!_eaa8a0bd}