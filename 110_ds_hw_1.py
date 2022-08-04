def qsort(inlist):
    if inlist == []: 
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater

def get_list_of_cnt_of_arr2_greater_than_arr1(arr1, arr2):
    len_1 = len(arr1)
    len_2 = len(arr2)
    index_1 = 0
    index_2 = 0
    
    cnt_arr2_greater_than_arr1 = []
    while index_1 < len_1 and index_2 < len_2:
        if arr1[index_1] < arr2[index_2]:
            cnt_arr2_greater_than_arr1.append(len_2-index_2)
            index_1 += 1
        else:
            index_2 += 1
    return cnt_arr2_greater_than_arr1

def merge_count(arrA, arrB, arrC):
    cnt_arrA_greater_than_arrB = get_list_of_cnt_of_arr2_greater_than_arr1(arrB, arrA)
    cnt_arrC_greater_than_arrB = get_list_of_cnt_of_arr2_greater_than_arr1(arrB, arrC)
    ans_list = [x*y for x,y in zip(cnt_arrA_greater_than_arrB,cnt_arrC_greater_than_arrB)]
    
    return sum(ans_list)



if __name__ == '__main__':
    n = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A1=qsort(A)
    B1=qsort(B)
    C1=qsort(C)
    print(merge_count(A1, B1, C1))