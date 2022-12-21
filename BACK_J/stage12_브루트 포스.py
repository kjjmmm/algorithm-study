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


# 와 어렵다... silver Class...
def ques4():
    a, b = map(int, input().split())

    arr=[]
    for i in range(a):
        arr.append(input())

    def ques4_sub(arr, x, y):
        cnt1=0
        for i in range(x[0],x[1]):
            for j in range(y[0],y[1]):                
                if i % 2 == 0 :
                    if j % 2 == 0 and arr[i][j] != 'W':
                        cnt1+=1
                    if j % 2 == 1 and arr[i][j] != 'B':
                        cnt1+=1
                if i % 2 == 1 :
                    if j % 2 == 0 and arr[i][j] != 'B':
                        cnt1+=1
                    if j % 2 == 1 and arr[i][j] != 'W':
                        cnt1+=1
        
        cnt2=0
        for i in range(x[0],x[1]):
            for j in range(y[0],y[1]):     
                if i % 2 == 0 :
                    if j % 2 == 0 and arr[i][j] != 'B':
                        cnt2+=1
                    if j % 2 == 1 and arr[i][j] != 'W':
                        cnt2+=1
                if i % 2 == 1 :
                    if j % 2 == 0 and arr[i][j] != 'W':
                        cnt2+=1
                    if j % 2 == 1 and arr[i][j] != 'B':
                        cnt2+=1
        
        return(min([cnt1,cnt2]))
    
    x = []
    for i in range(a-8+1):
        x.append([i, i+8])
    y = []
    for i in range(b-8+1):
        y.append([i, i+8])
    

    result_arr=[]
    for i in range(len(x)):
        for j in range(len(y)):
            result_arr.append(ques4_sub(arr,x[i],y[j]))

    print(min(result_arr));

ques4()

