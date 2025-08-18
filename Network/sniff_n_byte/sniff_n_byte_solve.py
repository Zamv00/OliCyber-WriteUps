import pyshark

cap = pyshark.FileCapture("sniff_n_byte\sniff_n_byte.pcapng", display_filter="tcp")

hex_string = ""

for pkt in cap:
    if "DATA" in pkt: #pacchetto TCP che contiene dati
        raw = pkt.data.data.replace(":", "")
        chunk = bytes.fromhex(raw).decode() 
        hex_string += chunk


cleaned_string = hex_string.replace("0x", "")
flag = bytes.fromhex(cleaned_string).decode()
print(flag)
#flag{7h3Y_5A0u_c4N_5N1ff_^-^}
