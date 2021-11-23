from collections import Counter, defaultdict
from math import comb

t = int(input())
for i in range(t):
    n = int(input())
    topics = []
    difficulties = []
    for j in range(n):
        t, d = list(map(int, input().split()))
        topics.append(t)
        difficulties.append(d)
    topic_dict = defaultdict(list)
    for i, t in enumerate(topics):
        topic_dict[t].append(difficulties[i])
    diff_dict = Counter(difficulties)
    res = 0
    visited = set()
    for i, topic in enumerate(topics):
        l = len(topic_dict[topic])
        if topic in visited or l == 1:
            continue
        visited.add(topic)
        for val in topic_dict[topic]:
            res += (l - 1) * (diff_dict[val] - 1)
        
    print(comb(n, 3) - res)