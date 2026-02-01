```env | grep -i flag || true``` cerchiamo stringa flag tra le variabili d'ambiente

```for mp in $(awk '$3 !~ /proc|sysfs|tmpfs|devtmpfs/ {print $2}' /proc/mounts | sort -u); do ``` con $() iteriamo nel risultato dell'espressione, che ad ogni interazione viene assegnata alla variabile mp. Il pezzo centrale legge il terzo campo ($3 tipo di filesystem) di /proc/mounts (ci aiuta hint della challenge) e seleziona solo le righe il cui tipo non corrisponde a /proc|sysfs|tmpfs|devtmpfs/ (inutili per la flag), con sort -u eliminiamo i duplicati
```  find "$mp" -xdev -type f -readable -size -128k 2>/dev/null \ ``` adesso cerca il filesystem a partire da mp, leggendo solo file regolari e leggibili con dimensione minore di 128k 
```  -exec grep -Hn --binary-files=without-match "flag{" {} + 2>/dev/null || true ``` esegue il comando su ogni file trovato: grep -Hn (stampa nome file e riga) evita i file binari e cerca la stringa "flag{" nella lista di file
``` done ```


**flag{l1nux_15_4_c0mpl3x_And_4m4Z1ng_cr34Tur3}**
