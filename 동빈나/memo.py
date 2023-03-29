### 복잡도

from random import randint
import time

# 배열에 10,000개의 정수를 삽입
array = []
for _ in range(10000):
    array.append(randint(1, 100)) # 1부터 100 사이의 랜덤한 정수

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i] # 스와프  

end_time = time.time() # 측정 종료
print("선택 정렬 성능 측정:", end_time - start_time) # 수행 시간 출력

# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

end_time = time.time() # 측정 종료
print("기본 정렬 라이브러리 성능 측정 :", end_time - start_time) # 수행 시간 출력

# ---------

# N = 1,000,000 이고 시간 복잡도 NlogN 일 경우 2천만번 수행 = 1초


## 탐색 알고리즘 DFS/BFS

DFS : Depth-First Search. 깊이 우선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘.
그래프는 노드와 간선으로 표현되며 이때 노드를 정점이라고도 말한다.
프로그래밍에서 그래프는 크게 2가지 방식으로 표현할수 있다.
 - 인접 행렬 : 2차원 배열로 그래프의 연결 관계를 표현하는 방식.
 - 인접 리스트 : 리스트로 그래프의 연결 관계를 표현하는 방식.
