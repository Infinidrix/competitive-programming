def solve(string, a, b):
    a -= string.count("0")
    b -= string.count("1")
    if min(a, b) < 0:
        return -1
    s = list(string)
    left = 0
    right = len(s) - 1
    pairs = 0
    while left < right:
        lc, rc = s[left], s[right] 
        if lc == "?" and rc != "?":
            if rc == '0':
                a -= 1
            if rc == '1':
                b -= 1
            if min(a, b) < 0:
                return -1
            s[left] = rc
        elif rc == "?" and lc != "?":
            if lc == '0':
                a -= 1
            if lc == '1':
                b -= 1
            if min(a, b) < 0:
                return -1
            s[right] = lc
        elif rc == lc == "?":
            pairs += 1 
        elif rc != lc:
            return -1
        left += 1
        right -= 1
    left = 0
    right = len(s) - 1
    while left < right:
        lc, rc = s[left], s[right]
        if rc == lc == "?":
            if a > 1:
                s[left] = s[right] = "0"
                a -= 2
            elif b > 1:
                s[left] = s[right] = "1"
                b -= 2
            else:
                return -1
        left += 1
        right -= 1
    if left == right:
        if a == 1:
            s[left] = "0"
        elif b == 1:
            s[right] = "1"
    return "".join(s)

t = int(input())

for i in range(t):
    a, b = list(map(int, input().split()))
    s = input()
    print(solve(s, a, b))
    