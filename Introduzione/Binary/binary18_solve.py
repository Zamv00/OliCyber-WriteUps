from pwn import *

host = "software-18.challs.olicyber.it"
port = 13001
r = remote(host,port)
r.recv(10000)
r.sendline()

for _ in range (100):
    try:
        r.recvuntil(b"0x") # ignoriamo tutto
    except:
        print(num)
    num = r.recvuntil(b" ").decode().strip() # fino al numero senza lo 0x che memorizziamo
    f = r.recv(100) # memorizziamo i prossimi 100 bytes con scritto packed a x bit
    if b"unpacked" in f and b"64" in f: #in base a che formato è indicato restituiamo packed o unpacked a 32 o 64
        r.send(u64(num))
    elif b"unpacked" in f and b"32" in f:
        r.send(u32(num))
    elif b"packed" in f and b"64" in f:
        r.send(p64(int(num, 16)))
    elif b"packed" in f and b"32" in f:
        r.send(p32(int(num, 16)))

print(r.recv(100).decode())

#flag{ab2dde2a2b764d65}