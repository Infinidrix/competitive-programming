def make_jump(loc, element, max):
	result = []
	if 0 < loc + element < max:
		result.append(loc + element)
	if 0 < loc - element < max:
		result.append(loc - element)
	return result


def find_nearest(seq, check, loc, places, jumps, round=1):
	possiblities = make_jump(loc, seq[loc], len(seq))
	found_one = False
	cand = 1000
	if loc == 87:
			print()
	for i in possiblities:
		if i in places:
			continue
		found_one = True
		hi = seq[i]
		hey = jumps[i]
		if seq[i] % 2 != check % 2:
			return round
		elif jumps[i] != 0 and cand > jumps[i] + 1:
			cand = jumps[i] + 1
	for i in possiblities:
		if i not in places:
			places.append(i)
			if cand < round+1:
				return cand
			return find_nearest(seq, check, i, places, jumps, round + 1)
	if not found_one:
		return -1


def populate_jump(seq):
	jumps = [-1] + [0 for i in range(len(seq) - 1)]
	for i in range(1, len(jumps)):
		jumps[i] = find_nearest(seq, seq[i], i, [i], jumps)
	return jumps


useless = input()
numbers = ["-1"] + input().split()
for i in range(len(numbers)):
	numbers[i] = int(numbers[i])
answer = populate_jump(numbers)

for i in range(len(answer)):
	answer[i] = str(answer[i])

print(" ".join(answer))