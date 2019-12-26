from randomly import randomizer

def find_min(li, starter):
	minn = starter
	for i in range(starter, len(li)):
		if minn > li[i]:
			minn = i
	return minn

def selection_sort(li):
	for i in range(len(li)):
		swapper = find_min(li, i)
		li[i], li[swapper] = li[swapper], li[i]
	return li
	
if __name__ == "__main__":
	print(selection_sort(randomizer(10000)))