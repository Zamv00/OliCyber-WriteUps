def xor(a, b):
    return bytes([ x ^ y for x,y in zip(a,b) ])

ct = "1e03132c3e681e300b7b30063301423c1a1c165f070c0d06015f07140e3748182d7a31064c031e36"
ct_bytes = bytes.fromhex(ct)
key = b"xorKEY" # xor tra ct e flag{
extended_key = (key * (len(ct_bytes) // len(key) + 1))[:len(ct_bytes)] #key * ris divisione intera +1 con slicing parte in eccesso

flag = xor(ct_bytes, extended_key)
print(flag)

#flag{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}