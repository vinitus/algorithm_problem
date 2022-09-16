import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

R, C = map(int, input().split())

d = [(-1,0),(1,0),(0,-1),(0,1)]

def check(y,x):
    return 0 <= y < R and 0 <= x < C

def bfs1():
    global cnt
    for y,x in water:
        arr[y][x] = 0
    while water:
        y, x = water.popleft()
        for dy,dx in d:
            new_y = y + dy
            new_x = x + dx
            if check(new_y, new_x):
                if arr[new_y][new_x] == '.':
                    arr[new_y][new_x] = arr[y][x] + 1
                    water.append((new_y,new_x))

def bfs2():
    global flood
    for y,x in now:
        arr[y][x] = 0
    while now:
        y, x = now.popleft()
        for dy,dx in d:
            new_y = y + dy
            new_x = x + dx
            if check(new_y, new_x):
                if (new_y,new_x) == end:
                    flood = min(flood,arr[y][x] + 1)
                elif arr[new_y][new_x] == '.':
                    arr[new_y][new_x] = arr[y][x] + 1
                    now.append((new_y, new_x))
                elif arr[new_y][new_x] != 'X' and arr[new_y][new_x] > arr[y][x] + 1:
                    arr[new_y][new_x] = arr[y][x] + 1
                    now.append((new_y,new_x))


arr = []
now = deque([])
water = deque([])
for y in range(R):
    tmp = list(input())
    for x in range(C):
        if tmp[x] == 'D':
            end = (y,x)
        elif tmp[x] == 'S':
            now.append((y,x))
        elif tmp[x] == "*":
            water.append((y,x))
    arr.append(tmp)

flood = 999999
bfs1()
bfs2()

if flood != 999999:
    print(flood)
else:
    print("KAKTUS")