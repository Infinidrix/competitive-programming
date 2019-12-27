def end_correcter(movt):
	sum_x = 0
	sum_y = 0
	remover_x = [(0, 0), (1, 0), (-1, 0)]
	remover_y = [(0, 0), (0, 1), (0, -1)]
	for i in range(len(movt)):
		sum_x += movt[i][0]
		sum_y += movt[i][1]
	while sum_x != 0:
		if sum_x < 0:
			movt.remove((-1, 0))
			sum_x += 1
		else:
			movt.remove((1, 0))
			sum_x -= 1
	while sum_y != 0:
		if sum_y < 0:
			movt.remove((0, -1))
			sum_y += 1
		else:
			movt.remove((0, 1))
			sum_y -= 1
	return movt	
	
def place_items(movt):
	count_U = min((movt.count("U"), movt.count("D")))
	count_R = min((movt.count("R"), movt.count("L")))
	if count_U == 0 and count_R == 0:
		return ""
	elif count_U == 0:
		return "LR"
	elif count_R == 0:
		return "UD"
	return "U"*count_U+"R"*count_R+"D"*count_U+"L"*count_R


rounds = int(input())
movt_dict = {"L": (-1, 0),"R":(1, 0), "U":(0, 1), "D":(0, -1)}
movt_dict_reverse = {(-1, 0):"L",(1, 0):"R", (0, 1):"U", (0, -1):"D"}
for i in range(rounds):
	numbers = list(input())
	for i in range(len(numbers)):
		numbers[i] = movt_dict[numbers[i]]
	movt = end_correcter(numbers)
	answer = "".join([movt_dict_reverse[i] for i in movt])
	real_answer = place_items(answer)
	print(len(real_answer))
	print(real_answer)
		