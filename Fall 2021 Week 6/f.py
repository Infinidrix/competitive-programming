l = list(map(int, input().split()))
l.sort()
b, g, r = l
total = 0
while r > 0 and g > 0 and r + g >= 3:
    add = min(r // 2, g)
    total += add
    r -= add * 2
    g -= add
    r, g, b = max(r, g, b), (r+b+g) - max(r, g, b) - min(r, g, b), min(r, g, b)
    
if r == b == g == 1:
    total += 1
print(total)