import requests
site = "http://web-01.challs.olicyber.it/"
r = requests.get(site)
print(r.text)

#flag{g3t7ing_4l0ng}