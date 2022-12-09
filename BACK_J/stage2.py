def ques1():
    a, b = map(int, input().split())
    if a < b :
        print("<")
    if a > b :
        print(">")
    if a == b :
        print("==")

def ques2():
    a = int(input())

    if a >= 90:
        print("A")
    elif a >= 80:
        print("B")
    elif a >=70:
        print("C")
    elif a >=60:
        print("D")
    else:
        print("F")

def ques3():
    a = int(input())
    if a % 4 == 0 and ( a % 100!=0 or a % 400 == 0):
        print(1)
    else:
        print(0)
    
def ques4():
    x = int(input())
    y = int(input())

    if x>0 and y>0:
        print(1)
    elif x>0 and y<0:
        print(4)
    elif x<0 and y>0:
        print(2)
    elif x<0 and y<0:
        print(3)


def ques5():
    a, b = map(int, input().split())
    min = a*60 + b - 45
    if min < 0 :
        min += 60*24
    x = min // 60
    y = min % 60
    print(x, y)

def ques6():
    a, b = map(int, input().split())
    c = int(input())

    total_min = a*60 + b + c
    if total_min >= 60 * 24:
        total_min -= 60 * 24

    h = total_min // 60
    m = total_min % 60

    print(h,m)

def ques7():
    a, b, c = map(int, input().split())

    arr = [a,b,c]
    arr.sort()

    if a==b and b==c:
        print(10000+1000*a)
    elif a==b or b==c or a==c:
        print(1000+100*arr[1])
    else :
        print(arr[2] * 100)
    
ques7()