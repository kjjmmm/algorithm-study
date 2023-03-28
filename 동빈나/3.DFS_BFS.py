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

print(queue)

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

print('반복적으로 구현',factorial_iterative(5))
print('재귀적으로 구현',factorial_recursive(5))






