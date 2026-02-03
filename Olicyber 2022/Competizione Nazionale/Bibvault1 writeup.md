La challenge ci fornisce una pagina di login e successivamente una home dove scaricare e vedere i file.

Una volta effettuata la registrazione, ci viene fornito un jwt con i seguenti parametri:


```
{
  "username": "zamv",

  "is_admin": 0,
}
```

Nel source code notiamo:

<img width="584" height="175" alt="immagine" src="https://github.com/user-attachments/assets/aecdc1f5-8c70-4640-ac57-51d550a84513" />


Ci basta modificare il jwt (che nel controllo non verifica la firma) per avere 
```username:gabibbo``` e scaricare la flag dai suoi file:

**flag{m41_f1d4rs1_d1_un_d3c0d3}**
