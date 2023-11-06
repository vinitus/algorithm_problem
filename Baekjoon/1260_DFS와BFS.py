import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N + 1):
    graph[i].sort()

visited = [False] * (N + 1)
visited[V] = True

dfs_print = ""


def dfs(idx):
    global dfs_print
    dfs_print += f"{idx} "
    for i in graph[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i)


dfs(V)

print(dfs_print)

visited = [False] * (N + 1)
visited[V] = True

q = deque([V])
bfs_print = f"{V}"

while q:
    idx = q.popleft()
    for i in graph[idx]:
        if not visited[i]:
            q.append(i)
            bfs_print += f" {i}"
            visited[i] = True

print(bfs_print)
