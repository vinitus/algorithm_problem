import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


N, W = map(int, input().split())

tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

answer = 0
visited = [False for _ in range(N + 1)]

q = deque([1])

while q:
    idx = q.popleft()
    visited[idx] = True
    if len(tree[idx]) == 1 and visited[tree[idx][0]]:
        answer += 1
    for i in tree[idx]:
        if not visited[i]:
            q.append(i)

print(W / answer)
