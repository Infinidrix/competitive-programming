def min_dist(pos):
	dist = 2*(max(pos) - min(pos))
	if dist < 5:
		return 0
	return dist - 4

rounds = int(input())
for i in range(rounds):
	numbers = input().split()
	for i in range(len(numbers)):
		numbers[i] = int(numbers[i])
	print(min_dist(numbers))