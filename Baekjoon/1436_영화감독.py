N = int(input())
six = '666'
count = 0
for i in range(1000*N):
    if six in str(i):
        count += 1
    if count == N:
        print(i)
        break