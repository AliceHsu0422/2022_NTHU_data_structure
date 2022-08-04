import sys 
data = []
for line in sys.stdin.readlines():
    line = list(map(int, line.split()))
    data.append(line)

def check_valid_seq(input_arr):
    cur = len(input_arr)
    queue = []
    for index in range(5, 0, -1):
        while(len(input_arr)>0) and (input_arr[-1] == cur):
            input_arr.pop()
            cur = cur - 1
        if (len(input_arr) > 0):
            queue.insert(0,input_arr[-1])
            input_arr.pop()
    while(len(queue)>0) and (queue[-1] == cur):
        queue.pop()
        cur = cur - 1
    if (len(queue) == 0) and (len(input_arr) == 0):
        return True
    else:
        return False

for x in range(2, len(data), 2):
    if (check_valid_seq(data[x])):
        print('YES')
    else:
        print('NO')