from pwn import *

host = "crypto-10.challs.olicyber.it"
port = 30003

r = remote(host,port)

r.recvuntil(b"\n\n")
m = r.recvuntil(b"?").decode().split()

pairs = []
mod, sol = 2, 4

for _ in range(5):
    pairs.append((int(m[mod]), int(m[sol])))
    mod += 5
    sol += 5


x = pairs[0][1]
M = pairs[0][0]

for mod, rem in pairs[1:]:
    k = 0
    while (x + k * M) % mod != rem:
        k += 1
    x = x + k * M
    M *= mod


final_mod = int(m[-3])
ans = x % final_mod

r.sendline(str(ans).encode())
r.interactive()

#flag{Ch1n3s3_m4th3m4t1c14n5_4r3_D0p3!}