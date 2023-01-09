def ques1():
    import sys
    input = sys.stdin.readline
    a, b = map(int, input().split())

    arr=[]
    for i in range(a):
        arr.append(int(input()))
    
    arr.sort(reverse=True)
    cnt = 0
    for i in range(len(arr)):
        if b == 0 : break
        if arr[i] <= b :
            cnt += b // arr[i]
            b = b % arr[i]
    print(cnt)
ques1()