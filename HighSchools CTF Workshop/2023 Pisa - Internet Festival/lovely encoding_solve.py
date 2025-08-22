import requests
import re
site = "http://js-awesome.challs.olicyber.it/"

def rot13(s): #grazie chat gpt
    return s.translate(str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    ))



r = requests.get(site).text
match = re.search(r'synt\{[^\}]+\}', r)
flag = match.group(0)
print(rot13(flag))

#flag{wait_is_this_crypto_or_web}