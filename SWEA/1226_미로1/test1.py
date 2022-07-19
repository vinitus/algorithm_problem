import sys

sys.stdin = open(r"SWEA\1226_미로1\input1.txt","r")

test_case = int(input())

miro_list = []

def Four_dir(y,x):
    return [[y,x+1],[y,x-1],[y+1,x],[y-1,x]]

def Count_Zero(tmp_list):
    count_zero = 0
    zero = True
    three = False
    for i in tmp_list:
        if (i == 0):
            count_zero += 1
        elif (i == 3):
            three = True
            break
    if three:
        return -1
    else:
        return count_zero

def Zero_is_1(tmp_list):
    for i in range(len(tmp_list)):
        if tmp_list[i] == 0:
            return i

def Zero_is_n(tmp_list):
    pass

for _ in range(16):
    tmp_list = list(map(int,input()))
    miro_list.append(tmp_list)

stop_flag = False
for i in range(16):
    for j in range(16):
        if miro_list[i][j] == 2:
            x,y = j,i
            stop_flag = True
            break
    if stop_flag:
        break

interchange = []
flag_ic = False
for _ in range(100):
    # 갈 곳이 2개 이상일 때
    four_dir_xy = Four_dir(y,x)     # 동 서 남 북
    four_dir_list = []
    for i in four_dir_xy:
        four_dir_list.append(miro_list[i[0]][i[1]])         # y x
    num_of_zeros = Count_Zero(four_dir_list)
    if num_of_zeros == -1:
        print(x,y)
        print(miro_list[y][x])
        print("1")
        break
    elif num_of_zeros == 1:
        if flag_ic:
            miro_list[y][x] = 1
        else:
            miro_list[y][x] = 1
        x,y = four_dir_xy[Zero_is_1(four_dir_list)][1],four_dir_xy[Zero_is_1(four_dir_list)][0]
    elif num_of_zeros > 1:
        miro_list[y][x] = 4
        interchange.append([x,y])
        x,y = four_dir_xy[Zero_is_1(four_dir_list)][1],four_dir_xy[Zero_is_1(four_dir_list)][0]
        flag_ic = True
    elif num_of_zeros is True:
        print("1")
        break
    elif num_of_zeros == 0:
        miro_list[y][x] = 1
        x, y = interchange[-1][0],interchange[-1][1]
        interchange.pop(-1)

for i in miro_list:
    print(i)