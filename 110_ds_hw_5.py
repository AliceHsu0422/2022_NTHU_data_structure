import bisect
from heapq import heappop, heappush, heapify

N = list(map(int, input().split()))
k = N[1]
n = N[0]
A = list(map(int, input().split()))  
def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

def Answer(arr,k,n):
    #sort_first_list=heapsort(arr[:k])
    heap = arr[:k]
    heap = [-i for i in heap]
    heapify(heap)
    compare = -(heappop(heap))
    print(compare, end=" ")
    for value in range(k,n):
        if arr[value] >= compare:
            print(compare, end=" ")
        else:
            heappush(heap, -arr[value])
            compare = -(heappop(heap))
            print(compare, end=" ")
Answer(A,k,n)