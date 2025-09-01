import requests

site = 'http://flagdownloader.challs.olicyber.it'

flag = ''
n = '0'

while n:
    r = requests.get(site+'/download/flag/'+ n)
    print(r.text[:100]) 
    try:
        j = r.json()
    except Exception as e:
        print("Errore JSON:", e)
        break
    n = j['n']
    flag += j['c']

print("FLAG:", flag)

#flag{la_pazienza_e_la_virtu_dei_forti_3578735382}