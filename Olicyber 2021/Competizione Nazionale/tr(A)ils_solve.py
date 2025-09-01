import requests

site = "http://trais.challs.olicyber.it/"

s = requests.session()

mv1 = s.get(f"{site}/api/move/2/2").cookies.text
print(mv1)
mv2 = s.get(f"{site}/api/move/2/1").text
mv3 = s.get(f"{site}/api/move/2/3").text
print(mv3)
