#!/bin/python3

import os
import sys
import heapq
#
# Complete the cookies function below.
#
def cookies(k, A):
    
    heapq.heapify(A)
    count = 0
    while A[0] < k:
        if len(A) < 2: return -1
        lowest = heapq.heappop(A)
        new_lowest = heapq.heappop(A)
        heapq.heappush(A, lowest + 2 * new_lowest)
        count += 1
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
