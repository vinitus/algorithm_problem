import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]

answer = 100

def backtracking(n,team1,team2):
    global answer
    n += 1

    if answer == 0:
        return

    if len(team2) == N//2 and len(team1) == N // 2:
        tmp = 0
        for y in range(N//2):
            for x in range(N//2):
                tmp += lst[team1[y]][team1[x]] - lst[team2[y]][team2[x]]
        answer = min(answer, abs(tmp))
        return
    
    if len(team1) < N//2:
        backtracking(n,team1+[n],team2)
    if len(team2) < N//2:
        backtracking(n,team1,team2+[n])

backtracking(-1,[],[])
print(answer)