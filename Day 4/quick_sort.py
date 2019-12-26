from randomly import randomizer
import random

def quick_sort(li):
	if len(li) > 1:
		chosen = random.randint(0, len(li)-1)
		li[chosen], li[0] = li[0], li[chosen]
		pivot = li[0]
		lesser_list = []
		greater_list = []
		for i in range(1, len(li)):
			if pivot <= li[i]:
				greater_list.append(li[i])
			else:
				lesser_list.append(li[i])
		greater_list = quick_sort(greater_list)
		lesser_list = quick_sort(lesser_list)
		return lesser_list + [pivot] + greater_list
	return li
	
if __name__ == "__main__":
	print(quick_sort(randomizer(10000)))