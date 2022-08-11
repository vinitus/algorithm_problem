import sys
input = sys.stdin.readline

N = int(input())

if N == 1 or N == 2:
    print(N)
else:
    tmp = 2
    while True:
        if N <= tmp:
            tmp //= 2
            print((N - tmp) * 2)
            break
        tmp *= 2        