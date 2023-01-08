
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