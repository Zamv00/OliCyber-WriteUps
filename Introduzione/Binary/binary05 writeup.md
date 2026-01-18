Analizziamo il binario con ghidra e osserviamo la funzione main:

<img width="518" height="692" alt="immagine" src="https://github.com/user-attachments/assets/6ef835a3-86e0-4362-acef-29a678c93804" />

La parte che ci interessa della funzione è in realtà principalmente il ciclo for che possiamo immaginare così:

``` for (int i = 0; i < 14; i++) { ```

```   var[i] = flag[i * 2]; ```

``` } ```

Possiamo da qui capire che ci interessa ogni carattere pari della variabile flag.

Adesso ci basta cercarla su ghidra:

<img width="774" height="633" alt="immagine" src="https://github.com/user-attachments/assets/4b8044f3-c161-439a-9f9f-9ab788cfce23" />

Notiamo che tra ogni carattere "effettivo" della flag c'è un byte 00 (spazio), ci basta quindi prendere gli altri:

```66 6c 61 67 7b 38 31 37 35 30 65 36 33 7d```

<img width="929" height="531" alt="immagine" src="https://github.com/user-attachments/assets/374c42eb-ddcd-4173-bcf6-ab0929ca78fd" />


**flag{81750e63}**
