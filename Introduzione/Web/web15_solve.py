from bs4 import BeautifulSoup
import requests

site = "http://web-15.challs.olicyber.it/"
req = (requests.get(site)).text
soup = BeautifulSoup(req, "html.parser")

css_files = [link["href"] for link in soup.find_all("link", rel="stylesheet")]

for css_file in css_files:

    css_file = site + css_file
    css_response = (requests.get(css_file)).text
    print(css_response)

js_files = [script["src"] for script in soup.find_all("script")]

for js_file in js_files:
    js_file = site + js_file
    js_response = (requests.get(js_file)).text
    print(js_response)


#flag{5n00ping_4r0und}
