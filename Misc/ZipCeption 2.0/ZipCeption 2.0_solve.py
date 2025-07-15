import zipfile
import os

current_zip = "100.zip" #zip di partenza
while current_zip.endswith(".zip"): #continuiamo fino a quando non abbiamo il file.txt della flag
    print(f"Estraendo {current_zip}...")

    with zipfile.ZipFile(current_zip, 'r') as z:
        with open("rockyou.txt", "r", encoding = "latin-1") as wordlist: #prendiamo le password da rockyou.txt
            
            for pwd in wordlist:
                password = pwd.strip().encode("utf-8")

                trying_file = z.namelist()[0]

                try:
                    z.open(trying_file, pwd = password).read(1) #proviamo a leggere il file, se non c'è nessun errore abbiamo trovato la password giusta
                    print(f"{current_zip} estratto con password {pwd.strip()}")
                    z.extractall(pwd=password)
                    current_zip = trying_file
                    break
                except Exception as e:
                    print(f"La password {password} non è corretta per il file {current_zip}")
            

if os.path.exists(current_zip):
    with open(current_zip, "r") as final_file:
        flag = final_file.read().strip()
        print(f"Flag: {flag}")


#flag{1snt3asyUnzipTh4t}
