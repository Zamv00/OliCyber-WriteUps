from pwn import *

host = "lucky.challs.olicyber.it"
port = 17000

r = remote(host,port)
r.sendline(b"1804289383") # rand con seed 1

data = r.recv(10000)
print(data.decode())

#ptm{Random_fUnction_is_sometimes_vulnerable}