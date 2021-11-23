
res = {"A": 0, "B": 0, "C": 0}


for _ in range(3):
    comp = input()
    if comp[1] == ">":
        res[comp[0]] += 1
        res[comp[2]] += 2
    else:
        res[comp[0]] += 2
        res[comp[2]] += 1
    
ans = [-1] * 3 
imp = False
for key, value in res.items():
    if ans[value - 2] != -1:
        print("Impossible")
        imp = True
        break
    else:
        ans[value - 2] = key
if not imp:
    print("".join(reversed(ans)))
    