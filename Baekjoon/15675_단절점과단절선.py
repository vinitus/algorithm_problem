import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
line = []
tree = {}
for _ in range(N - 1):
    a, b = map(int, input().split())
    line.append([a, b])
    tree[a] = tree.get(a, []) + [b]
    tree[b] = tree.get(b, []) + [a]

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 2:
        print("yes")
        continue
    if len(tree[k]) < 2:
        print("no")
        continue
    else:
        print("yes")
