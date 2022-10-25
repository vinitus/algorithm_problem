from re import L
import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
lst = list(list(map(int,input())) for _ in range(N))
visited = list(list(0 for _ in range(N)) for _ in range(N))
answer = [0, []]

def dfs(y,x):
    global answer
    stk = [(y,x)]
    visited[y][x] = 1
    cnt = 0
    while stk:
        y,x = stk.pop()
        cnt += 1
        for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N and lst[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = 1
                stk.append((ny,nx))
    else:
        answer[0] += 1
        answer[1].append(cnt)

for y in range(N):
    for x in range(N):
        if lst[y][x] and not visited[y][x]:
            dfs(y,x)
answer[1].sort()
print(answer[0])
for i in answer[1]:
    print(i)