# Il binario nel main fa una cosa di questo genere:
# for (int i = 0; i < 14; i++){
# flag[i] = flag[i] ^ key[i]; 
# }
# su ghidra possiamo ricavarci sia la flag che la chiave, e ci basta fare lo xor tra di esse per ottenere la vera flag:

flag_hex = "d4 5c dc bb 6b 1e d3 4a 4a 5e d2 df ac 7c" 
key_hex  = "b2 30 bd dc 10 7a e1 7b 2c 3b e2 ec 99 01"

flag = bytes.fromhex(flag_hex)
key  = bytes.fromhex(key_hex)

result = bytes([f ^ k for f, k in zip(flag, key)])

print(result)
print(result.hex())

#flag{d21fe035}