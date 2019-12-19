import math

def find_smallest_addable(a, b):
    if a > b:
        diff = a -b
    else:
        diff = b - a
    
    if diff == 0:
        return 0
    n = math.ceil((-1 + math.sqrt(1 + 8 * diff))/2)
    while (True):
        res = n*(n+1)/2
        if (res - diff) % 2 == 0:
            return n
        n += 1
        
useless = int(input())
for i in range(useless):
    a, b = [int(i) for i in input().split()]
    print(find_smallest_addable(a, b))
