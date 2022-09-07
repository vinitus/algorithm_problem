N = int(input())

room = []
for i in range(N):
    room.append(str(input()))

count_x = 0
for i in room:
    seat = list(i.split("X"))
    for j in seat:
        if len(j) >= 2:
            count_x += 1

for i in range(N):
    room[i] = list(room[i])


count_y = 0

for i in range(N):
    tmp = ""
    for j in range(N):
        tmp += room[j][i]
    seat = list(tmp.split("X"))
    for j in seat:
        if len(j) >= 2:
            count_y += 1
print(count_x,count_y)