def solve(a, b, dp):
    if (a == 1 and b == 1) or min(a, b) == 0:
        return 0
    a, b = max(a, b), min(a, b)
    if (a, b) in dp:
        return dp[(a, b)]
    if b == 1:
        dp[(a, b)] = 1 + solve(a - 2, b + 1, dp)
        return dp[(a, b)]
    dp[(a, b)] = 1 + max(solve(a - 2, b + 1, dp), solve(a + 1, b - 2, dp))
    return dp[(a, b)]

a, b = list(map(int, input().split()))

print(solve(a, b, {}))