from base64 import b64decode


enc_1 = "ZmxhZ3t3NDF0XzF0c19hbGxfYjE="
enc_2 = 664813035583918006462745898431981286737635929725

flag_1 = b64decode(enc_1)
n_bytes = (enc_2.bit_length() + 7) // 8
flag_2 = enc_2.to_bytes(n_bytes, 'big')
flag = flag_1+flag_2
print(flag)

#flag{w41t_1ts_all_b1ts?_4lw4ys_H4s_b33n}