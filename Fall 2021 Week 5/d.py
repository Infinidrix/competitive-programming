from collections import Counter
t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    counts = Counter(list(map(lambda x: (k - (int(x) % k)) % k, input().split())))
    maxi = max_val = 0
    for key, val in counts.items():
        if key == 0:
            continue
        if maxi < val - 1:
            max_val = key + 1
            maxi = val - 1
        elif maxi == val - 1:
            max_val = max(max_val, key + 1)
    print(k * maxi + max_val)