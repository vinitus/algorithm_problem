dwarf = []
for i in range(9):
    dwarf.append(int(input()))
sum_all = 0
for i in dwarf:
    sum_all += i
dwarf.sort()
sum_all_copy = sum_all
for i in range(9):
    for j in range(8,i,-1):
        stop_val = False
        if i == j:
            pass
        else:
            sum_all = sum_all_copy
            sum_all -= (dwarf[i] + dwarf[j])
            if sum_all == 100:
                for k in range(9):
                    if k == i or k == j:
                        pass
                    else:
                        print(dwarf[k])
                        stop_val = True
        if stop_val:
            break
    if stop_val:
        break