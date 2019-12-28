def can_garland(rgb):
	maxi = max(rgb)
	rgb.remove(maxi)
	others = sum(rgb)
	if maxi <= others + 1:
		return "YES"
	else:
		return "NO"

useless = int(input())
for i in range(useless):
	rgb = [int(i) for i in input().split()]
	print(can_garland(rgb))