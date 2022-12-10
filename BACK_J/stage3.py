
def ques1():
    a = int(input())
    for i in range(1,10):
        print(f"{a} * {i} = {a*i}")

def ques2():
    a = int(input())

    arr=[]
    for i in range(a):
        a, b = map(int, input().split())
        arr.append([a,b])
    for i in range(len(arr)):
        print(arr[i][0]+arr[i][1])

def ques3():
    a = int(input())
    sum=0;
    for i in range(1,a+1):
        sum+=i
    print(sum)

def ques4():
    total = int(input())
    n = int(input())

    sum=0
    for i in range(n):
        a, b = map(int, input().split())
        sum+=a*b
    if total == sum:
        print('Yes')
    else:
        print('No')



def ques5():
    import sys

    n = int(sys.stdin.readline().rstrip())
    for i in range(n):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        print(a+b)

def ques6():
    n = int(input())
    for i in range(n):
        a, b = map(int,input().split())
        print(f"Case #{i+1}: {a+b}")
        

        
def ques7():    
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        print(f"Case #{i+1}: {a} + {b} = {a+b}")

def ques8():
    n = int(input())
    for i in range(n):
        print("*"*(i+1))


def ques9():
    n = int(input())
    for i in range(n):
        print(" "* (n-(i+1)) + "*"* (i+1) )

def ques10():

    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0 :
            break;

        print(a+b)

def ques11():

    while True:
        try :
            a, b = map(int, input().split())
            print(a+b)
        except EOFError:
            break;

def ques12():
    first_input = input()
    if int(first_input) < 10 :
        first_input = "0"+first_input
    save = first_input
    cnt=0

    def ques12_sub(n):
        
        first = n[0]
        last = n[len(n)-1]
        c = str(int(first) + int(last))
        c = c[len(c)-1]
        return(last+c)

    while(True):
        save = ques12_sub(save)
        cnt+=1
        if first_input==save :
            print(cnt)
            break
        
# 파이썬 함수 정의 와 변수 선언은 보통 어떻게 할까 ? 
ques12()


