import requests
import re
from base64 import b64decode, b64encode

site = "http://cuki.challs.olicyber.it/"

r = requests.get(site)
flag = r.cookies["session"]
print(b64decode(flag).decode())

#flag{here_is_your_c00ki3_:3}