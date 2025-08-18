from pwn import *

host = "wordwang.challs.olicyber.it"
port = 10601

r = remote(host,port)
r.recvuntil("\n")
data = r.recvuntil("\n").decode().strip()
print(data)
payload = "?" + data.upper() + "!"
print(payload)
r.sendline(payload.encode())
r.interactive()

#flag{n1c3_0n3_jul13!Th4ts_w0rdw4ng!}
