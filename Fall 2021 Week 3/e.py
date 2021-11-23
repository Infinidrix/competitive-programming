from collections import defaultdict, deque

t = int(input())

for _ in range(t):
    _ = input()
    n, k = list(map(int, input().split()))
    # print(n, k)
    graph = defaultdict(list)
    count = [0 for _ in range(n)]
    visited = [False for _ in range(n)]
    for _ in range(n - 1):
        u, v = list(map(int, input().split()))
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
        count[u] += 1
        count[v] += 1
    queue = deque()
    for i in range(n):
        if count[i] == 1 or count[i] == 0:
            queue.append((i, 0))
    # print(graph, count, n, k)
    res = set()
    while queue:
        # print(queue)
        node, left = queue.popleft()
        res.add(node)
        for next in graph[node]:
            count[next] -= 1
            if count[next] == 1 and left != k - 1:
                queue.append((next, left + 1))
    print(n - len(res))
