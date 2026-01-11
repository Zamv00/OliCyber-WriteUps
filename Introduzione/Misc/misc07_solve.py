from pwn import *

host = "basicbash.challs.olicyber.it"
port = 38048

r = remote(host, port)
r.sendline(b"cd cartella")
r.sendline(b"ls -l .esempio")
line1 = r.recvline().decode().strip()
piece1 = int(line1.split()[4])
print(piece1)
r.sendline(b"cat gatto")
piece2 = r.recvline().decode().strip()
print(piece2)
r.sendline(b"./eseguibile")
piece3 = r.recvline().decode().strip()
print(piece3)
r.sendline(b"grep -r olicyber")
line = r.recvline().decode().strip()
piece4 = line.split(":", 1)[1]
print(piece4)

flag = "flag{" + str(piece1)+"_"+str(piece2)+"_"+str(piece3)+"_"+str(piece4) +"}"
print(flag)

#flag{109_ffeaf8a1a4a9a9ef_banananana_olicybercamp2025}