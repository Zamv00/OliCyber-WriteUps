La challenge ci fornisce un file execute-me, lo rendiamo eseguibile con chmod +x execute-me solo per scoprire che la flag non si trova nell'eseguibile.
Usiamo binwalk con l'opzione -e per estrarre un .mp3 dall'eseguibile, lo eseguiamo una seconda volta sul file listen-to-me.mp3 e otteniamo un file scan-me.png.
Scansionando il qr code otteniamo la flag:
**flag{b1nw4lk_i5_ur_fr13nd===}**
