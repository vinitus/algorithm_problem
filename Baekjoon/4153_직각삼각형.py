while True:
    length = list(map(int,input().split()))
    if max(length) == 0:
        break
    max_lenght = length.pop(length.index(max(length)))
    if length[0]**2 + length[1]**2 == max_lenght**2:
        print("right")
    else:
        print("wrong")