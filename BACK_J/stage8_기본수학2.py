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
    a, b = map(int, input().split())

    for i in range(a, b+1):
        


ques4()