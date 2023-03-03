from collections import deque

def solution(x, y, n):
    answer = -1
    if y == x:
        return 0
    q = deque([[y, 0]])
    while q:
        y, cnt = q.popleft()
        if y <= 0:
            continue
        else:
            if y - n == x:
                return cnt + 1
            q.append([y - n, cnt + 1])
            if y % 2 == 0:
                if y // 2 == x:
                    return cnt + 1
                q.append([y // 2, cnt + 1])
            if y % 3 == 0:
                if y // 3 == x:
                    return cnt + 1
                q.append([y // 3, cnt + 1])
    return answer