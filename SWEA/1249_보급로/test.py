import sys

sys.stdin = open(r"SWEA\1249_보급로\input2.txt","r")

N = int(input())

supply_road = []
empty_space = []
for _ in range(N):
    supply_road.append(list(map(int,input())))
    empty_space.append(list(-1 for _ in range(N)))
empty_space[0][0],empty_space[N-1][N-1] = 0,-2
empty_space[1][0], empty_space[0][1] = supply_road[1][0],supply_road[0][1]
standard = sum(supply_road[0])
for y in range(N):
    for x in range(N):
        if min(y,x) == 0 and max(y,x) == 1:
            continue
        