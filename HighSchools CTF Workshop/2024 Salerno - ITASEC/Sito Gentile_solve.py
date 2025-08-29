import requests

site = "http://sitogentile.challs.olicyber.it/"

r = requests.get(f"{site}/talk").headers

flags = {int(k.split("-")[-1]): v for k, v in r.items() if k.startswith("X-Flag")}
flag = "".join([flags[i] for i in sorted(flags.keys())]) #grazie gpt

print(flag)
#ITASEC{th3_1nt3rn3t_w0rk5_1n_my5t3r10us_w4ys}