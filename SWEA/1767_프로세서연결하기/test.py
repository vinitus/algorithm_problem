import sys
sys.stdin = open('sample_input.txt','r')

d = [(-1,0),(1,0),(0,-1),(0,1)]

def check(y,x,N):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False

# 1위치 찾기
def findOne(arr, N):
    one_yx = []
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 1:
                one_yx.append((y,x))
    return one_yx

# 노드가 갈 수 있는 방향을 정하기
def checkNode(one_yx):
    global d, N,lst
    tmp = []
    idx = -1
    for y, x in one_yx:
        idx += 1
        for dy,dx in d:
            my,mx = y+dy,x+dx
            while check(my,mx,N):
                if lst[my][mx] == 1:
                    break
            else:
                tmp.append()
        pass

# 탐색하기
def search():
    pass

T = int(input())
for t in range(1,T+1):
    N = int(input())
    lst = list(list(map(int,input().split())) for _ in range(N))
    one_lst = findOne(lst, N)
    one_lst = checkNode(one_lst)