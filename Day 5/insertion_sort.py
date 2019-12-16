from randomly import randomizer

def insertion_sort(a):
	for i in range(len(a)):
		key = a[i]
		while a[i-1]>key and i>0:
			a[i] = a[i-1]
			i -= 1
		a[i] = key
	return a
	
if __name__ == "__main__":
	print(insertion_sort(randomizer(10000)))