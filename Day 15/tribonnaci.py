def find_tribonacci(n, found_dict):
        if n in found_dict:
            return found_dict[n]
        if n == 2 or n == 1:
            found_dict[n] = 1
        elif n == 0:
            found_dict[n] = 0
        else:
            result = find_tribonacci(n-3, found_dict) + find_tribonacci(n-2, found_dict) + find_tribonacci(n-1, found_dict)
            found_dict[n] = result
        return found_dict[n]
print(find_tribonacci(4, {}))
