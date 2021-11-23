from itertools import permutations

t = int(input())

for i in range(t):
    input()
    r = input()
    b = input()
    prob = 0
    for curr_r, curr_b in zip(r, b):
        curr_r = int(curr_r)
        curr_b = int(curr_b)
        if curr_r > curr_b:
            prob += 1
        elif curr_r < curr_b:
            prob -= 1
    if prob > 0:
        print("RED")
    elif prob < 0:
        print("BLUE")
    else:
        print("EQUAL")