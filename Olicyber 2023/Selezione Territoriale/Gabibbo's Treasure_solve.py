import requests

site = "http://treasure.challs.olicyber.it/"

flag = requests.get(f"{site}/flag?password=Belandi, dammi la flag!").text
print(flag)

#flag{cl13nt_s1d3_p4ssw0rds_4r3_m0r3_3ff1c13nt}