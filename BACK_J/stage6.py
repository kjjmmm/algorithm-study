def ques1():
    a = input()
    print(ord(a))

def ques2():
    n =  int(input())
    str_nums = input()
    result=0
    for i  in range(len(str_nums)):
        result+=int(str_nums[i])
    print(result)

def ques3():
    input_str = input()
    arr = [-1]*26

    for i in range(len(input_str)):
        arr[ord(input_str[i])-97]=input_str.index(input_str[i])

    arr = list(map(str, arr))
    print(' '.join(arr))

def ques4():
    n = int(input())
    for i in range(n):
        n, s = input().split()

        result=""
        for j in range(len(s)):
            result+=s[j]*int(n)
        print(result)

def ques5():
    arr = [0]*26

    s = input()

    for i in range(len(s)):
        arr[ord(s[i].upper())-65]+=1
    mx = max(arr)

    chk = 0
    for j in range(len(arr)):
        if arr[j]==mx :
            chk += 1
    if chk > 1 :
        print("?")
    else :
        print(chr(arr.index(mx)+65))

def ques6():
    s = input()
    arr = s.split()
    print(len(arr))
    
    
def ques7():
    s = input()

    rev_s = ""
    for i in range(len(s)-1,-1,-1):
        rev_s+=s[i]
    arr = list(map(int, rev_s.split()))
    print(max(arr))

def ques8():
    s = input()
    arr = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]

    result=0
    for i in range(len(s)):
        result+=arr[ord(s[i])-65]
    print(result)

def ques9():
    s = input()
    arr = ["c=","c-","dz=","d-","lj","nj","s=","z="]

    for i in range(len(arr)):
        s=s.replace(arr[i],'*')
    print(len(s))

def ques10():
    n = int(input())
    cnt = 0

    for i in range(n):
        s = input()
        pre = ""
        arr = []
        for j in range(len(s)):
            if pre == s[j] : 
                continue
            pre = s[j]
            arr.append(pre)

        for k in range(len(arr)):
            if arr.count(arr[k]) > 1:
                break;
            if k==len(arr)-1:
                cnt+=1
    print(cnt)
    

ques10()








