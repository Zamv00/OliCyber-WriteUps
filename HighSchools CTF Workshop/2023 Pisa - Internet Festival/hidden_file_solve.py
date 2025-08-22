import requests

site = "http://hidden-file.challs.olicyber.it/"
#guardiamo robots.txt per notare qualcosa di interessante

r = requests.get(f"{site}/39185d1b78d1cec390b777d9e82c01a3/79df7045bba0bcb6303752558412f300.txt").text
print(r)

#flag{well_not_really_a_security_challenge_but_somewhere_you_need_to_start!}