from collections import defaultdict
import heapq
n, m = list(map(int, input().split()))

graph = defaultdict(list)

for i in range(m):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

heap = [1]
ans = []
visited = set([1])
while heap:
    curr = heapq.heappop(heap)
    ans.append(str(curr))
    for neigh in graph[curr]:
        if neigh not in visited:
            visited.add(neigh)
            heapq.heappush(heap, neigh)
print(" ".join(ans))