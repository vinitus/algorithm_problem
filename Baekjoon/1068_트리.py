import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
lst = list(map(int, input().split()))
remove_node = int(input())
lst[remove_node] = -1
answer = N - 1
visited = [False] * N
visited[remove_node] = True
q = deque([remove_node])

while q:
    node = q.popleft()
    for i in range(N):
        if lst[i] == node:
            q.append(i)
            if not visited[i]:
                visited[i] = True
                answer -= 1
                lst[i] = -1


for i in range(N - 1, -1, -1):
    if lst[i] == -1:
        continue

    if not visited[lst[i]]:
        visited[lst[i]] = True
        answer -= 1

print(answer)
