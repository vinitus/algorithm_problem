import sys
from collections import deque
from itertools import combinations
def input():
    return sys.stdin.readline().rstrip()

def check(y,x):
    return 0 <= y < N and 0 <= x < N

delta = [(-1,0),(1,0),(0,-1),(0,1)]

N, M = map(int,input().split())

virus = []
lab_ori = list(list() for _ in range(N))
for y in range(N):
    tmp = list(map(int,input().split()))
    for x in range(N):
        if tmp[x] == 2:
            virus.append((y,x))
            lab_ori[y].append(0)
        else:
            lab_ori[y].append(tmp[x])

arr = list(i for i in range(len(virus)))
subset = combinations(arr,M)
for sub in subset:
    lab = list(lab_ori[i][:] for i in range(N))
    virus_sub = []
    for i in sub:
        virus_sub.append(virus[i])
        y,x = virus[i]
        lab[y][x] = 2
    for y,x in virus_sub:
