def swap(inds, nums):
    left = 0 
    end = len(inds) - 1
    while left < end:
        nums[inds[left] - 1], nums[inds[end] - 1] = nums[inds[end] - 1], nums[inds[left] - 1]
        left += 1
        end -= 1
    

def solve(nums):
    res = []
    foundOnes = 1
    while foundOnes > 0:
        foundOnes = 0
        foundZeros = 0
        ans = []
        # print(nums)
        for i in range(len(nums) - 1, -1, -1):
            # print(i, nums[i])
            if nums[i] == 0 and foundOnes == 0:
                # print("Got here")
                foundZeros += 1
                ans.append(i + 1)
            if foundZeros > foundOnes and nums[i] == 1:
                foundOnes += 1
                ans.append(i + 1)
            if foundZeros == foundOnes and foundOnes > 1:
                res.append(sorted(ans))
                # print(ans)
                swap(ans, nums)
                ans = []
                foundOnes = 0
                foundZeros = 0
                break
        if foundOnes > 0:
            res.append(sorted(ans))
            swap(ans, nums)
    print(len(res))
    for i in res:
        print(len(i), end=" ")
        print(" ".join(map(str, i)))
    # print("Done")

t = int(input())

for i in range(t):
    _ = input()
    nums = list(map(int, list(input())))
    solve(nums)