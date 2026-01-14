import requests
site = "http://web-08.challs.olicyber.it/login"
payload = {"username": "admin", "password": "admin"}
req = requests.post(site,data = payload)
print(req.text)

#flag{53nding_d474_7h3_01d_w4y}