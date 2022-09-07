my_team = str(input())
N = int(input())
team_list = []
for i in range(N):
    team_list.append(list(str(input())))
team_list.sort()
L,O,V,E = 0,0,0,0
for i in list(my_team):
    if i == "L":
        L += 1
    elif i == "O":
        O += 1
    elif i == "V":
        V += 1
    elif i == "E":
        E += 1

win_list = []
for i in team_list:
    L1,O1,V1,E1 = L,O,V,E
    for j in list(i):
            if j == "L":
                L1 += 1
            elif j == "O":
                O1 += 1
            elif j == "V":
                V1 += 1
            elif j == "E":
                E1 += 1
    win = ((L1+O1) * (L1+V1) * (L1+E1) * (O1+V1) * (O1+E1) * (V1+E1)) % 100
    print(''.join(i),L1,O1,V1,E1,win)
    win_list.append(win)

print(''.join(team_list[win_list.index(max(win_list))]))