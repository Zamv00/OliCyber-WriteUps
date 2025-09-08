from pwn import *

host = "ssh.challs.olicyber.it"
port = "34009"

r = remote(host,port)
r.sendline(b"gabibbo")
r.sendline(b"p4ssw0rd_SSH_s3gr3t4")
r.sendline(b"cd Desktop")
r.sendline(b"cd olicyber")
r.sendline(b"cd 2022")
r.sendline(b"cd Olicyber_git_repository_2022")
r.sendline(b"cd network_brutta")
r.sendline(b"cat flag.txt")
flag = r.recvuntil(b"}").decode()
print(flag)

#flag{b3lla_st4_sh3ll_ssh...}