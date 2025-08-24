import requests
import re

site = "http://vectorial.challs.olicyber.it"

flag = requests.get(f"{site}/4.jpeg")

print(flag.headers)
#ITASEC{p1r4t3s_h4v3_7h3_fl46!}