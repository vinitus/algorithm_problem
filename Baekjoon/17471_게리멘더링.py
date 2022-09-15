import sys
from itertools import combinations
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
population = [0] + list(map(int,input().split()))
adj = {key:[] for key in range(1,N+1)}
for i in range(1,N+1):
    tmp = list(map(int,input().split()))
    if tmp[0] != 0:
        adj[i] += tmp[1:]

def dfs(subset):
    q = deque([subset[0]])
    visited = set([subset[0]])
    sum_tmp = 0
    while q:
        v = q.popleft()
        sum_tmp += population[v]
        for w in adj[v]:
            if w not in visited and w in subset:
                visited.add(w)
                q.append(w)

    return sum_tmp, len(visited)

arr = [i for i in range(1, N + 1)]

answer = 10**N

for i in range(1,N):
    subset = list(combinations(arr,i))
    for ele in subset:
        sum1, len1 = dfs(list(ele))
        sum2, len2 = dfs(list(j for j in range(1,N+1) if j not in ele))
        if len1 + len2 == N:
            answer = min(answer,abs(sum1 - sum2))

if answer != 10**N:
    print(answer)
else:
    print(-1)