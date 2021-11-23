def add_messages(start, end, total, x):
    second_half = (total * (total + 1)) >> 1
    mid = (start + end) >> 1
    left = total - mid
    messages = second_half - ((left * (left + 1)) >> 1)
    past = second_half - (((left + 1) * (left + 2)) >> 1)
    if past < x <= messages:
        return mid
    elif past >= x:
        return add_messages(start, mid -1, total, x)
    else:
        return add_messages(mid+1, end, total, x)


def first_messages(start, end, x):
    mid = (start + end) >> 1
    messages = (mid * (mid + 1)) >> 1
    past = (mid * (mid - 1)) >> 1
    if past < x <= messages:
        return mid
    elif past >= x:
        return first_messages(start, mid -1, x)
    else:
        return first_messages(mid+1, end, x)

t = int(input())

for _ in range(t):
    k, x = list(map(int, input().split()))

    first_half = (k * (k + 1)) >> 1
    
    second_half = (k * (k - 1)) >> 1

    if first_half + second_half <= x:
        print(int((k << 1) - 1))
    elif first_half <= x:
        print(int(k + add_messages(0, k - 1, k - 1, x - first_half)))
    else:
        print(int(first_messages(0, k, x)))
    # print("OVER")