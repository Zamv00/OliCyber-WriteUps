import requests
import re

site = "http://vuoto.challs.olicyber.it/"

html = requests.get(site).text
css = requests.get(f"{site}/css/style.css").text
js = requests.get(f"{site}/js/script.js").text

#grazie chat gpt
def extract_flag(text):
    match = re.search(r'flag\{.*?"(.*?)"', text)
    if match:
        return match.group(1)
    match = re.search(r'"(.*?)"', text)
    if match:
        return match.group(1)
    return ""


first_piece = extract_flag(html)
second_piece = extract_flag(css)
third_piece = extract_flag(js)

flag = f"{first_piece}{second_piece}{third_piece}"
print(flag)
#flag{you_can_t_see_me_in_the_browser}
