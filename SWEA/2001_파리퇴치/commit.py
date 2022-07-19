T = int(input())

for t in range(1,T+1):
    N, M = map(int,input().split())
    L = []
    
    for n in range(N):
        tmp = list(map(int,input().split()))
        L.append(tmp)

    max = 0
    # 한번 때리면 M만큼의 인덱스를 탐색해야함
    # 9x9 배열에서 2x2만큼 때리면
    # 0 1 2 3 4 5 6 7 8 에서 7을 때리면 8까지 잡기때문에 8은 탐색할 이유가 없음
    # -> 9 - 2 + 1 = 8   for문에 넣으면 0~7까지만 탐색하면된다
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for k in range(M):
                for l in range(M):
                    sum += L[i+k][j+l]
            if sum > max:
                max = sum

    print(f"#{t} {max}")