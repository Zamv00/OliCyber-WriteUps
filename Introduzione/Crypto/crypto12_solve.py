from pwn import *
import re, math

def discrete_log_bruteforce(g, h, p):
    cur = 1
    for x in range(p):
        if cur == h:
            return x
        cur = (cur * g) % p
    return None
#gpt
r = remote("crypto-12.challs.olicyber.it", 30005)

r.recv(1000)
r.sendline(b"p-1")

# ===== primo log discreto =====
r.recvuntil(b"\n\n")
frase = r.recv(1000).decode()
print(frase)

pattern = r"logaritmo discreto di (\d+) in base (\d+) \(mod (\d+)\)"
a, g, p = map(int, re.search(pattern, frase).groups())

# qui è banalissimo → log normale
x = int(math.log(a, g))
r.sendline(str(x).encode())

# ===== secondo log discreto =====
r.recvuntil(b"\n\n")
frase = r.recv(1000).decode()
print(frase)

a, g, p = map(int, re.search(pattern, frase).groups())
x = discrete_log_bruteforce(g, a, p)
r.sendline(str(x).encode())

# ===== Diffie-Hellman =====
frase = r.recvuntil(b"?").decode()
print(frase)

pattern = r"p = (\d+), g = (\d+).\nLa mia chiave pubblica è (\d+)"
p, g, A = map(int, re.search(pattern, frase).groups())

b = 15  # chiave privata nostra
B = pow(g, b, p)
shared = pow(A, b, p)

r.sendline(str(B).encode())
r.sendline(str(shared).encode())

r.interactive()

#flag{W3_st4Nd_t0d4Y_0n_th3_Br1nk_of_4_r3v01uTioN_1n_Cryptography.}
