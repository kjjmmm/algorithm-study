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

def ques2():
    import sys
    input = sys.stdin.readline

    def ques2_sub(n):
        str_n = str(n)

        result = n
        for i in range(len(str_n)):
            result += int(str_n[i])
        return result

    n = int(input())

    for i in range(1,10000001):
        if n <= i :
           print(0)
           break;
        if ques2_sub(i)==n :
           print(i)
           break;
def ques3():
    import sys
    input = sys.stdin.readline
    n = int(input())

    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    for i in range(len(arr)):
        cnt=0
        for j in range(len(arr)):
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                cnt+=1
        print(cnt+1, end=" ")


ques3()


