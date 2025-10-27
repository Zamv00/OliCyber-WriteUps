#chat gpt
import sys
from PIL import Image

ROUNDS = 42

def load_grid(path):
    img = Image.open(path).convert("L")
    w, h = img.size
    # threshold to be robust vs exact 0/255
    grid = [[1 if img.getpixel((x, y)) < 128 else 0 for x in range(w)] for y in range(h)]
    return grid, w, h

def forward_block(b):
    # b = (c00, c01, c11, c10)
    s = sum(b)
    if s == 2:
        return b
    if s == 3:
        # rotate (c10,c00,c01,c11) then invert
        c = (b[3], b[0], b[1], b[2])
        return tuple(x ^ 1 for x in c)
    # s in {0,1,4}: invert all
    return tuple(x ^ 1 for x in b)

def build_inv_map():
    m = {}
    for x in range(16):
        b = tuple((x >> k) & 1 for k in (3, 2, 1, 0))  # (c00,c01,c11,c10)
        m[b] = forward_block(b)
    inv = {v: k for k, v in m.items()}
    if len(inv) != 16:
        raise RuntimeError("Mapping not invertible")
    return inv

def inverse_round(grid, w, h, round_no, inv_map):
    off = (round_no - 1) % 2
    for j in range(0, h, 2):
        for i in range(0, w, 2):
            y = (off + j) % h
            x = (off + i) % w
            b = (
                grid[y][x],
                grid[y][(x + 1) % w],
                grid[(y + 1) % h][(x + 1) % w],
                grid[(y + 1) % h][x],
            )
            orig = inv_map[b]
            grid[y][x] = orig[0]
            grid[y][(x + 1) % w] = orig[1]
            grid[(y + 1) % h][(x + 1) % w] = orig[2]
            grid[(y + 1) % h][x] = orig[3]

def save_grid(grid, w, h, path):
    out = Image.new("L", (w, h))
    px = out.load()
    for X in range(w):
        for Y in range(h):
            px[X, Y] = 0 if grid[Y][X] == 1 else 255
    out.save(path)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 recover.py input.png [output.png]")
        sys.exit(1)
    inp = sys.argv[1]
    outp = sys.argv[2] if len(sys.argv) > 2 else "flag_recovered.png"

    grid, w, h = load_grid(inp)
    inv_map = build_inv_map()

    for r in range(ROUNDS, 0, -1):
        inverse_round(grid, w, h, r, inv_map)

    save_grid(grid, w, h, outp)
    print(f"Done -> {outp}")

if __name__ == "__main__":
    main()
 