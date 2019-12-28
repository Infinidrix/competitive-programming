def find_last_one(string):
	for i in range(len(string), 0, -1):
		if string[i - 1] == "1":
			return i


def find_num(string, start, end, length, num):
	#improve this
	num_str = str(num)
	for i in range(start - length, start):
		if i < 0: continue
		if string[i] == num_str:
			return True, i

	for i in range(end + 1, end + length + 1):
		if i >= len(string): break
		if string[i] == num_str:
			return True, i
	return False, 0


def perm_check(perm):
	loc = perm.index("1")
	result = ["1"]
	start = loc
	end = loc
	for i in range(len(perm) - 1):
		num = i + 2
		search_for = len(result) - find_last_one(result)
		found_flag = True
		min = start
		max = end
		stat = True
		for j in range(search_for + 1):
			stat, location = find_num(perm, start, end, search_for + 1, num - j)
			if not stat:
				break
			if min > location:
				min = location
			elif max < location:
				max = location
		if not stat:
			result.append("0")
			continue
		if max - min <= len(result):
			result.append("1")
			start = min
			end = max
		else:
			result.append("0")

	return "".join(result)


rounds = int(input())
for i in range(rounds):
	size = input()
	numbers = input().split()
	print(perm_check(numbers))