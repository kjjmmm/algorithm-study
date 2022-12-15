
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


ques5()
    
    