def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

m1 = "158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf"
m2 = "73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2"

m11 = bytes.fromhex(m1)
m22 = bytes.fromhex(m2)

print(xor(m11, m22))

#flag{x0R_f0r_th3_w1n!}
