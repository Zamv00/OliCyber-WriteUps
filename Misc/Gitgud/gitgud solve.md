La challenge ci fornisce un semplice file zip: gitgud.zip

Estraendolo, troviamo al suo interno 4 file:

```main.py ilovegraphicdesign.png key.txt README.md```

I file non hanno però al loro interno un contenuto realmente interessante, compreso main.py.

<img width="1307" height="718" alt="immagine" src="https://github.com/user-attachments/assets/45a4c3d7-c699-4e9a-8f65-8d97053d1d0d" />

Come suggerisce però il nome della challenge, se osserviamo tutto il contenuto della cartella con ls -a, notiamo una cartella .git, con il comando git log vediamo che ci sono stati diversi cambiamenti al file main.py

<img width="747" height="404" alt="immagine" src="https://github.com/user-attachments/assets/88df0de4-7845-46a2-a4bb-ae442f2e6e6f" />

Osserviamo il contenuto di main.py in un vecchio commit, e troviamo la flag:

<img width="678" height="681" alt="immagine" src="https://github.com/user-attachments/assets/54dc134d-37a7-4000-8f06-871794dbbf70" />

**flag{0h_n0_my_4p1_k3y}**



