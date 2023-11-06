import sys


def input():
    return sys.stdin.readline().rstrip()


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def print_left(node):
    print(node.data, end="")
    if node.left != ".":
        print_left(tree[node.left])
    if node.right != ".":
        print_left(tree[node.right])


def print_middle(node):
    if node.left != ".":
        print_middle(tree[node.left])
    print(node.data, end="")
    if node.right != ".":
        print_middle(tree[node.right])


def print_right(node):
    if node.left != ".":
        print_right(tree[node.left])
    if node.right != ".":
        print_right(tree[node.right])
    print(node.data, end="")


N = int(input())
tree = {}

for _ in range(N):
    mid, left, right = input().split()
    tree[mid] = Node(mid, left, right)

print_left(tree["A"])
print()
print_middle(tree["A"])
print()
print_right(tree["A"])
