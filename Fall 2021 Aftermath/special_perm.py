t = int(input())

for _ in range(t):
    n, a, b = list(map(int, input().split()))
    if a > b and a - b > 1:
        print("-1")
        continue
    if a > b:
        first = [i for i in range(a, n + 1)]
        second = [i for i in range(1, b + 1)]
    else:
        first = [i for i in range(n, b, -1)] 
        second = [i for i in range(1, a)]
        first.append(a)
        second.append(b)

    # print(first, second)
    for i in range(a + 1, b):
        if len(first) > len(second):
            second.append(i)
        else:
            first.append(i)
    if len(first) > n / 2 or len(second) > n / 2:
        print("-1")
    else:
        first.extend(second)
        print(" ".join(map(str, first)))
    # print("Over")
