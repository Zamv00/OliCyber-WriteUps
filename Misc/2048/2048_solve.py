from pwn import *
import re
#SOMMA, DIFFERENZA, DIVISIONE_INTERA,POTENZA,PRODOTTO
host = "2048.challs.olicyber.it"
port = 10007
r = remote(host,port)
data1 = r.recvuntil(b":").strip().decode()
i = 0
while True:
    try:
        data2 = r.recv(1024).strip().decode()
        numeri = list(map(int, re.findall(r"-?\d+", data2)))

        if "SOMMA" in data2:
            risultato = sum(numeri)
        elif "DIFFERENZA" in data2:
            risultato = numeri[0] - numeri[1]
        elif "DIVISIONE_INTERA" in data2:
            risultato = numeri[0] // numeri[1]
        elif "POTENZA" in data2:
            risultato = pow(numeri[0], numeri[1])
        elif "PRODOTTO" in data2:
            risultato = numeri[0] * numeri[1]

        r.sendline(str(risultato).encode())
        print(f"{i}: Ho inviato {risultato}")
        i+=1

    except Exception as e:
        print("Flag trovata!")
        print(data2)
        break

flag = r.recvline().decode().strip()
print(flag)

