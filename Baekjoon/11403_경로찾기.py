import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
lst = list(list(map(int,input().split())) for _ in range(N))

def dfs(idx):
    visited = [0 for _ in range(N)]
    stk = [idx]
    while stk:
        now = stk.pop()
        for x in range(N):
            if lst[now][x] == 1 and not visited[x]:
                stk.append(x)
                visited[x] = 1
                lst[idx][x] = 1

for i in range(N):
    dfs(i)

for row in lst:
    print(*row)