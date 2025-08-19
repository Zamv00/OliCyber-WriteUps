La challenge è un semplice flags shop, in cui abbiamo l'opzione di comprare 3 bandiere:

<img width="1919" height="269" alt="immagine" src="https://github.com/user-attachments/assets/71ed0477-389f-47a7-9828-1192bf373196" />

La "Bandiera anonymous" costa però 1000€, mentre il nostro credito è di 100€

Dando uno sguardo al sorgente, vediamo che ogni bandiera ha associati un id e un costo, in particolare, quella che ci interessa ha id 2:

<img width="630" height="514" alt="immagine" src="https://github.com/user-attachments/assets/83cdabf7-7461-4d01-bf11-d053e485d512" />

Tramite i devtools, (o con BurpSuite), compriamo la Bandiera Italiana, con costo 100, e notiamo che come richiesta abbiamo inviato:

<img width="126" height="53" alt="immagine" src="https://github.com/user-attachments/assets/2609904b-4d89-44fb-8535-944420caa4ee" />

A questo punto ci basta modificare l'id da "1" a "2":

<img width="546" height="99" alt="immagine" src="https://github.com/user-attachments/assets/c302e033-fbbe-4680-8381-163ec628f352" />

**flag{gr4zi3_p3r_l_4cqu1st0}**
