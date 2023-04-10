# 스택
stack = []
stack.append(5)
stack.append(4)
stack.pop()
stack.pop()

# 큐

from collections import deque

queue = deque()
queue.append(5)
queue.append(4)
queue.popleft()

# print(queue)

# 재귀 함수

def recursive_function(i):
    # 100번째 출력 했을 때 종료되도록 종료 조건 예시
    if i == 100:
        return
    
    print(i,'번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')

# recursive_function(1)

def factorial_iterative(n):
    result = 1 
    # 1부터 n까지의 수를 차례대로 곱하기

    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1 :
        return 1
    # n! = n * (n-1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n-1)

# print('반복적으로 구현',factorial_iterative(5))
# print('재귀적으로 구현',factorial_recursive(5))

# # DFS 실전 문제 음료수 얼려먹기

# n, m = map(int,input().split())

# graph = []
# for i in range(n):
#     graph.append(list(map(int,input())))

# # 입력 및 그래프 입력 받기.

# def dfs(x,y):
#     # 주어진 범위를 벗어나는 경우에는 즉시 종료
#     if x <= -1 or x >= n or y <= -1 or y >=m :
#         return False
    
#     # 현재 노트를 아직 방문하지 않았다면
#     if graph[x][y] == 0:
#         # 해당 노드 방문 처리
#         graph[x][y] = 1
        
#         # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
#         dfs(x-1,y)
#         dfs(x,y-1)
#         dfs(x+1,y)
#         dfs(x,y+1)
#         return True
#     return False

# result = 0

# for i in range(n):
#     for j in range(m):
#         # 현재 위치에서 DFS 수행
#         if dfs(i,j) == True:
#             result += 1

# print(result)


# BFS 미로 찾기

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int,input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  queue = deque()
  queue.append( (x,y) )
  # 큐가 빌때까지 반복
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m :
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx,ny))
  return graph[n-1][m-1]

print(bfs(0,0))




