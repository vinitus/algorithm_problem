from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()

N, K = map(int,input().split())
lst = []
q = deque([])
for y in range(N):
    tmp = list(map(int,input().split()))
    for x in range(N):
        if tmp[x] != 0:
            q.append((tmp[x],y,x))
    lst.append(tmp)
t,gy,gx = map(int,input().split())

d = [(-1,0),(1,0),(0,-1),(0,1)]

q = deque(sorted(q))

def bfs():
    global q
    n = 0
    cnt = len(q)
    while q and n != t:
        cnt -= 1
        now,y,x = q.popleft()
        for dy,dx in d:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if lst[ny][nx] == 0:
                    lst[ny][nx] = now
                    q.append((now,ny,nx))
                # elif lst[ny][nx] > lst[y][x]:
                #     lst[ny][nx] = now
                #     q.append((ny,nx))
        if cnt == 0:
            cnt = len(q)
            n += 1
            q = deque(sorted(q))
    print(lst[gy-1][gx-1])

bfs()