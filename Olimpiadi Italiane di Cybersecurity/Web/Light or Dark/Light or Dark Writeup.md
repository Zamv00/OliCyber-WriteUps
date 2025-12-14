Inizialmente la challenge ci propone solo l'opzione di cambiare tra tema chiaro e tema scuro

<img width="1871" height="987" alt="immagine" src="https://github.com/user-attachments/assets/d84a5e77-96ef-4c1d-bdb9-10fb9f3abb83" />

Scegliendo un tema tra i due, vediamo il seguente url:

```http://lightdark.challs.olicyber.it/index.php?tema=light.css```

Osservando il codice php notiamo due parti interessanti:
<img width="719" height="445" alt="immagine" src="https://github.com/user-attachments/assets/9b8983dc-b6b0-4d04-a42b-d690136abf02" />

<img width="334" height="59" alt="immagine" src="https://github.com/user-attachments/assets/a7fc80ba-8634-49ff-9ef6-f82860e96aa6" />

Ci serve un modo per fare path traversal a dove si trova la flag (presumibilmente flag.txt) bypassando sia il blocco sul ../ che sull'estensione.

Utilizziamo .../ per salire le directory (. + ./) e facciamo una null byte injection per bypassare il controllo sull'estensione

Il payload finale è ```http://lightdark.challs.olicyber.it/index.php?tema=.../.../.../.../.../flag.txt%00.css```

<img width="435" height="46" alt="immagine" src="https://github.com/user-attachments/assets/d1d912b6-d0ca-46bd-83d5-5ce4e9cefe9a" />

**flag{l1ght_1s_f0r_n00bs_d4rk_1s_f0r_h4ck3rs}**

