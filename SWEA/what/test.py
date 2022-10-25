import sys
sys.stdin = open('input2.txt','r')

d = [(-1,0),(1,0),(0,-1),(0,1)]

def check(y,x):
    return 0 <= y < N and 0 <= x < N

def backtracking(n,cnt,core,lst):
    global answer, core_if, core_answer
    now_lst = list(lst[i][:] for i in range(N))
    if n == len(one):
        if core == len(one):
            answer = min(answer, cnt)
            core_if = len(one)
        elif core_if < core:
            core_if = core
            core_answer = cnt
        elif core_if == core:
            core_answer = min(core_answer, cnt)
        return
    y, x = one[n]
    if not core_if == len(one):
        backtracking(n + 1, cnt, core, now_lst)
    for i in range(4):
        visited = []
        dy,dx = d[i]
        ny = y + dy
        nx = x + dx
        while check(ny,nx) and now_lst[ny][nx] == 0:
            now_lst[ny][nx] = 1
            visited.append((ny,nx))
            ny += dy
            nx += dx
        if check(ny,nx) and now_lst[ny][nx] == 1:
            for vy,vx in visited:
                now_lst[vy][vx] = 0
            continue
        backtracking(n+1,cnt+len(visited),core+1,now_lst)
        for vy, vx in visited:
            now_lst[vy][vx] = 0

T = int(input())

for t in range(1,T+1):
    N = int(input())
    lst = []
    one = []
    for y in range(N):
        tmp = list(map(int,input().split()))
        for x in range(1,N-1):
            if tmp[x] == 1 and y not in [0,N-1]:
                one.append((y,x))
        lst.append(tmp)
    answer = N**2
    core_answer = N**2
    core_if = 0
    backtracking(0,0,0,lst)
    if core_if != len(one):
        answer = core_answer
    print(f'#{t} {answer}')