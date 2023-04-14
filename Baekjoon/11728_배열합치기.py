import sys
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

a = b = 0
answer = []

while a != N or b != M:
    if a == N:
        answer += [B[b]]
        b += 1
    elif b == M:
        answer += [A[a]]
        a += 1
    else:
        if A[a] < B[b]:
            answer += [A[a]]
            a += 1
        else:
            answer += [B[b]]
            b += 1

print(*answer)