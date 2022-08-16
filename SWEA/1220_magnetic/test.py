import sys

sys.stdin = open('algorithm_problem/SWEA/1220_magnetic/input.txt','r')

for t in range(1,11):
    N = int(input())
    lst = list(list(map(int, input().split())) for _ in range(100))
    cnt = 0
    for i in range(100):
        stk = 0
        for j in range(100):
            if lst[j][i] == 1:
                stk += 1
            elif lst[j][i] == 2:
                if stk:
                    stk = 0
                    cnt += 1
    print(f"#{t} {cnt}")