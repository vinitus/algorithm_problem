N = int(input())
player = []
for i in range(N):
    player.append(str(input()))

selection = []
for i in player:
    selection.append(list(i)[0])

selection_set = set(selection)
result = []
for i in selection_set:
    count = 0
    for j in selection:
        if i == j:
            count += 1
        else:
            pass
    if count >= 5:
        result.append(i)
result.sort()
if len(result) != 0:
    print(''.join(i for i in result))
else:
    print("PREDAJA")