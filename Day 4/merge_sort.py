from randomly import randomizer
import math
def merge_sort(li, i = 0, j = None):
	if j == None:
		j = len(li)
	if i < j:
		middle = math.floor((i + j)/2)
		merge_sort(li, i, middle)
		merge_sort(li, middle+1, j)
		listed = []
		k = 0
		while i < middle and middle + k <= j:
			if li[i] < li[middle+k]:
				listed.append(li[i])
				i += 1
			else:
				listed.append(li[middle+k])
				k += 1
		if i == middle and middle + k <= j:
			listed.extend(li[middle+k:j])
		elif i<middle and not middle + k > j:
			listd.extend(li[i:middle])
		return listed
		
if __name__ == "__main__":
	print(merge_sort(randomizer(10000)))