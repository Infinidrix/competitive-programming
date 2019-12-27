def awarder(scores):
	loc = int(len(scores) / 2)
	while scores[loc] == scores[loc - 1]:
		if loc == 0: return "0 0 0"
		loc -= 1
	loc -= 1
	if loc < 4:
		return "0 0 0"
	index = 0
	while scores[index] == scores[index + 1]:
		index += 1
		if index + 1 >= int((loc - index) / 2):
			return "0 0 0"
	gold = index + 1
	while scores[gold + index + 1] == scores[gold + index + 2]:
		if loc - (gold + index + 1) <= gold:
			return "0 0 0"
		index += 1
	silver = index + 2
	bronze = loc - gold - silver + 1
	if gold >= bronze or gold >= silver or bronze+silver+gold > int(len(scores)/2):
		return "0 0 0"
	return str(gold) + " " + str(silver) + " " + str(bronze)


rounds = int(input())
for i in range(rounds):
	size = input()
	numbers = input().split()
	for i in range(len(numbers)):
		numbers[i] = int(numbers[i])
	print(awarder(numbers))
