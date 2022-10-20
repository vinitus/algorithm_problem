import sys
def input():
    return sys.stdin.readline().rstrip()

d = [(-1,0),(1,0),(0,-1),(0,1)]

R, C, K = map(int, input().split())
adj = [list(input()) for _ in range(R)]

visited = [[0 for _ in range(C)] for _ in range(R)]
answer = 0

def dfs(y, x, cnt):
    global answer
    visited[y][x] = 1
    if y == 0 and x == C-1:
        if cnt == K:
            answer += 1
        return 

    for dy,dx in d:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < R and 0 <= nx < C and visited[ny][nx] == 0 and adj[ny][nx] != 'T':
            visited[ny][nx] = 1
            dfs(ny, nx, cnt+1)
            visited[ny][nx] = 0

dfs(R-1, 0, 1)

print(answer)