
# https://www.hackerrank.com/challenges/equality-in-a-array/problem

def equalizeArray(arr):
    counts = [0 for i in range(101)]
    for i in arr:
        counts[i] += 1
    return len(arr) - max(counts)
