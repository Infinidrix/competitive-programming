from collections import deque
import bisect

t = int(input())

for i in range(t):
    string = input()
    possible = sorted(list(map(lambda x: ord(x) - ord('a'), input())))
    
    dist = 0
    
    for c in string:
        diff = ord(c) - ord('a')
        res = bisect.bisect_right(possible, diff)
        d = float('inf')
        if res == 0:
            d = min(possible[0] - diff, 26 - possible[-1] + diff)
        elif res == len(possible):
            d = min(diff - possible[-1], 1 + possible[0] + (25 - diff))
        else:
            d = min(possible[res] - diff, diff - possible[res - 1])
        dist += d
            
    print(f'Case #{i+1}: {dist}')