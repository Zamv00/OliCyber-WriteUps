import requests

site = "http://headache.challs.olicyber.it/"

r = requests.get(site)
print(r.headers['flag'])

#flag{s0no_1nc4strato_nell_h3ader}
