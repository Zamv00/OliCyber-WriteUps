import requests
import re

site = "http://spider.challs.olicyber.it"

flag1 = requests.get(f"{site}/supe3s3cretf0lder/flag1.txt").text #robots.txt
print(flag1)
flag2 = requests.get(f"{site}/standardNonSecretFolder/flag2.txt").text #sitemap.xml
print(flag2)

#flag{s3mbr1_un0_sp1d3R}