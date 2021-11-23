n = int(input())

nums = list(map(int, input().split()))
neg_count = 0
wildcard = 0
total = 0
for num in nums:
    if num >= 1:
        total += num - 1
    elif num <= -1:
        neg_count += 1
        total += -1 - num
    else:
        total += 1
        wildcard += 1
print(total + ((2 * (neg_count % 2)) if wildcard == 0 else 0))