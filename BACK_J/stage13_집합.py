
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
        
ques2()
        


    