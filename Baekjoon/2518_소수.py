M = int(input())
N = int(input())

tmp = N - M
sosu = []
for i in range(N):
    i+=1
    a = 1
    if i == 1:
        a = 0
    else:
        for j in sosu:
            if i % j == 0:
                a = 0
                break
    if a == 1:
        sosu.append(i)

tmp_list = list(range(M,N+1))

blank = []
for i in tmp_list:
    if i in sosu:
        blank.append(i)
        
if len(blank) != 0:
    print(sum(blank))
    print(min(blank))
else:
    print(-1)