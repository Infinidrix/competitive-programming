def correct(string):
	if "aa" in string or "bb" in string or "cc" in string:
		return -1
	listed = list(string)
	for i in range(len(listed)):
		if listed[i] == "?":
			loc = i
			choices = ["a","b","c","?","?","a","b","c"]
			if loc > 0:
				choices.remove(listed[loc-1])
			if loc < len(listed) - 1: 
				choices.remove(listed[loc+1])
			listed[loc] = choices[0]
	return "".join(listed)
		
rounds = int(input())
for i in range(rounds):
	string = input()
	print(correct(string))