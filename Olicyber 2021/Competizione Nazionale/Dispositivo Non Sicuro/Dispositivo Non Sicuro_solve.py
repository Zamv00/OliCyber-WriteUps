import pyshark

cap = pyshark.FileCapture("capture.pcapng", display_filter="dns")
d = {}

for p in cap:
    q = p.dns.qry_name.lower() 
    if "attacker.eve" in q: # prendiamo i dati in hex utili per ricostruire lo zip
        l = q.split(".")
        d[int(l[0],16)] = "".join(l[1:-2]) # convertiamo in int il primo pezzo del dns.qry_name, associamo ad ogni indice i dati in hex (togliendo il primo e gli ultimi 2 pezzi)

h = "".join(d[k] for k in sorted(d)) #ordina
data = bytes.fromhex(h)

open("out.bin","wb").write(data)

# flag{i5_dns_th3_new_c4vall0_di_7r01a?}