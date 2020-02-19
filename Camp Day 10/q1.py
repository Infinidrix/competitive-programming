
def remove_zero(listed):
	result = 0
	found = False
	temp = 0
	for i in listed:
		if i == 0 and found:
			temp += 1
		elif i == 1 and not found:
			found = True
		if i == 1:
			result += temp
			temp = 0
	return result

useless = int(input())
for i in range(useless):
	string = [int(i) for i in input()]
	print(remove_zero(string))
