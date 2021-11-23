a, b, c, d = list(map(int, input().split()))

factor = (1 - a/b) * (c/d)
miss = (1 - a/b) * (1 - c/d)
probs = [(miss ** (i - 1)) * factor for i in range(1, 10000)]
print(1 - sum(probs))