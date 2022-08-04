import sys 

#data = [line.rstrip().split() for line in sys.stdin.readlines()]
data = []
for line in sys.stdin.readlines():
    line = list(map(int, line.split()))
    data.append(line)

def check_valid_seq(input_arr):
    cur = len(input_arr)
    stack = []
    while(1):
        stack.append(input_arr[-1])
        input_arr.pop()
        while (len(stack) != 0) and (stack[-1] == cur):
            stack.pop()
            cur = cur - 1
            if (cur == 0):
                return True
        if len(input_arr) == 0:
            return False

for x in range(2, len(data), 2):
    if (check_valid_seq(data[x])):
        print('YES')
    else:
        print('NO')
