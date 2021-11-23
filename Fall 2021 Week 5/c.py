from collections import defaultdict, deque
import heapq
def solve():
    n = int(input())
    qs = list(map(int, input().split()))
    max_qual = -1
    max_ind = -1
    for i, q in enumerate(qs):
        if max_qual < q:
            max_qual = q
            max_ind = i
    m = int(input())
    graph = defaultdict(lambda : defaultdict(lambda : float("inf")))
    incoming = [0 for i in range(n)]
    for i in range(m):
        a, b, w = list(map(int, input().split()))
        a -= 1
        b -= 1
        graph[a][b] = min(graph[a][b], w)
    queue = [(0, max_ind)]
    total = 0
    visited = set()
    costs = [0 for i in range(n)]
    while queue:
        w, curr = heapq.heappop(queue)
        if curr in visited:
            if costs[curr] > w:
                total -= costs[curr] - w
                costs[curr] = w
            continue
        total += w
        costs[curr] = w
        visited.add(curr)
        for neigh, weight in graph[curr].items():
            heapq.heappush(queue, (weight, neigh))
    if len(visited) == n:
        return total
    else:
        return -1
print(solve())