n = int(input())
db = {}
changes = {}
for _ in range(n):
    old, new = input().split()
    if old in changes:
        original = changes[old]
        db[original] = new
        changes[new] = original
    else:
        db[old] = new
        changes[new] = old
print(len(db))
for key, val in db.items():
    print(key, val)