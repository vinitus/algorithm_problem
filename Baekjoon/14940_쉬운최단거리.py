import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def check(y, x):
    return 0 <= y < Y and 0 <= x < X


Y, X = map(int, input().split())
graph = []
start = (0, 0)
visited = [[False for _ in range(X)] for _ in range(Y)]
dijkstra = [[-1 for _ in range(X)] for _ in range(Y)]

for y in range(Y):
    x_input = list(map(int, input().split()))
    for x in range(X):
        if x_input[x] == 0:
            dijkstra[y][x] = 0
            visited[y][x] = True
        elif x_input[x] == 2:
            start = (y, x)
            dijkstra[y][x] = 0
            visited[y][x] = True
    graph.append(x_input)

q = deque([start])
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    y, x = q.popleft()
    for dy, dx in d:
        ny = y + dy
        nx = x + dx
        if check(ny, nx) and not visited[ny][nx]:
            dijkstra[ny][nx] = dijkstra[y][x] + 1
            visited[ny][nx] = True
            q.append((ny, nx))

for y in range(Y):
    for x in range(X):
        print(dijkstra[y][x], end=" ")
    print()
