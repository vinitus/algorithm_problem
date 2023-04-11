import sys
def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
lst = list(map(int, input().split()))

s = e = 0
answer = 0
visited = {}

while s < N and e != N:
    while e < N:
        if not visited.get(lst[e]):
            visited[lst[e]] = 1
            answer = max(answer, e - s + 1)
            e += 1
        else:
            if visited[lst[e]] < K:
                visited[lst[e]] += 1
                answer = max(answer, e - s + 1)
                e += 1
            else:
                visited[lst[s]] -= 1
                s += 1

print(answer)