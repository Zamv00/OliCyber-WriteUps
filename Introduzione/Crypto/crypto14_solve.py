import re
from pwn import *
from Crypto.Hash import SHA3_384, SHA224, HMAC
from Crypto.PublicKey import DSA
from Crypto.Util.number import *

r = remote("cr14.challs.olicyber.it", 30007)
r.recv(1000)

# SHA3
r.sendline(SHA3_384.new(b"hash_me_pls").hexdigest().encode())

# HMAC
r.recvuntil(b"'")
secret = bytes.fromhex(r.recvuntil(b"'").decode().strip("'"))
msg = "La mia integrità è importante!".encode()
h = HMAC.new(secret, msg, SHA224)
r.recv(1000)
r.sendline(h.hexdigest().encode())

# DSA params
r.recvuntil(b"'")
d = DSA.import_key(bytes.fromhex(r.recvuntil(b"'").decode().strip("'")))
r.recvuntil(b'\n')

for _ in range(3):
    f = r.recvuntil(b"? ").decode()
    r.sendline(str(getattr(d, re.search(r"[pqgxy]", f).group())).encode())

# Prime stuff
r.recvuntil(b"\n\n")
bits = int(re.search(r"(\d+)\s*bit", r.recv(100).decode()).group(1))
r.sendline(str(getPrime(bits)).encode())

r.recvuntil(b"= ")
n = int(r.recvuntil(b"\n"))
r.recvuntil(b"(si/no)?")
r.sendline(b"si" if isPrime(n) else b"no")

r.interactive()

#flag{kn0w1n6_(h0w_to_us3_A_l1Br4Ry)_i$_h4lf_th3_B4Tt1e}
