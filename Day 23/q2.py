def isYasserHappy(tastiness):
	summation = 0
	total_sum = sum(tastiness)
	for i in range(len(tastiness)):
		if tastiness[i] <= 0 and (-tastiness[i] >= summation or -tastiness[i] >= total_sum - summation - tastiness[i]) :
			return "NO"
		summation += tastiness[i]
	return "YES"

useless = int(input())
for i in range(useless):
	nums = int(input())
	tasty = [int(i) for i in input().split()]
	print(isYasserHappy(tasty))