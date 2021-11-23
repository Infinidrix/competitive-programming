t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))

    inds = list(map(int, input().split()))
    prices = list(map(int, input().split()))
    onInd = [0 for i in range(m)]
    total = 0
    for ind in inds:
        onInd[ind - 1] += 1
        total += prices[ind - 1]

    left = 0 
    end = len(prices) - 1
    while left < end:
        if onInd[end] == 0:
            end -= 1
        else:
            total -= prices[end] - prices[left]
            onInd[end] -= 1
            left += 1
    print(total)

