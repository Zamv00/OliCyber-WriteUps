import requests
from bs4 import BeautifulSoup
from bs4 import Comment
site = "http://web-14.challs.olicyber.it/"
def iscomment(tag):
    return isinstance(tag, Comment)

req = (requests.get(site)).text
soup = BeautifulSoup(req, "html.parser")

flag = soup.find_all(string = iscomment)
print(flag)

#flag{50m3b0dy_f0rg07_70_d31373_7hi5}