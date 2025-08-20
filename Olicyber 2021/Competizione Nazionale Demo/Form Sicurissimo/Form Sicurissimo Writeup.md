Aprendo il pcap, notiamo subito una GET particolare:

<img width="1511" height="457" alt="image" src="https://github.com/user-attachments/assets/16309033-9a20-47cf-ba52-224605629329" />

Possiamo quindi filtrare con `tcp.port == 1234`

Ci ritroviamo 126 pacchetti, ma molti contengono all'interno il messaggio che indica che la flag non è corretta, ci basta cercare quello in cui invece ci sia un messaggio di successo

<img width="461" height="506" alt="image" src="https://github.com/user-attachments/assets/644094bc-109b-4599-9df4-80026654cc3d" />

"fmcj{yo_ackyzb_ihruvcvjam}"

adesso ci basta ruotare ogni carattere di -i per ottenere la flag

**flag{ti_stanno_tracciando}**
