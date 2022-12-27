def ques1():
    n = int(input())
    arr = list(map(int, input().split()))

    result=0
    for i in range(n):
        
        tmp_cnt=0
        for j in range(1,arr[i]):
            if arr[i] % j == 0:
                tmp_cnt+=1

        if tmp_cnt==1:
            result+=1

    print(result)

def ques2():
    a = int(input())
    b = int(input())

    result = []
    for i in range(a,b+1):
        if i>2 and i%2==0:continue
        cnt=0
        for j in range(2,i):
            if i % j == 0:
                cnt+=1
            if cnt>0:break
        if cnt==0:
            result.append(i)

    if a==1 and b > 1 : del result[0]

    if a==1 and b==1 : print(-1)

    elif len(result)==0:
        print(-1)
    else:
        print(sum(result))
        print(result[0])

def ques3():
    import sys
    input = sys.stdin.readline
    n = int(input())

    breaker=True
    tmp=n

    while(breaker):

        if tmp < 4 : 

            if tmp==1:
                break

            print(tmp) 
            break

        for i in range(2,tmp):

            if tmp % i==0:
                print(i)
                tmp=tmp//i
                break;
            if i==tmp-1:
                breaker=False
                print(tmp)

def ques4(): 
    #소수의 범위가 주어질때 가장 빠른 에라토스테네스의 체.
    a, b = map(int, input().split())
    c = int(b**(0.5))+1

    arr = [True] * (b+1)
    arr[1]=False

    for i in range(2, c):
        if arr[i] == True:
            for j in range(2*i, b+1, i):
                arr[j]=False
    for i in range(a, b+1):
        if arr[i]==True : print(i)

def ques5():
    import sys
    input = sys.stdin.readline

    arr = [True] * (123456*2 + 1)
    c= int(len(arr)**0.5 + 1 )
    arr[1]=False
    for i in range(2, c):
        if arr[i]==True:
            for j in range(2*i, len(arr), i):
                    arr[j]=False
    while(True):

        n = int(input())
        if n == 0 : break

        print(sum(arr[n+1:n*2+1]))
# 소수 판별 -- 시간 초과
# def ques5_2():
#     import sys
#     input = sys.stdin.readline

#     def is_sos(x):

#         if x == 1 : return 1
#         c = int(x ** 0.5) +  1
#         for i in range(2,c):
#             if x % i == 0 : return False

#         return 1
#     while(True):
#         n = int(input())
#         if n == 0 : break

#         cnt=0
#         for i in range(n+1, 2*n+1):
#             if 1 == is_sos(i):
#                 cnt+=1
#         print(cnt)

def ques6():
    import sys
    input = sys.stdin.readline
    
    arr = [True]*(10001)
    c = int(len(arr)**0.5 + 1)
    arr[1]=False

    for i in range(2, c):
        if arr[i]==True:
            for j in range(2*i, 10001, i):
                arr[j]=False

    n = int(input())

    for _ in range(n):

        a = int(input())
        c = int(a**0.5+1)

        result=[]
        for i in range(2,a):
            if arr[i]==True and arr[a-i]==True:
                result.append([abs((a-i)-i), i, a-i])
        result.sort(key=lambda x : x[0])
        print(result[0][1], result[0][2])

def ques6_2():
    import sys
    input = sys.stdin.readline

    # 소수 판별 기본
    def is_prime(n):
        if n==1 :
            return False
        for i in range(2, int(n**0.5+1)):
            if n % i == 0 :
                return False
        return True
    
    rep = int(input())

    for _ in range(rep):
        n = int(input())
        a = n//2
        b = n//2

        while True:
            if is_prime(a) and is_prime(b):
                print(str(a),str(b))
                break
            else:
                a-=1
                b+=1





        
        
ques6()