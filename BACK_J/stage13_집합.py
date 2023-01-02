
def ques1():

    result=[]
    n = int(input())
    arr1 = set(input().split())

    m = int(input())
    arr2 = input().split()

    for i in arr2:
        if i in arr1 : 
            result.append(1)
        else :
            result.append(0)

    print(*result)


def ques2():
    import sys
    input = sys.stdin.readline

    a, b = map(int, input().split())

    arr=set()
    for i in range(a):
        arr.add(input())
    cnt=0
    for i in range(b):
        if input() in arr:
            cnt+=1

    print(cnt)
def ques6():
    a, b = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    print(len(A - B) + len(B - A))

        
def ques7():
    s = input()
    arr = set()
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            arr.add(s[i:j])
    print(len(arr))

ques7()
        


    