import requests
from bs4 import BeautifulSoup

site = "http://web-13.challs.olicyber.it/"
req = (requests.get(site)).text

soup = BeautifulSoup(req, "html.parser")
flag = [tag.get_text() for tag in soup.find_all("span", class_= "red")]
flag = "".join(flag)
print(flag)

#flag{donotrecommenddoingthisbyhand}