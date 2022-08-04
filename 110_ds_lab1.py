N=int(input())
A=sorted(list(map(int,input().split())))
M=int(input())
from bisect import bisect_left
from bisect import bisect_right

def Search(A, key):
    low = 0
    high = len(A)-1
    while low <= high:
        mid = int((low + high) / 2)
        if key == A[mid]:
            return 1
        elif key > A[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return 0




def Predecessor(A, key): 
    i = bisect_left(A, key) 
    if i != 0 :
        return A[i-1]
    else:
        return 0


def Successor(A, key): 
    i = bisect_right(A, key) 
    if (i >= len(A)) :
        return 0
    else:
        return A[i]
 
for line in range(M):
    op,v=map(int,input().split())
    if (op == 1):
        print(Search(A,v))
    elif (op == 2):
        print(Predecessor(A,v))
    elif (op == 3):
        print(Successor(A, v))