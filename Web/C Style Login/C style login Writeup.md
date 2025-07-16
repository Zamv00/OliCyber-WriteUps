La challenge presenta l'ennesima pagina di login:

<img width="593" height="420" alt="immagine" src="https://github.com/user-attachments/assets/43033e13-1da3-49dd-8d91-954d8cab543f" />

questa volta però ci fornisce anche il source code, di cui ci interessa una parte specifica:

<img width="399" height="132" alt="immagine" src="https://github.com/user-attachments/assets/5bff71ec-b43e-4e9f-844d-b495f4275b5b" />

Cosa succede? viene effettuato un controllo con strcmp() tra la password da noi inserita e la vera password, e se va a buon fine viene stampata la flag.

In realtà però questo tipo di controllo con strcmp() non è molto sicuro, infatti in PHP se viene inviato un array vuoto come parametro alla funzione, il confronto causerà un errore (“Array to string conversion”) e PHP ritornerà NULL.

Ci basta quindi inviare password[] : qualcosa per far si che il confronto diventi NULL == 0, che in loose comparison (come in questo caso) risulterà vero!

<img width="546" height="207" alt="immagine" src="https://github.com/user-attachments/assets/9450fe35-58fb-4c8f-9b59-ba60f80c9269" />

**flag{strcmp_1s_n0t_s0_s4f3}**

