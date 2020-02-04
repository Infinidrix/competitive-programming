def populate(freq, start):
	result = []
	while freq.count(0) != 4:
		if freq[start] == 0:
			return False, []
		result.append(str(start))
		freq[start] -= 1
		if start == 0 or (start == 1 and freq[0] == 0) or (start == 2 and freq[3] != 0):
			start += 1
		else:
			start -= 1
	return True, " ".join(result)

if __name__ == "__main__":
	freq = [int(i) for i in input().split()]
	for i in range(4):
		exists, string = populate(freq[:], i)
		if exists:
			print("YES")
			print(string)
			break
	if not exists:
		print("NO")
