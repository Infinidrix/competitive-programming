def get_k_set(nums, k):
    if k == 1:
        return len(nums)
    elems = set(nums)
    set2 = set()
    for num in nums:
        if num / k in elems and num / k not in set2:
            set2.add(num)
    return len(elems) - len(set2)

_, k = list(map(int, input().split()))

nums = list(map(int, input().split()))

print(get_k_set(nums, k))