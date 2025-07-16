import requests
import re

site = "http://roller.challs.olicyber.it/"


r = requests.get(f"{site}/get_flag.php", allow_redirects=False)
print(r.text)


#ci basta visitare http://roller.challs.olicyber.it/get_flag.php senza seguire il redirect al rick roll
#flag{r1ck_4st1ey_c14ssic_m3m3}
