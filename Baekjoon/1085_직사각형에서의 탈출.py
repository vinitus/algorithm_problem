#한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

# 1 ≤ w, h ≤ 1,000
# 1 ≤ x ≤ w-1
# 1 ≤ y ≤ h-1
# x, y, w, h는 정수

def get_length(a,b):
    return (a^2 + b^2) ** 0.5

x, y, w, h = map(int,input().split())

move_length_1 = h-y
move_length_2 = w-x

print(min(move_length_1,move_length_2,x,y))