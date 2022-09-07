N = int(input())
M = N
if N == 1:
    pass
else:
    while 1:
        a = 0
        for i in range(M-1):
            i += 2
            if M % i == 0 and M!=i:
                M = int( M / (i))
                print(i)
                break
            if i >= M:
                a = 1
                print(M)
                break
        if a == 1:
            break