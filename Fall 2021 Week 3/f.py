from typing import DefaultDict
from collections import defaultdict, deque


n, k, d = list(map(int, input().split()))

graph = defaultdict(list)
graph_loc = {}
police_stations = input().split()
queue = []
visited = set()
for station in police_stations:
    s = int(station)
    queue.append((s, 0))
    visited.add(s)
visited_edge = set()
for i in range(n-1):
    ans = list(map(int, input().split()))
    src, dest = ans
    graph_loc[(src, dest)] = i
    graph_loc[(dest, src)] = i
    graph[src].append(dest)
    graph[dest].append(src)
count = 0
curr = 0
all_index = []
while curr < len(queue):
    # print(queue, visited)
    node, dist = queue[curr]
    curr += 1
    if dist == d - 1:
        continue
    for next in graph[node]:
        ind = graph_loc[(node, next)]
        if ind in visited_edge:
            continue
        visited_edge.add(ind)
        if next in visited:
            count += 1
            all_index.append(str(ind + 1))
        else:
            visited.add(next)
            queue.append((next, dist + 1))
print(count)
print(" ".join(all_index))
        