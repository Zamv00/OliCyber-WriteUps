import requests

site = "http://unguessable.challs.olicyber.it"

r = requests.get(f"{site}/vjfYkHzyZGJ4A7cPNutFeM/flag").text #guardiamo il source
print(r)

#ptm{4lw4y5_ch3ck_th3_50urc3_c0d3}