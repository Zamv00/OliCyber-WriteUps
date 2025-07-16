Altra challenge che ci presenta una pagina di login:

<img width="642" height="240" alt="immagine" src="https://github.com/user-attachments/assets/81e036f2-944a-4bc4-bff7-404196c269cb" />

Possiamo registrarci o fare login, ma se osserviamo il source code notiamo subito che la parte interessante è in register.php:

<img width="897" height="320" alt="immagine" src="https://github.com/user-attachments/assets/49644f6e-5cb3-4888-b9e2-a96f1cfe1b0e" />

In particolare, quando ci registriamo viene eseguita la query ```"INSERT INTO users(username,password,admin) VALUES ('" . $username . "','" . $password . "',false);";```

Notiamo subito che di default admin viene impostata a false, il nostro compito è di trovare un modo per far si che venga impostata a true

usiamo quindi la seguente query in register.php:

username: ```username', 'password', true) --``` 

password: qualsiasi

in questo modo admin verrà impostata a true, e effettuando il login otterremo la flag:

<img width="1362" height="385" alt="immagine" src="https://github.com/user-attachments/assets/a2b57e4d-311b-47d4-9e19-17be215445f6" />

**flag{c0me_se1_div3ntato_admin}**
