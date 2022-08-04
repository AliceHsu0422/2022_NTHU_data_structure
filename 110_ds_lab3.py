import heapq
n=int(input())
A = list(map(int, input().split()))
A = [-x for x in A]
B = list(map(int, input().split()))

def heapsort(A,B,n):
    heapq.heapify(A)
    heapq.heapify(B)
    for i in range(0,n):
        temp = B[0]+ (-A[0]//2)
        temp1 = -A[0]-((-A[0])//2)
        heapq.heapreplace(A, -temp1)
        heapq.heapreplace(B, temp)
    print(abs(B[0]-abs(A[0])))
    
heapsort(A,B,n)