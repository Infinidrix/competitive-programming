from collections import defaultdict

n, m = list(map(int, input().split()))

parents = [i for i in range(n)]
graph = defaultdict(list)
incoming = [0 for i in range(n)]