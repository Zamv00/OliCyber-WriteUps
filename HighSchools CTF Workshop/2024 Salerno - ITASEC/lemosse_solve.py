import requests

s = requests.session()
site = "http://lemosse.challs.olicyber.it/"

r1 = s.get(f"{site}/step1").text
print(r1)

r2 = s.post(f"{site}/step2", data = {"hello" : "world", "dead" : "beef"}).text
print(r2)

r3 = s.put(f"{site}/step3").text
print(r3)

r4 = s.delete(f"{site}/step4").text
print(r4)

#ITASEC{step1_step2_step3_step4_and_flag}