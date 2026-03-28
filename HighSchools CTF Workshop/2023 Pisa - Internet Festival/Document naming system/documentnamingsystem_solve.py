import pyshark

cap = pyshark.FileCapture(r"C:\Users\Samuele\Documents\FIles Olicyber\document naming system\document_naming_system.pcapng", display_filter="dns")
flag = ""

for pkt in cap:
    name = pkt.dns.qry_name
    if "attacker" in name:
        flag += name.split(".")[0]

print(flag)
#flag{3vil_dns_s3rv3r!}
