def hash_check(password, hashed):
    if len(password) > len(hashed):
        return "NO"
    checker = list(password)
    final = list(password)
    founded = 0
    i = 0
    while i <= len(hashed):
        if i == len(hashed):
            if len(checker) != len(password) and hashed[i - 1] in final and i - founded >= len(password) - 1:
                i = founded
                checker = list(password)
        elif hashed[i] in checker:
            if len(checker) == len(password):
                founded = i
            checker.remove(hashed[i])
            if checker == []:
                return "YES"
        else:
            if hashed[i] not in final:
                founded = i
            elif len(checker) != len(password):
                i = founded
            if len(checker) != len(password):
                checker = list(password)
            
        i += 1
    return "NO"

useless = int(input())
for i in range(useless):
    password = input()
    hashed = input()
    print(hash_check(password, hashed))
