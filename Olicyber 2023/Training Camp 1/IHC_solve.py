from pwn import *
import re

HOST = "ihc.challs.olicyber.it"
PORT = 34008

flag = ""

r = remote(HOST,PORT)
r.recvuntil(b"invio!")
r.sendline()

while True:
    try:
        text = r.recvuntil(b"Risposta: ").decode()
    except EOFError:
        print("EOFError")
        break

    if "risultato" in text:
        match = re.search(r'(\d+)\s*([\+\-\*/])\s*(\d+)', text)

        n1 = int(match.group(1))
        op = match.group(2)
        n2 = int(match.group(3))

        if op == '+':
            ris = n1 + n2
        elif op == '-':
            ris = n1 - n2
        elif op == '*':
            ris = n1 * n2
        else:
            ris = n1 // n2

        r.sendline(str(ris).encode())


    elif "Quali" in text:
        s = text.split("stringa ")[1].strip().replace("?", "")
        pos = text.split("[")[1].split("]")[0]
        pos = [int(x) for x in pos.split(", ")]

        ris = ""
        for p in pos:
            ris += s[p-1]
        print(f"Conta lettere, posizioni: {pos}, stringa: {s}")
        r.sendline(ris.encode())

    elif "Restituiscimi" in text:
        s = text.split(":")[1].strip().replace("?", "")
        rs = s[::-1]
        print(f"stringa da fare al contrario: {s}")
        r.sendline(rs.encode())

    else:
        lettera = text.split("lettera ")[1].split(" ")[0]
        stringa = text.split("stringa ")[1].strip()

        i = 0

        for c in stringa:
            if c == lettera:
                i +=1
        print(f"lettera: {lettera}, numero di volte in {stringa}, {i}")
        r.sendline((str(i)).encode())

    data = r.recvuntil(b'\n').decode()
    if 'Corretto' in data:
        print("LETTERA FLAG: ", data)
        flag += data.split(":")[-1].strip()
    if '}' in flag:
        print(f"flag completa: {flag}")
        break


print(flag.replace('\n', ''))

#flag{fl46_m000000000000lTo_LuNg4_p3rCh3_s0n0_m000000000000lTo_5tr0n2o}