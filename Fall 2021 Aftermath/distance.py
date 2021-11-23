t = int (input())

for _ in range(t):
    x, y = list(map(int, input().split()))
    if (x + y) % 2 != 0 :
        print('-1 -1')
    else:
        print(f'{x//2} {y//2 + (int(x % 2 == 1 or y % 2 == 1))}')