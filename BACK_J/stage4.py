def ques1():
    n = input()
    arr = input().split()
    m = input()

    cnt=0
    for i in range(len(arr)):
        if arr[i]==m :
            cnt+=1
    print(cnt)

def ques2():
    a, b = map(int, input().split())
    c = list(map(int, input().split()))

    result = []
    for i in range(len(c)):
        if c[i] < b :
            result.append(str(c[i]))
    print(" ".join(result))

def ques3():
    n = int(input())
    arr = list(map(int,input().split()))
    print(min(arr), max(arr))

def ques4():
    arr=[]
    for i in range(9):
        arr.append(int(input()))        

    print(max(arr))
    print(arr.index(max(arr))+1)

def ques5():
    arr=[0]*31
    arr[0]=1

    for i in range(28):
        n = int(input())
        arr[n]+=1
    for i in range(len(arr)):
        if arr[i]==0 :
            print(i)

def ques6():
    arr=[]
    for i in range(10):
        arr.append(int(input()) % 42)
    arr = list(set(arr))
    print(len(arr))

def ques7():
    n = int(input())
    arr = list(map(int, input().split()))
    x = max(arr)

    for i in range(len(arr)):
        arr[i]=arr[i]/x*100
    avg = sum(arr)/len(arr)
    print(avg)

def ques8():
    n = int(input())

    arr=[]
    for i in range(n):
        arr.append(input())

    for i in range(len(arr)):
        sum=0
        point=1
        for j in range(len(arr[i])):
            if arr[i][j]=="O":
                sum+=point
                point+=1
            else : 
                point=1
                continue
        print(sum)

def ques9():

    def ques9_sub(arr):
        avg = (sum(arr)-arr[0])/(len(arr)-1)
        person = 0
        for i in range(1, len(arr)):
            if arr[i] > avg :
                person+=1
        percent = format(round(person / (len(arr)-1) * 100,3), ".3f")
        print(str(percent)+"%")

    n = int(input())
    for i in range(n):
        arr = list(map(int, input().split()))
        ques9_sub(arr)

ques9()