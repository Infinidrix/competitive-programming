def optimal_stacking(gifts, specials):
	max_index = 0
	movt_count = 0
	for i in range(len(specials)):
		found = False
		for j in range(max_index, len(gifts)):
			if specials[i] == gifts[j]:
				movt_count += 2*(j - i) + 1
				max_index = j
				found = True
				break;
		if not found:
			movt_count += 1
	return movt_count
	
useless = int(input())
for i in range(useless):
	a = input()
	gifts = [int(i) for i in input().split()]
	specials = [int(i) for i in input().split()]
	print(optimal_stacking(gifts, specials))