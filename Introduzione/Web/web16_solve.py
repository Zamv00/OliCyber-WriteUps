from bs4 import BeautifulSoup
import requests

l = {}
site = "http://web-16.challs.olicyber.it"
p = [""] #tutte le sottopagine
while True:
    for pos in p: #per ogni sottopagina
        r = requests.get(site + pos) #prendiamo le info
        print(site+pos)
        soup = BeautifulSoup(r.text, "html.parser")
        if "flag" in r.text: #se c'è la flag
            print(soup.find('h1'))
            exit(0)
        print(soup.find('h1'))
        for i in soup.find_all("a", href=True):
            if i['href'] not in l:
                l[i['href']] = True
                p.append(i['href'])
                r.close()

#flag{n0wh3r3_i5_54f3}