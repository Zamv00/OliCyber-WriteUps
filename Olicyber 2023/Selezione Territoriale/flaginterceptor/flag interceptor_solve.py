import pyshark

cap = pyshark.FileCapture("C:/Users/sansf/OliCyber-WriteUps/Olicyber 2023/Selezione Territoriale/flaginterceptor/flag-interceptor.pcap", display_filter="tcp && tcp.payload")

streams = {} #dict

for pkt in cap:
    src_ip = pkt.ip.src #memorizziamo ip
    payload_hex = pkt.tcp.payload.replace(":", "")
    payload_bytes = bytes.fromhex(payload_hex)
    payload_text = payload_bytes.decode("ascii", errors="ignore") #testo del tcp stream

    if src_ip not in streams:
        streams[src_ip] = "" #inizializziamo le chiavi (src ip)
    
    streams[src_ip] += payload_text #aggiungiamo il testo associato ad ogni ip
    
cap.close()

for ip, text in streams.items():
    print(f"IP: {ip}")
    clean = text.replace("\n", "").replace("\r", "").replace(" ", "")
    print(clean)

#10.0.0.35
#flag{parsing_pcaps_is_not_that_hard}
      

