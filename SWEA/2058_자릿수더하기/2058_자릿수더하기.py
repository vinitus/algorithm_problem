N = int(input())

total = 0

for i in range(3,-1,-1):
    total += N // 10**i
    N = N % 10**i

print(total)