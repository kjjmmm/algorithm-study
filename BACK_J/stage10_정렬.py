
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


def ques4():
    import sys
    n = int(sys.stdin.readline())

    arr=[]
    for i in range(n):
        arr.append(int(sys.stdin.readline()))
    arr.sort()

    for i in arr:
        print(i)


# 공간 복잡도 : 4mb = 100만개
# 시간 복잡도 : 1초 = 2천만번
# 카운팅 정렬까지 필요없고. 숫자의 범위가 1~10000 이므로 정렬에 카운트 해준다.
def ques5():
    import sys
    input = sys.stdin.readline

    count = [0] * 10001
    n = int(input())

    for i in range(n):
        count[int(input())] += 1

    for i in range(len(count)):
        for _ in range(count[i]):
            print(i)   


def ques6():
    import sys
    input = sys.stdin.readline

    n = int(input())

    arr=[]
    count_arr=[0]*8001
    for i in range(n):
        num = int(input())
        arr.append(num)
        count_arr[num+4000]+=1
    arr.sort()

    tmp_arr=[]
    for i in range(len(count_arr)):
        if max(count_arr)==count_arr[i]:
            tmp_arr.append(i-4000)
    tmp_arr.sort()

    result3=0
    if len(tmp_arr)>1 :
        result3=tmp_arr[1]
    elif len(tmp_arr)==1:
        result3=tmp_arr[0]
            
    result1=round(sum(arr)/n)
    result2=arr[int((n-1)/2)]
    result4=arr[-1]-arr[0]

    print(result1)
    print(result2)
    print(result3)
    print(result4)
    
def ques7():
    import sys
    input = sys.stdin.readline

    str_n = input()

    arr = list(str_n)
    arr.sort(reverse=True)
    result = ''.join(arr)

    print(result)

def ques8():
    import sys
    input = sys.stdin.readline

    n = int(input())

    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().split())))
    arr.sort(key=lambda x : (x[0], x[1]))
    
    for val in arr:
        print(val[0],val[1])


ques8()