def ques1():
    # 순열 조합 import
    from itertools import combinations
    import sys
    input = sys.stdin.readline
    
    a, b = map(int, input().split())
    arr = list(map(int, input().split()))

    com_arr = list(combinations(arr, 3))

    for i in range(len(com_arr)):
        com_arr[i]=sum(com_arr[i])
    
    com_arr.sort()
    
    result_num=0
    for i in range(len(com_arr)):
        if com_arr[i] > b : 
            break
        result_num=com_arr[i]
    
    print(result_num)
ques1()



