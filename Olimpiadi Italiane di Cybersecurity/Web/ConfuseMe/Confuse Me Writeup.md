C'è un campo di input, la parte interessante del source code è questa:

<img width="421" height="153" alt="immagine" src="https://github.com/user-attachments/assets/4c3021ce-e79e-4f74-bce0-68395dd349b1" />

La loose comparison è il problema principale, PHP infatti effettua type juggling durante il confronto, ci basta quindi inserire una stringa (che inizi con 0e) il cui hash inizi a sua volta con 0e

In questo modo, PHP li vedrà entrambi come numeri in notazione scientifica, rendendo il confronto 0 == 0 True, restituendo la flag:

**flag{0mg_php_c0mp4r150n_r34lly_5uck5}**
