import requests

site = "http://xorlandia.challs.olicyber.it/"

c_hex = "2e35233a272114063e1a06103d0d3804131c030e1c38150d36013d0202000c1a3d01301f0e1036003d0a16140305113d1b083e03481f"
cipher = bytes.fromhex(c_hex)

plain = b"ITASEC{"
key = bytes([c ^ p for c, p in zip(cipher, plain)]).decode()
print(key)

flag = requests.post(f"{site}/api/xor", json = {"key" : key, "text" : "2e35233a272114063e1a06103d0d3804131c030e1c38150d36013d0202000c1a3d01301f0e1036003d0a16140305113d1b083e03481f"})
print(flag.text)

#ITASEC{a_xor_b_equals_to_c_means_c_xor_b_equals_to_a!}