def five_div(targa, curr, total, has_elem):
    if curr >= len(targa):
        return has_elem and total % 5 == 0
    return five_div(targa, curr + 1, total, has_elem) or five_div(targa, curr + 1, total + targa[curr], True)

targa = [0,0,0,0,0]

while True:
    if not five_div(targa, 0, 0, False):
        print(targa)
    last_ind = 4
    targa[last_ind] += 1
    while last_ind >= 0 and targa[last_ind] > 4:
        targa[last_ind] = 0
        last_ind -= 1
        targa[last_ind] += 1
    if last_ind == -1:
        break
