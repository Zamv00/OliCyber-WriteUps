import random,string

hex_ct = "088596df93697e62d71cb143352ccb45be15463219c6cc917f9be83c1aa1f7d0217b4586c1058009" 
ct = bytes.fromhex(hex_ct)

def key_gen(k):
    random.seed(k) #stesso comportamento del cifrario
    return bytes([b ^ random.randint(0,255) for b in ct]) #per ogni byte del ct genera un altro byte e fa xor annullando la cifratura
    #la funziona ritorna un plaintext teorico con una delle chiavi

for k in range (256):
    pt = key_gen(k)
    try:
        s = pt.decode('utf-8')
    except UnicodeDecodeError:
        continue
    print(f"key={k} ->", s)

#flag{fl4g_4_c4s0_p3r_un_c1fr4r10_4_c4s0}