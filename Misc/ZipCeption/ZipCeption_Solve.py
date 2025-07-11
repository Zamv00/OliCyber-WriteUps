import zipfile
import os

current_zip = "flag3000.zip" #file da cui partiamo

for i in range(3000, -1, -1):
    print(f"estraendo {current_zip}...")

    with zipfile.ZipFile(current_zip, 'r') as z: #apriamo file in modalita lettura e estraiamo
        z.extractall()
        next_files = z.namelist() # lista con tutti i file estratti

    if len(next_files) == 0:
        print("zip vuoto.")
        break

    current_zip = next_files[0]  # aggiorna per la prossima iterazione considerando lo zip come il primo file estratto

print("\nFlag estratta, apri il file finale")
#flag{Un0_z1p_d3n7r0_un0_z1p_1mp0551b1l3!}
