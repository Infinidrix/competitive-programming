sx, sy, ex, ey = list(map(int, input().split()))

res = []
if sx == ex or sy == ey:
    res.append('1')
else:
    res.append('2')

#bishop
if abs(sx - ex) == abs(sy - ey):
    res.append('1')
elif abs(sx - ex) % 2 == abs(sy - ey) % 2:
    res.append('2')
else:
    res.append("0")
#king
res.append(str(max(abs(sx - ex),abs(sy - ey))))
print(" ".join(res))