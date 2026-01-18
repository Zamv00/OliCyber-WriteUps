from pwn import *
import re
host = "software-19.challs.olicyber.it"
port = 13002
e = ELF("./sw-19")
r = remote(host,port)
data = r.recvuntil(b"... Invia un qualsiasi carattere per iniziare ...").strip().decode()
r.sendline(b"a")

for _ in range (20):
    r.recvuntil(b" ")
    func = r.recvuntil(b": ").decode().replace(": ", "") # prendiamo il nome della funzione e ci togliamo il :
    print(func) #stampiamo il nome della funzione
    address = (hex(int(e.sym[func])).encode()) #sym resituisce l'indirizzo di func, int e hex convertono in intero esadecimale in bytes
    print(address)
    r.sendline(address)


flag = r.recvline().decode().strip()
print(flag)

#flag{e353daccc34b6fbd}