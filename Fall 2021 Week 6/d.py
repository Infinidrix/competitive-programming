from collections import deque

def isvalid(x, y, maze):
    if (not (0 <= x < len(maze) and 0 <= y < len(maze[0]))) or maze[x][y] == '#':
        return False
    neighbours = ((-1, 0), (1, 0), (0, 1), (0, -1), (0, 0))
    for dx, dy in neighbours:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 'B':
            return False
        
    return True

def solve():
    neighbours = ((-1, 0), (1, 0), (0, 1), (0, -1))
    n, m = list(map(int, input().split()))
    maze = [list(input()) for i in range(n)]
    queue = deque()
    queue.append((n - 1, m - 1))
    goods = sum(l.count("G") for l in maze)
    visited = set([(n - 1, m - 1)])
    while queue:
        x, y = queue.popleft()
        if not isvalid(x, y, maze):
            continue
        if maze[x][y] == 'G':
            goods -= 1
            if goods == 0:
                return "YES"
        for dx, dy in neighbours:
            nx, ny = x + dx, y + dy
            if isvalid(nx, ny, maze) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return "YES" if goods == 0 else "NO"
                



t = int(input())
for i in range(t):
    print(solve())