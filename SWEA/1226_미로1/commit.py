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
    interchange = []                            # IC 좌표를 넣기 위함. 스택 형식으로 구현!
    for _ in range(1000):
        four_dir_yx = Four_dir(y,x)     # 2중 리스트 구조상 yx로 나타내는게 편해서 yx로함! 동 서 남 북, 좌표 [y,x]
        four_dir_list = []              # 4방향에 뭐가잇는가(0,1,2,3,4,5)를 나타냄. 동 서 남 북
        for i in four_dir_yx:
            four_dir_list.append(miro_list[i[0]][i[1]])         # y x
        num_of_zeros = Count_Zero(four_dir_list)    # 0의 숫자를 셈. 왜 와이? 0이 한개면 거기로만 가면되고 2개면 선택을 해야함
        if num_of_zeros == -1:          # 도착지인 3을 만나서 -1가 리턴되면
            print(f"#{t} 1")            # 1을 출력하고
            break                       # 끝
        elif num_of_zeros == 1:         # 갈 곳이 1개면
            miro_list[y][x] = 1         # 지금 자리를 1로 만들고
            x,y = four_dir_yx[Find_zero(four_dir_list)][1],four_dir_yx[Find_zero(four_dir_list)][0] # 좌표를 그 위치로 이동
        elif num_of_zeros > 1:          # 1보다 크면
            miro_list[y][x] = 4         # 지금 자리를 4로 만듬 : 교차로라는 의미
            interchange.append([x,y])   # IC 리스트에 지금 좌표를 추가
            x,y = four_dir_yx[Find_zero(four_dir_list)][1],four_dir_yx[Find_zero(four_dir_list)][0] # 동서남북순으로 탐색하고 0인곳으로 이동
        elif num_of_zeros == 0:         # 갈곳이 없다면
            if len(interchange) != 0:   # 만약 돌아갈 IC가 있다면
                miro_list[y][x] = 1     # 현재 위치(막다른 곳)를 1로 만듬
                x, y = interchange[-1][0],interchange[-1][1]    # 가장 최근의 IC 좌표로 이동
                interchange.pop(-1)     # 이동하면 의미없으니 pop을 통해 없앰
                                        # IC가 3개고 1개를 지나왔어도 갈 곳이 2개면 다시 IC가 될거임
            else:
                print(f"#{t} 0")        # 돌아갈 IC가 없으면 끝
                break