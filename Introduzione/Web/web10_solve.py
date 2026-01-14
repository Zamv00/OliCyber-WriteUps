import requests
site = "http://web-10.challs.olicyber.it/"
allow = "head,options,get"
req = requests.put(site)
print(req.headers)

#flag{br34king_7h3_ru135}
