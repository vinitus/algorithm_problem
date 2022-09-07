N,M = map(int,input().split())
castle = []
for i in range(N):
    castle.append(list(str(input())))
count_x = 0
for i in range(N):
    if "X" not in castle[i]:
        count_x += 1
        for soldier in castle[i]:
            soldier = "O"

count_y = 0
for i in range(M):
    already = False
    for j in range(N):
        if castle[j][i] == "X":
            already = True
            break
    if already is False:
        count_y += 1

print(max(count_x,count_y))