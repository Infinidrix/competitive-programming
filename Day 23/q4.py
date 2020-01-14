def check_if_consistent(bins, i):
	#first_try = bins[0][i]
	#for j in bins:
	#	if j[i] != first_try:
	#		return False
	return bins[0][i] == bins[-1][i]

def remove_on(bin_nums, num, cond):
	i = 0
	while i < len(bin_nums):
		if bin_nums[i][num] != cond:
			bin_nums.pop(i)
			continue
		i += 1
			

def minimum_xor(nums):
	nums.sort()
	bin_nums = [bin(i).split('b')[1] for i in nums]
	bin_lencount = [len(i) for i in bin_nums]
	filler = max(bin_lencount)
	for i in range(len(nums)):
		bin_nums[i] = "0"*(filler - len(bin_nums[i]) + bin_nums[i]
	answer = []
	i = 0
	while i < filler:
		if check_if_consistent(bin_nums, i):
			answer.append(bin_nums[0][i])
			remove_on(bin_nums, i, bin_nums[0][i])
		else:
			check_if_consistent(bin_nums

useless = int(input())
nums = [int(i) for i in input().split()]
print(minimum_xor(nums))