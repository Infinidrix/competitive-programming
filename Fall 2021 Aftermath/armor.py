from collections import deque
from typing import ValuesView
n, m = list(map(int, input().split()))

q = int(input())

synergy = set()
for _ in range(q):
    synergy.add(tuple(map(int, input().split())))

queue = deque()
queue.append((1, 1, 0))
visited = set([(1, 1)])
sums = 0
while queue:
    armor, weapon, dist = queue.popleft()
    if n <= armor and m <= weapon:
        print(dist)
        break
    elif n < armor or m < weapon or armor + weapon < sums:
        continue
    sums = max(sums, armor + weapon)
    adds = weapon + armor + int((armor, weapon) in synergy)
    if (armor, adds) not in visited:
        queue.append((armor, adds, dist + 1))
        visited.add((armor, adds))
    if (adds, weapon) not in visited:
        queue.append((adds, weapon, dist + 1))
        visited.add((adds, weapon))