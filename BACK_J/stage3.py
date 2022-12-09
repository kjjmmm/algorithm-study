def ques1():
    a = int(input())
    for i in range(1,10):
        print(f"{a} * {i} = {a*i}")

def ques2():
    a = int(input())

    arr=[]
    for i in range(a):
        a, b = map(int, input().split())
        arr.append([a,b])
    for i in range(len(arr)):
        print(arr[i][0]+arr[i][1])

def ques3():
    a = int(input())
    sum=0;
    for i in range(1,a+1):
        sum+=i
    print(sum)

def ques4():
    total = int(input())
    n = int(input())

    sum=0
    for i in range(n):
        a, b = map(int, input().split())
        sum+=a*b
    if total == sum:
        print('Yes')
    else:
        print('No')

ques4()
