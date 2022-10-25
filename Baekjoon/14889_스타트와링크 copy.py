from itertools import combinations
import sys
def input():
    return sys.stdin.readline().rstrip()

def sumWithMembers(lst,me):
    return sum(lst[me]) + sum(row[me] for row in lst)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

total = sum(map(sum,arr))
score_with_another = list(sumWithMembers(arr,now) for now in range(N))

answer = 100
for subset in combinations(score_with_another, N//2):
    answer = min(answer, abs(total - sum(subset)))

print(answer)