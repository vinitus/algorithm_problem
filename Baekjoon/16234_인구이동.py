import sys
def input():
    return sys.stdin.readline().rstrip()

N, L, R = map(int, input().split())
lst = list(list(map(int,input().split())) for _ in range(N))
answer = 0

d = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs():
    global answer
    visited = list(list(0 for _ in range(N)) for _ in range(N))
    related = []
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                stk = [(y,x)]
                while stk:
                    y,x = stk.pop()
                    visited[y][x] = 1
                    for dy,dx in d:
                        ny = y + dy
                        nx = x + dx
                        if not visited[ny][nx] and L <= abs(lst[y][x] - lst[ny][nx]) <= R:
                            visited[ny][nx] = 1
                            stk.append((ny,nx))
                            