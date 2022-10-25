def f(ms):
    global i

    next = []
    for j in range(L):
        if Llst[j][i] < Llst[j][i+1]:
            next.append([Llst[j][i], Llst[j][i+1]])

    if next:
        next.sort(key=lambda x:-(x[1]-x[0]))

        k = 0
        number = []
        while True:
            ms -= next[k][0]
            number.append(k)
            if ms < 0:
                ms += next[k]
                k += 1
            if k == len(next):
                break

        for num in number:
            ms += next[num][1]

    return

t = int(input())
for tc in range(1, t+1):
    ms, ma = map(int, input().split())
    L, N = map(int, input().split())
    Llst = []
    for _ in range(L):
        lst = list(map(int, input().split()))
        Llst.append(lst)
    # print(tc, ms, ma, L, N, Llst)
    i = 0
    while i < N:
        if i > 0:
            ms += ma
        f(ms)

    print(ms)