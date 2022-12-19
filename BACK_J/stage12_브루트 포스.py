def ques1():
    # 순열 조합 import
    from itertools import permutations, combinations
    import sys
    input = sys.stdin.readline
    
    a, b = map(int, input().split())
    arr = list(map(int, input().split()))

    com_arr = list(combinations(arr, 3))
    
    com_arr.sort()
    result_num=0
    for i in range(len(com_arr)):
        if sum(com_arr[i]) > b : 
            break
        result_num=sum(com_arr[i])
    
    print(result_num)
ques1()



