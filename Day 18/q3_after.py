def count_costs(berry_order, start, end, move):
	costs = {0:0}
	count = 0
	moves = 0
	for i in range(start, end, move):
		moves += 1
		if berry_order[i] == 2:
			count -= 1
		else:
			count += 1
		if count not in costs:
			costs[count] = moves
		
	return costs

def min_cost(berry_order):
	remove = 0
	for i in berry_order:
		if i == 2:
			remove -= 1
		else:
			remove += 1
	half_way = len(berry_order) // 2
	l_costs = count_costs(berry_order, half_way - 1, -1, -1)
	r_costs = count_costs(berry_order, half_way, len(berry_order), 1)
	cost = len(berry_order)
	sign =  -1 if remove < 0 else 1
	remove = abs(remove)
	for i in range(0, remove + 1):
		l_num = sign * i
		r_num = sign * (remove - i)
		if l_num in l_costs and r_num in r_costs:
			cost = min(cost, l_costs[l_num] + r_costs[r_num])
	return cost


useless = int(input())
for i in range(useless):
	half_way = int(input())
	listed = [int(i) for i in input().split()]
	print(min_cost(listed))
