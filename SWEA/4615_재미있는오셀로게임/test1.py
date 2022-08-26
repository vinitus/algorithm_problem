import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    board = list(list([0] * N) for _ in range(N))
    idx = N // 2
    for i in range(2):
        board[idx-1][idx-1+i] = 2 - i
        board[idx][idx-1+i] = 1 + i
    order = []
    cross = [0,2,1]
    for _ in range(M):
        x,y,dol = map(int,input().split())
        order.append([x,y,dol])
        y -= 1
        x -= 1
        board[y][x] = dol
        pass
        for i in [-1,1]:
            idx = i
            cross_flag = False
            already_flag = False
            while 0 <= x + idx < N:
                if board[y][x+idx] == cross[dol]:
                    idx += i
                    cross_flag = True
                elif cross_flag and board[y][x+idx] == dol:
                    idx -= i
                    while board[y][x+idx] == cross[dol]:
                        board[y][x+idx] = dol
                        idx -= i
                    else:
                        break
                else:
                    break
            idx = i
            cross_flag = False
            while 0 <= y + idx < N:
                if board[y+idx][x] == cross[dol]:
                    idx += i
                    cross_flag = True
                elif cross_flag and board[y+idx][x] == dol:
                    idx -= i
                    while board[y+idx][x] == cross[dol]:
                        board[y+idx][x] = dol
                        idx -= i
                    else:
                        break
                else:
                    break
            idx = i
            cross_flag = False
            while 0 <= y + idx < N and 0 <= x + idx < N:
                if board[y+idx][x+idx] == cross[dol]:
                    idx += i
                    cross_flag = True
                elif cross_flag and board[y+idx][x+idx] == dol:
                    idx -= i
                    while board[y+idx][x+idx] == cross[dol]:
                        board[y+idx][x+idx] = dol
                        idx -= i
                    else:
                        break
                else:
                    break
            idx = i
            cross_flag = False
            while 0 <= y - idx < N and 0 <= x + idx < N:
                if board[y-idx][x+idx] == cross[dol]:
                    idx += i
                    cross_flag = True
                elif cross_flag and board[y-idx][x+idx] == dol:
                    idx -= i
                    while board[y-idx][x+idx] == cross[dol]:
                        board[y-idx][x+idx] = dol
                        idx -= i
                    else:
                        break
                else:
                    break
            idx = i
            cross_flag = False
            while 0 <= y + idx < N and 0 <= x - idx < N:
                if board[y + idx][x - idx] == cross[dol]:
                    idx += i
                    cross_flag = True
                elif cross_flag and board[y + idx][x - idx] == dol:
                    idx -= i
                    while board[y + idx][x - idx] == cross[dol]:
                        board[y + idx][x - idx] = dol
                        idx -= i
                    else:
                        break
                else:
                    break
    answer = [0,0,0]
    for i in board:
        for j in i:
            answer[j] += 1
    print(f'#{t} {answer[1]} {answer[2]}')