c = "fmcj{yo_ackyzb_ihruvcvjam}"

plaintext = ""
for i, ch in enumerate(c):
    if 'a' <= ch <= 'z':  
        new_char = chr((ord(ch) - ord('a') - i) % 26 + ord('a'))
        plaintext += new_char
    else:
        plaintext += ch

print(plaintext)
# flag{ti_stanno_tracciando}
