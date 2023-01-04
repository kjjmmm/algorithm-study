
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

ques5()