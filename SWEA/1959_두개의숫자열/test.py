import sys

sys.stdin = open("1959_두개의숫자열/input.txt","r")

# 길이가 5, 3인 리스트가 있을 때 문제에 해당하는 연산을 하려면
# 0 1 2 3 4
# 0 1 2
#   0 1 2
#     0 1 2

#이렇게 총 3번을 하면된다 3 => 5 - 3 + 1 => M - N + 1

T = int(input())

for t in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    max = 0
    if N < M:
        for i in range(M-N+1):
            result = 0
            for n in range(N):
                result = result + A[n]*B[i+n]
            if result > max:
                max = result
    else:
        for i in range(N-M+1):
            result = 0
            for n in range(M):
                result = result + A[i+n]*B[n]
            if result > max:
                max = result
    print(f"#{t} {max}")