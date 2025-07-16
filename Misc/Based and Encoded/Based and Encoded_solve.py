#da/a esadecimale
#da/a binario
#da/a base64
from pwn import *
import json
import re
from base64 import b64decode, b64encode

host = "based.challs.olicyber.it"
port = 10600
r = remote(host,port)

#grazie alan bovo
def bin_to_str(x):
    x = x.lstrip("0")
    my_int = int(x, 2)
    return my_int.to_bytes((my_int.bit_length() + 7) // 8, 'big')
 
i = 0
while True:
    try:
        data = r.recvuntil(b"Ora dammi una risposta!", timeout=2).decode()
    except EOFError:
        print("Connessione chiusa dal server.")
        break
    except:
        data = r.recv(timeout=2).decode() #grazie chat gpt
        print("flag:")
        print(data)
        break

    print(data)
    match = re.search(r'"message"\s*:\s*"([^"]+)"', data, re.DOTALL)
    if match is None:
        continue

    msg = match.group(1)
    print("messaggio:", msg)
    
    if "da esadecimale" in data:
        print("da esadecimale")
        answer = bytes.fromhex(msg).decode()
    
    elif "da binario" in data:
        print("da binario")
        answer = bin_to_str(msg).decode()
    
    elif "da base64" in data:
        print("da base64")
        answer = base64.b64decode(msg).decode()

    elif "a esadecimale" in data:
        print("a esadecimale")
        answer = msg.encode().hex()
    
    elif "a binario" in data:
        print("a binario")
        answer = ''.join(format(ord(c), '08b') for c in msg)
        answer = answer.lstrip("0") #grazie hexid0818
    
    elif "a base64" in data:
        print("a base64")
        answer = base64.b64encode(msg.encode()).decode()    

    print(f"Domanda {i} conclusa")
    output = {"answer": answer}
    print(output)
    json_output = json.dumps(output)
    r.sendline(json_output.encode())
    i+=1

r.interactive()

#flag in ottale
#oct_string = "146 154 141 147 173 144 063 143 060 144 063 137 164 150 061 163 137 060 156 137 146 060 162 137 163 061 172 063 137 155 162 137 142 060 156 144 175"
#flag = ''.join([chr(int(x, 8)) for x in oct_string.split()])
#print(flag)
#flag{d3c0d3_th1s_0n_f0r_s1z3_mr_b0nd}
