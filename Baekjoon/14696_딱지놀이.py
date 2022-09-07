N = int(input())

for _ in range(N):
    a_card = list(map(int,input().split()))
    b_card = list(map(int,input().split()))
    a_card.pop(0)   # 맨 앞의 숫자 제거
    b_card.pop(0)   # 맨 앞의 숫자 제거
    
    # 별, 동그라미, 네모, 세모를 각각 숫자 4, 3, 2, 1로 표현
    # A,B,D(raw)
    
    for i in range(4,0,-1):     # 승리 조건은 4부터 1까지 탐색하는 것
        sum_A = 0   # list로 구현하는 대신 합을 통해 메모리절약
        sum_B = 0   # list로 구현하는 대신 합을 통해 메모리절약
        for a in a_card:        # a_card 탐색
            if a == i:          # 지금 탐색하고 있는 조건과 같다면
                sum_A += i      # 더해줌
        for b in b_card:        # b_card 탐색
            if b == i:
                sum_B += i
        if sum_A > sum_B:       # a의 합이 더 크면 A승
            print("A")
            break
        elif sum_B > sum_A:
            print("B")
            break
        if i == 1 and sum_A == sum_B:   # 무승부 조건은 세모까지 탐색했고 둘다 같다면임
            print("D")