import sys
def input():
    return sys.stdin.readline().rstrip()

K, N = map(int,input().split())
lst = list(int(input()) for _ in range(K))

s = 0
e = max(lst)

while s <= e:
    m = (s+e) // 2
    if m == 0:
        break
    cnt = 0
    for i in lst:
        cnt += i // m
    if cnt >= N:
        s = m+1
    else:
        e = m-1

print(e)