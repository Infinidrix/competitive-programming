def solve(nums):
    ahead_zero = 0
    total = 0
    stack = []
    for i, num in enumerate(nums):
        if num == 1:
            if len(stack) != 0:
                j = stack.pop()
                total += i - j
            else:
                j = max(i + 1, ahead_zero)
                while j < len(nums):
                    if nums[j] == 0:
                        ahead_zero = j + 1
                        total += j - i
                        break
                    j += 1
        else:
            stack.append(i)
    return total
n = int(input())
 
nums = list(map(int, input().split()))
print(min(solve(nums), solve(list(reversed(nums)))))
