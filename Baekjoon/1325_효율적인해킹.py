import sys


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

answer = 0
answer_idx_list = []

for i in range(1, N + 1):
    cnt = 0
    stk = [i]
    visited = [False] * (N + 1)
    while stk:
        cnt += 1
        idx = stk.pop()
        for j in graph[idx]:
            if not visited[j]:
                stk.append(j)
                visited[j] = True
    if cnt > answer:
        answer = cnt
        answer_idx_list = [i]
    elif cnt == answer:
        answer_idx_list.append(i)

answer_idx_list.sort()

print(*answer_idx_list)
