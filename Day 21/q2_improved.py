def find_upper(lookup_array, item, start_point = 0):
	for i in range(start_point, len(lookup_array)):
		if lookup_array[i] > item:
			return i
	return -1

def find_removable(verse_length, time_limit):
	sum_array = []
	summed = 0
	for i in verse_length:
		summed += i
		sum_array.append(summed)
	
	final_index = find_upper(sum_array, time_limit)
	
	if final_index == -1:
		return 0
	max_possible = final_index + 1
	max_index_remove = -1
	maxi = max(verse_length[:final_index+1])
	new_index = find_upper(sum_array, time_limit + maxi)
	if new_index > max_possible or new_index == -1: return verse_length.index(maxi) + 1
	else:
		return 0
		
useless = int(input())
for i in range(useless):
	n, time = [int(i) for i in input().split()]
	verses = [int(i) for i in input().split()]
	print(find_removable(verses, time))
