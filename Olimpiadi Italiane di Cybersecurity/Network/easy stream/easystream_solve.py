import pyshark

cap = pyshark.FileCapture("easy_stream.pcapng", display_filter="http") #Apriamo il file pcap filtrando solo i pacchetti http

for pkt in cap: #per ogni pacchetto
    if hasattr(pkt.http, "file_data"): #controlla se il pacchetto contiene contenuto del corpo http
        chunk = bytes.fromhex(pkt.http.file_data.replace(":", "")) #rimuove i : dall'hex e converte in bytes
        text = chunk.decode(errors="ignore") # decodifica in stringa

        if "flag{" in text:
            print(text)

#flag{1sto3asy}
