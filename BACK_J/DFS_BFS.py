# https://www.acmicpc.net/problem/1260
# DFS와 BFS

# 정점 번호는 1부터 N까지
# n : 정점/노드의 개수, m : 간선의 개수, v : 탐색시작의 정점의 번호
from collections import deque

n, m, v = map(int, input().split())

graph = [ [0]*(n+1) for _ in range(n+1) ]
# 좌표 그리기
visited = [0]*(n+1)
# 방문 체크

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1
    # 좌표 x,y - y,x 그리기

def DFS(v):
    print(v, end=' ')
    visited[v]=1
    # dfs 방문 체크
    for i in range(1,n+1):
        if visited[i]==0 and graph[v][i]==1:
            # 방문하지 않았고, 그래프 연결된 경우 dfs 실행
            DFS(i)


def BFS(v):
    queue = deque([v])
    # 큐 생성
    visited[v] = 0
    # 방문처리를 0으로

    while(queue):
        v = queue.popleft()
        print(v, end=' ')

        for i in range(1, n+1):
            if visited[i] == 1 and graph[v][i] == 1 :
                queue.append(i)
                visited[i] = 0

DFS(v)
print()
BFS(v)





