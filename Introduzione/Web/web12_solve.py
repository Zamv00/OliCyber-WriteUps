import requests
from bs4 import BeautifulSoup


site = "http://web-12.challs.olicyber.it/"
req = (requests.get(site)).text

soup = BeautifulSoup(req, 'html.parser')
soup1 = soup.find_all('pre')
print(soup1)

#flag{7h3_14ngu4g3_0f_7h3_w3b}