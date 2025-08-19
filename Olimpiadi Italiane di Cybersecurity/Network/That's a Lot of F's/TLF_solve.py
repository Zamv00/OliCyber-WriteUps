import pyshark

cap = pyshark.FileCapture("LotOfF\\net2.pcap", display_filter="eth")

flag = ""

for pkt in cap:
    try:
        eth_type = int(pkt.eth.type, 16)
        if eth_type == 0xffff:
            mac = pkt.eth.dst.replace(":", "") 
            first_byte = mac[0:2]               
            flag += chr(int(first_byte, 16))    
    except AttributeError:
        continue

print(flag)

#flag{5tr4ng3_p4ck3t5}
