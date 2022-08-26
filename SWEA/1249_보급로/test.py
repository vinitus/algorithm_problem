import sys

sys.stdin = open("input.txt","r")

def check(y,x,N):
    if 0 <= y < N and 0 <= x < N:
        return 1
    else:
        return 0

def bfs(lst,N):
    max_val = sum(lst[0])
    for i in range(1,N):
        max_val += lst[i][-1]
    s = (0,0)
    e = (N-1,N-1)
    q = [[s[0],s[1],[(1,1)],0]]
    while q:
        y,x,visited,sum_value = q.pop(0)
        for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            yy,xx = y+dy,x+dx
            if check(yy,xx,N) and (yy,xx) not in visited:
                if sum_value+lst[yy][xx] > max_val:
                    continue
                elif (yy, xx) == e:
                    if sum_value < max_val:
                        max_val = sum_value
                    break
                q.append([yy,xx,visited+[(yy,xx)],sum_value+lst[yy][xx]])
    else:
        return max_val


T = int(input())
for t in range(1,T+1):
    N = int(input())

    supply_road = []
    empty_space = []

    for _ in range(N):
        supply_road.append(list(map(int,input())))

    print(f'#{t} {bfs(supply_road,N)}')