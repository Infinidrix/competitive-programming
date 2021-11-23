def merge(node1, node2):
    global total
    p1 = find_parent(node1)
    p2 = find_parent(node2)
    if sizes[p1] > 1:
        total -= (sizes[p1] * (sizes[p1] - 1)) >> 1
    if sizes[p2] > 1:
        total -= (sizes[p2] * (sizes[p2] - 1)) >> 1
    sizes[p1] += sizes[p2]
    sizes[p2] = 0
    parents[p2] = p1
    total += (sizes[p1] * (sizes[p1] - 1)) >> 1

def find_parent(node):
    while parents[node] != parents[parents[node]]:
        parents[node] = parents[parents[node]]
    return parents[node]

def count_sort(edges):
    counts = [0] * (2 * (10 ** 5) + 3)
    sorted_edges = [0] * len(edges)
    for edge in edges:
        counts[edge[0]] += 1
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    for edge in edges:
        counts[edge[0]] -= 1
        sorted_edges[counts[edge[0]]] = edge 
    return sorted_edges

n, m = list(map(int, input().split()))

parents = [i for i in range(n + 1)]
sizes = [1 for i in range(n + 1)]
total = 0
edges = []
for i in range(n - 1):
    u, v, w = list(map(int, input().split()))
    edges.append((w, v, u))

edges.append((2 * (10 ** 5) + 1, 0, 0))
sorted_edges = count_sort(edges)

temp_q = input().split()
queries = []
i = 0
for q in temp_q:
    queries.append((int(q), i))
    i += 1
sorted_queries = count_sort(queries)
ans = [0 for i in range(len(queries))]
i = 0
for query, ind in sorted_queries:
    while sorted_edges[i][0] <= query:
        merge(sorted_edges[i][1], sorted_edges[i][2])
        i += 1
    ans[ind] = str(total)
print(" ".join(ans)) 