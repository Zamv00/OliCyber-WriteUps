import requests
site = "http://web-07.challs.olicyber.it/"
headers = requests.head(site)
print(headers.headers)

#flag{r0gu3_m374d474}