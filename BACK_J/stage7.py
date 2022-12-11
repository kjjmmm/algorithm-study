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

ques2()
