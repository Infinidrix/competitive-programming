
def dfs(listed, start, visited, result):
	visited.add(start)
	result.append(chr(start + ord("a")))
	for i in listed[start]:
		if i not in visited:
			dfs(listed, i, visited, result)

def keyboard(string):		
	adj_list = [set() for i in range(26)]
	if len(string) == 1:
		return "YES\n" + "".join([chr(i + ord("a")) for i in range(len(adj_list)) if len(adj_list[i]) == 0])
	for i in range(len(string) - 1):
		index1 = ord(string[i]) - ord("a")
		index2 = ord(string[i+1]) - ord("a")
		if len(adj_list[index1]) == 2 and ord(string[i+1]) - ord("a") not in adj_list[index1]:
			return "NO"
		adj_list[index1].add(ord(string[i+1]) - ord("a"))
		if len(adj_list[index2]) == 2 and ord(string[i]) - ord("a") not in adj_list[index2]:
			return "NO"
		adj_list[index2].add(ord(string[i]) - ord("a"))
	start_index = -1
	for i in range(len(adj_list)):
		if len(adj_list[i]) == 1:
			start_index = i
			break
	if start_index == -1:
		return "NO"
	result = []
	# print(start_index)
	dfs(adj_list, start_index, set(), result)
	return "YES\n" + "".join(result + [chr(i + ord("a")) for i in range(len(adj_list)) if len(adj_list[i]) == 0])
	

useless = int(input())
for i in range(useless):
	string = input()
	print(keyboard(string))
