t = int(input())
colors = [set("ROAP"), set("BPGA"), set("YOGA")]

for i in range(t):
    _ = input()
    painting = input()
    total = 0
    for color in colors:
        curr = 0
        inPainting = False
        for p in painting:
            if p in color and not inPainting:
                curr += 1
                inPainting = True
            elif p not in color:
                inPainting = False
        total += curr
    print(f'Case #{i+1}: {total}')