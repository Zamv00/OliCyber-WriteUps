La challenge ci fornisce un servizio per comprare e vendere "PGCoin", ogni PGCoin vale 10€, e il nostro saldo iniziale è di 100€, mentre la flag costa 110€.

Ci viene inoltre dato il source code in php:

<img width="830" height="498" alt="immagine" src="https://github.com/user-attachments/assets/6e231cff-24df-4522-b5ff-0f90c771b847" />

Notiamo subito che i controlli su saldo e PGCoin vengono effettuati in maniera errata poichè solo dopo uno `sleep(2)` viene effettivamente aggiornato il saldo, il che rende il servizio vulnerabile a race condition:

Possiamo quindi utilizzare Burp Suite per gestire le richieste:

Compriamo quindi 1PGCoin, che porta il nostro saldo a 90€ e il numero di nostri PGCoin a 1.

Per ottenere più soldi dobbiamo adesso trovare un modo per vendere più PGCoin di quanti ne abbiamo realmente, e il modo più facile è quindi di intercettare la richiesta di vendita:

<img width="1411" height="732" alt="immagine" src="https://github.com/user-attachments/assets/9af17829-3184-4113-9c46-551999c571d6" />

Se la inviamo al repeater 2 volte avremo quindi 2 richieste di vendita possedendo un solo PGCoin.

Ed è proprio qui possiamo sfruttare lo `sleep(2)`, se infatti adesso inviamo entrambe le richieste contemporaneamente,
il controllo `if ($user['coins'] === 1) sleep(2)` passerà, in quei 2 secondi, 2 volte, portando il nostro saldo a 110€ e i nostri PGCoin a -1

<img width="920" height="603" alt="immagine" src="https://github.com/user-attachments/assets/1fc58d6b-5790-4c45-a6b3-44fede3431c4" />

A questo punto non ci resta altro da fare che acquistare la flag!:

<img width="739" height="141" alt="immagine" src="https://github.com/user-attachments/assets/597f439d-6704-4496-ad61-30f300673578" />

**flag{A_R4ce_c0nd1t10n_in_a_trading_system!?}**
