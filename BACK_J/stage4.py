def ques1():
    n = input()
    arr = input().split()
    m = input()

    cnt=0
    for i in range(len(arr)):
        if arr[i]==m :
            cnt+=1
    print(cnt)

ques1()