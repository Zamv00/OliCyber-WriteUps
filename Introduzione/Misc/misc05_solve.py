from pwn import *

host = "tcp.challs.olicyber.it"
port = 12210

r = remote(host, port)
print(r.recvall())

#flag{TcP_pR0t0c0L_3xP3r7}