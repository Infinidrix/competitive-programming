def find_min_time(presents, specials):
	max_index = 0
	min_time = 0
	for i in range(len(specials)):
		presents_location = presents.index(specials[i])
		if max_index < presents_location:
			time += 2 * (presents_location - i)
			max_index = presents_location
		time += 1
	return time

test_cases = int(input())
for i in range(test_cases):
	n = input()
	n_stack = [int(i) for i in input().split()]
	m_stack = [int(i) for i in input().split()]
	print(find_min_time(n_stack, m_stack))
