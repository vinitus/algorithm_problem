import sys
sys.stdin = open('sample_input.txt', 'r')x

def backdoor(lst_idx,seat,lst,cnt):
    global move_m,move_p,N,total,answer
    # print(seat, sum(seat), lst)

    if cnt == total:
        if sum(seat) < answer:
            answer=sum(seat)
            # print("end")

    if sum(seat) >= answer:
        return

    if lst[lst_idx%3][1] == 0:
        backdoor(lst_idx+1,seat,lst,cnt)
        return

    index = lst[lst_idx%3][0] - 1

    tmp = [0,0]
    for i in range(1,N+1):
        if not tmp[0] and 0 <= index-i < N and not seat[index-i]:
            lst[lst_idx%3][1] -= 1
            tmp[0] = 1
            seat[index-i] = i + 1
            backdoor(lst_idx + 1, seat, lst,cnt+1)
            lst[lst_idx%3][1] += 1
            seat[index-i] = 0
        if not tmp[1] and 0 <= index+i < N and not seat[index+i]:
            lst[lst_idx%3][1] -= 1
            seat[index + i] = i + 1
            backdoor(lst_idx + 1, seat, lst,cnt+1)
            tmp[1] = 1
            lst[lst_idx % 3][1] += 1
            seat[index + i] = 0
        if tmp[0] == 1 and tmp[1] == 1:
            break

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(list(map(int, input().split())) for _ in range(3))
    lst.sort()
    move_m,move_p = [],[]
    # move선언
    for i in range(1,N):
        move_m += [-i]
        move_p += [i]

    seat = [0] * N
    answer = 0
    total = 0
    answer = 60*20
    for i in range(3):
        total += lst[i][1]-1
        seat[lst[i][0]-1] = 1
        lst[i][1] -= 1

    backdoor(0,seat,lst,0)
    print(answer)