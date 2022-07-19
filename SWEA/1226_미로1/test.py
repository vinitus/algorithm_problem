import sys

sys.stdin = open(r"SWEA\1226_미로1\input.txt","r")

def Four_dir(y,x):                              # 4방위 좌표를 2중 리스트로 나타내는 함수
    return [[y,x+1],[y,x-1],[y+1,x],[y-1,x]]    # 각각 동 서 남 북

def Count_Zero(tmp_list):                       # 0의 갯수를 세는 함수
    count_zero = 0
    three = False                               # 3은 도착을 의미, 이를 판별하기 위한 변수
    for i in tmp_list:
        if (i == 0):
            count_zero += 1
        elif (i == 3):                          # 4방위 중 3을 만나면
            three = True                        # 네
            break
    if three:                                   # 3만나면
        return -1                               # -1 리턴
    else:
        return count_zero                       # 3을 못만나면 리턴값은 항상 0 이상

def Find_zero(tmp_list):                        # 4방위 중 0을 찾는 함수
    for i in range(len(tmp_list)):
        if tmp_list[i] == 0:                    # 순서대로 동서남북인걸 아니까
            return i                            # 인덱스만 리턴해주면 어디로 가야할지 아는거임

for t in range(1,11):
    test_case = int(input())

    # 미로를 입력받는 모습
    miro_list = []
    
    for _ in range(16):                             
        tmp_list = list(map(int,input()))
        miro_list.append(tmp_list)              # 2중 리스트를 가지는 미로 리스트가 된다

    # 시작 지점을 찾는 모습
    stop_flag = False                           # 시작지점인 2를 찾으면 멈추기 위함
    for i in range(16):
        for j in range(16):
            if miro_list[i][j] == 2:
                x,y = j,i                       # miro_list[i][j]에서 i는 y축을 나태내고 j는 x축을 나타냄
                stop_flag = True                # 바깥의 for문을 멈추기 위해
                break                           # 2중 for문 중 하나 멈춤
        if stop_flag:                           # 나머지도 멈춤
            break
    
    # 길을 찾아 이동하기
    interchange = []                            # IC 교차로를 넣기 위함. 스택 형식으로 구현!
    for _ in range(1000):
        if len(interchange) == 0:
            flag_ic = False                     # 교차로를 지나왔는지를 판별하기 위함
        # 갈 곳이 2개 이상일 때
        four_dir_xy = Four_dir(y,x)     # 동 서 남 북
        four_dir_list = []
        for i in four_dir_xy:
            four_dir_list.append(miro_list[i[0]][i[1]])         # y x
        num_of_zeros = Count_Zero(four_dir_list)
        if num_of_zeros == -1:
            print(f"#{t} 1")
            break
        elif num_of_zeros == 1:
            if flag_ic:
                miro_list[y][x] = 1
            else:
                miro_list[y][x] = 1
            x,y = four_dir_xy[Find_zero(four_dir_list)][1],four_dir_xy[Find_zero(four_dir_list)][0]
        elif num_of_zeros > 1:
            miro_list[y][x] = 4
            interchange.append([x,y])
            x,y = four_dir_xy[Find_zero(four_dir_list)][1],four_dir_xy[Find_zero(four_dir_list)][0]
            flag_ic = True
        elif num_of_zeros == 0:
            if len(interchange) != 0:
                miro_list[y][x] = 1
                x, y = interchange[-1][0],interchange[-1][1]
                interchange.pop(-1)
            else:
                print(f"#{t} 0")
                break