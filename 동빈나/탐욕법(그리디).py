# 거스름돈

def ques1(n):
    
    money = n
    coin_type=[500, 100, 50, 10]
    coins = 0

    for i in coin_type:
        coins += money // i
        money = money % i
    
    print(coins)
    


# 큰 수의 법칙

def ques2():

    # N = 배열의 크기
    # M = 총 더해지는 횟수
    # K = 반복 할 수 있는 횟수

    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    sum = 0

    while(True):

        if M == 0 : break

        for _ in range(K):
            if M == 0 : break
            sum += arr[0]
            M -= 1
        sum+=arr[1]
        M-=1

    print(sum)

# 숫자 카드 게임

def ques3():
    a, b = map(int, input().split())

    arr = []

    for i in range(a):
        arr.append( min(list(map(int,input().split()))) )
    
    print(max(arr))

ques3()