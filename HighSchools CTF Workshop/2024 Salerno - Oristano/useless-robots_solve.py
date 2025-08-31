import requests


site = "https://useless-robots.challs.olicyber.it"

r = requests.get(f"{site}/4a10eb719bf40679eec6").text #preso da /robots.txt
print(r)

#flag{b3_c4r3ful!_r0b075_4r3_w47ch1n5}

import base64

encoded_str = 'zMXHz3TJBdeZBNrFnwLKm19SmgCXBL9TngSZC19Tm19Zngr9'
decoded_str = base64.b64decode(encoded_str).decode('utf-8')
print(decoded_str)
