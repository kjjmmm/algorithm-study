
def ques1():
    n = int(input())

    arr=[]
    for i in range(n):
        a = int(input())
        arr.append(a)
    arr.sort()

    for i in arr:
        print(i)

def ques2():
    arr=[]
    for _ in range(5):
        a = int(input())
        arr.append(a)
    arr.sort()
    print(int(sum(arr)/5))
    print(arr[2])

def ques3():
    a, b = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)
    print(arr[b-1])
ques3()
    
    