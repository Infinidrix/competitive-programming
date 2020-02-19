import math

def min_div(number, listed):
	counts = [0 for i in range(60)]
	for i in listed:
		counts[int(math.log(i, 2))] += 1
	num_listed = [int(i) for i in bin(number)[2:]]
	num_listed.reverse()
	running_sum = 0
	cost = 0
	# print(counts, num_listed)
	for i in range(len(num_listed)):
		if num_listed[i] == 1:
			if counts[i] > 0:
				running_sum += (counts[i] - 1) * (2**i)
			elif running_sum >= 2 ** i:
				running_sum -= 2 ** i
			else:
				take_index = -1
				for j in range(i, 60):
					if counts[j] > 0:
						take_index = j
						counts[take_index] -= 1
						break
				if take_index == -1:
					return -1
				running_sum += (2 ** take_index) - 2 ** i
				# print(take_index, i)
				cost += take_index - i
		else:
			running_sum += counts[i] * (2 ** i)
	return cost

useless = int(input())
for i in range(useless):
	number, length = [int(i) for i in input().split()]
	numbers = [int(i) for i in input().split()]
	print(min_div(number, numbers))
