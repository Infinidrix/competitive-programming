from typing import DefaultDict
import sys
from collections import defaultdict

def remove_order(graph, disrespect, node, is_root):
    res = []
    disrespected = disrespect[node]
    for next_node in graph[node]:
        res.extend(remove_order(graph, disrespect, next_node, False))
        disrespected = disrespected and disrespect[next_node]
    if disrespected and not is_root:
        res.append(str(node + 1))
    return res
def remove_order_iter(graph, disrespect, root, n):
    res = []
    for i in range(n):
        include = (i != root) and disrespect[i]
        for child in graph[i]:
            include = include and disrespect[child] == 1
        if include:
            res.append(str(i + 1))
    return res
sys.setrecursionlimit(10 ** 5 + 7)

n = int(input())
graph = defaultdict(list)
disrespect = [0 for i in range(n)]
root = -1
for i in range(n):
    p, c = map(int,input().split())
    if p == -1:
        root = i
    else:    
        graph[p - 1].append(i)
    disrespect[i] = c
# ans = sorted(remove_order(graph, disrespect, root, True))
ans = remove_order_iter(graph, disrespect, root, n)
if len(ans) == 0:
    print("-1")
else:
    print(" ".join(ans))