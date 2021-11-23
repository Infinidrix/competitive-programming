import heapq
class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
    def __lt__(self, node):
        return True

t = int(input())

for p in range(t):
    _ = input()
    string = input()
    head = Node(100)
    heap = []
    next_heap = []
    curr = head
    for i, c in enumerate(string):
        curr.next = Node(int(c), prev=curr)
        if (curr.val + 1) % 10 == curr.next.val:
            heapq.heappush(heap, (curr.val, curr))
        curr = curr.next
    curr.next = Node(100, prev=curr)
    while heap or next_heap:
        if not heap:
            heap, next_heap = next_heap, heap
        val, curr = heapq.heappop(heap)
        if curr.val == 100 or (curr.val + 1) % 10 != curr.next.val:
            continue
        curr.val = (curr.val + 2) % 10
        curr.next.val = 100
        curr.next = curr.next.next
        curr.next.prev = curr
        if (curr.val + 1) % 10 == curr.next.val:
            heapq.heappush(next_heap, (curr.val, curr))
        if (curr.prev.val == (curr.val - 1) % 10):
            heapq.heappush(next_heap, (curr.prev.val, curr.prev))
    curr = head.next
    res = []
    while curr.next:
        res.append(str(curr.val))
        curr = curr.next
    
    print(f'Case #{p+1}: {"".join(res)}')