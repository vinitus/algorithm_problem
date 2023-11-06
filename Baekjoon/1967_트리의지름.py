import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
tree = [[] for _ in range(N + 1)]


def dfs(node, total):
    q = deque([[node, total]])
    while q:
        node, total = q.popleft()
        for i in tree[node]:
            child, cost = i
            if visited[child] == -1:
                visited[child] = cost + total
                q.append([child, cost + total])


def reset_visited(idx):
    visited = [-1] * (N + 1)
    visited[idx] = 0

    return visited


tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    tree[a].append([b, c])
    tree[b].append([a, c])

visited = reset_visited(1)
visited[1] = 0
dfs(1, 0)

node1 = visited.index(max(visited))
visited = reset_visited(node1)
dfs(node1, 0)

print(max(visited))
