Se inviamo `curl -v -X OPTIONS https://training-camp.challs.olicyber.it/ -i` notiamo

<img width="465" height="110" alt="immagine" src="https://github.com/user-attachments/assets/8f495122-ef51-4273-b119-722749199352" />

Possiamo quindi inviare una richiesta con header custom per trovare la flag:

`curl.exe -v https://training-camp.challs.olicyber.it/ -H "X-Secret-Message: hello"`

**flag{h34d4r5_4r3_n07_s3cr375!}**
