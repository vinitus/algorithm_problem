from re import T


N = int(input())
for i in range(N,0,-1):
    yes_no = True
    for j in list(str(i)):
        if j != "4" and j != "7":
            yes_no = False
            break
    if yes_no is True:
        print(i)
        break