T = int(input())

for t in range(1,T+1):
    N,K = map(int,input().split())

    puzzle = []                 # 공간을 2차원으로 나타내기 위해 2차원 리스트 사용
    for n in range(N):
        tmp = list(map(int,input().split()))
        puzzle.append(tmp)

    result = 0
    for i in puzzle:
        count = 0
        for j in range(N):          # if로 리스트의 요소가 1이면 count를 1 더해줄거임
            if i[j] == 1:           # 1이 아니면 count랑 요구하는 문자열 수 K랑 비교
                count += 1
                if j == N - 1:          # 근데 마지막이면 그냥 더하고 끝나버리니까
                    if count == K:      # 비교해줘야함
                        result += 1
            else:
                if count == K:
                    result += 1
                    count = 0
                else:
                    count = 0
    
    # 여긴 세로 버전이에요
    for i in range(N):
        count = 0
        for j in range(N):
            if j == N - 1:
                if puzzle[j][i] == 1:
                    count += 1
                else:
                    pass
                if count == K:
                    result += 1
            elif puzzle[j][i] == 1:
                count +=1
            else:
                if count == K:
                    result += 1
                    count = 0
                else:
                    count = 0
    print(f"#{t} {result}")