Il pcap presenta più di 46k pacchetti, ma come suggeritoci dalla descrizione della challenge, possiamo filtrare quelli interessanti con: `frame contains "ricetta"`

A questo punto ci vengono evidenziati due pacchetti:

<img width="1476" height="110" alt="immagine" src="https://github.com/user-attachments/assets/ddf60679-cf34-4210-b2ab-cf06aee2e2ce" />

Seguendo il flusso del primo:
<img width="764" height="72" alt="immagine" src="https://github.com/user-attachments/assets/86d972d2-b9e5-4314-87f3-a643c0d562fb" />

Seguendo il flusso del secondo:

<img width="574" height="335" alt="immagine" src="https://github.com/user-attachments/assets/13e39d7a-bdc6-483b-ac0b-b46b5c70d682" />

Tramite il contenuto in bytes andiamo a ricostruirci il file zip e lo estraiamo con la password trovata nel primo pacchetto:

**flag{l'1n6r3d13n73_536r370_è_am0r3..e_p4t4t3}**

