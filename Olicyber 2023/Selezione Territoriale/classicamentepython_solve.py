flag = "f{anuiraaso_lfltnfi_sin_aime_rotpze_gne_ca_roi}_"

step = 12
final_flag = ""

for start in range(step): #da 0 a 11
    i = start # i parte da un punto diverso man mano che andiamo avanti
    while i < len(flag):
        final_flag += flag[i] 
        i += step #un carattere ogni 12

print(final_flag)
    


#flag{finalmente_un_cifrario_a_trasposizione}