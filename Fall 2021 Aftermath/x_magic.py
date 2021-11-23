def solve(a , b, x):
    a, b = max(a, b), min(a, b)
    while a >= x:
        a, b = max(a, b), min(a, b)
        if b == 0:
            print("NO")
            return
        if (((a - b) % b == x % b and a >= x) or 
            ((b - a) % b == x % b and a >= x) or 
            x == b):
            print("YES")
            return
        else:
            a, b = b, a - b * (a // b)
    print("NO")

t = int(input())

for _ in range(t):
    a, b, x = list(map(int, input().split()))
    solve(a, b, x)