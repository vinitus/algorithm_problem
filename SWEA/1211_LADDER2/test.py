import sys

sys.stdin = open(r"SWEA\1211_LADDER2\input.txt","r")

def search_left_right(x, y, dir_flag, tmp_list):            # x, y, 지금 가는 방향, 좌우 값 리스트
    if x == 0:              # 지금 왼쪽끝에 있다면 tmp_list에는 우측의 값만 담기게됨
        if tmp_list[0] == 1 and dir_flag != "L":    # 오른쪽이 1이지만 내가 왼쪽으로 가고있다면 이건 지금 사다리타고 왼쪽에서 왔다는 뜻이니까 가면안됨 => 왼쪽으로 가고 있지않으면 오른쪽으로 감
            return x + 1, y,"R"
        else:
            return x, y + 1, "D"    # 지금 상태가 왼쪽으로 가고있고 오른쪽이 1이라면 아래로 가야함
    elif x == 99:           # 오른쪽끝도 같은 로직
        if tmp_list[0] == 1 and dir_flag != "R":
            return x - 1, y, "L"
        else:
            return x, y + 1, "D"
    else:           # 평범한 상황이면 tmp_list에는 좌측, 우측에 해당하는 값이 입력됨
        if tmp_list[0] == 1 and tmp_list[1] == 1:   #왼쪽, 오른쪽이 둘다 1이면 지금 나는 사다리의 가로축을 타고 있는거임 -> 진행방향으로 계속가야함. y축은 이동해선안됨
            if dir_flag == "L":             # 지금 왼쪽으로 사다리 가로축을 타고 있다면
                return x - 1, y, "L"        # 그대로 왼쪽
            else:                           # ㅇㅇ
                return x + 1, y, "R"        # ㅇㅇ
        elif tmp_list[0] == 1:              # 왼쪽만 1이면?
            if dir_flag == "R":             # 내가 지금 오른쪽으로 가고 있고 왼쪽이 1이면 내가왔던곳임
                return x, y + 1, "D"        # 그럼 내려가
            else:                           # 아니면 왼쪽으로
                return x - 1, y, "L"
        elif tmp_list[1] == 1:              # 왼쪽이 1일때와 같은 로직
            if dir_flag == "L":
                return x, y + 1, "D"
            else:
                return x + 1, y, "R"
        else:                               # 양쪽다 0이면?
            return x,y + 1, "D"             # 내려가

for _ in range(10):
    t = int(input())                            # test_case 번호
    ladder = []                                 # 2차원 리스트로 선언하기 위한 바깥 리스트 선언

    for _ in range(100):                        # 100줄씩 입력받음
        tmp = list(map(int,input().split()))
        ladder.append(tmp)

    one_in_ladder = []                          # 첫줄 중 내가 시작할 수 있는 1이 있는 곳

    for i in range(len(ladder[0])):
        if ladder[0][i] == 1:
            one_in_ladder.append(i)

    short_start = [0,9999]                      # 가장 짧은 코스를 저장하기 위한 list

    for one in one_in_ladder:                   # 1이 있는 곳만 계산하면 됨
        count = 0                               # 몇번 움직였나를 count
        y,x = 0,one                             # x,y 좌표를 첫째줄인 y=0 , 시작할 수 있는 곳인 x = one
        dir_flag = "D"                          # 첫 상태는 down임
        for _ in range(10000):                  # while문 하는 것보단 어차피 100*100에서 갈 수 있는 최대 횟수는 만번임
            if x == 0:                          # x == 0이거나 99면 좌 우는 하나밖에없슴
                x,y,dir_flag = search_left_right(x,y,dir_flag,[ladder[y][x+1]])
            elif x == 99:                       # x == 0이거나 99면 좌 우는 하나밖에없슴
                x,y,dir_flag = search_left_right(x,y,dir_flag,[ladder[y][x-1]])
            else:
                x,y,dir_flag = search_left_right(x,y,dir_flag,[ladder[y][x-1],ladder[y][x+1]])
            count += 1                          # 1번 움직엿으니 +1
            if y == 99:                         # y가 맨 밑에 도착!
                break
        if short_start[1] > count:              # 지금 count가 원래의 가장 짧은 것보다 짧으면
            short_start = [one,count]           # update
        
    print(f'#{t} {short_start[0]}')