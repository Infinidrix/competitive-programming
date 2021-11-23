import heapq
n, m = list(map(int, input().split()))

queue = []
queue.append((0, n))
visited = set()

while queue:
    dist, curr = heapq.heappop(queue)
    if curr in visited or curr < 0:
        continue
    visited.add(curr)
    if curr == m:
        print(dist)
        break
    if curr > m:
        heapq.heappush(queue, (dist + curr - m, m))
    else:
        heapq.heappush(queue, (dist + 1, curr * 2))
        heapq.heappush(queue, (dist + 1, curr - 1))
