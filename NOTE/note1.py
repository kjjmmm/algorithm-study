# 시간 측정

import time
start_time = time.time() # 측정 시작

# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("time: ", end_time - start_time) # 수행 시간 출력


# 유클리드 호제법
# 최대공약수를 구한다.
# 최대공약수(Greatest Common Divisor, GCD)
# 최소공배수(Lowest Common Multiple, LCM)
#  gcd(a, b) = 1 이면 a, b 는 서로소 관계 이다.



# (a>b)일때 a 와 b 의 최대공약수는 b 와 r 의 최대공약수와 같다. r은 a를 b로 나눈 나머지.
# 보통 재귀 함수로 구현한다.

def euclidean(a, b):

    print('start',a%b)

    if a % b == 0 : 
        return b
    # b 는 최대 공약수 : GCD

    else :
        a, b = b, a % b
        return euclidean(a, b)

print(euclidean(17,3))