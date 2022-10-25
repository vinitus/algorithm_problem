from collections import deque

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))

    mx = max(lst)
    if lst == [mx]*n:
        print(f'#{tc} {0}')
    else:
        sm = 0
        for i in lst:
            sm += mx - i
        # print(sm)
        day = 0
        if sm >= 3:
            val = sm//3
            day += 2*val
            sm = sm%3
        if sm == 2:
            print(f'#{tc} {day+2}')
        elif sm == 1:
            print(f'#{tc} {day+1}')
        else:
            print(f'#{tc} {day}')