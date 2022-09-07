from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()

def cal(lst, idx, n):
    lst = deque(lst)
    if idx == 2:
        lst.appendleft(lst.popleft() + n)
        lst[1] -= 1
        lst = list(lst)
        lst[idx] -= 1
        return lst
    elif idx == 3:
        lst.appendleft(lst.popleft() - n)
        lst[1] -= 1
        lst = list(lst)
        lst[idx] -= 1
        return lst
    elif idx == 4:
        lst.appendleft(lst.popleft() * n)
        lst[1] -= 1
        lst = list(lst)
        lst[idx] -= 1
        return lst
    elif idx == 5:
        tmp = lst.popleft()
        if tmp < 0:
            lst.appendleft(-(-tmp // n))
        else:
            lst.appendleft(tmp // n)
        lst[1] -= 1
        lst = list(lst)
        lst[idx] -= 1
        return lst

N = int(input())
lst = list(map(int,input().split()))
order = list(map(int,input().split()))

q = [[lst[0],N-1]]
q[0].extend(order)
q = deque(q)
remain = q[0][1]
while remain:
    tmp = q.popleft()
    remain = tmp[1]
    if remain == 0:
        q.append(tmp)
    else:
        for j in range(2, 6):
            if tmp[j]:
                q.append(cal(tmp, j, lst[N - remain]))

q = sorted(q)

print(q[-1][0], q[0][0])