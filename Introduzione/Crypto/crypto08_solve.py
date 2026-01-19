from pwn import *

host = "crypto-08.challs.olicyber.it"
port = 30001

r = remote(host, port)

f = r.recvuntil(b"=").decode().replace(" =", "").split(" ")
t = []
for i in f:
    if i != '%':
        t.append(int(i))
r.recv(1000)
r.sendline(f"{t[0]%t[1]}".encode())
r.recv(1000)
r.recvuntil(b"\n\n")
f = r.recvuntil(b"?").decode().replace("mod", "%").replace("(","").replace(")","").replace("?","").replace("== ","")
f = f.split(" ")
r.recv(1000)
if int(f[0]) == int(f[1])%int(f[3]):
    r.sendline(b"si")
else:
    r.sendline(b"no")
r.recvuntil(b"\n\n")
print(r.recv(1000))

#flag{t1ck_t0ck_M4th_1s_0n_th3_Cl0cK}


