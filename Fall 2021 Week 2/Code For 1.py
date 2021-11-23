def tree_traverse(num, depth, node_count):
    if depth == 0:
        return []
    if num >= (2 ** (depth - 1)):
        num &= (1 << (depth - 1)) - 1
        res = tree_traverse(num, depth - 1, node_count * 2)
        res.append(node_count)
    else:
        res = tree_traverse(num, depth - 1, node_count * 2 - 1)
        res.append(node_count - 1)
    return res

def num_of_ones(num, left, right):
    str_num = map(int, bin(num)[2:])
    left_path = tree_traverse(left - 1, len(str_num), 1)
    right_path = tree_traverse(right, len(str_num), 1)
    res = 0
    for i, l, r in zip(str_num, left_path, right_path):
        res += i * (r - l)
    return res

n, l, r = list(map(int, input().split()))

print(num_of_ones(n, l, r))