import sys


def input():
    return sys.stdin.readline().rstrip()


N, X = map(int, input().split())
blog = [0] + list(map(int, input().split()))

for i in range(1, N + 1):
    blog[i] += blog[i - 1]

answer = 0
cnt = 0

for i in range(X - 1, N + 1):
    cal = blog[i] - blog[i - X]
    if cal > answer:
        answer = cal
        cnt = 1
    elif cal == answer:
        cnt += 1

if answer:
    print(answer)
    print(cnt)
else:
    print("SAD")
