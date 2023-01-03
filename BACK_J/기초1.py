
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

ques3()