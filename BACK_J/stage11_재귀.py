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

def merge_sort(s, e):
    if s > e:
        return []
    if s == e:
        return [arr[s]]
    mid = (s + e) // 2
    l = merge_sort(s, mid)
    r = merge_sort(mid + 1, e)
    lr = l + r
    lr.sort()
    global cnt
    if cnt + (e - s + 1) < m:
        cnt += e - s + 1
        return lr
    else:
        print(lr[m - cnt - 1])
        exit()


n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
cnt = 0
merge_sort(1, n)
print(-1)



