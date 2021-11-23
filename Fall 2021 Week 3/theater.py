n, m, t = list(map(int, input().split()))

total = 1
fact = [1] + [ total := total * i for i in range(1, 31)]
ways = 0
for i in range(4, min(n + 1, t)):
    boys = fact[n] // (fact[i] * fact[n - i])
    girls = fact[m] // (fact[t - i] * fact[m - (t - i)])
    ways += boys * girls 
print(ways)