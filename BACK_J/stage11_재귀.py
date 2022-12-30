def ques1():
    import sys
    input = sys.stdin.readline
    
    n = int(input())

    result=1
    for i in range(2,n+1):
        result*=i
    print(result)


def ques2():

    arr=[0,1]
    for _ in range(19):
        arr.append(arr[-1]+arr[-2])
    
    print(arr[int(input())])

def ques3():

    def recursion(s, l, r,cnt):
        cnt+=1
        if l >= r :
            return [1,cnt];
        elif s[l] != s[r] :
            return [0,cnt]
        else :
            return recursion(s, l+1, r-1,cnt)

    def isPalindrome(s,cnt):
        return recursion(s, 0, len(s)-1,cnt)

    n = int(input())
    for i in range(n):
        cnt = 0
        s = input()
        arr  = isPalindrome(s,cnt)
        print(' '.join(list(map(str, arr))))

def ques4():

    def merge_sort(arr):
        if len(arr) < 2 :
            return arr
        mid = len(arr) // 2
        low_arr = merge_sort(arr[:mid])
        high_arr  = merge_sort(arr[mid:])

        merged_arr = []
        l = h = 0

        while l < len(low_arr) and h < len(high_arr):
            


ques4()