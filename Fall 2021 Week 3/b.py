class Node:
    def __init__(self, odd = None, even = None, count = 0):
        self.right = odd
        self.left = even
        self.count = count

def add(val, node, ind):
    # print(f"got to {node=} with {ind=}")
    if not node:
        node = Node()
    if ind == -1:
        node.count += 1
        return node
    if ind >= len(val) or int(val[len(val) - ind - 1]) % 2 == 0:
        node.left = add(val, node.left, ind - 1)
    else:
        node.right = add(val, node.right, ind - 1)
    # print(f"final to {node=} with {ind=} and children {node.left.count if node.left else 'blank'}, {node.right.count if node.right else 'blank'}")
    return node

def remove(val, node, ind):
    if not node:
        node = Node()
    if ind == -1:
        node.count -= 1
        return node
    if ind >= len(val) or int(val[len(val) - ind - 1]) % 2 == 0:
        node.left = remove(val, node.left, ind - 1)
        return node
    else:
        node.right = remove(val, node.right, ind - 1)
        return node

def check(val, node, ind):
    # print(f"check to {node=} with {ind=}")
    while True:
        if ind == -1:
            return node.count
        # print(f"final to {node=} with {ind=} and children {node.left.count if node.left else 'blank'}, {node.right.count if node.right else 'blank'}")
        if ind >= len(val) or int(val[len(val) - ind - 1]) % 2 == 0:
            node = node.left
            ind -= 1
        else:
            node = node.right
            ind -= 1


ops = int(input())

root = Node()
height = 18
for _ in range(ops):
    op, val = input().split()
    if op == "+":
        add(val, root, height - 1)
    elif op == "-":
        remove(val, root, height - 1)
    elif op == "?":
        print(check(val, root, height - 1))