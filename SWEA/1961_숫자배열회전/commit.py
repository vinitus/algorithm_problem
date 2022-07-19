T = int(input())

for t in range(1,T+1):
    N = int(input())

    L = []

    for n in range(N):
        tmp = list(map(int,input().split()))
        L.append(tmp)

    x_90 = []
    x_180 = []
    x_270 = []

    for i in range(N):          # 90도를 돌리면 1열이 1행이되는데 역순인거임
        tmp = ""
        for j in range(N-1,-1,-1):  # 그래서 거꾸로 시작하는거임
            tmp += str(L[j][i])
        x_90.append(tmp)

    for i in range(N-1,-1,-1):  # 180도를 돌리면 그냥 역순으로 접근하면 되는거임
        tmp = ""
        for j in range(N-1,-1,-1): 
            tmp += str(L[i][j])
        x_180.append(tmp)

    for i in range(N-1,-1,-1):  # 270도를 돌리면 1열이 3행이 되는거임 그래서 역순!
        tmp = ""
        for j in range(N):
            tmp += str(L[j][i])
        x_270.append(tmp)
    
    print(f"#{t}")
    for i in range(N):
        print(f"{x_90[i]} {x_180[i]} {x_270[i]}")