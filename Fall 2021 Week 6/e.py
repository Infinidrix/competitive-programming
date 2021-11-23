t = int(input())
for i in range(t):
    n, x = list(map(int, input().split()))

    nums = list(map(int, input().split()))

    sorted_nums = sorted(nums)
    start = n - x
    found = False
    for i in range(start, len(nums) - start):
        if nums[i] != sorted_nums[i]:
            print("NO")
            found = True
            break
    if not found:
        print("YES")
