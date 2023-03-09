N, M = map(int,input().split())

visited = {}
sum_index_list = 0
for i in range(1,N+1):
    sum_index_list += i
    visited[i] = set()

for _ in range(M):
    first, target = map(int,input().split())
    visited[target].add(first)

for key, value in visited.items():
    visited[key] = sorted(list(value))

answer = [0 for _ in range(N+1)]

index_list = [1 for _ in range(N+1)]
index_list[0] = 0

idx = 1
while sum_index_list > 0:
    if idx > N:
        idx = sum_index_list.index(1)
    elif not index_list[idx]:
        idx += 1
        continue

    elif not visited[idx]:
        answer[idx] = 1
        index_list[idx] = 0
        sum_index_list -= idx
        idx += 1
    else:
        max_long = 0
        max_idx = 0
        while visited[idx]:
            tmp = visited[idx].pop()
            if not answer[tmp]:
                if max_idx:
                    visited[idx].append(max_idx)
                idx = tmp
                visited[idx].append(tmp)
                break
            else:
                max_idx = tmp
                max_long = max(max_long, answer[tmp])
        else:
            answer[idx] = max_long + 1
            index_list[idx] = 0
            sum_index_list -= idx
            idx += 1

print(*answer[1:])