Collegandoci al servizio con ncat ci si presenta questo:

<img width="150" height="40" alt="immagine" src="https://github.com/user-attachments/assets/c5c130d8-90f6-426c-b57c-fb29571aff05" />

Osservando il pcap, notiamo che nei pacchetti TCP ce ne sono alcuni nel quale il server restituisce "LOGIN SUCC"
Ci basta aspettare di ricevere NONCE con lo stesso numero di uno dei pacchetti dove viene restituito "LOGIN SUCC"

<img width="480" height="124" alt="immagine" src="https://github.com/user-attachments/assets/8133b214-3356-4054-877e-790deb3d57b6" />


<img width="624" height="123" alt="immagine" src="https://github.com/user-attachments/assets/709bfeb5-7635-48b1-afdc-24a03fa2f444" />

**flag{i7s_l1k3_My_iP0ds_s7ucK_oN_R3P14y}**


