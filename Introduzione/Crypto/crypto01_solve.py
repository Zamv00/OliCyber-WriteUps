enc_flag = [102, 108, 97, 103, 123, 117, 103, 104, 95, 78, 117, 109, 66, 51, 114, 53, 95, 52, 49, 114, 51, 52, 100, 121, 125]
flag = ""
for char in enc_flag:
    flag += chr(char)

print(flag)

#flag{ugh_NumB3r5_41r34dy}