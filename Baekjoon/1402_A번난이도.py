T = int(input())

for t in range(T):
    A, B = map(int,input().split())
    A_copy = A
    A_divisor = []
    while A != 1:
        for i in range(2,A_copy+1):
            if A % i == 0:
                A_divisor.append(i)
                A = A // i
                break
            else:
                pass
        for i in A_divisor:
            
    print(A_divisor)