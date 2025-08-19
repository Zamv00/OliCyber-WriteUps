import pyshark

cap = pyshark.FileCapture("udp\chall.pcapng", display_filter="udp")
text = ""

for pkt in cap:
    if "DATA" in pkt:
        data = bytes.fromhex(pkt.data.data.replace(":", ""))
        text += data.decode(errors="ignore")
        
print(text)

#flag{with_UDP_computer_applications_can_send_messages_in_this_c4s3_r3f3rr3d_t0_as_datagr4ms}
