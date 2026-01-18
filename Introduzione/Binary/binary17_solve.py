from pwn import *
import re
host = "software-17.challs.olicyber.it"
port = 13000
r = remote(host,port)
# r.interactive()
data = r.recvuntil(b"... Invia un qualsiasi carattere per iniziare ...").strip().decode()
r.sendline(b"a")

for _ in range (10):
    data1 = r.recvuntil(b"somma questi numeri")
    data2 = r.recvuntil(b"Somma? : ").strip().decode()

    # re.findall cerca tutte le corrispondenze del pattern in una stringa, il nostro pattern è "-?\d+" -?: può essere negativo, \d+: un numero, map li rende tutti interi
    numeri = list(map(int, re.findall(r"-?\d+", data2)))
    somma = sum(numeri)
    print(somma)
    r.sendline(str(somma))

flag = r.recvline().decode().strip()
print(flag)

#flag{455b7c904a9fb4a6}