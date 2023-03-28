from random import randint
import time

# 구현이란 : 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정 [완전탐색, 시뮬레이션 유형] 을 포함한다.
# 완전 탐색 : 모든 경우의 수를 주저 없이 다 계산하는 해결 방법
# 시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행

# 상하좌우

def ques1():
    n = int(input())
    arr = list(input().split())

    x = 1
    y = 1

    for i in arr:
        if i == 'L':
            if x > 0 :
                x-=1
            
        elif i == 'R':
            if x < n :
                x+=1

        elif i == 'U':
            if y > 1 :
                y-=1

        elif i == 'D':
            if y < n :
                y+=1
    
    print(y, x)

# 시각

def ques2():
    
    n = int(input())

    start_time=time.time()

    cnt = 0

    for i in range(n+1):
        for j in range(60):
            for k in range(60):

                if '3' in str(i) or '3' in str(j) or '3' in str(k) :
                    cnt+=1

    end_time = time.time()


    print(cnt, end_time-start_time)

# 왕실의 나이트

def ques3():
    key = input()

    x = ord(key[0])-96
    y = int(key[1])
    
    steps = [(2,1),(2,-1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2)] # 8가지
    cnt = 0

    for i in steps:
        if x + i[0] > 0 and y + i[1] > 0:
            cnt+=1

    print(cnt)

# 게임 개발
def ques4():
    n,m = map(int,input().split())

    x,y,d = map(int,input().split())

    game_map=[]
    for i in range(m):
        game_map.append( list(map(int,input().split())) )

    rot = 0
    cnt = 1
    game_map[x][y]=1
    while(True):

        if rot > 4 : break

        if d == 0:
            if y-1 < 0 or game_map[x][y-1] == 1 :
                d = 3
                rot+=1
            else : 
                y-=1
                game_map[x][y]=1
                cnt+=1
                print(x, y, "입력")
        elif d == 1:
            if x+1 > n or game_map[x+1][y] == 1 :
                d = 0
                rot+=1
            else : 
                x+=1
                game_map[x][y]=1
                cnt+=1
                print(x, y, "입력")
        elif d == 2:
            if y+1 > m or game_map[x][y+1] == 1 :
                d = 1
                rot+=1
            else : 
                y+=1
                game_map[x][y]=1             
                cnt+=1
                print(x, y, "입력")
        elif d == 3:
            if x-1 < 0 or game_map[x-1][y] == 1 :
                d = 2
                rot+=1
            else :
                x-=1
                game_map[x][y]=1
                cnt+=1
                print(x, y, "입력")
    print(game_map)
    print(cnt)

ques4()
