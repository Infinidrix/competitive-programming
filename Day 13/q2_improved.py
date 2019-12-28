def perm_check(perm):
	pos = [0 for i in range(len(perm) + 1)]
	for i in range(len(perm)):
		pos[int(perm[i])] = i
	result = []
	max = pos[1]
	min = pos[1]
	for i in range(1, len(perm)+1):
		if max < pos[i]:
			max = pos[i]
		elif min > pos[i]:
			min = pos[i]
		if max - min + 1 > i:
			result.append("0")
		else:
			result.append("1")
	return "".join(result)

rounds = int(input())
for i in range(rounds):
	size = input()
	numbers = input().split()
	print(perm_check(numbers))