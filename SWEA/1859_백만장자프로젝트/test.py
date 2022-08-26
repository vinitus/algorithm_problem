import sys
sys.stdin = open('input.txt','r')
T = int(input())
for t in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    max_value = lst[-1]
    answer = 0
    for i in range(N-1,-1,-1):
        if max_value >= lst[i]:
            answer += max_value-lst[i]
        else:
            max_value = lst[i]
    print(f"#{t} {answer}")