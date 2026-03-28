import pyshark

cap = pyshark.FileCapture(r"C:\Users\Samuele\Documents\FIles Olicyber\dominio non sospetto\dominio_non_sospetto.pcap", display_filter="""frame contains "snakectf" """)

ripetizione = []
d = {}
flag = ""

for pkt in cap:
    name = pkt.dns.qry_name.split(".")[0]
    index, flag_piece = name.split("-")
    if not ripetizione or flag_piece != ripetizione[-1]: #lista non vuota e flag_piece non ripetuto
        ripetizione.append(flag_piece)
        d[int(index)] = flag_piece

flag = "".join(d[i] for i in sorted(d))
print(flag)

#flag{ecco_un_esfiltrazione_dns}
