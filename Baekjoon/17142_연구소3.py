import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
def input():
    return sys.stdin.readline().rstrip()

def check(y,x):
    return 0 <= y < N and 0 <= x < N

N, M = map(int,input().split())
lab_original = []
virus_can = deque([])
for y in range(N):
    lab_original.append(list(map(int,input().split())))
    for x in range(N):
        if lab_original[y][x] == 2:
            # lab_original[y][x] = 0
            virus_can.append((y,x))
arr = [i for i in range(len(virus_can))]

subset = list(combinations(arr,M))
answer = 100
for sub in subset:
    lab = deepcopy(lab_original)
    virus = deque(list(virus_can[i] for i in sub))
    while virus:
        y,x = virus.popleft()
        for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            new_y = y + dy
            new_x = x + dx
            if check(new_y,new_x):
                if lab[new_y][new_x] == 0:
                    lab[new_y][new_x] = lab[y][x] + 1
                    virus.append((new_y, new_x))
                elif lab[new_y][new_x] == 2:
                    for ddy, ddx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        n_y,n_x = new_y+ddy,new_x+ddx
                        if check(n_y,n_x) and lab[n_y][n_x] == 0:
                            lab[new_y][new_x] = lab[y][x] + 1
                            virus.append((new_y, new_x))
                            break
                        elif check(n_y,n_x) and lab[n_y][n_x] == 2:
                            if (new_y,new_x) in virus:
                                break
                    else:
                        pass
                else:
                    if lab[new_y][new_x] > lab[y][x] + 1:
                        lab[new_y][new_x] = lab[y][x] + 1
                        virus.append((new_y, new_x))

    now_max = 0
    for i in lab:
        if 0 in i:
            now_max = -1
            break
        if now_max < max(i):
            now_max = max(i)
    if now_max < answer and now_max != -1:
        answer = now_max
if answer == 100:
    print(-1)
else:
    print(answer - 2)