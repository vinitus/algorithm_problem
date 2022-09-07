def factorial(num):
    tmp = 1
    for i in range(1, num+1):
        tmp *= i
    return tmp


T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    bridge = int( factorial(m) / (factorial(n) * factorial(m - n)) )
    print(bridge)