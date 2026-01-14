import requests
site = "http://web-09.challs.olicyber.it/login"
payload = {"username": "admin", "password": "admin"}
req = requests.post(site, json = payload)
print(req.text)

#flag{w31c0m3_70_7h3_y34r_2000}