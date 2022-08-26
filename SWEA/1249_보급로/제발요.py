from collections import deque
import sys

sys.stdin = open("input.txt","r")

def check(x,y):
    global N
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False

def move():
    global supply_road, answer, q
    while q:
        tmp = q.popleft()
        y,x = tmp[0],tmp[1]
        for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            my,mx = y+dy, x+dx
            if check(my,mx) and answer[my][mx] > answer[y][x]+supply_road[my][mx]:
                answer[my][mx] = answer[y][x]+supply_road[my][mx]
                q.append([y,x])
    return answer[-1][-1]

T = int(input())
for t in range(1,T+1):
    N = int(input())
    supply_road = list(list(map(int,input())) for _ in range(N))
    nine = 9*N**2
    answer = list([nine] * N for _ in range(N))
    q = deque()
    q.append([0,0])
    print(f'#{t} {move()}')