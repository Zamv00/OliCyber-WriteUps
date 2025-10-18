from pwn import *

host = "nt-master.challs.olicyber.it" 
port = 11001

r = remote(host,port)
for _ in range (10):
    r.recvuntil(b"N = ")
    N = int(r.recvline().strip())
    r.sendline(f"{N-1} 1".encode())
r.interactive()

#ptm{as_dumb_as_a_sanity_check_4976ab37ed7f66e}