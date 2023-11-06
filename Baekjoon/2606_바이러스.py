import sys


def input():
    return sys.stdin.readline().rstrip()


com = int(input())
N = int(input())
graph = [[] for _ in range(com + 1)]

for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

stk = [1]
visited = [False] + [False] * com

while stk:
    idx = stk.pop()
    visited[idx] = True
    for i in graph[idx]:
        if not visited[i]:
            stk.append(i)

cnt = 0
for i in visited:
    if i:
        cnt += 1

print(cnt - 1)
