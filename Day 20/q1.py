import math

def count_mins(a, b, c, r):
    a_in = False
    b_in = False
    
    if c - r <= a <= c + r:
        a_in = True
    if c - r <= b <= c + r:
        b_in = True
    
    if b_in and a_in:
        return 0
    elif not(b_in or a_in):
        if abs(a-c) + abs(b-c) > abs(a - b): #They're on the same side
            return abs(a-b)
        else:
            return abs(a-b) - 2 * r
    elif a_in:
        return abs(b - c) - r
    else:
        return abs(a - c) - r
    
useless = int(input())
for j in range(useless):
    numbers = [int(i) for i in input().split()]
    print(count_mins(numbers[0], numbers[1], numbers[2], numbers[3]))
