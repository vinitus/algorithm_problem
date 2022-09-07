for i in range(3):
    # 입력받기
    dot_list = list(map(float,input().split()))

    # 각 점의 좌표를 구하는 모습
    dot1 = [dot_list[0],dot_list[1]]
    dot2 = [dot_list[2],dot_list[3]]
    dot3 = [dot_list[4],dot_list[5]]
    dot4 = [dot_list[6],dot_list[7]]
    # 2번째 3번째 좌표를 같게 만드는 모습
    while True:
        if dot2 == dot3:
            break
        dot2,dot1 = dot1,dot2
        if dot2 == dot3:
            break
        # 한번 바꾼 것을 다시 돌려놓는 모습
        dot2,dot1 = dot1,dot2
        dot3,dot4 = dot4,dot3

    # 공통된 점을 제외하고 다른 두점의 중간 지점을 구함
    tmp = [(dot1[0] + dot4[0])/2,(dot1[1] + dot4[1])/2]

    # 공통된 점을 중간 지점에서 반전
    result = [0.000,0.000]
    for i in range(2):
        if tmp[i] > dot2[i]:
            result[i] = dot2[i] + (tmp[i] - dot2[i]) * 2
        else:
            result[i] = dot2[i] - (dot2[i] - tmp[i]) * 2
    print(f"{result[0]:.3f} {result[1]:.3f}")
