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

def ques4():
    import math
    a, b, v = map(int, input().split())

    day=0
    h = 0
    v-=b #한번만큼 빼줌

    print(math.ceil(v/(a-b)))


def ques6():
    
    t = int(input()) #TEST CASE

    for i in range(t) :
    
        k = int(input()) #층
        n = int(input()) #호

        arr=[[0] * (n+1) for i in range(k+1)] #0층 부터 k층까지 배열 선언

        for i in range(1,n+1):
            arr[0][i]=i
        
        def ques6_sub(k,n): 
            sum=0
            for i in range(1,n+1):
                sum+=arr[k-1][i]
            return sum

        for i in range(1,k+1):
            for j in range(1,n+1):
                arr[i][j]=ques6_sub(i,j)
        
        print(arr[k][n])

def ques8():

    a, b = map(int, input().split())

    print(a+b)



ques4()