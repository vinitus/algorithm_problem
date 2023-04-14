N = int(input())
lst = list(map(int,input().split()))

lst.sort()

s = 0
e = N - 1

min_answer = 10**9 * 2 + 1
answer = []

while s < e:
    shake = lst[s] + lst[e]

    if abs(shake) < abs(min_answer):
        min_answer = shake
        answer = [lst[s], lst[e]]

    if shake < 0:
        s += 1
    elif shake == 0:
        break
    else:
        e -= 1

print(min(answer), max(answer))