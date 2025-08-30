import requests
import re
site = "http://vectorcraft.challs.olicyber.it"

r = requests.get(f"{site}/logo.svg").text
match = re.search(r'ITASEC\{[^\}]+\}', str(r))
flag = match.group(0)
print(flag)

#ITASEC{y0u_c4n_f1nd_t3xt_wh3r3_y0u_l3ast_3xp3ct_1t}