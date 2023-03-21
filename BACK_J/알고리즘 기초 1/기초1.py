
def ques1():
    import sys
    input = sys.stdin.readline
    n = int(input())

    arr=[]
    for i in range(n):

        s = input()
        if 'push' in s:
            arr.append(int(s.split()[1]))
        if 'pop' in s:
            if len(arr)==0 : 
                print(-1)
            else:
                print(arr.pop(-1))
        if 'size' in s:
            print(len(arr))
        if 'empty' in s:
            if len(arr)==0:print(1)
            else : print(0)
        if 'top' in s:
            if len(arr)==0:print(-1)
            else:print(arr[-1])

def ques2():
    n = int(input())

    for i in range(n):
        arr = input().split()
        for j in range(len(arr)):
            arr[j]=arr[j][::-1]
        print(' '.join(arr))

def ques3():
    n = int(input())
    for i in range(n):

        s = input()
        while(True):
            if '()' in s :
                s=s.replace('()','')
            else : 
                break
        if len(s)>0 : print("NO")
        elif len(s)==0: print("YES")

def ques4():
    # 문제가 이해가안됨...스택 수열
    import sys
    input = sys.stdin.readline
    count = 1
    temp = True
    stack = []
    op = []

    n = int(input())
    for i in range(n):
    
        num = int(input())
        while count <= num:
            stack.append(count)
            op.append('+')
            count+=1
        if stack[-1] == num:
            stack.pop()
            op.append('-')
        else :
            temp = False
            break
    if temp == False:
        print("NO")
    else:
        for i in op:
            print(i)

def ques5():
    import sys
    input = sys.stdin.readline
    st1 = list(input().rstrip())
    st2=[]
    for _ in range(int(input())):
        cmm = input().split()

        if cmm[0]=='L':
            if st1:
                st2.append(st1.pop())
        elif cmm[0]=='D':
            if st2:
                st1.append(st2.pop())
        elif cmm[0]=='B':
            if st1:
                st1.pop()
        elif cmm[0]=='P':
            st1.append(cmm[1])    
    st1.extend(reversed(st2))
    print(''.join(st1))

def ques6():
    import sys
    input = sys.stdin.readline
    n = int(input())
    que = []
    for i in range(n):
        cmm = input().split()
        if cmm[0] == 'push':
            que.append(cmm[1])
        elif cmm[0] =='front':
            if que:
                print(que[0])
            else:
                print(-1)
        elif cmm[0] == 'back':
            if que:
                print(que[-1])
            else:
                print(-1)
        elif cmm[0] == 'size':
            print(len(que))
        elif cmm[0] == 'pop':
            if que:
                print(que[0])
                que.pop(0)
            else:
                print(-1)
        elif cmm[0] == 'empty':
            if que:
                print(0)
            else :
                print(1)
                
def ques7():
    a, b = map(int,input().split())
    arr = [i for i in range(1,a+1)]
    result = []
    
    cnt=0
    for i in range(a):
        cnt += b-1
        if cnt >= len(arr):
            cnt = cnt%len(arr)
        result.append(str(arr.pop(cnt)))
    print('<'+', '.join(result)+'>')

def ques8():
    import sys
    input = sys.stdin.readline

    deq = []
    n = int(input())
    for i in range(n):

        cmmd = input().split()

        if cmmd[0] == 'push_back':
            deq.append(cmmd[1])
        elif cmmd[0] == 'push_front':
            deq.insert(0,cmmd[1])
        elif cmmd[0] == 'front':
            if deq:
                print(deq[0])
            else:
                print(-1)
        elif cmmd[0] == 'back':
            if deq:
                print(deq[-1])
            else:
                print(-1)
        elif cmmd[0] == 'size':
            print(len(deq))
        elif cmmd[0] == 'pop_front':
            if deq:
                print(deq.pop(0))
            else:
                print(-1)
        elif cmmd[0] == 'pop_back':
            if deq:
                print(deq.pop(-1))
            else:
                print(-1)
        elif cmmd[0] == 'empty':
            if deq:
                print(0)
            else:
                print(1)

def ques9():

    s = input()

    tmp_str = ''
    result = ''
    rev = True
    for i in range(len(s)):
        if s[i] == '<':
            rev=False
            result+=tmp_str[::-1]
            result+='<'
            tmp_str=''
        elif s[i] == '>':
            rev=True
            result+=tmp_str
            tmp_str=''
            result+='>'
        elif s[i] == ' ':
            if rev==True:
                result+=tmp_str[::-1]
            else:
                result+=tmp_str
            result+=' '
            tmp_str=''
        elif i == (len(s)-1):
            if s[i]=='>':
                result+='>'
            else :
                tmp_str+=s[i]
                result+=tmp_str[::-1]
        else:
            tmp_str+=s[i]
    print(result)

def ques10():
    s = input().replace("()","|")
    s = s.strip("|")

    result=0
    line=0
    
    for i in range(len(s)):
        if s[i]=='(':
            line+=1
        elif s[i]=="|":
            result+=line
        elif s[i]==")":
            result+=1
            line-=1

    print(result)


def ques11():
    # 골드 클라스에 놀라 자빠진다.
    # 왜 stack 은 index로 저장해야하는지 알아보자.
    import sys
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    stack = []
    result =  [-1 for i in range(n)]

    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()]=arr[i]
        stack.append(i)

    print(*result)

# 나머지
def ques12():
    A, B, C = map(int, input().split())

    print((A+B)%C)
    print(((A%C) + (B%C))%C)
    print((A*B)%C)
    print(((A%C) * (B%C))%C)

# 최대공약수와 최소공배수
def ques13():
    a, b = map(int, input().split())

    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            print(i)
            print(int(a*b/i))
            break

# 최소공배수 - 뉴클리드 호제법 공부
def ques14():
    import sys
    import math
    input = sys.stdin.readline
    n = int(input())

    for i in range(n):
        
        a, b = map(int,input().split())
        print(math.lcm(a,b))

# 오등큰수
def ques15():
    # n = int(input())
    # input_arr = list(map(int,input().split()))

    # arr=[0]*1000001

    # result=[]
    # for i in range(len(input_arr)):
    #     arr[input_arr[i]]+=1

    # for i in range(len(input_arr)-1):
    #     for j in range(i+1,len(input_arr)):
    #         if arr[input_arr[i]]<arr[input_arr[j]]:
    #             result.append(input_arr[j])
    #             break
    #         elif j==len(input_arr)-1:
    #             result.append(-1)
    # result.append(-1)
    # print(*result)

    import sys
    input = sys.stdin.readline

    from collections import Counter

    n = int(input())
    aa = list(map(int,input().split()))
    ff = Counter(aa)
    stack = []
    ngf = [-1] * n

    for i in range(n):
        while stack and ff[aa[stack[-1]]] < ff[aa[i]]:
            ngf[stack.pop()] = aa[i]
        stack.append(i)

    print(*ngf) 

def ques16():
    import sys
    input = sys.stdin.readline
    def is_prime(n):
        if n == 1 :
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    breaker=True
    while breaker:
        num = int(input())
        if num == 0 : 
            breaker=False 
            break
        a, b = 3, num-3
        while b > 0 :
            if a > b :
                print('"Goldbach\'s conjecture is wrong."')
                break
            if is_prime(a) and is_prime(b):
                print(f'{num} = {a} + {b}')
                break
            else :
                a += 1
                b -= 1
        
def ques17():
    result=1
    n = int(input())
    for i in range(n,0,-1):
        result*=i
    str_result=str(result)

    cnt=0
    for i in range(len(str_result)-1,0,-1):
        if str_result[i]=='0':
            cnt+=1
        else: break
    print(cnt)

ques17()




