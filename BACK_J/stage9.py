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
    

ques1()


