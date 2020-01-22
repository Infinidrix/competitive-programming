

def min_time_finder(stack, to_be_sent):
	max_travel = 0
	time = 0
	for i in range(len(to_be_sent)):
		present = to_be_sent[i]
		found_location = -1
		for j in range(max_travel, len(stack)):
			if stack[j] == present:
				found_location = j
				break
		if found_location == -1:
			time += 1
		else:
			max_travel = found_location
			time += 2*(found_location - i) + 1
	return time
# n - length stack
# m -length of list of presents
# O(m + n)
# o(1)
test_cases = int(input())
for i in range(test_cases):
	n, m = input().split()
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]
	print(min_time_finder(a, b))
