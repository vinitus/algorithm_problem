def star(star_list,count,goal):
    # *********   9x9에서 구역을 우선 9으로 나누고 영역마다 가운데를 비움
    # * ** ** *   -> 지워나갈 영역은 점 하나니까 0
    # *********   -> 옮겨갈 거리는 1 -> 4 -> 7이니까 3
    # ***   ***     
    # * *   * *   그 다음은 중앙을 비워야함, 이동을 하지않음
    # *********   -> 지워나갈 영역은 -1,0,1 각 방향으로 1씩
    # * ** ** *
    # *********

    # move_index는 중앙점에서 지워나갈 영역을 나타내기 위함
    move_index = (count - 1) // 2       

    # count는 재귀함수의 탈출 조건이기도 하지만 중앙점에서 얼마나 이동할지를 선택        
    count *= 3

    # count 값에 따른 이동 가능 횟수
    # 27x27기준 처음에 3칸(=count)마다 찍으면 27 / 3 = 9
    # 27x27의 중앙은 13,13이고 1,4,7,10,14,17,20,23,26 => 9번
    tmp = goal // count

    # 중앙 구하기
    middle = (goal - 1) // 2

    for x_i in range(-(tmp-1)//2,(tmp-1)//2+1):             # 9번 기준 -4 ~ +4
        for y_i in range(-(tmp-1)//2,(tmp-1)//2+1):         # 9번 기준 -4 ~ +4
            # 중앙 값에서 움직일 때의 좌표를 나타내기 위함
            middle_x = middle + count*x_i                   
            middle_y = middle + count*y_i

            for x in range(-move_index,move_index+1):       # 지워나갈 영역을 선택
                for y in range(-move_index,move_index+1):
                    star_list[middle_x+x][middle_y+y] = " "

    if count == goal:
        for x in star_list:
            for y in x:
                print(y,end="")
        return
    else:
        star(star_list,count,goal)

T = int(input())
star_dot = []           # 입력값에 따른 TxT를 *로 만들거임
for i in range(T):                              # T-1만큼 *로 채우고 마지막 자리는 *과 \n으로 채움
    tmp_list = list("*" for j in range(T-1))    # 2차원으로 다루기 위해 리스트 추가 선언
    tmp_list.append("*\n")                      # 마지막 자리는 줄바꿈을 위해 \n을 붙이걸 따로 추가
    star_dot.append(tmp_list)
star(star_dot,1,T)                              # 함수 실행