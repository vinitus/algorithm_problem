import sys


def input():
    return sys.stdin.readline().rstrip()


K = int(input())
lst = list(map(int, input().split()))

# for i in range(1,K+1):
#     print(*lst[2**(K-i)-1::2**(K-i+1)])

for i in range(K - 1, -1, -1):
    print(*lst[2**i - 1 :: 2 ** (i + 1)])
