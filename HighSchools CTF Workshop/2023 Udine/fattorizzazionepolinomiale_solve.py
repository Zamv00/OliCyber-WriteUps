def encrypt(x):
    return (x-1)*(x**2+1)*(x-3)*(x+17)

target = 5444532567301
limit = 65536

for x in range(limit):
    if encrypt(x) == target:
        print("Segreto:", x)
        break

# 350
# flag{f4tt0r1zz4z10n3_p0l1n0mi4l3}