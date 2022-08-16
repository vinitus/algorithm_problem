import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1,T+1):
    N = int(input())
    lst = list(list(map(int,input().split())) for _ in range(N))

    row_col = []

    for row in range(N):
        tmp = [0, 0, 0]
        for col in range(N):
            if lst[row][col] != 0:
                for d_row in range(1,N-row):
                    if lst[row + d_row][col] == 0:
                        tmp[1] = d_row
                        break
                for d_col in range(1, N - col):
                    if lst[row][col+d_col] == 0:
                        tmp[2] = d_col
                        break
                for d_row in range(tmp[1]):
                    for d_col in range(tmp[2]):
                        lst[row+d_row][col+d_col] = 0
                tmp[0] = tmp[1]*tmp[2]
                row_col.append(tmp)
                tmp = [0,0,0]
    row_col.sort()

    print(f"#{t} {len(row_col)}", end="")
    for i in row_col:
        print(f' {i[1]} {i[2]}', end="")
    print()