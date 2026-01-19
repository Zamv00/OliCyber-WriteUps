def xor(a):
    for i in range(256):
        candidate = bytes(x ^ i for x in a)
        print(f"Key: {i}, Decoded: {candidate}")

ciphertext = "104e137f425954137f74107f525511457f5468134d7f146c4c"

bytescipher = bytes.fromhex(ciphertext)

xor(bytescipher)