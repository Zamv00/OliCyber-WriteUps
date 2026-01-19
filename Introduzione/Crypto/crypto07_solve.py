from Crypto.Cipher import DES, AES, ChaCha20
from Crypto.Util.Padding import *
from Crypto import Random

pt = "La lunghezza di questa frase non è divisibile per 8".encode("utf-8") 
cipher = DES.new(bytes.fromhex("a67b7b8306afaadd"), DES.MODE_CBC) 
r = cipher.iv
f = cipher.encrypt(pad(pt, 8, "x923"))
print("des ct: ", f.hex())
print("des iv: ", r.hex())

c_key = Random.get_random_bytes(32)
print("aes key: ", c_key.hex())
plain = b'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'
cipher = AES.new(c_key, AES.MODE_CFB, segment_size=24)
f = cipher.encrypt(pad(plain, 16, "pkcs7"))
print("aes iv: ", cipher.iv.hex())
print("aes ct:", f.hex())

key = bytes.fromhex("9b115c46c0c6197466b4173b7891ff566c9abc615d2b0de10cab9949d796e28d")
cipher = bytes.fromhex("dcc4f58692f02b06c06ea48ce2bde92e6fcbd60330ab6eb07d75f39b")
nonce = bytes.fromhex("2fd67d516a47a9e6")
s = ChaCha20.new(key=key, nonce=nonce)
print("ASCII text: ", s.decrypt(cipher).decode())


#flag{4rt1ficial_Symm3trY_Yrt3mmyS_laicif1tr4}