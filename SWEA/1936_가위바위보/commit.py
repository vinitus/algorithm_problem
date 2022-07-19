# 가위 : 1  바위 : 2  보 : 3
# 가위와 바위, 바위랑 보는 숫자의 크기로 승리를 가르면 되지만
# 보와 가위는 역순임

A, B = map(int,input().split())

if (min(A,B) == 1) and (max(A,B) == 3): # A,B 중 하나는 1이고 하나는 3이면
    if A == 3:                          # A가 3이면?
        print("B")                      # A는 보, B는 가위니까 B승
    else:
        print("A")
else:
    if A > B:
        print("A")
    else:
        print("B")