# 소수 복습 https://www.acmicpc.net/problem/1978

def prime():

    n = int(input())
    arr = list(map(int, input().split()))

    def is_prime(n):
        if n==1:
            return False
        
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    result = 0
    for i in range(n):
        if is_prime(arr[i]):
            result+=1
    print(result)
#  소수 2 https://www.acmicpc.net/problem/1929
def prime2():

    a, b = map(int, input().split())
    arr = [True]*(b+1)
    arr[1]=False # 1은 소수가 아니다.
    c = int(b**0.5)

    for i in range(2, c+1):
        if arr[i]==True: # if문 필요한 이유. 다시 반복하게 되므로.
            for j in range(2*i, b+1, i):
                arr[j]=False

    for i in range(a,b+1):
        if arr[i]==True:
            print(i)

prime2()