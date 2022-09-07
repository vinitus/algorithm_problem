x, y = map(int,input().split())
for i in range(1,x):
    if i == 2:
        y += 28
    elif i <= 7:
        if i % 2 == 0:
            y += 30
        elif i % 2 == 1:
            y += 31
    else:
        if i % 2 == 1:
            y += 30
        elif i % 2 == 0:
            y += 31

weekend = list(map(str,("SUN, MON, TUE, WED, THU, FRI, SAT").split(", ")))

print(weekend[y%7])