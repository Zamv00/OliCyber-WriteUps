Il sito ci da l'opzione di fare un nuovo test e di verificare se l'abbiamo passato tramite la funzione get result:
<img width="420" height="114" alt="immagine" src="https://github.com/user-attachments/assets/a4624bfe-cb34-4ea2-9615-85054796e131" />

<img width="263" height="201" alt="immagine" src="https://github.com/user-attachments/assets/dcb1967e-101f-4b6c-a8a6-6929ca2aa8a6" />

<img width="262" height="150" alt="immagine" src="https://github.com/user-attachments/assets/0add3448-f46b-486e-b8b3-4b04736a7af0" />

Se però diamo uno sguardo al source code di `/record_result`:

<img width="766" height="925" alt="immagine" src="https://github.com/user-attachments/assets/b7bdaf48-b5a4-4639-b34f-ded7cc116ac3" />

Abbiamo un check sull'admin token lato client! ci basta rieseguire i passaggi del controllo per ottenere il token:

`8218d355-38ff-4bc3-9336-adf7f1ba55be`

A questo punto ci basta inserire l'admin token e il test id e selezionare la casella `passed?`

<img width="283" height="214" alt="immagine" src="https://github.com/user-attachments/assets/b0dbaf31-cc0b-48b2-8356-120557575e84" />

**flag{1_l0v3_cl13nt_ch3cks_<3}**
