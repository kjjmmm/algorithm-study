# 재귀함수의 팩토리얼.
# 이것조차 이해하는데 어려웠음

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print(factorial(5))