La challenge si presenta così:

<img width="572" height="339" alt="immagine" src="https://github.com/user-attachments/assets/45a7db0f-797e-4fe7-a508-35af9e2800f5" />

Possiamo infatti inserire un username, e ottenere una password. Se però proviamo a cambiare quella dell'admin...

<img width="301" height="23" alt="immagine" src="https://github.com/user-attachments/assets/588f5e85-891d-43e0-8104-cd3f6ffeb671" />

Un dettaglio importante è però come viene gestito il cambio della password, se infatti inseriamo come username "user" veniamo portati a questo url: "http://password-changer.challs.olicyber.it/change-password.php?token=dXNlcg=="

Ci interessa in particolare l'ultima parte: token=dXNlcg==

Infatti:

<img width="1525" height="589" alt="immagine" src="https://github.com/user-attachments/assets/389b9491-39ca-49e0-a7d5-9c72a833e94c" />

Il token è semplicemente la codifica in base64 dell'username da noi inserito!

Ci basta a questo punto inserire nel token "YWRtaW4=" (cioè admin in base64) per ottenere la flag:

<img width="1029" height="90" alt="immagine" src="https://github.com/user-attachments/assets/69ca40b4-5dee-4d60-9a0b-c0a167b6088f" />

**flag{0h_n0_y0u_c4n_m0d1fy_urls}**
