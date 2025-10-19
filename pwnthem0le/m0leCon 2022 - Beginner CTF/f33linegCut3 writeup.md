Se inseriamo l'immagine su aperisolve notiamo subito un commento particolare:

``` 010101000110100001100101010011010110100101100111011010000111010001111001010100000110000101110111 ```

Che convertito in ascii da -> ``` "TheMightyPaw" ```

La challenge non è però finita qui, se infatti proviamo un semplice ```steghide extract -sf selfie.jpeg``` troveremo subito un message.zip

Se lo estriamo usando come password "TheMightyPaw" troveremo la flag in flag.txt

**ptm{n33d_M0r3_c4TN1p_b0ss}**