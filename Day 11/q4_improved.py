def max_finder(seq):
	tracker = [0 for i in range(len(seq))]
	max_count = 0
	for i in range(1, len(tracker)):
		if seq[i] > seq[i-1]:
			tracker[i] = tracker[i-1] + 1
		else:
			tracker[i] = 0
	for i in range(1, len(tracker)):
		if tracker[i] == 0:
			if seq[i-2] < seq[i]:
				if i+1 < len(seq) and 0 in tracker[i+1:]:
					addable = tracker[tracker.index(0, i+1) - 1]
				else:
					addable = tracker[-1]
				temp_max = tracker[i-1] + addable
				if temp_max > max_count:
					max_count = temp_max
			if i+1 < len(seq) and seq[i-1] < seq[i+1]:
				if i+1 < len(seq) and 0 in tracker[i+1:]:
					addable = tracker[tracker.index(0, i+1) - 1]
				else:
					addable = tracker[-1]
				temp_max = tracker[i-1] + addable
				if temp_max > max_count:
					max_count = temp_max
	if max_count == 0:
		max_count = max(tracker)
		if max_count == 0:
			return 0
	return max_count + 1
			
useless = input()		
numbers = input().split()
for i in range(len(numbers)):
	numbers[i] = int(numbers[i])
print(max_finder(numbers))