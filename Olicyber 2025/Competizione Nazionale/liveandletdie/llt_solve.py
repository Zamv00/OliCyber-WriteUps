from scapy.all import rdpcap, IP, ICMP

packets = rdpcap(r"C:\Users\sansf\OliCyber-WriteUps\Olicyber 2025\Competizione Nazionale\liveandletdie\llt.pcap")

ttl_values = []
flag = ""

for pkt in packets:
    if IP in pkt and ICMP in pkt:
        if pkt[IP].dst == "172.67.157.96": # ttl diverso dagli altri
            ttl_values.append(pkt[IP].ttl)

for ttl in ttl_values:
    flag += chr(ttl)
print(flag)

#flag{t1me_to_liv3_7im3_t0_d1e_3c286cdd}
