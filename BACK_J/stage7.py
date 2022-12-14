def ques1():
    import math
    a, b ,c = map(int, input().split())

    if b >= c : 
        print(-1)
    else :
        result = math.ceil((a+1)/(c-b))
        print(result)


# 대가리 터질뻔했네 ;;;
def ques2():
    n = int(input())
    cnt = 1
    sum = 1

    if n==1: print(1)

    else :
        while True:

            if (n-1) <= 6 * sum:
                break
            cnt+=1
            sum+=cnt
        print(cnt+1)


# 늙었다 ...... 이해가 좀 늦네
def ques3():
    n = int(input())
    a=1 # 어느 라인에 있는가 ? 
    while True:
        if a*(a+1)/2>=n:
            break;
        a+=1

    dif = int(a*(a+1)/2 - n)

    b=0
    c=0
    if a % 2 == 0 : 
        b = a - dif 
        c = dif + 1
    else :
        b = 1 + dif
        c = a - dif
    print(f"{b}/{c}")

ques3()