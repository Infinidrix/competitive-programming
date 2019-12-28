def find_increasing(seq, used = False):
	if len(seq) == 0:
		return 0
	count = 0
	max_count = 0
	for i in range(1, len(seq)):
		if seq[i] > seq[i - 1]:
			count += 1
		elif not used and (i >= 2 and seq[i+1] > seq[i-1]):
			used = True
			prev_count = count
		elif i >= 2 and seq[i+1] > seq[i-1]:
			other_side_count = 0
			for j in range(i, len(seq)-1):
				if seq[j+1] > seq[j]:
					other_side_count += 1
				else:
					break
			if other_side_count > prev_count:
				count += other_side_count - prev_count
			if max_count < count:
				max_count = count
			count = 0
			used = False
		else:
			if max_count < count:
				max_count = count
			count = 0
			used = False
	if max_count < count:
		max_count = count
	if max_count == 0:
		return 0
	return max_count + 1


useless = input()
numbers = input().split()
for i in range(len(numbers)):
	numbers[i] = int(numbers[i])
print(find_increasing(numbers))