from collections import defaultdict

def dfs(graph, visited, )

def find_edges(graph1, graph2, n):
    visited1 = [-1 for i in range(n + 1)]
    visited1_hash = {}
    for i in range(1, n + 1):
        if visited1[i] == -1:
            res = dfs(graph1, visited1, i)
            visited1_hash[i] = res

n, e1, e2 = list(map(int, input().split()))

graph1 = defaultdict(list)
graph2 = defaultdict(list)

for _ in range(e1):
    u, v = list(map(int, input().split()))
    graph1[u].append(v)
    graph1[v].append(u)

for _ in range(e2):
    u, v = list(map(int, input().split()))
    graph2[u].append(v)
    graph2[v].append(u)

find_edges(graph1, graph2)