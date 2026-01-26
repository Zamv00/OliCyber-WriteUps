import random


def decrypt(data):
    n = 4
    L = len(enc)
    righe = L // n
    cols = []
    for i in range(n):
        cols.append(enc[i*righe : (i+1)*righe])
    res = ""
    for r in range(righe):
        for c in range(n):
            res += cols[c][r]
    return res


enc = "f{anuiraaso_lfltnfi_sin_aime_rotpze_gne_ca_roi}_"
print(decrypt(enc))


#flag{finalmente_un_cifrario_a_trasposizione}
