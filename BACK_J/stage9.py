def ques1():
    n, m = map(int, input().split())

    arr1 = [[0] * m for _ in range(n)]
    arr2 = [[0] * m for _ in range(n)]
    result = [[0] * m for _ in range(n)]

    for i in range(n):
        arr = list(map(int, input().split()))
        for j in range(m):
            arr1[i][j]=arr[j]
    for i in range(n):
        arr = list(map(int, input().split()))
        for j in range(m):
            arr2[i][j]=arr[j]

    for i in range(n):
        tmp_arr=[]
        for j in range(m):
            tmp_arr.append(str(arr1[i][j] + arr2[i][j]))
        a = " ".join(tmp_arr)
        print(a)

def ques2():
    arr = [[0] for _ in range(9)]
    n = 0 
    m = 0
    row_max = []
    for i in range(9):
        arr[i] = list(map(int,input().split()))
        row_max.append(max(arr[i]))

    result_mx = max(row_max)
    print(result_mx)
    for i in range(9):
        for j in range(9):
            if arr[i][j]==result_mx:
                n=i
                m=j
                break;
        
    print(n+1,m+1)

ques2()


