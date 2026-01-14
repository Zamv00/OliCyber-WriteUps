import requests
params = {"id" : "flag"}
site = "http://web-02.challs.olicyber.it/server-records"
r = requests.get(site, params=params)

print(r.text)

#flag{wh47_i5_y0ur_qu3ry}