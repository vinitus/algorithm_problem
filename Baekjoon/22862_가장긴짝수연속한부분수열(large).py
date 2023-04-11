import sys
def input():
    return sys.stdin.readline().rstrip()

S, K = map(int, input().split())
lst = list(map(int, input().split()))

s = 0
e = 0
answer = 0
export_cnt = 0
if lst[e] % 2 == 0:
    answer += 1

while s < S and e < S:
    if s == e:
        e += 1
        continue

    if lst[s] % 2 == 1:
        s += 1
        if export_cnt:
            export_cnt -= 1
        continue
    
    while e < S:
        if lst[e] % 2 == 0:
            answer = max(answer, e - s + 1 - export_cnt)
            e += 1
        else:
            if export_cnt < K:
                e += 1
                export_cnt += 1
            else:
                while lst[s] % 2 == 0:
                    s += 1
                break

print(answer)