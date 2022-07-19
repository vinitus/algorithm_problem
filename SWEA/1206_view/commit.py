for t in range(1,11):
    test_case = int(input())
    building_list = list(map(int,input().split()))
    total = 0                                       # 총 세대수를 저장할 변수
    for i in range(2,test_case-2):                  # 양 끝의 2자리는 포함하지 않음
        stop_flag = False                           # for문 정지, 세대 수를 포함할 것인가에 대한 조건 변수
        height_dif = building_list[i]               # 세대 수는 일단 세대 수임
        for j in range(1,3):                        # 좌우로 1,2만큼 옮겨다녀야댐
            if (building_list[i] < building_list[i-j]) or (building_list[i] < building_list[i+j]):      # 좌, 우로 1, 2칸의 건물이 나보다 크면
                stop_flag = True                    # 나중에 세대수를 더하지 않을 것이다
                break                               # 그리고 멈춤
            if building_list[i] - building_list[i-j] < height_dif:      # 만약 건물 높이 차이가 지금까지의 높이 차보다 작으면
                height_dif = building_list[i] - building_list[i-j]      # 업데이트
            if building_list[i] - building_list[i+j] < height_dif:
                height_dif = building_list[i] - building_list[i+j]
        if stop_flag is not True:                   # stop_flag가 True라면 2칸 이내에 건물이 나보다 높은거임
            total += height_dif                     # 높지 않았다면 해당 건물의 전망 좋은 세대수를 total에 더해줌
    
    print(f'#{t} {total}')