t = int(input())

for i in range(t):
    n, k = list(map(int, input().split()))

    nums = sorted(list(map(int, input().split())))

    total = 0
    moves = n - 1
    for i in range(len(nums) - 1, -1, -1):
        num = nums[i]
        if n - num <= moves:
            total += 1
            moves -= n - num
        else:
            break
    print(total)