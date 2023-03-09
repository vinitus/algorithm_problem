import sys
def input():
    return sys.stdin.readline().rstrip()

N, k = map(int,input().split())

digit = 1
while k > 0:
    tmp = 9 * digit
    for i in range(digit-1):
        tmp *= 10
    digit += 1
    k -= tmp

k += tmp - 1
digit -= 1

min_start = 10 ** (digit - 1)

share = k // digit

position = k % digit

goal_value = share + min_start

if goal_value > N:
    print(-1)
else:
    goal_value = str(goal_value)

    print(goal_value[position])