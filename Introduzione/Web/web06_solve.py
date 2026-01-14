import requests

s = requests.Session()
site = "http://web-06.challs.olicyber.it/token"
req = s.get(site)
cookie = s.cookies
print(cookie)
site_2 = "http://web-06.challs.olicyber.it/flag"
req2 = requests.get(site_2, cookies=cookie)
print(req2.text)

#flag{7w0_574g3_4cc3s5}