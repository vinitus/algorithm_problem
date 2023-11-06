import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
lst = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(N - 1):
    a, b = map(int, input().split())
    lst[a] += [b]
    lst[b] += [a]

q = deque([1])

while q:
    idx = q.popleft()
    for i in lst[idx]:
        if not visited[i]:
            visited[i] = idx
            q.append(i)

for i in range(2, N + 1):
    print(visited[i])
