import sys
def input():
    return sys.stdin.readline().rstrip()

Y, X, N = map(int,input().split())

# 붐버맨의 맵 만들기
boomber_map = []
for i in range(Y):
    x_input_list = list(input())
    for x in range(X):
        if x_input_list[x] == "O":
            x_input_list[x] = 2
        else:
            x_input_list[x] = 0
    boomber_map.append(x_input_list)

# 횟수를 셀 변수
cnt = 1

# 유효 범위 체크 함수
def range_checker(y,x):
    if 0 <= y < Y and 0 <= x < X:
        return True
    else:
        return False

d = [[0,-1],[0,1],[-1,0],[1,0]]

# 터뜨릴 좌표를 담을 스택
boom_position_stk = []

while cnt < N:
    for y in range(Y):
        for x in range(X):
            if not boomber_map[y][x]:
                boomber_map[y][x] = 1
            elif boomber_map[y][x] == 1:
                boomber_map[y][x] = 2
            elif boomber_map[y][x] == 2:
                boomber_map[y][x] = 3
            elif boomber_map[y][x] == 3:
                boom_position_stk.append((y,x))
                for dy, dx in d:
                    ny = y + dy
                    nx = x + dx
                    if range_checker(ny, nx):
                        boom_position_stk.append((ny,nx))
    while boom_position_stk:
        y,x = boom_position_stk.pop()
        boomber_map[y][x] = 0
    cnt += 1

# 출력
for boomber_x in boomber_map:
    value_to_print = ''
    for boomber_x_ele in boomber_x:
        if not boomber_x_ele:
            value_to_print += '.'
        else:
            value_to_print += 'O'
    print(value_to_print)