Il sito presenta diverse pagine, se andiamo a admin.html abbiamo la possibiltà di inserire la password, che risulta sempre sbagliata.

Se però osserviamo il source code:

<img width="767" height="145" alt="immagine" src="https://github.com/user-attachments/assets/3c46b9df-b5e0-4456-9f85-18c4fabf9a3f" />

Possiamo qui modificare da `<form action="javascript:login('regular_user')">` a `<form action="javascript:login('admin')">`

Essendo il check client side, questa semplice modifica ci permette di fare il login anche senza sapere la password, ottenendo la flag:

<img width="405" height="156" alt="immagine" src="https://github.com/user-attachments/assets/f7279cb9-f885-453e-a580-9660865b0ec2" />

**flag{cl13nt_5id3_l0g1n_m4k3s_m3_s4d}**
