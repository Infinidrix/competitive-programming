from collections import defaultdict
t = int(input())

for i in range(t):
    input()
    nums = list(map(int, input().split()))
    mean = sum(nums)/len(nums)
    count = defaultdict(int)
    res = 0
    for num in nums:
        res += count[num - mean]
        count[mean - num] += 1
    print(res)