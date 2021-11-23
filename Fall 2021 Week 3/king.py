
def quad(px, py, cx, cy):
    if px > cx and py > cy:
        return 0
    if px < cx and py > cy:
        return 1
    if px < cx and py < cy:
        return 2
    if px > cx and py < cy:
        return 3

n = int(input())
qx, qy = list(map(int, input().split()))
kx, ky = list(map(int, input().split()))
cx, cy = list(map(int, input().split()))

if quad(kx, ky, qx, qy) == quad(cx, cy, qx, qy):
    print("YES")
else:
    print("NO")