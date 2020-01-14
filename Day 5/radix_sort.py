def counting_sort(array, key_value):
	counting_array = [0 for i in range(10)]
	for i in array:
		counting_array[int(i[key_value])] += 1
	for i in range(1, len(counting_array)):
		counting_array[i] += counting_array[i-1]
	return_array = [0 for i in range(len(array))]
	print(counting_array, key_value)
	for i in range(len(array)):
		counting_array[int(array[i][key_value])] -= 1
		print(array[i], counting_array[int(array[i][key_value])])
		return_array[counting_array[int(array[i][key_value])]] = array[i]
	print("return array", return_array, key_value)
	return return_array
	
def radix_sort(array):
	maxi = 0
	for i in range(len(array)):
		if maxi < len(array[i]):
			maxi = len(array[i])
	for i in range(len(array)):
		array[i] = "0"*(maxi - len(array[i])) + array[i]
	for i in range(maxi-1, -1, -1):
		array = counting_sort(array, i)
	return array

print(radix_sort(['41', '34', '25', '12', '90']))