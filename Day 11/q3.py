def substring_adder(string, lookup):
	index = 0
	subsum = 0
	for i in range(len(string)):
		if string[i] in lookup:
			index += 1
		else:
			subsum += (index)*(index+1)/2
			index = 0
	return int(subsum + (index) * (index + 1) / 2)
	

no_uses = input()
string = input()
lookup = input().split()
print(substring_adder(string, lookup))