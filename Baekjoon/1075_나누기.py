N = int(input())
F = int(input())

N_copy = N - (N % 100) 

for i in range(100):
    N = N_copy + i
    if N % F == 0:
        break

if len(str(i)) == 1:
    print(f"0{i}")
else:
    print(i)