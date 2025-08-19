Il sito ci fornisce una pagina di login/register, ed il backend è scritto interamente in ruby, ci sono alcuni punti particolarmente interessanti:

<img width="386" height="180" alt="immagine" src="https://github.com/user-attachments/assets/a2523327-9769-4a42-98ec-cabd96b454b7" />


<img width="750" height="144" alt="immagine" src="https://github.com/user-attachments/assets/a9d6e9f3-1c4c-4d68-9f65-4bbce16c7c10" />

Succede qualcosa di strano, inviando una post vuota a ```/admin/init``` il sito ci restituisce uno username con il valore ```is_admin = 1``` nel formato ```{"username" : "admin-1234"}```

Possiamo provare a registrarci utilizzando il nome fornitoci in risposta alla post e una password a scelta, e poi ad effettuare il login.

Successivamente, la funzione ```check_login()``` controlla se esiste un utente con quel nome e quella password partendo dal più recente (```ORDER BY id DESC LIMIT 1```):
<img width="852" height="107" alt="immagine" src="https://github.com/user-attachments/assets/95f27172-f215-407d-912a-79ad1411ec97" />

La funzione ```is_admin``` però, prende in ingresso lo username da noi inserito, ma controlla il primo elemento presente nella tabella (```LIMIT 1```), incontrando effettivamente la variabile ```is_admin = 1```:
<img width="663" height="96" alt="immagine" src="https://github.com/user-attachments/assets/a5629c55-cc7e-439a-b784-219312adfdbd" />

<img width="1867" height="944" alt="immagine" src="https://github.com/user-attachments/assets/fe40dae5-c441-440d-8845-27d48dd58162" />

**flag{s1mpl3r_th4n_3xp3ct3d_but_ruby_1s_c00l_y34h}**

