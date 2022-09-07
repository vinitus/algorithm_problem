N, m, M, T, R = map(int,input().split())
count = 0
trainning = 0
min = m
if m + T > M:
    print(-1)
else:
    while True:
        count += 1
        if m + T <= M:
            m += T
            trainning += 1
        else:
            if m - R >= min:
                m -= R
            else:
                m = min
        if trainning == N:
            print(count)
            break