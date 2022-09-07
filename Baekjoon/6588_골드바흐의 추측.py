#골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n<10000이 주어진다.

# import time
# import sys

# start = time.time()
# def prime(number):
#     if number == 1:
#         return False
#     for i in range(2,int(number**0.5)+1):
#         if number % i == 0:
#             return False
#     return True

# list_prime = set()
# for i in range(2,10001):
#     if prime(i):
#         list_prime.add(i)

# T = int(sys.stdin.readline())

# while T != 0:
#     n = int(sys.stdin.readline())
#     min = 9999
#     min_tmp = 9999
#     min_i = 9999
#     for i in list_prime:
#         if i > n / 2:
#             break
#         tmp = n-i
#         if tmp in list_prime:
#             if min > tmp - i:
#                 min = tmp - i
#                 min_i = i
#                 min_tmp = tmp
#     print(min_i, min_tmp)
#     T -= 1

import time
import sys

def prime(number):
    if number == 1:
        return False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

T = int(sys.stdin.readline())

while T != 0:
    n = int(sys.stdin.readline())
    for i in range(n//2):
        to_min = n // 2
        to_min -= i
        tmp = n - to_min
        if prime(to_min):
            if prime(tmp):
                print(min(to_min,tmp),max(to_min,tmp))
                break       
    T -= 1