A, B = map(int,input().split())
C = int(input())

B += C
while True:
    if B >= 60:
        B -= 60
        A += 1
    else:
        break

while True:
    if A >= 24:
        A -= 24
    else:
        break

print(A, B)