import requests
import re

site = "http://not-a-robot.challs.olicyber.it"

r = requests.get(f"{site}/pl5_d0nt_vi51t_me").text  #robots.txt

match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{robots_will_take_over_the_world}