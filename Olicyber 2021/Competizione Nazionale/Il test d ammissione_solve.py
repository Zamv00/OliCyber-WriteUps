from pwn import remote, context

def solve():
    resp = b""
    for i,m in enumerate(mosse):
        cur_level = stato[m[0]]
        assert all([stato[mi] == cur_level for mi in m])
        for _ in range(cur_level, 5):
            resp += str(i+1).encode() + b" "
    return resp

with remote("test1.challs.olicyber.it", 15004) as r:
    # context.log_level = 'debug'
    r.recvlines(20)

    livello = r.recvline().decode()
    while livello.startswith("Livello"):
        print(f"\r{livello}", end = "")
        stato = [int(_) for _ in r.recvline(False).decode().split()]
        mosse = []
        while True:
            s = r.recvline(False).decode()
            if s == "":
                break
            mosse.append(["ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(_) for _ in s.split()])
        res = solve()
        r.sendline(res)
        r.recvlines(2)
        livello = r.recvline().decode()
        print(livello)

    r.interactive()


#flag{questo_era_facile}