t = int(input())

for i in range(t):
    n = int(input())
    prev = 0
    nums = list(map(int, input().split()))

    for i, num in enumerate(nums):
        count = max(num, prev)
        if count == 0:
            print(chr(ord('a') + 1 + ((i) % 25)))
        else:
            print('a' * count)
        prev = num
    if prev != 0:
        print("a" * prev)
    else:
        print(chr(ord('a') + 1 + ((len(nums)) % 25)))
