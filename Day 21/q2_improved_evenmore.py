def find_upper(lookup_array, item, start_point = 0, find_if_higher = False, cur_index = 0):
	for i in range(start_point, len(lookup_array)):
		if lookup_array[i] > item:
			return i
		if find_if_higher and i > cur_index: return -1
	return -1

def find_removable(verse_length, time_limit):
	sum_array = []
	max_array = [-1]
	summed = 0
	for i in verse_length:
		summed += i
		sum_array.append(summed)
		if i > max_array[-1]:
			max_array.append(i)
		else:
			max_array.append(max_array[-1])
	max_array.pop(0)
	final_index = find_upper(sum_array, time_limit)
	
	if final_index == -1:
		return 0
    
	maxi = max_array[final_index]
	new_index = find_upper(sum_array, time_limit + maxi, True, final_index + 1)
	if new_index == -1: return verse_length.index(maxi) + 1
	else:
		return 0
		
useless = int(input())
for i in range(useless):
	n, time = [int(i) for i in input().split()]
	verses = [int(i) for i in input().split()]
	print(find_removable(verses, time))
