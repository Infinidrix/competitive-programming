# time was up at this point

def create_list(listed_int):
    list1 = listed_int[:len(listed_int)//2]
    list2 = listed_int[len(listed_int)//2:]
    count_prev = []
    count_fwd = []
    i = 0
    while i < len(list2) - 1:
        res = list2[i]
        for j in range(len(list2) - i):
            if res != list2[j+i]:
                break
        i = i + j
        count_fwd.append(j)
    if list2[-1] == list2[-2]:
        count_fwd[-1] += 1
    else:
        count_fwd.append(1)
    i = len(list1) - 1
    
    list1.reverse()
    list2 = list1
    count_prev = count_fwd[:]
    count_fwd = []
    i = 0
    while i < len(list2) - 1:
        res = list2[i]
        for j in range(len(list2) - i):
            if res != list2[j+i]:
                break
        i = i + j
        count_fwd.append(j)
    if list2[-1] == list2[-2]:
        count_fwd[-1] += 1
    else:
        count_fwd.append(1)

    return count_fwd, count_prev

def min_removal(listed_int):
    if listed_int.count(1) == listed_int.count(2):
        return 0
    count_prev, count_fwd = create_list(listed_int)
    if listed_int.count(1) > listed_int.count(2):
        pass
    
min_removal([])
