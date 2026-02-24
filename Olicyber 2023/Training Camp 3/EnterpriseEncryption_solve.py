ct = "7971737c7e6d7866646f2c28712e7c2f2f717b402e2b7177292b40772e402a73402f71732f402867407b2c62"

ct = bytes.fromhex(ct)
l = len(ct)

flag = (b''.join(bytes([(x^31), (y^31)]) for x,y in zip(ct[:l//2], ct[l//2:])))
flag =  flag.decode()
print("Flag disordinata: ", flag)

first_part = ""
second_part = ""
third_part = ""
fourth_part = ""
i = 0
for char in flag:
    first_part += flag[i]
    i += 4

    if i >= len(flag):
        break

i = 1
for char in flag:
    second_part += flag[i]
    i += 4

    if i >= len(flag):
        break
i = 2
for char in flag:
    third_part += flag[i]
    i += 4

    if i >= len(flag):
        break

i = 3
for char in flag:
    fourth_part += flag[i]
    i += 4

    if i >= len(flag):
        break


final_flag = first_part + second_part + third_part + fourth_part
print(final_flag)

#flag{3nc0d1n6_15_n07_3ncryp710n_4h4h_l0l_xd}