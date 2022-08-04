from collections import deque

n = int(input())
m = int(input())

deq = [deque() for _ in range(n)]

for _ in range(m):
    ops = list(map(int, input().split()))
    if ops[0] == 0:
        op, i, j, k = ops
        if j == 0:
            deq[k-1].appendleft(i)
        else:
            deq[k-1].append(i)
    else:
        op, j, k = ops
        if j == 0:
            print(deq[k-1].popleft())
        else:
            print(deq[k-1].pop())        
        